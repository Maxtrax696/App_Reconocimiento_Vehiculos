import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart' as p;
import 'package:vehicule_detector_app/history_page.dart';
import 'package:shared_preferences/shared_preferences.dart';


void main() {
  runApp(VehicleDetectorApp());
}

class VehicleDetectorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Detector de Vehículos',
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: VehicleDetectorPage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class VehicleDetectorPage extends StatefulWidget {
  @override
  _VehicleDetectorPageState createState() => _VehicleDetectorPageState();
}

class _VehicleDetectorPageState extends State<VehicleDetectorPage> {
  File? _image;
  Map<String, dynamic>? _vehicleInfo;
  bool _isLoading = false;

  final ImagePicker _picker = ImagePicker();

  Future<void> _pickImage(ImageSource source) async {
    final XFile? image = await _picker.pickImage(source: source);
    if (image != null) {
      setState(() {
        _image = File(image.path);
        _vehicleInfo = null;
      });
      await _sendImageToBackend(_image!);
    }
  }

  Future<void> _sendImageToBackend(File imageFile) async {
    setState(() {
      _isLoading = true;
    });

    final uri = Uri.parse("http://54.226.57.7/analyze");

    final request = http.MultipartRequest('POST', uri);
    request.files.add(
      await http.MultipartFile.fromPath(
        'file',
        imageFile.path,
        filename: p.basename(imageFile.path),
      ),
    );

    try {
      final response = await request.send();
      final responseBody = await response.stream.bytesToString();

      if (response.statusCode == 200) {
        final jsonResponse = json.decode(responseBody);
        print("Respuesta JSON recibida: $jsonResponse");

        setState(() {
          _vehicleInfo = jsonResponse;
        });
        if (jsonResponse["success"] == true) {
          final scanData = jsonResponse["data"]["data"];
          await _addToHistory(scanData);
        }
      } else {
        _showError("Error del servidor: ${response.statusCode}");
      }
    } catch (e) {
      _showError("Error de red: $e");
    }

    setState(() {
      _isLoading = false;
    });
  }

  // 👇 NUEVO MÉTODO
  Future<void> _addToHistory(Map<String, dynamic> scanData) async {
    final prefs = await SharedPreferences.getInstance();
    final history = prefs.getStringList('scanHistory') ?? [];

    history.insert(0, json.encode(scanData));

    if (history.length > 10) {
      history.removeLast();
    }

    await prefs.setStringList('scanHistory', history);
  }

  void _showError(String message) {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(message)));
  }

  TableRow _buildTableRow(String key, dynamic value) {
    return TableRow(children: [
      Padding(
        padding: EdgeInsets.all(8),
        child: Text(key, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
      ),
      Padding(
        padding: EdgeInsets.all(8),
        child: Text(value?.toString() ?? '', style: TextStyle(color: Colors.white)),
      ),
    ]);
  }

  @override
  Widget build(BuildContext context) {
    final data = _vehicleInfo?['data']?['data'];
    final isSuccess = _vehicleInfo?['success'] == true;
    final errorMessage = _vehicleInfo?['error'];

    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text('DETECTOR DE VEHICULOS'),
        backgroundColor: Colors.red,
        foregroundColor: Colors.white,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Container(
              height: 220,
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.grey[900],
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.white, width: 2),
              ),
              child: _image != null
                  ? ClipRRect(
                      borderRadius: BorderRadius.circular(10),
                      child: Image.file(
                        _image!,
                        fit: BoxFit.cover,
                        width: double.infinity,
                        height: double.infinity,
                      ),
                    )
                  : Center(
                      child: Icon(
                        Icons.image,
                        color: Colors.white70,
                        size: 80,
                      ),
                    ),
            ),
            SizedBox(height: 20),
            if (_isLoading) ...[
              CircularProgressIndicator(color: Colors.white),
              SizedBox(height: 10),
              Text("Analizando imagen...", style: TextStyle(color: Colors.white)),
            ]
            else if (isSuccess && data != null) ...[
              Container(
                margin: EdgeInsets.only(top: 10),
                padding: EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white10,
                  borderRadius: BorderRadius.circular(12),
                ),
                constraints: BoxConstraints(
                  minHeight: 150,
                  maxHeight: 300, // o usa MediaQuery si quieres que sea relativo a la pantalla
                ),
                child: SingleChildScrollView(
                  child: Table(
                    defaultVerticalAlignment: TableCellVerticalAlignment.middle,
                    columnWidths: {
                      0: FixedColumnWidth(80),
                      1: FlexColumnWidth(),
                    },
                    children: [
                      _buildTableRow("Marca", data["marca"]),
                      _buildTableRow("Modelo", data["modelo"]),
                      _buildTableRow("Año", data["año"]),
                      _buildTableRow("Precio", data["precio"]),
                      _buildTableRow("Detalle", data["reseña"]),
                    ],
                  ),
                ),
              ),
            ]
            else if (!isSuccess && errorMessage != null) ...[
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text(
                  errorMessage.toString(),
                  style: TextStyle(
                    color: Colors.redAccent,
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              )
            ],
            Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  icon: Icon(Icons.photo),
                  label: Text("Galería"),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.black,
                  ),
                  onPressed: () => _pickImage(ImageSource.gallery),
                ),
                ElevatedButton.icon(
                  icon: Icon(Icons.camera_alt),
                  label: Text("Cámara"),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.black,
                  ),
                  onPressed: () => _pickImage(ImageSource.camera),
                ),
              ],
            ),
            SizedBox(height: 10),
            ElevatedButton.icon(
              icon: Icon(Icons.history),
              label: Text("Ver historial de escaneos"),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: Colors.black,
              ),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => HistoryPage()),
                );
              },
            ),

            SizedBox(height: 10),
          ],
        ),
      ),
    );
  }
}
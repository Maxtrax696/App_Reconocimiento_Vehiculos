import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class HistoryPage extends StatefulWidget {
  @override
  _HistoryPageState createState() => _HistoryPageState();
}

class _HistoryPageState extends State<HistoryPage> {
  List<Map<String, dynamic>> _history = [];

  @override
  void initState() {
    super.initState();
    _loadHistory();
  }

  Future<void> _loadHistory() async {
    final prefs = await SharedPreferences.getInstance();
    final historyData = prefs.getStringList('scanHistory') ?? [];

    setState(() {
      _history = historyData
          .map((entry) => json.decode(entry) as Map<String, dynamic>)
          .toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text('HISTORIAL DE ESCANEOS'),
        backgroundColor: Colors.red,
        foregroundColor: Colors.white,
      ),
      body: _history.isEmpty
          ? Center(
              child: Text(
                'Aún no hay escaneos',
                style: TextStyle(color: Colors.white70),
              ),
            )
          : GridView.builder(
              padding: EdgeInsets.all(12),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 12,
                crossAxisSpacing: 12,
                childAspectRatio: 0.75,
              ),
              itemCount: _history.length,
              itemBuilder: (context, index) {
                final scan = _history[index];
                return Container(
                  width: 280,
                  margin: EdgeInsets.only(right: 16),
                  padding: EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.white10,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: Colors.white24),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Center(
                        child: Icon(
                          Icons.directions_car_filled_rounded,
                          color: Colors.redAccent,
                          size: 48,
                        ),
                      ),
                      SizedBox(height: 8),
                      Text("Marca: ${scan["marca"]}", style: TextStyle(color: Colors.white)),
                      Text("Modelo: ${scan["modelo"]}", style: TextStyle(color: Colors.white)),
                      Text("Año: ${scan["año"]}", style: TextStyle(color: Colors.white)),
                      Text("Precio: ${scan["precio"]}", style: TextStyle(color: Colors.white)),
                      SizedBox(height: 8),
                      Text("Detalle:", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      Expanded(
                        child: SingleChildScrollView(
                          child: Text(scan["reseña"] ?? "", style: TextStyle(color: Colors.white)),
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
    );
  }
}

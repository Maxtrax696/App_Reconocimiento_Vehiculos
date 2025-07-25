def construir_verificador_prompt():
    return (
        "Tu tarea es verificar si la imagen proporcionada contiene un vehículo terrestre a motor claramente visible.\n\n"
        "Debes responder con **solo una** de las siguientes palabras clave, sin comillas ni explicaciones:\n"
        "Especificaciones para sin_vehiculo\n"
        "NO se deben considerar válidos:\n"
        "- sin_vehiculo → Si NO hay ningún vehículo claramente visible\n"
        "- Vehículos marítimos, aéreos, agrícolas, industriales o de tamaño extremo\n"
        "- Juguetes, ilustraciones deformadas o diseños sin base real y de peliculas animadas (como vehiculos de las peliculas Cars que tengan estas caracteristicas irreales como ojos, boca o extremidades humanas)\n\n"

        "Especificaciones para un_vehiculo\n"
        "Un vehículo se considera válido si cumple TODAS las siguientes condiciones:\n"
        "- un_vehiculo → Si hay exactamente UN vehículo claramente visible o varios del mismo modelo repetido (aunque en diferentes colores)\n"
        "- Es un modelo terrestre a motor (auto, motocicleta, SUV, camión liviano y autobuses)\n"
        "- Está bien enfocado, no está obstruido y ocupa al menos un 25% del área de la imagen\n"
        "- Tiene vista clara de su forma (frontal, lateral o trasera)\n"
        "- Puede estar en una imagen real o generada por IA (como arte estilo anime) siempre que represente un modelo real con proporciones coherentes\n\n"
        "- Si hay múltiples vehículos idénticos (mismo modelo y diseño general, aunque cambien los colores), considera la imagen como **un_vehiculo**.\n"
        "- Si el vehiculo es a escala (como modelos de coleccion), pero mantiene las proporciones reales y no tiene caracteristicas irreales (como ojos o boca), se considera un_vehiculo\n\n"

        "Tu respuesta debe ser exactamente una de las dos palabras clave anteriores."
        
    )

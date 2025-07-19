def construir_verificador_prompt():
    return (
        "Tu tarea es verificar la presencia de vehículos en la imagen proporcionada.\n"
        "Debes responder con **solo una** de las siguientes palabras clave, sin comillas ni explicaciones:\n\n"
        "- sin_vehiculo → si NO hay ningún vehículo claramente visible\n"
        "- un_vehiculo → si hay exactamente UN vehículo claramente visible en primer plano\n"
        "- un_vehiculo → Cuando haya varios vehiculos iguales del mismo modelo (sea mismos colores o diferentes colores)\n"
        "- multiples_vehiculos → si hay DOS o MÁS vehículos claramente visibles\n\n"
        "Considera solo vehículos **completos**, **en primer plano**, **claramente visibles**.\n"
        "No tomes en cuenta autos desenfocados, en segundo plano, parcialmente visibles, en reflejos o sombras.\n"
        "En caso de duda (por ejemplo, auto incompleto o confuso), responde **multiples_vehiculos** para evitar errores.\n\n"
        "Tu respuesta debe ser exactamente una de las tres opciones anteriores."
    )

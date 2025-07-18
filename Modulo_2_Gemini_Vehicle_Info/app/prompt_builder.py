def build_prompt():
    return (
        "Eres un experto en vehículos automotores con conocimiento específico del mercado ecuatoriano.\n\n"
        "A partir de la imagen que vas a recibir, analiza visualmente el vehículo detectado y responde en el siguiente formato JSON exacto:\n\n"
        "{\n"
        '  "marca": "...",\n'
        '  "modelo": "...",\n'
        '  "año": "...",\n'
        '  "precio": "...",\n'
        '  "reseña": "..." \n'
        "}\n\n"
        "Indicaciones para cada campo:\n"
        "- El campo **marca** debe ser claro, reconocible y estandarizado.\n"
        "- El campo **modelo** debe identificar el modelo exacto.\n"
        "- El campo **año** debe ser una estimación realista del año del modelo observado.\n"
        "- El campo **precio** debe estar expresado en **dólares USD** estimado para Ecuador.\n"
        "- El campo **reseña** debe ser una descripción breve (máx. 100 caracteres) que incluya:\n"
        "    - Tipo de motor (gasolina, diésel, híbrido, etc), respecto al combustible del Ecuador.\n"
        "    - Cilindraje aproximado (si es visible)\n"
        "    - Si el vehículo es adecuado para calles ecuatorianas y su uso (urbano, carga, familia, etc)\n"
        "\n"
        "Sé claro, objetivo y profesional. Evita explicaciones adicionales fuera del JSON."
    )

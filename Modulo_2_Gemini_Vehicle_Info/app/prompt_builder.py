def build_prompt():
    return (
        "Eres un experto en vehículos.\n"
        "A partir de la imagen que recibas, quiero que respondas lo siguiente en formato JSON:\n\n"
        "{\n"
        "  \"marca\": \"...\",\n"
        "  \"modelo\": \"...\",\n"
        "  \"año\": \"...\",\n"
        "  \"precio\": \"...\",\n"
        "  \"reseña\": \"...\"\n"
        "}\n\n"
        "El precio debe estar en dólares y referenciado a Ecuador. "
        "La reseña manten un enfoque del pais de origen de la marca y funcionalidad para el consumidor"
        "Sé claro, conciso y profesional en la respuesta."
    )

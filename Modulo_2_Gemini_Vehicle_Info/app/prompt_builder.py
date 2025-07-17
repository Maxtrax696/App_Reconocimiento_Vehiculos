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
        "Tendras en cuenta que el año debe ser especifico del vehiculo, donde haras una mejor prediccion de este, ya que habra modelos similares de otros años."
        "El precio debe estar en dólares."
        "La reseña manten un enfoque del pais de origen de la marca y funcionalidad para el consumidor"
        "Agrega tipo de motor del vehiculo, cilindraje y si el combstible del ecuador es recomendable para este y si es recomendable para las calles del Ecuador"
        "Sé claro, conciso y profesional en la respuesta, no debe sobrepasar los 100 caracterteres"
    )

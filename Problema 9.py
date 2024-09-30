def omitir_vocales(texto):

    vocales = "aeiouAEIOU"
    
    texto_sin_vocales = ''.join(letra for letra in texto if letra not in vocales)
    
    return texto_sin_vocales

texto_usuario = input("Ingrese su mensaje de texto:")
resultado = omitir_vocales(texto_usuario)

print("Texto sin vocales:", resultado)

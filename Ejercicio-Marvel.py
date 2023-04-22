# escriba un programa que permita adivinar
# un personaje de Marvel en base a estas preguntas:
# 1 ¿ Puede Volar?
# 2 ¿ Es Humano ?
# 3 ¿ Tiene Mascara?
print("responde las 3 preguntas y adivino tu personaje")
can_fly = input("Puede volar? S/N ")
is_human = input("Es humano? S/N ")
have_mask = input("Usa Mascara? S/N ")


if can_fly == "s":
    if is_human == "s":
        if have_mask == "s":
            print("tu personaje SI vuela, SI es humano y SI tiene mascara")
            print("Tu personaje Marvel es: IROMAN")
        else:
            print("tu personaje SI vuela, SI es humano y NO tiene mascara")
            print("Tu personaje Malvern es: CAPITAN MARVEL")
    else:
        if have_mask == "s":
            print("tu personaje SI vuela, NO es humano y SI tiene mascara")
            print("Tu personaje Malvern es: RONAN ACCUSER")
        else:
            print("tu personaje SI vuela, NO es humano y NO tiene mascara")
            print("Tu personaje Malvern es: VISION")
else:
    if is_human == "s":
        if have_mask == "s":
            print("tu personaje NO vuela, SI es humano y SI tiene mascara")
            print("Tu personaje Malvern es: SPIDERMAN")
        else:
            print("tu personaje NO vuela, SI es humano y NO tiene mascara")
            print("Tu personaje Malvern es: HULK")
    else:
        if have_mask == "s":
            print("tu personaje NO vuela, NO es humano y SI tiene mascara")
            print("Tu personaje Malvern es: BLACK BOLT")
        else:
            print("tu personaje NO vuela, NO es humano y NO tiene mascara")
            print("Tu personaje Malvern es: THANOS")
print("Gracias por participar!!")

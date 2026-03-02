# and(y) or(o) not(no)

temperatura = 50
llueve = False

if temperatura > 20 and not llueve:
    print("Día perfecto para salir al parque.")

elif temperatura > 40 or llueve:
    print("¡Cuidado! El clima es extremo, mejor quédate en casa.")

elif temperatura > 15 and llueve:
    print("Lleva un paraguas y una chaqueta ligera.")

else:
    print("Mejor quédate en casa y mira una película.")
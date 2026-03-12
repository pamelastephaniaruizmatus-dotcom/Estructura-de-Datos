def evaluar_posfija(expresion):
    pila = []
    tokens = expresion.split()

    for token in tokens:
       
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            pila.append(float(token))
        else:
         
            try:
                b = pila.pop()
                a = pila.pop()
                
                if token == '+':
                    pila.append(a + b)
                elif token == '-':
                    pila.append(a - b)
                elif token == '*':
                    pila.append(a * b)
                elif token == '/':
                    pila.append(a / b)
                elif token == '^':
                    pila.append(a ** b)
            except IndexError:
                return "Error: Expresión mal formada"

    return pila[0] if pila else "Error"

-
expresion_ejemplo = "5 3 + 8 2 / *"  # Equivalente a: (5 + 3) * (8 / 2)
resultado = evaluar_posfija(expresion_ejemplo)

print(f"Expresión Posfija: {expresion_ejemplo}")

print(f"Resultado: {resultado}")

# Tabuada ::
while True:
    tab = int(input(f"Qual tabuada deseja :"))
    if tab < 0:
        break
    print(f"=" * 20)
    for c in range(1, 11):
        print(f"{tab} x {c} = {tab * c}")
print(f"-" * 20)
print(f"Programa de Tabuada finalizado ;)")
print(f"-" * 20)

# Soma ::
print(f"-" * 20)
s1 = int(input(f"Qual primeiro deseja somar : "))
s2 = int(input(f"Qual segundo deseja somar : "))
print(f"A soma de {s1} e {s2} é igual {s1 + s2}")
print(f"-" * 20)

# Multiplicacao ::
print(f"-" * 20)
m1 = int(input(f"Qual primeiro deseja mutiplicar : "))
m2 = int(input(f"Qual segundo deseja mutiplicar : "))
print(f"A multiplicação de {m1} e {m2} é igual {m1 * m2}")
print(f"-" * 20)

# Subtração ::
print("=" * 20)
sub1 = int(input(f"Qual primeiro deseja Subritair : "))
sub2 = int(input(f"Qual segundo número que deseja subtrair : "))
print(f"O resultado da subtração entre {sub1} e {sub2} é {sub1 - sub2}")
print("=" * 20)

# Divisão ::
print("=" * 20)
div1 = float(input(f"Qual numero deseja Dividir: "))
div2 = float(input(f"Dividir por quanto: "))
print(f"A divisão entre {div1} e {div2} é {div1 / div2 }")
print("=" * 20)

# Módulação (Resto) ::
print("=" * 20)
d1 = float(input(f"Qual numero deseja o Resto: "))
d2 = float(input(f"Resto divido por quanto: "))
print(f"A divisão entre {d1} e {d2} é {div1 % div2 }")
print("=" * 20)

# Potenciacao ::
print(f"-" * 20)
p1 = int(input(f"Qual primeiro deseja Potencia : "))
p2 = int(input(f"Qual segundo deseja Potencia : "))
print(f"A multiplicação de {p1} e {p2} é igual {p1 ** p2}")
print(f"-" * 20)

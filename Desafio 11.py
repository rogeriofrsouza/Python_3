alt = float(input('Altura da parede (m): '))
larg = float(input('Largura da parede (m): '))
a = alt * larg
t = a / 2
print(f'Sua parede tem a dimensão de {alt:.2f}x{larg:.2f} e sua área é de {a:.2f}m².')
print(f'Para pintar essa parede, você precisará de {t:.2f} litros (L) de tinta.')

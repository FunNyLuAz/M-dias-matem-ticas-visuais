import matplotlib.pylab as pyplot
import numpy as np


def main():
    # Variáveis inicias
    a = 3
    b = 1

    # Cálculo dos valores de X e Y
    radius = (a + b) / 2
    angle = np.linspace(0, np.pi, 1000)
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    # Cálculo de outras variáveis
    ma = radius # Média aritmética
    mg = np.sqrt(a * b) # Média geométrica
    mh = 2 / (1/a + 1/b) # Média harmônica
    ve = np.sqrt((a**2 + b**2) / 2) # Valor eficaz / Raiz do valor quadrático médio 
    diff = a - ma #(Obs.: a - ma == ma - b)
    alpha = 90 - np.arcsin(mh / mg) # Ângulo entre topo da média geométrica e topo da média harmônica

    # Configuração do gráfico
    pyplot.figure("Médias matemáticas visuais", figsize=(9, 7))
    pyplot.title("Médias matemáticas visuais")
    pyplot.gca().set_aspect('equal', 'datalim')

    # Plotagens básicas no gráfico
    pyplot.axhline(y=0, linewidth=1, linestyle="--", color="black")  # Eixo X
    pyplot.axvline(x=0, linewidth=1, linestyle="--", color="black")  # Eixo Y
    pyplot.plot(x, y, linestyle="--", color="black") # Meio-círculo

    # A
    pyplot.plot([-radius, a - radius], [0, 0], linewidth=2, color="blue", label="A")

    # B
    pyplot.plot([radius, radius - b], [0, 0], linewidth=2, color="orange", label="B")

    # Média aritmética
    pyplot.plot([0, 0], [0, ma], linewidth=2, color="green", label="M. aritmética")

    # Média geométrica
    pyplot.plot([diff, diff], [0, mg], linewidth=2, color="purple", label="M. geométrica")

    # Média harmônica
    pyplot.plot([diff, diff - mh * np.cos(alpha)], [mg, mg - mh * np.sin(alpha)], linewidth=2, color="pink", label="M. harmônica")
    pyplot.plot([diff, diff - mh * np.cos(alpha)], [0, mg - mh * np.sin(alpha)], linestyle="--", linewidth=2, color="pink")

    # Valor eficaz / Raiz do valor quadrático médio
    pyplot.plot([0, diff], [np.sqrt(ve**2 - (diff)**2), 0], linewidth=2, color="red", label="Valor eficaz")

    pyplot.plot(0, 0, marker=".", markersize=8, color="black")  # Origem
    pyplot.plot(-radius, 0, marker=".", markersize=8, color="black")  # Fim esquerdo do meio círculo
    pyplot.plot(radius, 0, marker=".", markersize=8, color="black")  # Fim direito do meio círculo
    pyplot.plot(a - radius, 0, marker=".", markersize=8,color="black")  # União entre A e B
    pyplot.plot(0, radius, marker=".", markersize=8, color="black")  # União entre Média aritmética e Valor eficaz
    pyplot.plot(a - radius, np.sqrt(a * b), marker=".", markersize=8, color="black")  # União entre Média geométrica e Média harmômica

    # Mostrar gráfico
    pyplot.legend(loc="upper right")
    pyplot.show()


if __name__ == "__main__":
    main()

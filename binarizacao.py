import cv2
from matplotlib import pyplot
import numpy


def obter_imagem():
    imagem = cv2.imread("imagens/img777.jpg", 0)

    return imagem


def exibir_imagem(imagem):
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_imagem(imagem):
    cv2.imwrite("imagens/img-binarizada.jpg", imagem)


def aplicar_scharr_x_y(imagem):
    imagem_com_scharr_x = cv2.Scharr(imagem, cv2.CV_64F, 1, 0)
    imagem_com_scharr_y = cv2.Scharr(imagem, cv2.CV_64F, 0, 1)

    return imagem_com_scharr_x + imagem_com_scharr_y


def aplicar_sobel_x(imagem):
    imagem_com_sobel = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)

    return imagem_com_sobel


def aplicar_sobel_y(imagem):
    imagem_com_sobel = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)

    return imagem_com_sobel


def aplicar_sobel_x_y(imagem):
    imagem_com_sobel_x_y = aplicar_sobel_x(imagem) + aplicar_sobel_y(imagem)

    return imagem_com_sobel_x_y


def main():
    salvar_imagem(aplicar_scharr_x_y(obter_imagem()))


if __name__ == '__main__':
    main()

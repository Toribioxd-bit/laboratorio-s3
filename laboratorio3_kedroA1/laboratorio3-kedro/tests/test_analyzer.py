import numpy as np
from laboratorio3_kedro.pipelines.histogram.analyzer import ImageAnalyzer

def test_calcular_histograma_devuelve_256_valores():
    imagen = np.zeros((10, 10), dtype=np.uint8)
    analyzer = ImageAnalyzer()

    histograma = analyzer.calcular_histograma(imagen)

    assert len(histograma) == 256


def test_clasificar_imagen_oscura():
    histograma = np.zeros(256)
    histograma[10] = 100
    histograma[200] = 10

    analyzer = ImageAnalyzer()

    resultado = analyzer.clasificar_imagen(histograma)

    assert resultado == "oscura"
import cv2
import matplotlib.pyplot as plt
import os

from laboratorio3_kedro.pipelines.histogram.analyzer import ImageAnalyzer


def analizar_imagen(filepath: str) -> dict:
    """Carga una imagen y devuelve su análisis"""

    imagen = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen: {filepath}")

    analyzer = ImageAnalyzer()
    histograma = analyzer.calcular_histograma(imagen)
    clasificacion = analyzer.clasificar_imagen(histograma)

    # 📊 GUARDAR IMAGEN DEL HISTOGRAMA
    os.makedirs("data/08_reporting", exist_ok=True)

    plt.figure()
    plt.plot(histograma)
    plt.title("Histograma de la imagen")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")
    plt.savefig("data/08_reporting/histograma.png")
    plt.close()

    return {
        "ruta_imagen": filepath,
        "clasificacion": clasificacion,
        "histograma": histograma.tolist(),
    }
from kedro.pipeline import Pipeline, node
from laboratorio3_kedro.pipelines.histogram.nodes import analizar_imagen

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=analizar_imagen,
            inputs="params:image_path",
            outputs="resultado_analisis",
            name="analizar_imagen_node",
        )
    ])
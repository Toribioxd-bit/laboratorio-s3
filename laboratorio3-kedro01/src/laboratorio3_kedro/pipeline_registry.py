from kedro.pipeline import Pipeline
from laboratorio3_kedro.pipelines.histogram.pipeline import create_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    pipeline = create_pipeline()

    return {
        "__default__": pipeline,
        "histogram": pipeline,
    }
from dagster import asset
from chess_pipeline.chess_pipeline_integration import run_chess_pipeline

@asset
def chess_dlt_asset():
    return run_chess_pipeline()
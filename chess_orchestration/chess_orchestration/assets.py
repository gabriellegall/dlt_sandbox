from dagster import asset

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from chess_pipeline import run_chess_pipeline

@asset
def chess_dlt_asset():
    return run_chess_pipeline()

chess_dlt_asset() # To remove once fixed
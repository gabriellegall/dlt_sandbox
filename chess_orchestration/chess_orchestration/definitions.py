from dagster import Definitions
from .assets import chess_dlt_asset

defs = Definitions(
    assets=[chess_dlt_asset],
)
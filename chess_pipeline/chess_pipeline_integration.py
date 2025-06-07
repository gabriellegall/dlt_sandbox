import dlt
from chess import source

def run_pipeline():
    pipeline = dlt.pipeline(
        pipeline_name="chess_pipeline",
        destination='postgres',
        dataset_name="chess_players_games_data",
    )

    data = source(
        ["zundorn", "piwi100"],
        start_month="2024/01",
        end_month="2025/06"
    )

    info = pipeline.run(
        data.with_resources("players_games"),
        write_disposition="merge",
        primary_key="uuid"
    )

    print(info)

if __name__ == "__main__":
    run_pipeline()
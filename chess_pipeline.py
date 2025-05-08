import dlt
from chess import source

if __name__ == "__main__":

    # configure the pipeline: provide the destination and dataset name to which the data should go
    pipeline = dlt.pipeline(
        pipeline_name="chess_pipeline",
        destination='postgres',
        dataset_name="chess_players_games_data",
    )

    # create the data source by providing a list of players and start/end month in YYYY/MM format
    data = source(
        ["piwi100"],
        start_month="2024/01",
        end_month="2025/05",
    )

    # load the "players_games" and "players_profiles" out of all the possible resources
    info = pipeline.run(data.with_resources("players_games"))
    print(info)
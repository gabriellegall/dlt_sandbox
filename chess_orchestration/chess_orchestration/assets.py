import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) #C:\Users\User\dlt_sandbox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'chess_pipeline'))) #C:\Users\User\dlt_sandbox\chess_pipeline
from chess_pipeline import chess_pipeline_integration
from dagster import asset

@asset
def chess_dlt_asset():
    return chess_pipeline_integration.run_pipeline()

chess_dlt_asset()

# https://docs.dagster.io/integrations/libraries/dlt
# https://dlthub.com/blog/dlt-dagster
# https://pipeline2insights.substack.com/p/data-ingestion-with-dlt-bluesky-to-s3-on-dagster
# https://github.com/dlt-hub/dlt-dagster-demo/tree/main/github-issues/github_issues
# https://dlthub.com/docs/general-usage/credentials/setup#secretstoml-and-configtoml
# https://dlthub.com/docs/walkthroughs/deploy-a-pipeline/deploy-with-dagster
# https://github.com/dlt-hub/dlthub-education/blob/main/workshops/workshop_august_2024/part2/deployment/deploy_dagster/README.md
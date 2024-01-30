from Predicting_rainfall_project import logger
from Predicting_rainfall_project.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


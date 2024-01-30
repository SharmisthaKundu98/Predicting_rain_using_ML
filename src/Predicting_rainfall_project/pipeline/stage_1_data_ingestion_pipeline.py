from Predicting_rainfall_project.config.configaration import ConfigurationManager
from Predicting_rainfall_project.components.data_ingestion_components import DataIngestion
from Predicting_rainfall_project import logger

STAGE_NAME = "Data ingestion stage"

# create data_ingestion_pipeline class
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        # get the configuration details using config manager
        config = ConfigurationManager()
        # initialize the data ingestion component with the configurations
        data_ingestion_config = config.get_data_ingestion_config()
        # call the method of data ingestion component to read and process the data
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # download the data
        data_ingestion.download_file()
        # unzip the file
        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionTrainingPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        
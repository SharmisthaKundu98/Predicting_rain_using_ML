from Predicting_rainfall_project.constants import *
from Predicting_rainfall_project.utils.common import read_yaml , create_directories
from Predicting_rainfall_project.entity.config_entity import DataIngestionConfig

#configuration manager class

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config1 = self.config.data_ingestion

        create_directories([config1.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config1.root_dir,
            source_URL= config1.source_URL,
            local_data_file= config1.local_data_file,
            unzip_dir= config1.unzip_dir 
        )

        return data_ingestion_config


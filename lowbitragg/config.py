import os

class Config:
    def __init__(self):
        # Model Settings
        self.model_name = 'default_model'
        self.model_version = '1.0'

        # Retriever Configuration
        self.retriever_type = 'default_retriever'
        self.retriever_params = {'param1': 'value1', 'param2': 'value2'}

        # Compression Parameters
        self.compression_enabled = True
        self.compression_level = 5

        # Environment Variable Support
        self.load_environment_variables()

    def load_environment_variables(self):
        self.model_name = os.getenv('MODEL_NAME', self.model_name)
        self.model_version = os.getenv('MODEL_VERSION', self.model_version)
        self.retriever_type = os.getenv('RETRIEVER_TYPE', self.retriever_type)
        self.compression_enabled = os.getenv('COMPRESSION_ENABLED', self.compression_enabled)
        self.compression_level = int(os.getenv('COMPRESSION_LEVEL', self.compression_level))

    def __repr__(self):
        return f'Config(model_name={self.model_name}, model_version={self.model_version}, retriever_type={self.retriever_type}, compression_enabled={self.compression_enabled}, compression_level={self.compression_level})'
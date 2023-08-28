import os
from fb01_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- fb01_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- fb01_models/config: Production')
    case _:
        config = ConfigLocal()
        print('- fb01_models/config: Local')
    
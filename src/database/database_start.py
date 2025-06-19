from database_config import DatabaseConfig
from sqlalchemy import create_engine
from database_models import Base

if __name__ == '__main__':
    database_operation = DatabaseConfig()

    connection_string = database_operation.connection_string
    
    engine = create_engine(connection_string)
    
    print("Dropping all tables")
    Base.metadata.drop_all(engine)


    print("Creating all tables")    
    Base.metadata.create_all(engine)
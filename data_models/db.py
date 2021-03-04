from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf.config import DevelopmentConfig


engine = create_engine(
    "mysql+pymysql://"
    + DevelopmentConfig.db_username
    + ":"
    + DevelopmentConfig.db_password
    + "@"
    + DevelopmentConfig.db_host
    + "/"
    + DevelopmentConfig.db_database,
    convert_unicode=True,
    pool_pre_ping=True,
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from data_models.entity import store
    Base.metadata.create_all(bind=engine)

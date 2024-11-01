from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parãmetros para conexão com banco de dados.
db_user = "user"
db_password = "123"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço/caminho para conexão com banco de dados Mysql.
DATABASE = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#conctando ao banco de dados.
db = create_engine(DATABASE)
Session = sessionmaker(bind=db)
sesssion = Session()

#gerenciado conexão com banco de dados.
@contextmanager
def get_db():
    db = Session()
    try:
         yield db
         db.commit()
    except Exception as error:
         db.rollback()
         raise error
    finally:
         db.close()
import model
from database import engine

model.Base.metadata.create_all(engine)
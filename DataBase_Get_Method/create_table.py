from database import engine
import model

model.Base.metadata.create_all(bind = engine )
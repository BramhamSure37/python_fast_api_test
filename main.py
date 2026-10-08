from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Product
from database import SessionLocal, engine
import database_models
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"])

from sqlalchemy.orm import Session
database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(
        id=1,
        name="Product 1",
        description="Description 1",
        price=10.0,
        quantity=5
    ),
    Product(
        id=2,
        name="Product 2",
        description="Description 2",
        price=20.0,
        quantity=10
    ),
    Product(
        id=3,
        name="Product 3",
        description="Description 3",
        price=30.0,
        quantity=15
    )
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(
                database_models.Product(
                    **product.model_dump()
                )
            )

        db.commit()

    db.close()


# GET all products
@app.get("/products")
def get_products(DB :Session = Depends(get_db)):
    db_products = DB.query(database_models.Product).all()
    return db_products
    # db connection
    # db = SessionLocal()
    # query
    # db.query()

    return products


# GET product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int, DB: Session = Depends(get_db)):
        db_product  = DB.query(database_models.Product).filter(database_models.Product.id == id).first() 
        if db_product:
            return db_product
        return 'product not found'

    


# POST - Add product
@app.post("/products")
def add_product(product: Product, DB: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    DB.add(db_product)
    DB.commit()
    DB.refresh(db_product)
    return db_product


# PUT - Update product
@app.put("/products/{id}")
def update_product(id: int, product: Product, DB: Session = Depends(get_db)):
     db_product  = DB.query(database_models.Product).filter(database_models.Product.id == id).first() 
     if db_product:
         
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        DB.commit()
        return "product updated"
     else:
        return 'product not found'


    



# DELETE - Delete product
@app.delete("/products/{id}")
def delete_product(id: int, DB: Session = Depends(get_db)):
    db_product  = DB.query(database_models.Product).filter(database_models.Product.id == id).first() 
    if db_product:
        DB.delete(db_product)
        DB.commit()
        return "Product deleted"
    else:
        return 'product not found'

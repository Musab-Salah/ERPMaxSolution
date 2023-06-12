from src.models import Product, ProductMovement
from src import  db


class ProductManager():
    def get_all_product():
        products = Product.query.all()
        return products
    

    def add_product(request):
            name = request.form['name']
            new_product =  Product(
                product_name=name,
            )
            db.session.add(new_product)
            try:
                db.session.commit()
                return True
            except Exception :
                db.session.rollback() 
                return False  

    def edit_product(request,product):
        product.product_name = request.form['name']
        try:
            db.session.commit()
            return True
        except Exception :
            db.session.rollback() 
            return False  


    def delete_product(id):
        product = Product.query.filter_by(product_id=id).first()
        product_movement = ProductMovement.query.filter_by(product_id=id).first()
        if product and not product_movement:
            try:
                db.session.delete(product)
                db.session.commit()
                return True
            except Exception :
                db.session.rollback() 
                return False  
        else: return False  
  
                    
    

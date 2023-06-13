from src.models import Product, ProductMovement
from src import  db


class ProductManager():
    def get_all_product():
        products = Product.query.all()
        return products
    
    def get_product(id):
        product = Product.query.get(id)
        return product
    
    def add_edit_product(request, product):
            name = request.form['name']
            if not product:
                new_product =  Product(
                    product_name=name,
                )
                db.session.add(new_product)
            else :
                product.product_name = name
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
  
                    
    

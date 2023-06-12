from sqlalchemy import or_
from src.models import  ProductMovement
from src import  db


class ProductMovementManager():
    def get_all_product_movement():
        return ProductMovement.query.all()
         
    def add_product_movement(request):
        from_id = request.form['from']
        to_id = request.form['to']
        product_id = request.form['product']
        qty = request.form['qty']
   
        movements = ProductMovement.query.filter(
            or_(
                ProductMovement.to_location_id == to_id,
                ProductMovement.to_location_id == from_id
            ),
            ProductMovement.product_id == product_id
        ).order_by(ProductMovement.timestamp.desc()).first() 

        if movements is not None :
          total=movements.qty-int(qty)
        else:total=-1  
        if int(qty) > 0:
            if from_id and to_id:
                if  total >=0:
                    new_product_movement = ProductMovement(
                        from_location_id=from_id,
                        to_location_id=to_id,
                        qty=qty,
                        product_id=product_id
                    )
                    db.session.add(new_product_movement)
                else:
                    return False
            elif (from_id and not to_id) : 
                if total >=0 :              
                    new_product_movement = ProductMovement(
                        from_location_id=from_id,
                        to_location_id=to_id,
                        qty=qty,
                        product_id=product_id
                    )
                    db.session.add(new_product_movement)  
                else:
                    return False
            elif (to_id and not from_id):
                    new_product_movement = ProductMovement(
                        from_location_id=from_id,
                        to_location_id=to_id,
                        qty=qty,
                        product_id=product_id
                    )
                    db.session.add(new_product_movement)  
            try:
                db.session.commit()
                return True
            except Exception:
                db.session.rollback()
                return False
        else:
            return False


    def edit_product_movement(request,movement):
        movement.from_location_id = request.form['from']
        movement.to_location_id = request.form['to']
        movement.product_id = request.form['product']
        movement.qty = request.form['qty']        
        try:
            db.session.commit()
            return True
        except Exception :
            db.session.rollback() 
            return False  


    def delete_product_movement(id):
        movement = ProductMovement.query.filter_by(movement_id=id).first()
        try:
            db.session.delete(movement)
            db.session.commit()
            return True
        except Exception :
            db.session.rollback() 
            return False  
  
                    
    

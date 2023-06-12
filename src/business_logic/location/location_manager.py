from src.models import Location,ProductMovement
from src import  db


class LocationManager():
    def get_all_location():
        locations = Location.query.all()
        return locations
    

    def add_location(request):
            name = request.form['name']
            new_location =  Location(
                location_name=name,
            )
            db.session.add(new_location)
            try:
                db.session.commit()
                return True
            except Exception :
                db.session.rollback() 
                return False  

    def edit_location(request,location):
        location.location_name = request.form['name']
        try:
            db.session.commit()
            return True
        except Exception :
            db.session.rollback() 
            return False  


    def delete_location(id):
        location = Location.query.filter_by(location_id=id).first()
        product_movement = ProductMovement.query.filter_by(movement_id=id).first()
        if location and not product_movement:
            try:
                db.session.delete(location)
                db.session.commit()
                return True
            except Exception :
                db.session.rollback() 
                return False  
        else: return False  
  
                    
    

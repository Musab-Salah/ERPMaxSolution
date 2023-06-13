from src.models import Location,ProductMovement
from src import  db


class LocationManager():
    def get_all_location():
        locations = Location.query.all()
        return locations
    
    def get_location(id):
        location = Location.query.get(id)
        return location
    

    def add_edit_location(request, location):
            name = request.form['name']
            if not location:
                new_location =  Location(
                    location_name=name,
                )
                db.session.add(new_location)
            else: 
                location.location_name = name
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
  
                    
    

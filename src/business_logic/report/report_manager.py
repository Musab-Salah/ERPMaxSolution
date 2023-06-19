from src.models import Product, Location, ProductMovement
class ReportManager:
    def get_product_balance():
        locations = Location.query.all()
        products = Product.query.all()
        movements = ProductMovement.query.filter(
            (ProductMovement.to_location_id.in_([location.location_id for location in locations])) |
            (ProductMovement.from_location_id.in_([location.location_id for location in locations]))
        ).all()

        balance = {}

        for location in locations:
            products_in_location = []
            
            for product in products:
                total_in = sum(movement.qty for movement in movements if
                            movement.to_location_id == location.location_id and movement.product_id == product.product_id)
                total_out = sum(movement.qty for movement in movements if
                                movement.from_location_id == location.location_id and movement.product_id == product.product_id)

                qty = total_in - total_out
                
                if qty >= 0 and (total_in > 0 or total_out > 0):
                    products_in_location.append({
                        'Product ID': product.product_id,
                        'Product Name': product.product_name,
                        'Qty': qty
                    })
            
            if products_in_location:
                balance[location.location_id] = {
                    'Location ID': location.location_id,
                    'Location Name': location.location_name,
                    'Products': products_in_location
                }
        
        return balance


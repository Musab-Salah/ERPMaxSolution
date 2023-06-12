from src.models import Product, Location, ProductMovement
class ReportManager:
    def get_product_balance():
        locations = Location.query.all()
        products = Product.query.all()
        balance = {}
        for location in locations:
            products_in_location = []
            for product in products:
                movements_in = ProductMovement.query.filter_by(to_location=location, product_id=product.product_id).all()
                total_in = 0
                for movement in movements_in:
                    total_in += movement.qty
                
                movements_out = ProductMovement.query.filter_by(from_location=location, product_id=product.product_id).all()
                total_out = 0
                for movement in movements_out:
                    total_out += movement.qty

                qty = total_in - total_out
                if qty >= 0 and (movements_out or movements_in):
                    products_in_location.append({
                        'Product': product.product_name,
                        'Qty': qty
                    })        
            if products_in_location:
                balance[location.location_name] = products_in_location
        return balance
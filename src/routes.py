from src.business_logic.report.report_manager import ReportManager
from src.business_logic.product.product_manager import ProductManager
from src.business_logic.location.location_manager import LocationManager
from src.business_logic.product_movement.product_movement_manager import ProductMovementManager

from src.models import Product, Location, ProductMovement
from src import app
from flask import  render_template, request


@app.route("/")
def index():
    balance = ReportManager.get_product_balance()
    return render_template('/report/report.html', balance=balance)

# Product
@app.route('/products')
def get_all_product():
    return render_template('/product/products.html', products=ProductManager.get_all_product())

@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        if ProductManager.add_edit_product(request,None):
            return render_template('success_faild.html', success=True,redirect_to='/products')
        else: return render_template('success_faild.html', success=False,redirect_to='/products')
    else :return render_template('/product/add_edit_product.html')


@app.route('/product/edit/<string:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.filter_by(product_id=id).first()
    if request.method == 'POST':
        if ProductManager.add_edit_product(request,product):
            return render_template('success_faild.html', success=True,redirect_to='/products')
        else: return render_template('success_faild.html', success=False,redirect_to='/products')
    else :return render_template('/product/add_edit_product.html', product=product)


@app.route('/product/delete/<string:id>', methods=['GET', 'POST'])
def delete_product(id):
    if request.method == 'POST':
        if ProductManager.delete_product(id):
            return render_template('success_faild.html', success=True,redirect_to='/products')
        else: return render_template('success_faild.html', success=False,redirect_to='/products')              
    else :
        return render_template('delete_confirm.html', product=ProductManager.get_product(id))


 # Location
@app.route('/locations')
def get_all_location():
    return render_template('/location/locations.html', locations=LocationManager.get_all_location())

@app.route('/location/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        if LocationManager.add_edit_location(request,None):
            return render_template('success_faild.html', success=True,redirect_to='/locations')
        else: return render_template('success_faild.html', success=False,redirect_to='/locations')
    else :return render_template('/location/add_edit_location.html')


@app.route('/location/edit/<string:id>', methods=['GET', 'POST'])
def edit_location(id):
    location = Location.query.filter_by(location_id=id).first()
    if request.method == 'POST':
        if LocationManager.add_edit_location(request,location):
            return render_template('success_faild.html', success=True,redirect_to='/locations')
        else: return render_template('success_faild.html', success=False,redirect_to='/locations')
    else :return render_template('/location/add_edit_location.html', location=location)


@app.route('/location/delete/<string:id>', methods=['GET', 'POST'])
def delete_location(id):
    if request.method == 'POST':
        if LocationManager.delete_location(id):
            return render_template('success_faild.html', success=True,redirect_to='/locations')
        else: return render_template('success_faild.html', success=False,redirect_to='/locations')
    else :return render_template('delete_confirm.html', location=LocationManager.get_location(id))


# ProductMovement

@app.route('/product_movements')
def get_all_movement():
    return render_template('/product_movement/product_movements.html', movements=ProductMovementManager.get_all_product_movement())

@app.route('/product_movement/add', methods=['GET', 'POST'])
def add_movement():
    products = Product.query.all()
    locations = Location.query.all()
    if request.method == 'POST':
        if ProductMovementManager.add_edit_product_movement(request,None):
            return render_template('success_faild.html', success=True,redirect_to='/product_movements')
        else: return render_template('success_faild.html', success=False,redirect_to='/product_movements')    
    else :return render_template('/product_movement/add_edit_product_movement.html',products=products ,locations=locations)


@app.route('/product_movement/edit/<string:id>', methods=['GET', 'POST'])
def edit_movement(id):
    movement = ProductMovement.query.filter_by(movement_id=id).first()
    products = Product.query.all()
    locations = Location.query.all()
    if request.method == 'POST':
        if ProductMovementManager.add_edit_product_movement(request,movement):
            return render_template('success_faild.html', success=True,redirect_to='/product_movements')
        else: return render_template('success_faild.html', success=False,redirect_to='/product_movements')    
    else :return render_template('/product_movement/add_edit_product_movement.html', movement=movement,products=products ,locations=locations)

@app.route('/product_movement/delete/<string:id>', methods=['GET', 'POST'])
def delete_movement(id):
    if request.method == 'POST':
        if ProductMovementManager.delete_product_movement(id):
            return render_template('success_faild.html', success=True,redirect_to='/product_movements')
        else: return render_template('success_faild.html', success=False,redirect_to='/product_movements')    
    else :return render_template('delete_confirm.html', movement=ProductMovementManager.get_product_movement(id))



"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand).filter(Brand.founded=='1903',
    Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
db.session.query(Brand).filter(db.or_(Brand.discontinued!=None,
    Brand.founded<1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Brand.name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    print db.session.query(Model.name, Model.brand_name, Brand.
        headquarters).filter(Model.year==year)
    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_cars = db.session.query(Brand.name, Model.name).all()
    for car in all_cars:
        print car


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# This is a Flask-SQLAlchemy Query Object. This is an object that contains all
# data from the brands table where the name is 'Ford'. No records were returned because
# we did not actually ask to fetch a record with this query (i.e. .all(), .one() etc. )

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that associates data between two other tables
# in a database. It manages a many-to-many relationship (e.g. between products
# and purchasers). Association tables can be "true" association tables, with no
# additional data, or they can contain additional important info, as with products,
# purchasers or customers, and order numbers.


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()
    
def get_models_between(start_year, end_year):
    return Model.query.filter(Model.year >= start_year,
        Model.year < end_year).all()


































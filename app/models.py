from . import db
from datetime import datetime

# entidades: User, Perfil, Category, Product, Buy


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String(94))
    email = db.Column(db.String(100), unique=True, nullable=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfiles.id'), nullable=False)
    #perfiles = db.relationship('Perfil', backref=db.backref('perfiles', lazy=True))

    def __repr__(self):
        return '<Tipo Usuario %r>' % self.username

    @classmethod
    def users_list(cls):
        try:
            user = User.query.all()
            return user
        except Exception as ex:
            raise Exception(ex)



class Perfil(db.Model):

    __tablename__ = 'perfiles'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30))
    user_id = db.relationship('User')

    def __repr__(self):
        return '<Tipo Usuario %r>' % self.description


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    product_id = db.relationship('Product')

    def __repr__(self):
        return '<Category: %r>' % self.name


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    price = db.Column(db.REAL)
    stock = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Product: %r>' % self.description

#
# class Buy(db.Model):
#      __tablename__ = 'buys'
#      uuid = db.Column(db.String(36), primary_key=True)
#      created_at = db.Column(db.DateTime, default=datetime.utcnow())



#     user_id = db.Column()
#     product_id = db.Column()
from src import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Serial, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    alumni = db.relationship(
        'Alumni',
        uselist=False,
        back_populates='users'
    )

    def __init__(self, name=None, email=None, image_url=None):
        self.name = name
        self.email = email
        self.image_url = image_url

    def __repr__(self):
        return '<User {0}>'.format(self.name)


class Alumnus(db.Model):

    __tablename__ = "alumni"

    alumnus_id = db.Column(db.Serial, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    country_of_origin = db.Column(db.String, nullable=False)
    high_school = db.Column(db.String, nullable=False)
    undergrad_school = db.Column(db.String)
    graduate_school = db.Column(db.String)
    usap_class = db.Column(db.Integer, nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)
    city_of_residence = db.Column(db.Integer, nullable=False)
    country_of_residence = db.Column(db.Column, nullable=False)

    work_history = db.relationship('WorkHistory', backref='alumni')
    emails = db.relationship('Email', backref='alumni')
    phone_numbers = db.relationship('PhoneNumber', backref='alumni')
    majors = db.relationship('Major', backref='alumni')
    minors = db.relationship('Minor', backref='alumni')
    expertise = db.relationship('Expertise', backref='alumni')
    sectors = db.relationship('Sectors', backref='alumni')
    user = db.relationship(
        'User',
        uselist=False,
        back_populates='alumni'
    )

    def __init__(self, image_url=None, first_name=None,
                 last_name=None, country_of_origin=None,
                 high_school=None, undergrad_school=None,
                 graduate_school=None, usap_class=None,
                 graduation_year=None, city_of_residence=None,
                 country_of_residence=None):

        self.image_url = image_url
        self.first_name = first_name
        self.last_name = last_name
        self.country_of_origin = country_of_origin
        self.high_school = high_school
        self.undergrad_school = undergrad_school
        self.graduate_school = graduate_school
        self.usap_class = usap_class
        self.graduation_year = graduation_year
        self.city_of_residence = city_of_residence
        self.country_of_residence = country_of_residence


class WorkHistory(db.Model):

    __tablename__ = "work_history"

    id = db.Column(db.Serial, primary_key=True)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )
    company_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String, nullable=False)

    def __init__(self, company_name=None, city=None, country=None,
                 start_date=None, end_date=None, title=None):

        self.company_name = company_name
        self.city = city
        self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.title = title


class Email(db.Model):

    __tablename__ = "emails"

    id = db.Column(db.Serial, primary_key=True)
    address = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )


class PhoneNumber(db.Model):

    __tablename__ = "phone_numbers"

    id = db.Column(db.Serial, primary_key=True)
    number = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )


class Major(db.Model):

    __tablename__ = "majors"

    id = db.Column(db.Serial, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )


class Minor(db.Model):

    __tablename__ = "minors"

    id = db.Column(db.Serial, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )


class Expertise(db.Model):

    __tablename__ = "expertise"

    id = db.Column(db.Serial, primary_key=True)
    skill = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )


class Sector(db.Model):

    __tablename__ = "majors"

    id = db.Column(db.Serial, primary_key=True)
    industry = db.Column(db.String, nullable=False)
    alumnus_id = db.Column(
        db.Integer,
        db.ForeignKey('Alumni.alumnus_id')
    )

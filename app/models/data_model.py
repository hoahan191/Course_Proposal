from ..models.db import db

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(255), unique=True, nullable=False)
    courses = db.relationship('Course', backref='category', lazy=True)
    skills = db.relationship('Skill', backref='category', lazy=True)

class Provider(db.Model):
    __tablename__ = 'provider'
    provider_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provider_name = db.Column(db.String(255), unique=False, nullable=False)
    courses = db.relationship('Course', backref='provider', lazy=True)

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(255), unique=True, nullable=False)
    course_description = db.Column(db.String(255), unique=True, nullable=True)
    course_rate = db.Column(db.Integer,unique=False, nullable=True)
    course_path = db.Column(db.String(255),unique=True , nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.provider_id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id', ondelete='CASCADE'), nullable=False)
    course_programming_languages = db.relationship('CourseProgrammingLanguage', backref='course', lazy=True)

class CourseProgrammingLanguage(db.Model):
    __tablename__ = 'course_programming_language'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id', ondelete='CASCADE'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('programming_language.language_id'), nullable=False)

class ProgrammingLanguage(db.Model):
    __tablename__ = 'programming_language'
    language_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language_name = db.Column(db.String(255), unique=True, nullable=False)
    course_programming_languages = db.relationship('CourseProgrammingLanguage', backref='programming_language', lazy=True)

class Skill(db.Model):
    __tablename__ = 'skill'
    skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skill_name = db.Column(db.String(255), unique=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id', ondelete='CASCADE'), nullable=False)

    
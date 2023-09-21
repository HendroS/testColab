from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
URI='postgresql://postgres:050897@localhost:5432/sherly_library' #default port 5432
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)

book_author = db.Table ('book_author', 
                        db.Column ('book_id', db.Integer, db.ForeignKey('books.book_id'), primary_key=True),
                        db.Column ('author_id', db.Integer, db. ForeignKey('authors.author_id'), primary_key=True))

class Category(db.Model):
    category_id = db.Column(db.Integer, nullable=False, primary_key=True)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text,nullable=True)
    book = db.relationship('Books', backref='category', lazy=True) #This relationship establishes a one-to-many relationship between categories and books. Each category can be associated with multiple books, and the backref='category' parameter sets up a reverse relationship from books to categories.
    
    # def __repr__(self):
    #     # return '<Category %r>' % self.genre
    #     return f'<Category {self.genre}>'
    
class Authors(db.Model):
    author_id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name= db.Column(db.String(50), nullable=True)
    nationality = db.Column(db.String(50), nullable=False)
    birthyear = db.Column(db.Integer, nullable=False)
    books = db.relationship('Books', secondary=book_author, lazy='subquery', 
                              backref=db.backref('book_author', lazy=True))
    # def __repr__(self):
    #     return f'Authors {self.first_name} {self.last_name}'

class Books(db.Model):
    book_id = db.Column (db.Integer, nullable=False, primary_key=True)
    title = db.Column (db.String(200),nullable=False)
    book_pages = db.Column (db.Integer ,nullable=True )
    publishyear = db.Column (db.Integer ,nullable=True )
    category_id = db.Column (db.Integer ,db.ForeignKey('category.category_id'),nullable=True )
    authors = db.relationship('Authors', secondary=book_author, lazy='subquery', 
                              backref=db.backref('book_author', lazy=True))
    # tags = db.relationship('Tag', secondary=tags, lazy='subquery',
    #     backref=db.backref('pages', lazy=True))

@app.route('/')
def home():
	return {
		'message': 'Welcome to building RESTful APIs with Flask and SQLAlchemy'
	}

@app.route('/categories',methods=['GET', 'POST'])
def category():
    if request.method =='GET':
        return jsonify ([{'category_id':c.category_id,
                        'genre':c.genre,
                        'description':c.description,
                        'book': [b.title for b in c.book]} for c in Category.query.all()])
    # a=Category()
    # categories=a.query.all()
    # result=[]
    # for c in categories :
    #     print(c)
    #     books=[]
    #     for b in c.book :
    #         books.append(b.title)
    #     result.append({'category_id':c.category_id,
    #                    'genre':c.genre,
    #                    'description':c.description,
    #                    'book': books})
    # return {
	# 		'result':result
	# 		}
    elif request.method == 'POST' :
        data=request.json
        if not 'genre' in data or not 'description' in data:
            return {
			        'error': 'Bad Request',
			        'message': 'Name or email not given'
		            }, 400
        create = Category(
            genre=data['genre'],
            description=data['description']
		    )
        db.session.add(create)
        db.session.commit()
        return {'genre':create.genre,
                'description' : create.description},201
        #POST test body parameter input
        # {
        #     "genre":"tes1",
        #     "description":"tes1"
        # }
        #POST test body parameter input if description not included
        # {
        #     "genre":"tes2"
        # }

@app.route('/authors', methods=['GET','POST'])
def author():
    if request.method == 'GET':
        authors=Authors.query.all()
        result=[]
        for a in authors:
            result.append({
                        'author_id':a.author_id,
                        'author_name' : f'{a.first_name} {a.last_name}',
                        # 'first_name':a.first_name,
                        # 'last_name' : a.last_name,
                        'nationality':a.nationality,
                        'birthyear' : a.birthyear,
                        'book' : [book.title for book in a.books]})
        return {
                'result':result
			    }
    elif request.method == 'POST' :
        data=request.json
        create = Authors(
            first_name=data['first_name'],
            last_name=data['last_name'],
            nationality=data['nationality'],
            birthyear=data['birthyear']
		    )
        db.session.add(create)
        db.session.commit()
        return {'first_name':create.first_name,
                'last_name' : create.last_name,
                'nationality': create.nationality,
                'birthyear' : create.birthyear},201

@app.route('/authors/<author_id>', methods=['GET','PUT'])
def author_id(author_id):
    if request.method == 'GET':
        getauthor=Authors.query.filter_by(author_id=author_id).first_or_404(description='There is no author_id')
        return {'author_id':getauthor.author_id,
                'author_name' : f'{getauthor.first_name} {getauthor.last_name}',
                'nationality':getauthor.nationality,
                'birthyear' : getauthor.birthyear}
    elif request.method =='PUT':
        data=request.json
        putauthor=Authors.query.filter_by(author_id=author_id).first_or_404(description='There is no author_id')
        # putauthor.author_name = f'{data["first_name"]} {data["last_name"]}'
        putauthor.first_name = data['first_name']
        putauthor.last_name = data['last_name']
        putauthor.nationality = data['nationality']
        putauthor.birthyear = data['birthyear']
        db.session.commit()
        return {'author_id': putauthor.author_id,
                # 'author_name' : f'{putauthor.first_name} {putauthor.last_name}',
                'first_name' : putauthor.first_name,
                'last_name' : putauthor.last_name,
                'nationality' : putauthor.nationality,
                'birthyear' : putauthor.birthyear}


@app.route('/books')
def book():
    books=Books.query.all()
    result=[]
    for b in books:
        result.append({'book_id':b.book_id,
                       'title':b.title,
                       'book_pages':b.book_pages,
                       'publishyear' : b.publishyear,
                       'authors': [f'{author.first_name} {author.last_name}' for author in b.authors],
                       'category' : b.category.genre }) #satu buku satu kategori
    return {
			'result':result
			}

@app.route('/books/<book_id>', methods=['GET','PUT'])
def book_id(book_id):
    if request.method == 'GET':
        getbook=Books.query.filter_by(book_id=book_id).first_or_404(description='There is no author_id')
        return {'book_id' : getbook.book_id,
                'title' : getbook.title,
                'book_pages' : getbook.book_pages,
                'publishyear' : getbook.publishyear,
                'category' : getbook.category.genre,
                'author' : [f'{author.first_name} {author.last_name}' for author in getbook.authors]}

if __name__ =='__main__':
    app.run(debug=True)
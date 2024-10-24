from flask import Flask
from .database import db
from .models import taxi
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://default:k8VMOdLGi5eD@ep-white-mud-a4n1izln.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/taxis")
def taxis_route():
    taxis = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users=taxis)

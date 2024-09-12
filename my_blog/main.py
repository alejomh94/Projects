from flask import Flask, render_template, url_for, request
from post import Post
import requests
import smtplib

posts = requests.get("https://api.npoint.io/88d24b19cc700225caa4").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
OWN_EMAIL = YOUR EMAIL
OWN_PASSWORD = YOUR PASSWORD



app = Flask(__name__)


@app.route('/')
def index():
    css_url = url_for("static", filename="/css/styles.css")
    jb_url = url_for("static", filename="/js/scripts.js")
    img_favico = url_for("static", filename="/assets/favicon.ico")
    img_home = url_for("static", filename="../static/assets/img/home-bg.jpg")
    return render_template("index.html", css_url=css_url,
                           jb_url=jb_url, img_favico=img_favico, img_home=img_home,
                           all_post=post_objects)

@app.route('/about')
def about():
    css_url = url_for("static", filename="/css/styles.css")
    jb_url = url_for("static", filename="/js/scripts.js")
    img_favico = url_for("static", filename="/assets/favicon.ico")
    return render_template("about.html", css_url=css_url,
                           jb_url=jb_url, img_favico=img_favico)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    css_url = url_for("static", filename="/css/styles.css")
    jb_url = url_for("static", filename="/js/scripts.js")
    img_favico = url_for("static", filename="/assets/favicon.ico")
    return render_template("contact.html", css_url=css_url,
                           jb_url=jb_url, img_favico=img_favico, msg_sent=False)


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    css_url = url_for("static", filename="/css/styles.css")
    jb_url = url_for("static", filename="/js/scripts.js")
    img_favico = url_for("static", filename="/assets/favicon.ico")
    return render_template("post.html",  css_url=css_url,
                           jb_url=jb_url, img_favico=img_favico, post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}".encode('utf-8')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, SENT TO EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)


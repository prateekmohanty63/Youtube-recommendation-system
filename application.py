from flask import Flask,render_template,request

import running_youtube
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search_topic")
def search_topic():
    return render_template("search_topic.html")

@app.route("/result",methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      s=""
      for key, value in result.items():
          s=value
      ss=running_youtube.main(s)
      print("ss is",ss)
      print("ss is",type(ss))
      img_url=[]
      for video in ss:
            urls = "https://img.youtube.com/vi/"+video[0]+"/maxresdefault.jpg"
            img_url.append(request.urlretrieve(url, 'image1.jpg'))
      return render_template("result.html",result = ss,url=img_url)
if __name__ == "__main__":
    app.run(debug=True)

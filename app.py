#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html", result=90.22 + (-50.60 * rate)))
    else:
        return(render_template("index.html", result="waiting......."))

if __name__ == "__main__":
    app.run()


# In[ ]:





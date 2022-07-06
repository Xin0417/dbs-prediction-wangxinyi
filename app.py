#!/usr/bin/env python
# coding: utf-8

# In[45]:


from flask import Flask,render_template,request


# In[46]:


import joblib


# In[47]:


app = Flask(__name__)


# In[48]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(requeat.form.get("rates"))
        print(rates)
        model = joblib.load("Regression.joblib")
        r = model.predict([[rates]])
        return(render_template("index.html",result = r))
    else:
        return(render_template("index.html",result = "WAITING"))


# In[49]:


if __name__ == "__main__":
    app.run()


# In[ ]:





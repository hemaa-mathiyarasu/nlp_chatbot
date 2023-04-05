from flask import Flask, render_template,url_for, request
app=Flask(__name__,template_folder='template')
@app.routr('/')
def chat():
    
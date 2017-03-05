from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def retail_anayisis_demo_flask():
	return render_template("index.html")

@app.route("/vips")
def show_vip_lists():

	#test. create pseudo vip lists for test purposes.
	vip_list = []
	vip_a = {'Gender':'male', 'Age':35, 'Last visit':'2017-03-01', 'Frequency of visit':3.5}
	vip_b = {'Gender':'female', 'Age':28, 'Last visit':'2017-03-02', 'Frequency of visit':7.5}
	vip_list.append(vip_a)
	vip_list.append(vip_b)

	return render_template("vips.html", vips = vip_list)
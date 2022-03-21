from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, get_candidate
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def list():
    return render_template('list.html', condidates=load_candidates_from_json())


@app.route("/candidate/<int:uid>")
def single(uid):
    candidate = get_candidate(uid)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, len=len(candidates))


@app.route("/skills/<skill>")
def skill(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template('skills.html', candidates=candidates, len=len(candidates), skill=skill)


app.run(debug=True)


import json

import pkg_resources


def load_candidates_from_json():

    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

data = load_candidates_from_json()


def get_candidate(candidate_id):
    for candidate in data:
        if candidate_id == candidate['id']:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }


def get_candidates_by_name(candidate_name):
   e = []
   for i in data:
        if candidate_name.lower() in i['name'].lower():
            e.append(i)
   return e
print(get_candidates_by_name('D'))


def get_candidates_by_skill(skill_name):
    r = []
    for i in data:
        skills = i['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            r.append(i)
    return r
# skills = {
#     "HTML" : "50%",
#     "CSS" : "70%",
#     "JS": "50%",
#     "PHP" : "50%"
# }
# for key, value in skills.items():
#     print(f"{key} => {value}")
myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}
for lang, frameworks in myUltimateSkills.items():
    print(f"{lang} Language:")
    print("")
    for framework, progress in frameworks.items():
        print(f"-{framework} => {progress}")
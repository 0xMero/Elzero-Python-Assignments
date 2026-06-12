# Assignment 1
# def get_score(**scores):
#     for subject, score in scores.items():
#         print(f"{subject} => {score}")
# get_score(Math=90, Science=80, Language=70)
# Assignment 2
# def get_people_scores(name="", **scores):
#     if name:
#         if scores:
#             print(f"Hello {name} This Is Your Score Table:")
#             for subject, score in scores.items():
#                 print(f"{subject} => {score}")
#         else:
#             print(f"Hello {name} You Have No Scores To Show")
#     else:
#         if scores:
#             for subject, score in scores.items():
#                 print(f"{subject} => {score}")
# get_people_scores(math="90%")
# Assignment 3
scores_list = {
    "Math"  :"90",
    "Science" : "80",
    "Language" : "70"
}
def get_the_scores(name="", **scores):
    if name:
        if scores:
            print(f"Hello {name} This Is Your Score Table:")
            for subject, score in scores.items():
                print(f"{subject} => {score}")
        else:
            print(f"Hello {name} You Have No Scores To Show")
    else:
        if scores:
            for subject, score in scores.items():
                print(f"{subject} => {score}")
get_the_scores(**scores_list)
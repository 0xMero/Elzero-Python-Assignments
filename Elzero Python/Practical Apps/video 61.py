def show_skills(name, *skills, **skills_with_progress):
    print(f"Hello {name}\nSkills without Progress:")
    for skill in skills:
        print(f"{skill}")
    print(f"Skills with progress:")
    for skill_with_progress, progress in skills_with_progress.items():
        print(f"{skill_with_progress} => {progress}")
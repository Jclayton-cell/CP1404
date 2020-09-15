from Practicals.Prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
for language in languages:
    print(language)
    if language.is_dynamic():
        print("***** {} is dynamic".format(language.name))
    else:
        print("***** {} is not dynamic :(".format(language.name))

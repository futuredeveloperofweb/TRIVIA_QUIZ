from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.quiz.models import Quiz, Question, Option

User = get_user_model()


class Command(BaseCommand):
    help = (
        "Generate 10 quizzes with 10 questions each on programming "
        "languages (Python, JavaScript, HTML) for beginners"
    )

    quizzes_data = {
        "Python": [
            {
                "question": 'What is a correct syntax to output "Hello World" in Python?',
                "options": [
                    {"text": 'print("Hello World")', "is_correct": True},
                    {"text": 'echo "Hello World"', "is_correct": False},
                    {"text": 'p("Hello World")', "is_correct": False},
                    {"text": 'printf("Hello World")', "is_correct": False},
                ],
            },
            {
                "question": "How do you insert COMMENTS in Python code?",
                "options": [
                    {"text": "#This is a comment", "is_correct": True},
                    {"text": "//This is a comment", "is_correct": False},
                    {"text": "/*This is a comment*/", "is_correct": False},
                    {"text": "--This is a comment", "is_correct": False},
                ],
            },
            {
                "question": "Which one is NOT a legal variable name?",
                "options": [
                    {"text": "my-var", "is_correct": True},
                    {"text": "my_var", "is_correct": False},
                    {"text": "myVar", "is_correct": False},
                    {"text": "_myvar", "is_correct": False},
                ],
            },
            {
                "question": "How do you create a variable with the numeric value 5?",
                "options": [
                    {"text": "x = 5", "is_correct": True},
                    {"text": "x = int(5)", "is_correct": True},
                    {"text": "x = 5;", "is_correct": False},
                    {"text": "int x = 5", "is_correct": False},
                ],
            },
            {
                "question": "What is the correct file extension for Python files?",
                "options": [
                    {"text": ".py", "is_correct": True},
                    {"text": ".python", "is_correct": False},
                    {"text": ".pyt", "is_correct": False},
                    {"text": ".pt", "is_correct": False},
                ],
            },
            {
                "question": "How do you create a variable with the floating number 2.8?",
                "options": [
                    {"text": "x = 2.8", "is_correct": True},
                    {"text": "x = float(2.8)", "is_correct": True},
                    {"text": "x = 2,8", "is_correct": False},
                    {"text": "x = (2.8)", "is_correct": False},
                ],
            },
            {
                "question": "What is the correct syntax to output the type of a variable or object in Python?",
                "options": [
                    {"text": "print(type(x))", "is_correct": True},
                    {"text": "print(typeOf(x))", "is_correct": False},
                    {"text": "print(typeof(x))", "is_correct": False},
                    {"text": "print(typeof x)", "is_correct": False},
                ],
            },
            {
                "question": "Which function can be used to make a list?",
                "options": [
                    {"text": "list()", "is_correct": True},
                    {"text": "make_list()", "is_correct": False},
                    {"text": "create_list()", "is_correct": False},
                    {"text": "new_list()", "is_correct": False},
                ],
            },
            {
                "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
                "options": [
                    {"text": "strip()", "is_correct": True},
                    {"text": "trim()", "is_correct": False},
                    {"text": "len()", "is_correct": False},
                    {"text": "ptrim()", "is_correct": False},
                ],
            },
            {
                "question": "Which method can be used to return a string in upper case letters?",
                "options": [
                    {"text": "upper()", "is_correct": True},
                    {"text": "uppercase()", "is_correct": False},
                    {"text": "toUpperCase()", "is_correct": False},
                    {"text": "up()", "is_correct": False},
                ],
            },
        ],
        "JavaScript": [
            {
                "question": "Inside which HTML element do we put the JavaScript?",
                "options": [
                    {"text": "<script>", "is_correct": True},
                    {"text": "<javascript>", "is_correct": False},
                    {"text": "<js>", "is_correct": False},
                    {"text": "<scripting>", "is_correct": False},
                ],
            },
            {
                "question": "Where is the correct place to insert a JavaScript?",
                "options": [
                    {
                        "text": "Both the <head> section and the <body> section are correct",
                        "is_correct": True,
                    },
                    {"text": "The <head> section", "is_correct": False},
                    {"text": "The <body> section", "is_correct": False},
                ],
            },
            {
                "question": 'What is the correct syntax for referring to an external script called "xxx.js"?',
                "options": [
                    {"text": '<script src="xxx.js">', "is_correct": True},
                    {"text": '<script href="xxx.js">', "is_correct": False},
                    {"text": '<script name="xxx.js">', "is_correct": False},
                    {"text": '<script file="xxx.js">', "is_correct": False},
                ],
            },
            {
                "question": 'How do you write "Hello World" in an alert box?',
                "options": [
                    {"text": 'alert("Hello World");', "is_correct": True},
                    {"text": 'msg("Hello World");', "is_correct": False},
                    {"text": 'msgBox("Hello World");', "is_correct": False},
                    {"text": 'alertBox("Hello World");', "is_correct": False},
                ],
            },
            {
                "question": "How do you create a function in JavaScript?",
                "options": [
                    {"text": "function myFunction()", "is_correct": True},
                    {"text": "function:myFunction()", "is_correct": False},
                    {"text": "function = myFunction()", "is_correct": False},
                    {"text": "def myFunction()", "is_correct": False},
                ],
            },
            {
                "question": 'How do you call a function named "myFunction"?',
                "options": [
                    {"text": "myFunction()", "is_correct": True},
                    {"text": "call myFunction()", "is_correct": False},
                    {"text": "call function myFunction()", "is_correct": False},
                    {"text": "call.myFunction()", "is_correct": False},
                ],
            },
            {
                "question": "How to write an IF statement in JavaScript?",
                "options": [
                    {"text": "if (i == 5)", "is_correct": True},
                    {"text": "if i == 5 then", "is_correct": False},
                    {"text": "if i = 5 then", "is_correct": False},
                    {"text": "if (i = 5)", "is_correct": False},
                ],
            },
            {
                "question": "How does a WHILE loop start?",
                "options": [
                    {"text": "while (i <= 10)", "is_correct": True},
                    {"text": "while i = 1 to 10", "is_correct": False},
                    {"text": "while (i <= 10; i++)", "is_correct": False},
                    {"text": "while (i = 0)", "is_correct": False},
                ],
            },
            {
                "question": "How can you add a comment in a JavaScript?",
                "options": [
                    {"text": "//This is a comment", "is_correct": True},
                    {"text": "<!--This is a comment-->", "is_correct": False},
                    {"text": "**This is a comment**", "is_correct": False},
                    {"text": "!!This is a comment!!", "is_correct": False},
                ],
            },
            {
                "question": "What is the correct way to write a JavaScript array?",
                "options": [
                    {
                        "text": 'var colors = ["red", "green", "blue"]',
                        "is_correct": True,
                    },
                    {
                        "text": 'var colors = (1:"red", 2:"green", 3:"blue")',
                        "is_correct": False,
                    },
                    {
                        "text": 'var colors = "red", "green", "blue"',
                        "is_correct": False,
                    },
                    {
                        "text": 'var colors = 1 = ("red"), 2 = ("green"), 3 = ("blue")',
                        "is_correct": False,
                    },
                ],
            },
        ],
        "HTML": [
            {
                "question": "What does HTML stand for?",
                "options": [
                    {"text": "Hyper Text Markup Language", "is_correct": True},
                    {"text": "Home Tool Markup Language", "is_correct": False},
                    {
                        "text": "Hyperlinks and Text Markup Language",
                        "is_correct": False,
                    },
                ],
            },
            {
                "question": "Who is making the Web standards?",
                "options": [
                    {"text": "The World Wide Web Consortium", "is_correct": True},
                    {"text": "Google", "is_correct": False},
                    {"text": "Microsoft", "is_correct": False},
                    {"text": "Mozilla", "is_correct": False},
                ],
            },
            {
                "question": "Choose the correct HTML element for the largest heading:",
                "options": [
                    {"text": "<h1>", "is_correct": True},
                    {"text": "<h6>", "is_correct": False},
                    {"text": "<heading>", "is_correct": False},
                    {"text": "<head>", "is_correct": False},
                ],
            },
            {
                "question": "What is the correct HTML element for inserting a line break?",
                "options": [
                    {"text": "<br>", "is_correct": True},
                    {"text": "<break>", "is_correct": False},
                    {"text": "<lb>", "is_correct": False},
                    {"text": "<linebreak>", "is_correct": False},
                ],
            },
            {
                "question": "What is the correct HTML for adding a background color?",
                "options": [
                    {
                        "text": '<body style="background-color:yellow;">',
                        "is_correct": True,
                    },
                    {"text": "<background>yellow</background>", "is_correct": False},
                    {"text": '<body bg="yellow">', "is_correct": False},
                    {"text": '<body background="yellow">', "is_correct": False},
                ],
            },
            {
                "question": "Choose the correct HTML element to define important text",
                "options": [
                    {"text": "<strong>", "is_correct": True},
                    {"text": "<important>", "is_correct": False},
                    {"text": "<i>", "is_correct": False},
                    {"text": "<b>", "is_correct": False},
                ],
            },
            {
                "question": "Choose the correct HTML element to define emphasized text",
                "options": [
                    {"text": "<em>", "is_correct": True},
                    {"text": "<i>", "is_correct": False},
                    {"text": "<italic>", "is_correct": False},
                    {"text": "<e>", "is_correct": False},
                ],
            },
            {
                "question": "Which character is used to indicate an end tag?",
                "options": [
                    {"text": "/", "is_correct": True},
                    {"text": "<", "is_correct": False},
                    {"text": "*", "is_correct": False},
                    {"text": "^", "is_correct": False},
                ],
            },
            {
                "question": "How can you make a numbered list?",
                "options": [
                    {"text": "<ol>", "is_correct": True},
                    {"text": "<ul>", "is_correct": False},
                    {"text": "<dl>", "is_correct": False},
                    {"text": "<list>", "is_correct": False},
                ],
            },
            {
                "question": "How can you make a bulleted list?",
                "options": [
                    {"text": "<ul>", "is_correct": True},
                    {"text": "<ol>", "is_correct": False},
                    {"text": "<dl>", "is_correct": False},
                    {"text": "<list>", "is_correct": False},
                ],
            },
        ],
    }

    def handle(self, *args, **kwargs):
        user = User.objects.filter(is_superuser=True).first()

        if not user:
            self.stdout.write(
                self.style.ERROR("No superuser found. Please create a superuser first.")
            )
            return

        for topic, questions in self.quizzes_data.items():
            for i in range(1, 4):  # Create 3 quizzes per topic
                quiz_title = f"{topic} Quiz {i}"
                quiz_description = f"This is a beginner level quiz on {topic}."
                quiz = Quiz.objects.create(
                    title=quiz_title, description=quiz_description, created_by=user
                )
                self.stdout.write(self.style.SUCCESS(f"Created quiz: {quiz_title}"))

                for question_data in questions:
                    question_text = question_data["question"]
                    question = Question.objects.create(
                        quiz_id=quiz,
                        question_text=question_text,
                        question_type="multiple-choice",
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f"  Created question: {question_text}")
                    )

                    for option_data in question_data["options"]:
                        option_text = option_data["text"]
                        is_correct = option_data["is_correct"]
                        Option.objects.create(
                            question_id=question,
                            text=option_text,
                            is_correct=is_correct,
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'    Created option: {option_text} ({"correct" if is_correct else "incorrect"})'
                            )
                        )

        self.stdout.write(
            self.style.SUCCESS("Successfully generated quizzes and questions")
        )

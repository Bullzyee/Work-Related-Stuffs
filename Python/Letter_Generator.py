
import textwrap

social_data = []

name = input("Enter you name: ")
address = input('Enter your address: ')
zip_code = input("Enter your ZIP code: ")
phone = input("Enter your phone number: ")
email = input('Enter your email: ')
while True:
ask = input("Would you like to add professional social media account? (maximum of 2) (y/n): ")
if ask == "y":
number = int(input("How many professional social media accounts would you like to add?: "))
for i in range(1,number+1):
social_media = input("Enter the social media platform " + str(i) + ": " )
social_name = input("Enter your name in social media platform " + str(i) + ": ")
social_link = textwrap.dedent(input("Paste the link or type your name on social media " + str(i) + ": "))
social_data.append([social_media,social_name, social_link])
break
elif ask == "n":
print("")
break
else:
print("Invalid Choice")
continue


company = input("Enter the company's name: ")
company_address = input("Enter the company address: ")
date = input("Enter the date today: ")
subject = input("Enter the subject of your email: e.g. job applciation, ojt request, etc: ")
paragraph = int(input("How many pargraphs does your letter have?: "))

def read_multiline(text):
print(text + " (type 'finish' on its own line when finished):")
lines = []
while True:
line = input()
if line.strip() == "finish":
break
lines.append(line)
return "\n".join(lines)



paragraph_data= []
for z in range(1, paragraph + 1):
entry = read_multiline("Paste or type paragraph number " + str(z) + " (Exclude 'the dear hiring manager' part and 'respecfully yours')")
paragraph_data.append(entry)

letter_template_one = textwrap.dedent(r"""\documentclass[11pt]{letter}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{parskip}
\usepackage{xcolor}

\hypersetup{
colorlinks=true,
urlcolor=blue
}

\thispagestyle{empty}

\begin{document}

\begin{center}
{\LARGE\bfseries @@name@@}\\[4pt]
@@address@@, @@zip@@\\
Phone: @@phone@@ \quad | \quad
Email: \href{mailto:@@email@@}{@@email@@}\\
""")


letter_one = (letter_template_one
.replace("@@name@@", name)
.replace("@@address@@", address)
.replace("@@email@@", email)
.replace("@@phone@@", phone)
.replace("@@date@@", date)
.replace("@@zip@@", zip_code)
)


letter_template_two = textwrap.dedent(r"""@@date@@

\vspace{0.7cm}

Hiring Manager\\
@@company@@\\
@@company_address@@

\vspace{0.6cm}

\textbf{Subject: @@subject@@}

\vspace{0.5cm}

Dear Hiring Manager,

""")


letter_template_three = textwrap.dedent(r"""\vspace{0.7cm}

\noindent Respectfully yours,\\[-3pt]
\textbf{@@name@@}

\end{document}""")


letter_two = (letter_template_two
.replace("@@date@@", date)
.replace("@@company@@", company)
.replace("@@company_address@@", company_address)
.replace("@@subject@@", subject)
)


letter_three = (letter_template_three
.replace("@@name@@", name)
)


print("Copy the overleaf LaTex code below: ")
print()
print(letter_one)


for j in social_data:
print(j[0] + str(":"))
print(" \\href{" + str(j[2])+ str("}") + "{" + str(j[1])+"}")
print("\\\\")


print(textwrap.dedent(r"""\vspace{0.5cm}
\rule{\textwidth}{0.6pt}
\end{center}
\vspace{0.5cm}"""))


print(letter_two)


for c in paragraph_data:
print(c)
print("\\\\")


print(letter_three)

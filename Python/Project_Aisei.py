



import textwrap
print("INSTRUCTIONS: This program will require you to answer questions about your document. At the end of the program, a LaTEX code will be provided.")
print("Paste the code to overleaf latex on google, hit recompile, then download the PDF file.")
print("REMINDER: You can always choose to use microsoft word to format the document if your client does not approve the LaTEX document.")


print("")

def get_multiline_input(prompt):#multiple lines
print(prompt)
print("(Paste your paragraph, then press Enter(on keyboard) on an empty line to finish)")
lines = []
while True:
line = input()
if line.strip() == "":
break
lines.append(line)
return " ".join(lines)

stop = True
while stop:
print("Continue[1]")
print("Exit[2]")
c = input("Enter your choice: ")
print("")

if c == "1":
stop = False
print("What kind of document would you like to create? ")
print("")
print("BUILD A RESUME [1]")#VALIDATED
print("DEED OF ABSOLUTE SALE (MOTOR) [2]") #VAlIDATED
print("AFFIFAVIT OF LOSS [3]") #VALIDATED
print("DEED OF ABSOLUTE SALE (REAL PROPERTY)[4]") #VALIDATED
print("SPECIAL POWER OF ATTORNEY [5]")
print("DEED OF DONATION [6]") #VALIDATED
print("CONTRACT TO SELL [7]") #VALIDATED
print("RESIGNATION LETTER TEMPLATE [8]") #VALIDATED
c2 = input("Enter your choice: ")
print("")

if c2 == "1":
print("What type or resume would you like it to be?: ")
print("NEW YORK STYLE RESUME (PREFERRED BY COMPANIES: No Personal Information) [1]")
print("PHILIPPINES STYLE RESUME (WITH PICTURE (manual coding) AND PERSONAL INFORMATION) [2]")
print("")
print("CHOOSING A RESUME ALWAYS DEPENDS ON THE CUSTOMER. HOWEVER, YOU SHOULD GENERALLY NOT INCLUDE PERSONAL DETAILS LIKE HEIGHT, WEIGHT, AGE, DATE OF BIRTH, ETC ON A MODERN RESUME. NOT INCLUDING THOSE THINGS MAY HELP THE HR TO FOCUS ON YOUR SKILLS AND AVOID HIRING BIAS.")
print("NOTE: IF YOUR CUSTOMER HAS NO PROJECTS PROVIDED OR THEIR EXPERIENCE IS LIMITED, YOU MIGHT WANT TO CHOOSE OPTION 2 TO MAXIMIZE THE WHOLE PAPER ")
resume_style = input("Enter your choice: ")

if resume_style == "1":

resume_name = input("Enter the name of your client: ")
while True:
resume_number = input("Does your client have a number? (y/n): ")
if resume_number == "y":
resume_number = input("Enter the contact number of your client: ")
break
elif resume_number == "n":
resume_number = " "
break
else:
print("Invalid Choice")
while True:
resume_email = input("Does your client have an active email? (y/n): ")
if resume_email == "y":
resume_email = input("Enter the email of your client: ")
break
elif resume_email == "n":
resume_email = " "
break
else:
print("Invalid Choice")

resume_citizen = input("Enter the citizenship of your client: ")



def resume_one():
resume_template_one = textwrap.dedent(r"""
\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\usepackage[scale=0.90,lf]{FiraMono}

\definecolor{light-grey}{gray}{0.83}
\definecolor{dark-grey}{gray}{0.3}
\definecolor{text-grey}{gray}{.08}

\DeclareRobustCommand{\ebseries}{\fontseries{eb}\selectfont}
\DeclareTextFontCommand{\texteb}{\ebseries}


\usepackage{contour}
\usepackage[normalem]{ulem}
\renewcommand{\ULdepth}{1.8pt}
\contourlength{0.8pt}
\newcommand{\myuline}[1]{%
\uline{\phantom{#1}}%
\llap{\contour{white}{#1}}%
}

\usepackage{tgheros}
\renewcommand*\familydefault{\sfdefault}

\usepackage[T1]{fontenc}


\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{0in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\titleformat {\section}{
\bfseries \vspace{2pt} \raggedright \large
}{}{0em}{}[\color{light-grey} {\titlerule[2pt]} \vspace{-4pt}]


\newcommand{\resumeItem}[1]{
\item\small{
{#1 \vspace{-1pt}}
}
}

\newcommand{\resumeSubheading}[4]{
\vspace{-1pt}\item
\begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
\textbf{#1} & {\color{dark-grey}\small #2}\vspace{1pt}\\
\textit{#3} & {\color{dark-grey} \small #4}\\
\end{tabular*}\vspace{-4pt}
}

\newcommand{\resumeSubSubheading}[2]{
\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textit{\small#1} & \textit{\small #2} \\
\end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
#1 & {\color{dark-grey}} \\
\end{tabular*}\vspace{-4pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}


\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{0pt}}

\color{text-grey}



\begin{document}


\begin{center}
\textbf{\Huge @@name@@} \\ \vspace{5pt}
\small \faPhone* \texttt{@@number@@} \hspace{1pt} $|$
\hspace{1pt} \faEnvelope \hspace{2pt} \texttt{@@email@@} \hspace{1pt} $|$
\hspace{1pt} \faMapMarker* \hspace{2pt}\texttt{@@citizenship@@ Citizen}
\\ \vspace{-3pt}
\end{center}


\section{EXPERIENCE}
\resumeSubHeadingListStart
""")

resume_template_one_final = (resume_template_one
.replace("@@name@@", resume_name)
.replace("@@number@@", resume_number)
.replace("@@email@@", resume_email)
.replace("@@citizenship@@", resume_citizen)
)
print(resume_template_one_final)

resume_one()

resume_number_experience = int(input("How many experiences would you like to add in your client?: "))
resume_experience_data = []

print()
print("PARAGRAPH FORM [1]")
print("BULLETED FORM [2]")

while True:
resume_experience_description_style = input("How would you like to describe your job description in your resume?: ")
if resume_experience_description_style in ("1", "2"):
break
print("Enter your choice: ")

for i in range(1, resume_number_experience + 1):
resume_experience_entry = input("Enter company/institution number " + str(i)+ ": ")
resume_date = input("Enter your employment date in company number " + str(i) + ": ")
resume_position = input("Enter your position at company number " + str(i) + ": ")
resume_location = input("Enter the location of company number " + str(i) + ": ")

if resume_experience_description_style == "1":

description = get_multiline_input("Paste the paragraph for company number " + str(i) + ": ")
bullets = [description]
else:
num_bullets = int(input("How many bullet points would you like to add for company number " + str(i) + "?: "))
bullets = []
for b in range(1, num_bullets + 1):
bullet_text = input("Enter bullet point " + str(b) + "for company number " + str(i) + ': ')
bullets.append(bullet_text)

resume_experience_data.append([resume_experience_entry, resume_date, resume_position, resume_location, bullets])
print()

for j in resume_experience_data:
print("\\resumeSubheading")
print(" {" + j[0] + "}{" + j[1] + "}")
print(" {" + j[2] + "}{" + j[3] + "}")
print(" \\resumeItemListStart")
for bullet in j[4]:
print(" \\resumeItem{" + bullet + "}")
print(" \\resumeItemListEnd")
print("\\resumeSubHeadingListEnd")

resume_number_projects = int(input("How many projects would you like to add for your client?: "))
resume_project_data = []

for i in range(1, resume_number_projects + 1):
resume_project_name = input("Enter the name of project number " + str(i) + ": ")
resume_project_date = input("Enter the date range of project number " + str(i) + ": ")

num_bullets = int(input("How many bullet points would you like to add for project number " + str(i) + "?: "))
bullets = []
for b in range(1, num_bullets + 1):
bullet_text = input("Enter bullet point " + str(b) + " for project number " + str(i) + ": ")
bullets.append(bullet_text)

resume_project_data.append([resume_project_name, resume_project_date, bullets])
print()

print("\\section{PROJECTS}")
print("\\resumeSubHeadingListStart")
for j in resume_project_data:
print(" \\resumeProjectHeading")
print(" {\\textbf{" + j[0] + "}} {" + j[1] + "}")
print(" \\resumeItemListStart")
for bullet in j[2]:
print(" \\resumeItem{" + bullet + "}")
print(" \\resumeItemListEnd")
print("\\resumeSubHeadingListEnd")

resume_number_education = int(input("How many education entries would you like to add for your client?: "))
resume_education_data = []

for i in range(1, resume_number_education + 1):
resume_school = input("Enter the name of school number " + str(i) + ": ")
resume_school_date = input("Enter the date range for school number " + str(i) + ": ")
resume_degree = input("Enter the degree earned at school number " + str(i) + ": ")
resume_school_location = input("Enter the location of school number " + str(i) + ": ")

num_details = int(input("How many detail lines (coursework, research, etc.) for school number " + str(i) + "?: "))
details = []
for d in range(1, num_details + 1):
detail_text = input("Enter detail line " + str(d) + " for school number " + str(i) + ": ")
details.append(detail_text)

resume_education_data.append([resume_school, resume_school_date, resume_degree, resume_school_location, details])
print()

print("\\section {EDUCATION}")
print(" \\resumeSubHeadingListStart")
for j in resume_education_data:
print(" \\resumeSubheading")
print(" {" + j[0] + "}{" + j[1] + "}")
print(" {" + j[2] + "}{" + j[3] + "}")
print(" \\resumeItemListStart")
for detail in j[4]:
print(" \\resumeItem {" + detail + "}")
print(" \\resumeItemListEnd")
print(" \\resumeSubHeadingListEnd")

num_skill_categories = int(input("How many skill categories would you like to add (e.g. Languages, Tools)?: "))
resume_skill_data = []

for i in range(1, num_skill_categories + 1):
skill_label = input("Enter the label for skill category " + str(i) + " (e.g. Languages): ")
skill_values = input("Enter the skills for category " + str(i) + ", comma separated: ")
resume_skill_data.append([skill_label, skill_values])

print("\\section{SKILLS}")
print(" \\begin{itemize}[leftmargin=0in, label={}]")
print(" \\small{\\item{")
for j in resume_skill_data:
print(" \\textbf{" + j[0] + "} {: " + j[1] + "}\\vspace{2pt} \\\\")
print(" }}")
print(" \\end{itemize}")

print("\\end{document}")


elif resume_style == "2":
def get_detail_lines(prompt_label):
lines = []
while True:
try:
count = int(input("How many" + str(prompt_label) + " detail lines would you like to add? (0 if none): "))
break
except ValueError:
print("Please enter a number")
for i in range(1, count + 1):
category = input(" Detail " + str(i) + " label (e.g. GPA, Supervisor): ")
value = input(" Detail " + str (i) + " value: ")
lines.append(r"\textbf{" + category + r":} " + value + r" \\")
return "\n".join(lines)

def get_bullets(prompt_label):
bullets = []
while True:
try:
count = int(input("How many bullet points for this " + str(prompt_label) + "? "))
break
except ValueError:
print("Please enter a number")
for i in range(1, count + 1):
bullet_text = input(" Bullet " + str(i)+": ")
bullets.append(r" \item " + bullet_text)
if not bullets:
return ""
return "\\begin{itemize}\n" + "\n".join(bullets) + "\n\\end{itemize}"

resume_name = input("Enter the name of your client: ")
while True:
resume_number = input("Does your client have a number? (y/n): ")
if resume_number == "y":
resume_number = input("Enter the contact number of your client: ")
break
elif resume_number == "n":
resume_number = " "
break
else:
print("Invalid Choice")

while True:
resume_email = input("Does your client have an active email? (y/n): ")
if resume_email == "y":
resume_email = input("Enter the email of your client: ")
break
elif resume_email == "n":
resume_email = " "
break
else:
print("Invalid Choice")
resume_citizen = input("Enter the citizenship of your client: ")
resume_address = input('Enter the address of your client: ')
resume_template_one = textwrap.dedent(r"""

\documentclass[11pt,a4paper]{article}

\usepackage[left=0.8in,top=0.8in,right=0.8in,bottom=0.8in]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[default]{sourcesanspro}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{parskip}

\definecolor{titleblue}{HTML}{00199e}
\definecolor{subtitleblue}{HTML}{2ec1e0}
\definecolor{darktext}{HTML}{222222}

\color{darktext}
\linespread{0.9}
\setlength{\parskip}{0.1em}

\titleformat{\section}{\Large\bfseries\color{titleblue}}{}{0em}{}
\titlespacing*{\section}{0pt}{0.7em}{0.15em}

\newcommand{\blueitem}[1]{\textcolor{subtitleblue}{\textbf{#1}}}

\setlist[itemize]{label=\textbullet, leftmargin=*, noitemsep, topsep=0pt, parsep=0pt}


\begin{document}


{\Huge \textbf{\textcolor{titleblue}{@@name@@}}} \vspace{0.2em}

@@address@@ \\
Mobile: @@number@@ \\
Email: @@email@@ \\
Nationality: @@citizenship@@

\vspace{0.4em}


""")

resume_template_one_final = (resume_template_one
.replace("@@name@@", resume_name)
.replace("@@number@@", resume_number)
.replace("@@email@@", resume_email)
.replace("@@citizenship@@", resume_citizen)
.replace("@@address@@", resume_address)
)

while True:
resume_objective = input("Would your client want to have a career objective?: (y/n) ")
if resume_objective == "y":
resume_objective_text = input("Paste or type the career objective here: ")
resume_objective = textwrap.dedent(r"""
\section*{Career Objective}
@@objective_text@@

""").replace("@@objective_text@@", resume_objective_text)
break
elif resume_objective == "n":
resume_objective = ""
break
else:
print("Invalid Input")
while True:
resume_personal_info = input("Would you like to add personal information? (y/n): ")
if resume_personal_info == "y":
resume_personal_info_number = int(input("Enter how many personal information would you like to add: "))
resume_personal_info_data = []
for i in range(1, resume_personal_info_number + 1):
entry = input("Enter the category of personal information " + str(i) + ": ")
entry_value = input("Enter the value of entry " + str(i) + ": ")
resume_personal_info_data.append([entry, entry_value])

resume_personal_info_items = "\n".join(
r" \item \textbf{" + category + r":} " + value
for category, value in resume_personal_info_data
)
resume_personal_info_final = textwrap.dedent(r"""
\section*{Personal Information}
\begin{itemize}
@@personal_info_items@@
\end{itemize}

""").replace("@@personal_info_items@@", resume_personal_info_items)
break
elif resume_personal_info == "n":
resume_personal_info_final = ""
break
else:
print("Invalid Choice")

while True:
resume_education_add = input("Would you like to add an Education section? (y/n): ")
if resume_education_add == "y":
edu_count = int(input("How many education entries would you like to add?: "))
edu_entries = []
for i in range(1, edu_count + 1):
print(f"-- Education entry {i} --")
edu_dates = input(" Dates (e.g. 2024 -- 2026): ")
edu_degree = input(" Degree/Title (e.g. MSc in Robotics): ")
edu_school = input(" University name: ")
edu_location = input(" Location: ")
edu_details = get_detail_lines("education")
edu_entries.append(textwrap.dedent(r"""
\blueitem{@@dates@@: @@degree@@} \\
\textit{@@school@@, @@location@@} \\
@@details@@
""").replace("@@dates@@", edu_dates)
.replace("@@degree@@", edu_degree)
.replace("@@school@@", edu_school)
.replace("@@location@@", edu_location)
.replace("@@details@@", edu_details))
resume_education_final = (
"\\section*{Education}\n"
+ "\n\\vspace{0.3em}\n".join(edu_entries)
+ "\n"
)
break
elif resume_education_add == "n":
resume_education_final = ""
break
else:
print("Invalid Choice")


while True:
resume_experience_add = input("Would you like to add an Experience section? (y/n): ")
if resume_experience_add == "y":
exp_count = int(input("How many experience entries would you like to add?: "))
exp_entries = []
for i in range(1, exp_count + 1):
print(f"-- Experience entry {i} --")
exp_dates = input(" Dates (e.g. May 2025 -- Aug 2025): ")
exp_title = input(" Job title: ")
exp_company = input(" Company/Organization: ")
exp_bullets = get_bullets("experience entry")
exp_entries.append(textwrap.dedent(r"""
\blueitem{@@dates@@: @@title@@} \\
\textit{@@company@@}
@@bullets@@
""").replace("@@dates@@", exp_dates)
.replace("@@title@@", exp_title)
.replace("@@company@@", exp_company)
.replace("@@bullets@@", exp_bullets))
resume_experience_final = (
"\\section*{Experience}\n"
+ "\n\\vspace{0.3em}\n".join(exp_entries)
+ "\n"
)
break
elif resume_experience_add == "n":
resume_experience_final = ""
break
else:
print("Invalid Choice")


while True:
resume_pub_add = input("Would you like to add an Academic Publications section? (y/n): ")
if resume_pub_add == "y":
pub_count = int(input("How many publications would you like to add?: "))
pub_entries = []
for i in range(1, pub_count + 1):
print(f"-- Publication {i} --")
pub_title = input(" Publication title: ")
pub_venue = input(" Venue/Status (e.g. Under review. [arXiv]): ")
pub_authors = input(" Author list (bold your client's name yourself if needed): ")
pub_entries.append(textwrap.dedent(r"""
\blueitem{@@title@@.} @@venue@@ \\
\textit{@@authors@@}
""").replace("@@title@@", pub_title)
.replace("@@venue@@", pub_venue)
.replace("@@authors@@", pub_authors))
resume_pub_final = (
"\\section*{Academic Publications}\n"
+ "\n\\vspace{0.2em}\n".join(pub_entries)
+ "\n"
)
break
elif resume_pub_add == "n":
resume_pub_final = ""
break
else:
print("Invalid Choice")
while True:
resume_proj_add = input("Would you like to add a Projects/Research section? (y/n): ")
if resume_proj_add == "y":
proj_count = int(input("How many project entries would you like to add?: "))
proj_entries = []
for i in range(1, proj_count + 1):
print(f"-- Project entry {i} --")
proj_title = input(" Project title | year (e.g. Autonomous Ag System | 2025): ")
proj_org = input(" Organization/Lab: ")
proj_bullets = get_bullets("project entry")
proj_entries.append(textwrap.dedent(r"""
\blueitem{@@title@@} \\
\textit{@@org@@}
@@bullets@@
""").replace("@@title@@", proj_title)
.replace("@@org@@", proj_org)
.replace("@@bullets@@", proj_bullets))
resume_proj_final = (
"\\section*{Projects/Research}\n"
+ "\n\\vspace{0.3em}\n".join(proj_entries)
+ "\n"
)
break
elif resume_proj_add == "n":
resume_proj_final = ""
break
else:
print("Invalid Choice")

while True:
resume_skills_add = input("Would you like to add a Skills section? (y/n): ")
if resume_skills_add == "y":
resume_skills_list = input("Enter skills, comma separated: ")
resume_skills_langs = input("Enter languages spoken (e.g. English (Fluent), Arabic (Native)): ")
resume_skills_final = textwrap.dedent(r"""
\section*{Skills}
@@skills_list@@ \\
Languages: @@skills_langs@@
""").replace("@@skills_list@@", resume_skills_list) \
.replace("@@skills_langs@@", resume_skills_langs)
break
elif resume_skills_add == "n":
resume_skills_final = ""
break
else:
print("Invalid Choice")


while True:
resume_ref_add = input("Would you like to add a References section? (y/n): ")
if resume_ref_add == "y":
ref_count = int(input("How many references would you like to add?: "))
ref_entries = []
for i in range(1, ref_count + 1):
print(f"-- Reference {i} --")
ref_name = input(" Name: ")
ref_title = input(" Title/Position: ")
ref_dept = input(" Department: ")
ref_institution = input(" Institution: ")
ref_email = input(" Email: ")
ref_entries.append(textwrap.dedent(r"""
\begin{minipage}[t]{0.48\textwidth}
\textbf{@@name@@} \\
@@title@@ \\
@@dept@@ \\
@@institution@@ \\
Email: @@email@@
\end{minipage}""").replace("@@name@@", ref_name)
.replace("@@title@@", ref_title)
.replace("@@dept@@", ref_dept)
.replace("@@institution@@", ref_institution)
.replace("@@email@@", ref_email))
resume_ref_final = (
"\\section*{References}\n\n"
+ "%\n\\hfill\n".join(ref_entries)
+ "\n"
)
break
elif resume_ref_add == "n":
resume_ref_final = ""
break
else:
print("Invalid Choice")
resume_style_two_final = (
resume_template_one_final
+ resume_objective
+ resume_personal_info_final
+ resume_education_final
+ resume_experience_final
+ resume_pub_final
+ resume_proj_final
+ resume_skills_final
+ resume_ref_final
+ "\n\\end{document}\n"
)

print(resume_style_two_final)

else:
print("Invalid Choice")



elif c2 == "2":
motor_day = input("Enter the nth day of transaction: ")
if motor_day == "1":
motor_day = motor_day+"st"
elif motor_day == "2":
motor_day = motor_day +"nd"
elif motor_day == "3":
motor_day = motor_day+"rd"
else:
motor_day = motor_day+"th"
motor_month = input("Enter the month of transaction: ")
motor_year = input("Enter the year of transaction: ")
motor_country = input("Enter the country where the transaction occurs: ")
motor_place = input("Enter what place did the transaction took place: ")
motor_vendor = input("Enter the name of the vendor: ")
motor_vendor_civil = input("Enter the civil status of the vendor: ")
motor_vendor_address = input("Enter the address of the vendor: ")
motor_vendee = input("Enter the name of the vendee: ")
motor_vendee_civil = input("Enter the civil status of the vendee: ")
motor_vendee_address = input("Enter the address of the vendee: ")
motoe_brand = input('Enter the brand of motor: ')
motor_model = input("Enter the model/year of the motor: ")
motor_plate = input('Enter the plate number of the motor: ')
motor_engine = input('Enter the engine number of the motor: ')
motor_color = input('Enter the color of the motor: ')
motor_cor = input("Enter the certificate of registration (CR) number of the motor: ")
motor_or = input("Enter the Official Receipt (OR) number: ")
motor_price_word = input("Enter the amount of motor in words: ")
motor_price_figures = input("Enter the amount of motor in figures (including the currency sign): ")
motor_notary = input("Enter the municipality, and province where the document is being notarized: ")
motor_vendor_id = input("Enter the valid ID presented by the vendor: ")
motor_vendor_id_number_details = input("Enter the ID number/details of the ID provided by the vendor: ")
motor_vendor_id_place_issued = input("Enter the where the ID of the vendor get issued or enter the date when it was issued: ")
motor_vendee_id = input("Enter the valid ID presented by the vendee: ")
motor_vendee_id_number_details = input("Enter the ID number/details of the ID provided by the vendee: ")
motor_vendee_id_place_issued = input("Enter the where the ID of the vendee get issued or enter the date when it was issued: ")

motor_template = textwrap.dedent(r"""
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.75in]{geometry}
\usepackage{times}
\usepackage{setspace}
\singlespacing
\pagenumbering{gobble}
\setlength{\parindent}{0pt}

\begin{document}

\begin{center}
{\Large\bfseries DEED OF ABSOLUTE SALE OF MOTOR VEHICLE}
\end{center}

\vspace{0.4em}
\noindent
KNOW ALL MEN BY THESE PRESENTS:

\vspace{0.4em}
\noindent
This DEED OF ABSOLUTE SALE, made and executed this @@day@@ day of @@month@@, @@year@@, at @@place@@, @@country@@, by and between:

\vspace{0.4em}
\noindent
@@vendor@@, of legal age, Filipino, @@vendorcivil@@, with residence and postal address at @@vendoraddress@@, hereinafter referred to as the \textbf{VENDOR};

\vspace{0.4em}
\noindent
-- and --

\vspace{0.4em}
\noindent
@@vendee@@, of legal age, Filipino, @@vendeecivil@@, with residence and postal address at @@vendeeaddress@@, hereinafter referred to as the \textbf{VENDEE};

\vspace{0.4em}
\noindent
\textbf{WITNESSETH:} That WHEREAS, the VENDOR is the registered and lawful owner of a motor vehicle more particularly described as follows:

\vspace{0.2em}
\begin{tabbing}
\hspace{4cm} \= \kill
Make/Brand: \> @@brand@@ \\
Model/Year: \> @@model@@ \\
Plate No.: \> @@plate@@ \\
Engine No.: \> @@engine@@ \\
Color: \> @@color@@ \\
Certificate of Registration (CR) No.: \> @@cor@@ \\
Official Receipt (OR) No.: \> @@or@@ \\
\end{tabbing}

\noindent
(hereinafter referred to as the "VEHICLE")

\vspace{0.4em}
\noindent
WHEREAS, the VENDOR has offered to sell and the VENDEE has agreed to purchase the above-described VEHICLE for and in consideration of the amount of \textbf{@@pricefigures@@} (Philippine Pesos, @@pricewords@@ only), Philippine currency, receipt of which is hereby acknowledged by the VENDOR in full;

\vspace{0.4em}
\noindent
NOW, THEREFORE, for and in consideration of the foregoing premises, the VENDOR hereby SELLS, TRANSFERS, and CONVEYS, absolutely and unconditionally, unto the said VENDEE, his/her heirs, successors, and assigns, the above-described VEHICLE, free from all liens and encumbrances of whatever nature;

\vspace{0.4em}
\noindent
That the VENDOR warrants valid title to and peaceful possession of the said VEHICLE, and further warrants to defend the same from any claims of any and all persons whomsoever.

\vspace{0.4em}
\noindent
IN WITNESS WHEREOF, the parties have hereunto set their hands this @@day@@ day of @@month@@, @@year@@, at @@place@@, @@country@@.

\vspace{1em}
\noindent
\underline{\hspace{6cm}} \hfill \underline{\hspace{6cm}} \\
VENDOR \hfill VENDEE

\vspace{0.5em}
\noindent
\textbf{Signed in the presence of:}

\vspace{0.5em}
\noindent
\underline{\hspace{6cm}} \hfill \underline{\hspace{6cm}}

\newpage
\begin{center}
\textbf{ACKNOWLEDGMENT}
\end{center}

\noindent
REPUBLIC OF THE PHILIPPINES) \\
CITY/MUNICIPALITY OF @@notaryplace@@ ) S.S.

\vspace{0.4em}
\noindent
BEFORE ME, a Notary Public for and in @@notaryplace@@, personally appeared:

\vspace{0.4em}
\begin{tabbing}
\hspace{5cm} \= \hspace{4cm} \= \kill
\textbf{Name} \> \textbf{ID No./Details} \> \textbf{Date/Place Issued} \\[0.5em]
@@vendor@@ \> @@vendorid@@ @@vendoriddetails@@ \> @@vendoridissued@@ \\[1em]
@@vendee@@ \> @@vendeeid@@ @@vendeeiddetails@@ \> @@vendeeidissued@@ \\
\end{tabbing}

\noindent
known to me and to me known to be the same persons who executed the foregoing Deed of Absolute Sale, and they acknowledged to me that the same is their free and voluntary act and deed.

\vspace{0.4em}
\noindent
This instrument, consisting of two pages, including this page on which the acknowledgment is written, has been signed by the parties and their witnesses on each and every page thereof.

\vspace{0.4em}
\noindent
WITNESS MY HAND AND SEAL, on the date and place first above written.

\vspace{1em}
\noindent
\\
\noindent Notary Public

\vspace{0.4em}
\noindent
Doc. No. \underline{\hspace{2cm}}\\
Page No. \underline{\hspace{2cm}}\\
Book No. \underline{\hspace{2cm}}\\
Series of @@year@@

\end{document}""")

motor_final = (motor_template
.replace("@@day@@", motor_day)
.replace("@@month@@", motor_month)
.replace("@@year@@", motor_year)
.replace("@@place@@", motor_place)
.replace("@@country@@", motor_country)
.replace("@@vendorcivil@@", motor_vendor_civil)
.replace("@@vendoraddress@@", motor_vendor_address)
.replace("@@vendor@@", motor_vendor)
.replace("@@vendeecivil@@", motor_vendee_civil)
.replace("@@vendeeaddress@@", motor_vendee_address)
.replace("@@vendee@@", motor_vendee)
.replace("@@brand@@", motoe_brand)
.replace("@@model@@", motor_model)
.replace("@@plate@@", motor_plate)
.replace("@@engine@@", motor_engine)
.replace("@@color@@", motor_color)
.replace("@@cor@@", motor_cor)
.replace("@@or@@", motor_or)
.replace("@@pricewords@@", motor_price_word)
.replace("@@pricefigures@@", motor_price_figures)
.replace("@@notaryplace@@", motor_notary)
.replace("@@vendoriddetails@@", motor_vendor_id_number_details)
.replace("@@vendoridissued@@", motor_vendor_id_place_issued)
.replace("@@vendorid@@", motor_vendor_id)
.replace("@@vendeeiddetails@@", motor_vendee_id_number_details)
.replace("@@vendeeidissued@@", motor_vendee_id_place_issued)
.replace("@@vendeeid@@", motor_vendee_id)
)

print("Copy the overleaf LaTex code below: ")
print(motor_final)



elif c2 == "3":
loss_city = input("Enter the city or municipality where the client is physically located (and signing this document): ")
loss_city = loss_city.upper()
loss_client = input("Enter the name of your client: ")
loss_civil = input("Enter the civil status of your client: ")
while True:
loss_nationality = input("Is your client a Filipino citizen? (y/n): ")
if loss_nationality == "y":
loss_nationality = "Filipino"
break
elif loss_nationality == "n":
x = input("Enter the nationality of you client: ")
loss_nationality = str(x)
break
else:
print("Invalid Choice")

loss_resident = input("Enter the residency of your client: ")
loss_item = input("Enter the lost item (e.g. ATM, ID card, etc): ")
loss_reference = input("Enter the ID/Reference No.: ")
loss_issued = input("Enter who issued the lost item if appplicable: ")
loss_date_issued = input("Enter what date does the item get issued if appplicable: ")
loss_date_time = input("Enter approximately what time or date did the item get lost: ")
loss_place = input("Where did the item get lost?: ")
loss_agency = input("Enter the name of agency/institution requiring this affidavit: ")
loss_day = input("Enter nth day today (or when this affidavit is to be signed): ")
if loss_day =="1":
loss_day = loss_day+"st"
elif loss_day == "2":
loss_day = loss_day +"nd"
elif loss_day == "3":
loss_day = loss_day+"rd"
else:
loss_day = loss_day+"th"
loss_month = input("Enter the month: ")
loss_year = input("Enter year: ")
loss_id = input("Enter the valid ID presented by your client: ")
loss_id_number = input("Enter the ID number, if applicable: ")
loss_id_place_issued = input("Enter what place/date did the ID get issued: ")

def affidavit_of_loss():
loss_template = textwrap.dedent(r"""\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{times}
\usepackage{setspace}
\usepackage{ragged2e}
\onehalfspacing
\pagenumbering{gobble}

\begin{document}

\begin{center}
{\Large\bfseries AFFIDAVIT OF LOSS}
\end{center}

\vspace{1em}
\noindent
REPUBLIC OF THE PHILIPPINES) \\
CITY/MUNICIPALITY OF @@place@@ ) S.S.

\vspace{1.5em}
\noindent
I, @@name@@, of legal age, @@civil@@, Filipino citizen, and a resident of @@resident@@, after having been duly sworn to in accordance with law, do hereby depose and state that:

\vspace{1em}
\begin{enumerate}
\item I am the lawful owner/holder of a @@item@@ with the following details:

\vspace{0.5em}
\noindent
ID/Reference No.: @@referenceid@@
\hspace{3cm} Issued by: @@issued@@ \\
\hspace{1cm} Date Issued: @@dateissued@@

\item That on or about @@timelost@@, while I was at @@placelost@@, I discovered that the above-described item was missing/lost despite diligent search and effort to locate the same;

\item That the loss was not due to my fault or negligence, and I have not sold, pawned, or otherwise disposed of the said item;

\item That I am executing this affidavit to attest to the truth of the foregoing facts and for whatever legal purpose it may serve, including the request for a replacement/issuance of a new @@item@@;

\item That I am executing this Affidavit of Loss to attest to the truth of the foregoing and in compliance with the requirements of @@institution@@.
\end{enumerate}

\newpage
IN WITNESS WHEREOF, I have hereunto set my hand this @@day@@ day of @@month@@, @@year@@, at @@place@@, Philippines.

\vspace{4em}
\noindent
@@name@@\\[-18pt]
\noindent
\underline{\hspace{6cm}} \\
\hspace{7cm}Affiant \\


\vspace{1em}
\noindent
Valid Government ID Presented: @@idpresented@@ \\
ID No.: @@idnumberpresented@@ \hspace{3cm} Date/Place Issued: @@iddatepissued@@
\vspace{2em}
\noindent\\
\textbf{SUBSCRIBED AND SWORN} to before me this @@day@@ day of @@month@@, @@year@@, at @@place@@, Philippines, affiant exhibiting to me his/her competent evidence of identity as indicated above.

\vspace{4em}
\noindent
\noindent Notary Public

\noindent
Doc. No. \underline{\hspace{2cm}}\\
Page No. \underline{\hspace{2cm}}\\
Book No. \underline{\hspace{2cm}}\\
Series of @@year@@.

\end{document}""")

loss_template_final = (loss_template
.replace("@@place@@", loss_city)
.replace("@@name@@", loss_client)
.replace("@@civil@@", loss_civil)
.replace("@@resident@@", loss_resident)
.replace("@@item@@", loss_item)
.replace("@@referenceid@@", loss_reference)
.replace("@@issued@@", loss_issued)
.replace("@@dateissued@@", loss_date_issued)
.replace("@@timelost@@", loss_date_time)
.replace("@@placelost@@", loss_place)
.replace("@@institution@@", loss_agency)
.replace("@@day@@", loss_day)
.replace("@@month@@", loss_month)
.replace("@@year@@", loss_year)
.replace("@@idpresented@@", loss_id)
.replace("@@idnumberpresented@@", loss_id_number)
.replace("@@iddatepissued@@", loss_id_place_issued)

)

print(loss_template_final)


print("")
print("Paste the overleaf LaTEX code below: ")
affidavit_of_loss()


elif c2 == "4":
real_day = input("Enter the nth day of transaction (day where this document is to be signed): ")
if real_day =="1":
real_day = real_day+"st"
elif real_day == "2":
real_day = real_day +"nd"
elif real_day == "3":
real_day = real_day+"rd"
else:
real_day = real_day+"th"
real_month = input("Enter the month of transaction (month where this document is to be signed): ")
real_year = input("Enter the year of transaction (year where this document is to be signed): ")
real_country = input("Enter what country does this transaction occur: ")
real_address = input("Enter the city/province where this document is to be signed: ")
real_vendor = input("Enter the name of the vendor: ")
real_vendor_civil = input("Enter the civil status of the vendor: ")
real_vendor_address = input("Enter the address of the vendor: ")
real_vendee = input("Enter the name of the vendee: ")
real_vendee_civil = input("Enter the civil status of the vendee: ")
real_vendee_address = input("Enter the address of the vendee: ")
real_property_address = input("Enter the physical address of the property: ")

print("Does your client have a TCT or OCT number?")
print("TRANSFER CERTIFICATE OF TITLE (TCT) NUMBER [1]")
print("ORIGINAL CERTIFICATE OF TITLE (OCT) NUMBER [2]")
while True:
real_title_choice = input("Enter your choice: ")
if real_title_choice == "1":
real_title_label = "Transfer Certificate of Title (TCT)"
break
elif real_title_choice == "2":
real_title_label = "Original Certificate of Title (OCT)"
break
else:
print("Invalid Choice")

real_title_number = input(f"Enter the {real_title_label} number: ")
real_lot_no = input("Enter the Lot No.: ")
real_block_no = input("Enter the Block No. (leave blank if not applicable): ")
real_area = input("Enter the area of the property (in square meters): ")
real_tax_dec = input("Enter the Tax Declaration No.: ")
real_price_words = input("Enter the purchase price in words: ")
real_price_figures = input("Enter the purchase price in figures (including the currency sign): ")
real_notary = input("Enter the municipality/province where the document is being notarized: ")
real_vendor_id = input("Enter the valid ID presented by the vendor: ")
real_vendor_id_details = input("Enter the ID number/details of the vendor's ID: ")
real_vendor_id_issued = input("Enter where/when the vendor's ID was issued: ")
real_vendee_id = input("Enter the valid ID presented by the vendee: ")
real_vendee_id_details = input("Enter the ID number/details of the vendee's ID: ")
real_vendee_id_issued = input("Enter where/when the vendee's ID was issued: ")

real_property_template = textwrap.dedent(r"""
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.75in]{geometry}
\usepackage{times}
\usepackage{setspace}
\singlespacing
\pagenumbering{gobble}
\setlength{\parindent}{0pt}

\begin{document}

\begin{center}
{\Large\bfseries DEED OF ABSOLUTE SALE OF REAL PROPERTY}
\end{center}

\vspace{0.4em}
\noindent
KNOW ALL MEN BY THESE PRESENTS:

\vspace{0.4em}
\noindent
This DEED OF ABSOLUTE SALE, made and executed this @@day@@ day of @@month@@, @@year@@, at @@address@@, @@country@@, by and between:

\vspace{0.4em}
\noindent
@@vendor@@, of legal age, Filipino, @@vendorcivil@@, with residence and postal address at @@vendoraddress@@, hereinafter referred to as the \textbf{VENDOR};

\vspace{0.4em}
\noindent
-- and --

\vspace{0.4em}
\noindent
@@vendee@@, of legal age, Filipino, @@vendeecivil@@, with residence and postal address at @@vendeeaddress@@, hereinafter referred to as the \textbf{VENDEE};

\vspace{0.4em}
\noindent
\textbf{WITNESSETH:} That WHEREAS, the VENDOR is the registered and lawful owner of a parcel of land, together with the improvements thereon, more particularly described as follows:

\vspace{0.2em}
\begin{tabbing}
\hspace{5cm} \= \kill
@@titlelabel@@ No.: \> @@titlenumber@@ \\
Lot No.: \> @@lotno@@ \\
Block No.: \> @@blockno@@ \\
Area: \> @@area@@ square meters \\
Tax Declaration No.: \> @@taxdec@@ \\
Property Address: \> @@propertyaddress@@ \\
\end{tabbing}

\noindent
(hereinafter referred to as the "PROPERTY")

\vspace{0.4em}
\noindent
WHEREAS, the VENDOR has offered to sell and the VENDEE has agreed to purchase the above-described PROPERTY for and in consideration of the amount of \textbf{@@pricefigures@@} (Philippine Pesos, @@pricewords@@ only), Philippine currency, receipt of which is hereby acknowledged by the VENDOR in full;

\vspace{0.4em}
\noindent
NOW, THEREFORE, for and in consideration of the foregoing premises, the VENDOR hereby SELLS, TRANSFERS, and CONVEYS, absolutely and unconditionally, unto the said VENDEE, his/her heirs, successors, and assigns, the above-described PROPERTY, free from all liens and encumbrances of whatever nature;

\vspace{0.4em}
\noindent
That the VENDOR warrants valid title to and peaceful possession of the said PROPERTY, and further warrants to defend the same from any claims of any and all persons whomsoever, and shall cause the transfer of the corresponding certificate of title in the name of the VENDEE at the VENDEE's expense unless otherwise agreed.

\vspace{0.4em}
\noindent
IN WITNESS WHEREOF, the parties have hereunto set their hands this @@day@@ day of @@month@@, @@year@@, at @@address@@, @@country@@.

\vspace{1em}
\noindent
\underline{\hspace{6cm}} \hfill \underline{\hspace{6cm}} \\
VENDOR \hfill VENDEE

\vspace{0.5em}
\noindent
\textbf{Signed in the presence of:}

\vspace{0.5em}
\noindent
\underline{\hspace{6cm}} \hfill \underline{\hspace{6cm}}

\newpage
\begin{center}
\textbf{ACKNOWLEDGMENT}
\end{center}

\noindent
REPUBLIC OF THE PHILIPPINES) \\
CITY/MUNICIPALITY OF @@notaryplace@@ ) S.S.

\vspace{0.4em}
\noindent
BEFORE ME, a Notary Public for and in @@notaryplace@@, personally appeared:

\vspace{0.4em}
\begin{tabbing}
\hspace{5cm} \= \hspace{4cm} \= \kill
\textbf{Name} \> \textbf{ID No./Details} \> \textbf{Date/Place Issued} \\[0.5em]
@@vendor@@ \> @@vendorid@@ @@vendoriddetails@@ \> @@vendoridissued@@ \\[1em]
@@vendee@@ \> @@vendeeid@@ @@vendeeiddetails@@ \> @@vendeeidissued@@ \\
\end{tabbing}

\noindent
known to me and to me known to be the same persons who executed the foregoing Deed of Absolute Sale, and they acknowledged to me that the same is their free and voluntary act and deed.

\vspace{0.4em}
\noindent
This instrument, consisting of two pages, including this page on which the acknowledgment is written, has been signed by the parties and their witnesses on each and every page thereof.

\vspace{0.4em}
\noindent
WITNESS MY HAND AND SEAL, on the date and place first above written.

\vspace{1em}
\noindent
\\
\noindent Notary Public

\vspace{0.4em}
\noindent
Doc. No. \underline{\hspace{2cm}}\\
Page No. \underline{\hspace{2cm}}\\
Book No. \underline{\hspace{2cm}}\\
Series of @@year@@

\end{document}""")

real_property_final = (real_property_template
.replace("@@day@@", real_day)
.replace("@@month@@", real_month)
.replace("@@year@@", real_year)
.replace("@@address@@", real_address)
.replace("@@country@@", real_country)
.replace("@@vendorcivil@@", real_vendor_civil)
.replace("@@vendoraddress@@", real_vendor_address)
.replace("@@vendor@@", real_vendor)
.replace("@@vendeecivil@@", real_vendee_civil)
.replace("@@vendeeaddress@@", real_vendee_address)
.replace("@@vendee@@", real_vendee)
.replace("@@titlelabel@@", real_title_label)
.replace("@@titlenumber@@", real_title_number)
.replace("@@lotno@@", real_lot_no)
.replace("@@blockno@@", real_block_no)
.replace("@@area@@", real_area)
.replace("@@taxdec@@", real_tax_dec)
.replace("@@propertyaddress@@", real_property_address)
.replace("@@pricewords@@", real_price_words)
.replace("@@pricefigures@@", real_price_figures)
.replace("@@notaryplace@@", real_notary)
.replace("@@vendoriddetails@@", real_vendor_id_details)
.replace("@@vendoridissued@@", real_vendor_id_issued)
.replace("@@vendorid@@", real_vendor_id)
.replace("@@vendeeiddetails@@", real_vendee_id_details)
.replace("@@vendeeidissued@@", real_vendee_id_issued)
.replace("@@vendeeid@@", real_vendee_id)
)

print("Paste the overleaf LaTEX code below: ")
print(real_property_final)



elif c2 == "5":
def attorney_overleaf():
print(textwrap.dedent(r"""\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{times}
\usepackage{setspace}
\onehalfspacing
\pagenumbering{gobble}

\begin{document}

\begin{center}
{\Large\bfseries SPECIAL POWER OF ATTORNEY}
\end{center}

\vspace{1em}
\noindent
KNOW ALL MEN BY THESE PRESENTS:

\vspace{1em}
\noindent
I, \underline{\hspace{7cm}}, of legal age, Filipino, \underline{\hspace{2cm}} (civil status), with residence and postal address at \underline{\hspace{7cm}}, do hereby name, constitute, and appoint \underline{\hspace{6cm}}, of legal age, Filipino, with residence and postal address at \underline{\hspace{7cm}}, to be my true and lawful Attorney-in-Fact, for me and in my name, place, and stead, to do and perform the following acts, to wit:

\vspace{1em}
\begin{enumerate}
\item To \underline{\hspace{10cm}}\\
\underline{\hspace{10cm}}\\
\underline{\hspace{10cm}};

\item To sign, execute, and deliver any and all documents, papers, and instruments necessary or incidental to the foregoing, including but not limited to receipts, applications, and agreements;

\item To represent me, and to appear on my behalf, before any government agency, office, bank, or private institution, in connection with the matter/s stated above;

\item To do and perform such other acts and things as may be necessary or proper in the premises, as fully and effectively as I might or could lawfully do if personally present.
\end{enumerate}

\vspace{1em}
\noindent
HEREBY GIVING AND GRANTING unto my said Attorney-in-Fact full power and authority to do and perform every act and thing whatsoever requisite and necessary to be done in and about the premises, as fully to all intents and purposes as I might or could lawfully do if personally present, hereby ratifying and confirming all that my said Attorney-in-Fact shall lawfully do or cause to be done by virtue of these presents.

\vspace{1em}
\noindent
This Special Power of Attorney shall remain in full force and effect until revoked by me in writing, and shall not be affected by my subsequent incapacity, disability, or absence, unless expressly revoked.

\vspace{1em}
\noindent
IN WITNESS WHEREOF, I have hereunto set my hand this \underline{\hspace{1.5cm}} day of \underline{\hspace{2.5cm}}, 20\underline{\hspace{1cm}}, at \underline{\hspace{4cm}}, Philippines.

\vspace{4em}
\noindent
\hspace{7cm}\underline{\hspace{6cm}} \\
\hspace{7cm}Principal \\
\hspace{7cm}(Signature over Printed Name)

\vspace{2em}
\noindent
\textbf{Signed in the presence of:}

\vspace{3em}
\noindent
\underline{\hspace{6cm}} \hfill \underline{\hspace{6cm}}

\vspace{2em}
\noindent
\begin{center}
\textbf{ACKNOWLEDGMENT}
\end{center}

\noindent
REPUBLIC OF THE PHILIPPINES) \\
CITY/MUNICIPALITY OF \underline{\hspace{4cm}}\ ) S.S.

\vspace{1em}
\noindent
BEFORE ME, a Notary Public for and in \underline{\hspace{5cm}}, personally appeared \underline{\hspace{6cm}}, known to me and to me known to be the same person who executed the foregoing Special Power of Attorney, and he/she acknowledged to me that the same is his/her free and voluntary act and deed, exhibiting to me his/her competent evidence of identity as follows:

\vspace{1em}
\noindent
ID Presented: \underline{\hspace{5cm}} \hspace{1cm} ID No.: \underline{\hspace{3cm}} \hspace{1cm} Date/Place Issued: \underline{\hspace{4cm}}

\vspace{1em}
\noindent
WITNESS MY HAND AND SEAL, on the date and place first above written.

\vspace{4em}
\noindent
\hspace{7cm}\underline{\hspace{6cm}} \\
\hspace{7cm}Notary Public

\vspace{1em}
\noindent
Doc. No. \underline{\hspace{2cm}}\\
Page No. \underline{\hspace{2cm}}\\
Book No. \underline{\hspace{2cm}}\\
Series of 20\underline{\hspace{1cm}}.

\end{document}
"""))
print("Paste the overleaf LaTEX code below: ")
attorney_overleaf()
elif c2 == "6":
day_donation = input("Enter nth day of donation: ")
if day_donation =="1":
day_donation = day_donation+"st"
elif day_donation == "2":
day_donation = day_donation +"nd"
elif day_donation == "3":
day_donation = day_donation+"rd"
else:
day_donation = day_donation+"th"
month_donation = input("Enter the month of donation: ")
year_donation = input("Enter the year of donation: ")
country_donation = input("Enter what country does the donation occurs: ")
place_donation = input("Enter the place of donation: ")
donor_name = input("Enter the donor's name: ")
donor_civil_status = input("Enter the donor's civil status: ")
donor_address = input("Enter the donor's address: ")
donee_name = input("Enter the donee's name: ")
donee_civil_status = input("Enter the donee's civil status: ")
donee_address = input("Enter the donee's address: ")
donate_description = input("Enter the full technical description of the real property(e.g. Lot No., Block No., TCT/OCT No., area in squae meters, location, etc)")
while True:
donation_condition = input("Does the donation have a condition?: (y/n): ").strip().lower()
if donation_condition == "y":
donation_condition_text = input("This donation is made subject to the condition that (continue): ")
donation_condition = donation_condition_text
break
elif donation_condition == "n":
donation_condition = "None"
break
else:
print("Invalid Choice")
donor_id = input("What type of ID does the donor have?: ")
donee_id = input("What type of ID does the donee have?: ")
donor_id_date_place = input("Enter the donor's ID Date/Place Issued: ")
donee_id_date_place = input("Enter the donee's ID Date/Place Isued: ")

deed_of_donation_template = textwrap.dedent(r"""
\documentclass[12pt]{article}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{times}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage{lastpage}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\small Page \thepage\ of \pageref{LastPage}}
\titleformat{\section}{\normalfont\bfseries\large}{\thesection.}{0.5em}{}
\titlespacing*{\section}{0pt}{1.2em}{0.8em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\onehalfspacing
\begin{document}

\begin{center}
{\LARGE \bfseries DEED OF DONATION}
\end{center}

\vspace{1em}

KNOW ALL MEN BY THESE PRESENTS:

This Deed of Donation is made and executed on this @@day@@ day of @@month@@, @@year@@, at @@place@@, @@country@@, by and between:

\vspace{0.5em}

\textbf{@@Donorname@@}, of legal age, Filipino, \textbf{@@civildonor@@}, and a resident of \textbf{@@addressdonor@@}, hereinafter referred to as the "\textbf{DONOR}";

\vspace{0.5em}

\hfill \textbf{-- and --}

\vspace{0.5em}

\textbf{@@Doneename@@}, of legal age, Filipino, \textbf{@@civildonee@@}, and a resident of \textbf{@@addressdonee@@}, hereinafter referred to as the "\textbf{DONEE}".

\section{Recitals}
\begin{enumerate}[leftmargin=1.5em]
\item The DONOR is the lawful and registered owner of the property described in Section 2 below, free from all liens and encumbrances.
\item The DONOR, out of love, affection, and liberality, and without any consideration, desires to donate the said property to the DONEE, who accepts the same.
\end{enumerate}

\section{Description of Property Donated}
The property subject of this donation is described as follows:

\vspace{0.5em}
\textit{@@description@@}

\newpage
\section{Terms and Conditions}
\begin{enumerate}[leftmargin=1.5em]
\item The DONOR hereby voluntarily transfers and conveys, by way of donation, unto the DONEE, his/her heirs, and assigns, the above-described property, free from all liens and encumbrances.
\item The DONEE hereby accepts this donation and is grateful for the liberality of the DONOR.
\item This donation is made subject to the condition that \textbf{@@condition@@}.
\item All expenses relative to the transfer of ownership, including but not limited to documentary stamp tax, transfer tax, and registration fees, shall be for the account of the \textbf{[Donor/Donee]}.
\end{enumerate}

\section{Acceptance by the Donee}
The DONEE hereby accepts this donation and the property herein donated, and is grateful for the liberality of the DONOR.

\vspace{2em}

\textbf{IN WITNESS WHEREOF}, the parties have hereunto set their hands on the date and place first above written.

\vspace{3em}

\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
\textbf{@@Donorname@@} \\
Donor
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
\textbf{@@Doneename@@} \\
Donee
\end{minipage}

\vspace{3em}

\textbf{Signed in the presence of:}

\vspace{2em}

\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
Witness 1
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
Witness 2
\end{minipage}

\vspace{3em}

\newpage
\begin{center}
\textbf{ACKNOWLEDGMENT}
\end{center}

Republic of the Philippines) \\
@@country,place@@\,\,\,\,\,\,\,\,)SS.

\vspace{1em}

BEFORE ME, a Notary Public for and in the above jurisdiction, personally appeared:

\vspace{0.5em}
\begin{tabular}{@{}lll@{}}
\textbf{Name} & \textbf{Competent Evidence of Identity} & \textbf{Date/Place Issued} \\[0.3em]
@@Donorname@@ & @@idonor@@ & @@dateidonor@@ \\{}
@@Doneename@@ & @@idonee@@ & @@dateidonee@@ \\
\end{tabular}

\vspace{1em}

known to me and to me known to be the same persons who executed the foregoing Deed of Donation, and acknowledged to me that the same is their free and voluntary act and deed.

\vspace{1em}

WITNESS MY HAND AND SEAL on the date and place first above written.

\vspace{3em}

\underline{\hspace{6cm}} \\
Notary Public

\vspace{1em}
Doc. No. \underline{\hspace{2cm}} \\
Page No. \underline{\hspace{2cm}} \\
Book No. \underline{\hspace{2cm}} \\
Series of \underline{\hspace{2cm}}

\end{document}
""")
deed_of_donation = (
deed_of_donation_template
.replace("@@day@@", day_donation )
.replace("@@month@@", month_donation)
.replace("@@year@@", year_donation)
.replace("@@place@@", place_donation)
.replace("@@Donorname@@", donor_name)
.replace("@@civildonor@@", donor_civil_status)
.replace("@@addressdonor@@", donor_address)
.replace("@@Doneename@@", donee_name)
.replace("@@civildonee@@", donee_civil_status)
.replace("@@addressdonee@@", donee_address)
.replace("@@country@@", country_donation)
.replace("@@description@@", donate_description)
.replace("@@condition@@", donation_condition)
.replace("@@country,place@@", country_donation + " " + place_donation)
.replace("@@idonor@@",donor_id)
.replace("@@idonee@@" ,donee_id)
.replace("@@dateidonor@@", donor_id_date_place)
.replace("@@dateidonee@@", donee_id_date_place)


)

print("Paste the overleaf LaTEX code below: ")
print(deed_of_donation)

elif c2 == "7":
day_sell = input("Enter nth day of sell: ")
if day_sell == "1":
day_sell = day_sell + "st"
elif day_sell == "2":
day_sell = day_sell + "nd"
elif day_sell == "3":
day_sell = day_sell + "rd"
else:
day_sell = day_sell + "th"
month_sell = input("Enter what month does the item sold: ")
year_sell = input("Enter what year does the item sold: ")
country_sell = input("Enter what country does the transaction occur: ")
place_sell = input("Enter the place of transaction: ")
vendor_name = input("Enter the seller's name: ")
vendor_civil_status = input("Enter the seller's civil status: ")
vendor_address = input("Enter the seller's address: ")
vendee_name = input("Enter the buyer's name: ")
vendee_civil_status = input("Enter the buyer's civil status: ")
vendee_address = input("Enter the buyer's address: ")
item_description = input("Enter the full technical description of the property (e.g. Lot No., Block No., TCT/OCT No., area in square meters, location, etc): ")
price_figures = input("Enter the total purchase price in figures (e.g. 500,000.00): ")
price_words = input("Enter the total purchase price in words (e.g. Five Hundred Thousand Pesos): ")
down_payment = input("Enter the down payment/reservation fee amount: ")
balance_amount = input("Enter the remaining balance amount: ")
payment_schedule = input("Enter the payment schedule (e.g. monthly installments of PHP X for Y months): ")
payment_mode = input("Enter the mode of payment (cash/check/bank transfer): ")
grace_period = input("Enter the grace period (in days) before rescission: ")
while True:
possession_choice = input("Is possession transferred upon signing or upon full payment? (signing/full): ").strip().lower()
if possession_choice == "signing":
possession_terms = "transferred upon signing"
break
elif possession_choice == "full":
possession_terms = "transferred upon full payment"
break
else:
print("Invalid Choice")
while True:
risk_choice = input("Who bears the risk of loss? (seller/buyer): ").strip().lower()
if risk_choice == "seller":
risk_party = "Seller"
break
elif risk_choice == "buyer":
risk_party = "Buyer"
break
else:
print("Invalid Choice")
while True:
expenses_choice = input("Who shoulders taxes and transfer expenses? (seller/buyer): ").strip().lower()
if expenses_choice == "seller":
expenses_party = "Seller"
break
elif expenses_choice == "buyer":
expenses_party = "Buyer"
break
else:
print("Invalid Choice")
city_province = input("Enter the city/province for governing law/jurisdiction: ")
sell_witness = input("Enter the name of the witness: ")
sell_witness_2 = input("Enter the name of the 2nd witness: ")
vendor_id = input("What type of ID does the seller have?: ")
vendee_id = input("What type of ID does the buyer have?: ")
vendor_id_date_place = input("Enter the seller's ID Date/Place Issued: ")
vendee_id_date_place = input("Enter the buyer's ID Date/Place Issued: ")

contract_to_sell_template = textwrap.dedent(r"""
\documentclass[12pt]{article}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{times}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage{lastpage}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\small Page \thepage\ of \pageref{LastPage}}
\titleformat{\section}{\normalfont\bfseries\large}{\thesection.}{0.5em}{}
\titlespacing*{\section}{0pt}{1.2em}{0.8em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\onehalfspacing
\begin{document}

\begin{center}
{\LARGE \bfseries CONTRACT TO SELL}
\end{center}

\vspace{1em}

This Contract to Sell is made and executed on this @@day@@ day of @@month@@, @@year@@, at @@place@@, @@country@@, by and between:

\vspace{0.5em}

\textbf{@@sellername@@}, of legal age, Filipino, \textbf{@@sellercivil@@}, and a resident of \textbf{@@selleraddress@@}, hereinafter referred to as the "\textbf{VENDOR}";

\vspace{0.5em}

\hfill \textbf{-- and --}

\vspace{0.5em}

\textbf{@@buyername@@}, of legal age, Filipino, \textbf{@@buyercivil@@}, and a resident of \textbf{@@buyeraddress@@}, hereinafter referred to as the "\textbf{VENDEE}".

\section{Subject Property}
The VENDOR is the registered/lawful owner of the property more particularly described as:

\vspace{0.5em}
\textit{@@description@@}

\vspace{0.5em}
(hereinafter referred to as the "\textbf{Property}").

\section{Purchase Price and Terms of Payment}
\begin{enumerate}[leftmargin=1.5em]
\item The total purchase price of the Property is \textbf{PHP @@pricefigures@@ (@@pricewords@@)}.
\item \textbf{Down Payment / Reservation Fee:} The VENDEE shall pay VENDOR the amount of \textbf{PHP @@downpayment@@} upon signing of this Contract, receipt of which is hereby acknowledged.
\item \textbf{Balance:} The remaining balance of \textbf{PHP @@balance@@} shall be paid in accordance with the following schedule: \textit{@@paymentschedule@@}.
\item Payments shall be made via \textbf{@@paymentmode@@} to the VENDOR or the VENDOR's authorized representative.
\end{enumerate}

\newpage
\section{Condition of the Sale}
\begin{enumerate}[leftmargin=1.5em]
\item This Contract to Sell does not, by itself, transfer ownership of the Property to the VENDEE. Ownership shall remain with the VENDOR until full payment of the purchase price.
\item Upon full payment of the purchase price, the VENDOR shall execute the corresponding \textbf{Deed of Absolute Sale} in favor of the VENDEE and shall deliver all pertinent documents necessary for the transfer of title/ownership.
\item Should the VENDEE fail to pay any installment when due, the VENDOR shall have the right to: (a) demand immediate payment of the overdue amount with a grace period of \textbf{@@graceperiod@@} days; or (b) rescind this Contract and forfeit payments already made as liquidated damages, at the VENDOR's option.
\end{enumerate}

\section{Possession and Risk of Loss}
Possession of the Property shall be \textbf{@@possessionterms@@}. The risk of loss or damage to the Property shall be borne by the \textbf{@@riskparty@@} until full payment and transfer of title.

\section{Taxes and Expenses}
All taxes, fees, and expenses relative to the transfer of title, including but not limited to capital gains tax, documentary stamp tax, transfer tax, and registration fees, shall be for the account of the \textbf{@@expensesparty@@}, unless otherwise agreed in writing.

\section{Warranties}
The VENDOR warrants that the Property is free from all liens, encumbrances, and adverse claims, and that the VENDOR has the full right and authority to enter into this Contract.

\section{Governing Law}
This Contract shall be governed by the laws of the Republic of the Philippines. Any dispute arising herefrom shall be brought before the proper courts of \textbf{@@cityprovince@@}.

\vspace{2em}

\textbf{IN WITNESS WHEREOF}, the parties have hereunto set their hands on the date and place first above written.

\vspace{3em}

\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
\textbf{@@sellername@@} \\
Vendor
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
\textbf{@@buyername@@} \\
Vendee
\end{minipage}

\vspace{3em}

\textbf{Signed in the presence of:}

\vspace{2em}

\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
@@witness1@@
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\centering
\underline{\hspace{5cm}} \\
@@witness2@@
\end{minipage}

\vspace{3em}

\newpage
\begin{center}
\textbf{ACKNOWLEDGMENT}
\end{center}

Republic of the Philippines \\
@@countryplace@@ \hfill SS.

\vspace{1em}

BEFORE ME, a Notary Public for and in the above jurisdiction, personally appeared:

\vspace{0.5em}
\begin{tabular}{@{}lll@{}}
\textbf{Name} & \textbf{Competent Evidence of Identity} & \textbf{Date/Place Issued} \\[0.3em]
@@sellername@@ & @@sellerid@@ & @@sellerdateid@@ \\{}
@@buyername@@ & @@buyerid@@ & @@buyerdateid@@ \\
\end{tabular}

\vspace{1em}

known to me and to me known to be the same persons who executed the foregoing Contract to Sell consisting of \underline{\hspace{1cm}} page(s), including this page on which the acknowledgment is written, and acknowledged to me that the same is their free and voluntary act and deed.

\vspace{1em}

WITNESS MY HAND AND SEAL on the date and place first above written.

\vspace{3em}

\underline{\hspace{6cm}} \\
Notary Public

\vspace{1em}
Doc. No. \underline{\hspace{2cm}} \\
Page No. \underline{\hspace{2cm}} \\
Book No. \underline{\hspace{2cm}} \\
Series of \underline{\hspace{2cm}}

\end{document}
""")
contract_to_sell = (
contract_to_sell_template
.replace("@@day@@", day_sell)
.replace("@@month@@", month_sell)
.replace("@@year@@", year_sell)
.replace("@@place@@", place_sell)
.replace("@@country@@", country_sell)
.replace("@@sellercivil@@", vendor_civil_status)
.replace("@@selleraddress@@", vendor_address)
.replace("@@buyercivil@@", vendee_civil_status)
.replace("@@buyeraddress@@", vendee_address)
.replace("@@description@@", item_description)
.replace("@@pricefigures@@", price_figures)
.replace("@@pricewords@@", price_words)
.replace("@@downpayment@@", down_payment)
.replace("@@balance@@", balance_amount)
.replace("@@paymentschedule@@", payment_schedule)
.replace("@@paymentmode@@", payment_mode)
.replace("@@graceperiod@@", grace_period)
.replace("@@possessionterms@@", possession_terms)
.replace("@@riskparty@@", risk_party)
.replace("@@expensesparty@@", expenses_party)
.replace("@@cityprovince@@", city_province)
.replace("@@witness1@@", sell_witness)
.replace("@@witness2@@", sell_witness_2)
.replace("@@countryplace@@", country_sell + " " + place_sell)
.replace("@@sellerid@@", vendor_id)
.replace("@@buyerid@@", vendee_id)
.replace("@@sellerdateid@@", vendor_id_date_place)
.replace("@@buyerdateid@@", vendee_id_date_place)
.replace("@@sellername@@", vendor_name)
.replace("@@buyername@@", vendee_name)
)

print("Paste the overleaf LaTEX code below: ")
print(contract_to_sell)

elif c2 == "8":
resign_name = input("Enter the name of your client: ")
resign_address = input("Enter the address of you client: ")
resign_city_province = input("Enter the city or province of your client: ")
resign_zip = input("Enter the zip code: ")
while True:
resign_email_question = input("Does you client has an email? (y/n): ")
if resign_email_question == "y":
resign_email_question = input("Enter the email of your client: ")
break
elif resign_email_question == "n":
resign_email_question = " "
break
else:
print("Invalid Choice")

while True:
resign_phone_question = input("Does you client has a phone number (y/n): ")
if resign_phone_question == "y":
resign_phone_question = input("Enter the phone number of your client: ")
break
elif resign_phone_question == "n":
resign_phone_question = " "
break
else:
print("Invalid Choice")
resign_date = input("Enter the date of resignation: ")
resign_recipient = input("Enter the recipient's name: ")
resign_position = input("Enter the recipient's position (e.g. Manager, HR, etc): ")
resign_company = input("Enter the company's name: ")
resign_company_address = input("Enter the company's address: ")
resign_former_position = input("Enter your client's position at the comapny: ")
resign_last_day = input("Enter your client's last day at the company (date) : ")

paragraphs = int(input("How many paragraphs does the resignation letter have?: "))
contents = []
for z in range(1, paragraphs+1):
entry = get_multiline_input("Paste paragraph number " + str(z) + ": ")
contents.append(entry)

resignation_letter_template_one = textwrap.dedent(r"""\documentclass[11pt]{article}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{times}
\usepackage{setspace}
\setstretch{1.15}
\pagenumbering{gobble}

\begin{document}

\begin{flushleft}
@@fullname@@ \\{}
@@clientaddress@@ \\{}
@@place@@, @@zip@@ \\{}
@@email@@ \\{}
@@contact@@
\end{flushleft}

\vspace{1em}
\noindent
@@resignationdate@@

\vspace{1em}
\noindent
@@recipient@@ \\{}
@@recipient_position@@ \\{}
@@company_name@@ \\{}
@@company_address@@

\vspace{1em}
\noindent
Dear @@recipient@@,

""")

resignation_letter_template_one_final = (
resignation_letter_template_one
.replace("@@fullname@@", resign_name)
.replace("@@clientaddress@@", resign_address)
.replace("@@place@@", resign_city_province)
.replace("@@zip@@", resign_zip)
.replace("@@email@@", resign_email_question)
.replace("@@contact@@", resign_phone_question)
.replace("@@resignationdate@@", resign_date)
.replace("@@recipient@@", resign_recipient)
.replace("@@recipient_position@@", resign_position)
.replace("@@company_name@@", resign_company)
.replace("@@company_address@@", resign_company_address)
)

print(resignation_letter_template_one_final)
for i in contents:
print("\\vspace{1em}")
print("\\noindent")
print(i)
print()

print("\\vspace{1em}")
print("\\noindent")
print()

print("Thank you again for the opportunity to be part of " + str(resign_company) + ". I wish the company continued success in the future.")
print("\\vspace{1.2em}")
print("\\noindent")
print("Sincerely,")
print("\\vspace{2em}")
print("\\noindent")
print("\\textbf{" + str(resign_name) + "} \\\\")
print(str(resign_former_position))
print("\\end{document}")

else:
print("Invalid Choice")


elif c == "2":
print("See you soon! ")
break

else:
print("Invalid Input. Please Try Again")
print("")
continue

print("")

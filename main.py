
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from time import sleep
from random import choice
from threading import Thread

running = True

paragraph = ["A teacher's professional duties may extend beyond formal teaching. Outside of the classroom teachers may accompany students on field trips, supervise study halls, help with the organization of school functions, and serve as supervisors for extracurricular activities. In some education systems, teachers may have responsibility for student discipline.",
             "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study,  The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed... fast typists... keep their hands fixed on one position, instead of moving them over the keyboard, and more consistently use the same finger to type a certain letter. To quote doctoral candidate Anna Feit: 'We were surprised to observe that people who took a typing course, performed at similar average speed and accuracy, as those that taught typing to themselves and only used 6 fingers on average",
             "The first personnel management department started at the National Cash Register Co. in 1900. The owner, John Henry Patterson, organized a personnel department to deal with grievances, discharges and safety, and training for supervisors on new laws and practices after several strikes and employee lockouts. During the 1970s, companies experienced globalization, deregulation, and rapid technological change which caused the major companies to enhance their strategic planning and focus on ways to promote organizational effectiveness. This resulted in developing more jobs and opportunities for people to show their skills which were directed to effective applying employees toward the fulfillment of individual, group, and organizational goals. Many years later the major/minor of human resource management was created at universities and colleges also known as business administration.",
             "An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission. One example: Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets. Products on the market must reveal the names of all ingredients on the label. Language must be in clear and precise terms that can be understood by everyone. This practice is very crucial for the lives of many people. It is prudent that we recall that the FDA specifically requires that all goods are pure, safe, and wholesome. The FDA states that all goods be produced under highly sanitary conditions. Drugs must be completely safe and must also be effective for their stated purpose. This policy applies to cosmetics that must be both safe and pure. Individuals are often totally unappreciative of the FDA's great dedication.",
             "Two members of the 1984 class of Jefferson High School are chairing a group of 18 to look for a resort for the 20-year class reunion. A lovely place 78 miles from the city turns out to be the best. It has 254 rooms and a banquet hall to seat 378. It has been open 365 days per year since opening on May 30, 1926. They will need 450 to reserve the resort. Debbie Holmes was put in charge of buying 2,847 office machines for the entire firm. Debbie visited more than 109 companies in 35 states in 6 months. She will report to the board today in Room 2784 at 5 p.m. The board will consider her report about those 109 firms and recommend the top 2 or 3 brands to purchase. Debbie must decide before August 16. Lynn Greene said work started on the project March 27, 2003. The 246 blueprints were mailed to the office 18 days ago. The prints had to be 100 percent accurate before they were acceptable. The project should be finished by May 31, 2025. At that time there will be 47 new condominiums, each having at least 16 rooms. The building will be 25 stories.",
             "The fastest typing speed ever, 216 words per minute, was achieved by Stella Pajunas-Garnand from Chicago in 1946 in one minute on an IBM electric. As of 2005, writer Barbara Blackburn was the fastest English language typist in the world, according to The Guinness Book of World Records. Using the Dvorak Simplified Keyboard, she had maintained 150 wpm for 50 minutes, and 170 wpm for shorter periods, with a peak speed of 212 wpm. Blackburn, who failed her QWERTY typing class in high school, first encountered the Dvorak keyboard in 1938, quickly learned to achieve very high speeds, and occasionally toured giving speed-typing demonstrations during her secretarial career. She appeared on Late Night with David Letterman on January 24, 1985, but felt that Letterman made a spectacle of her. Blackburn died in April 2008.",
             "Editing is a growing field of work in the service industry. Paid editing services may be provided by specialized editing firms or by self-employed (freelance) editors. Editing firms may employ a team of in-house editors, rely on a network of individual contractors or both. Such firms are able to handle editing in a wide range of topics and genres, depending on the skills of individual editors. The services provided by these editors may be varied and can include proofreading, copy editing, online editing, developmental editing, editing for search engine optimization (SEO), etc. Self-employed editors work directly for clients or offer their services through editing firms, or both. They may specialize in a type of editing and in a particular subject area. Those who work directly for authors and develop professional relationships with them are called authors' editors.",
             ]


def Reset():
    sample.config(text=choice(paragraph))
    input.delete(0, END)
    input.config(state=DISABLED)

    global running
    running = False


def play():
    time_elapsed = 0
    global speed
    while running:
        time_elapsed += 0.1
        sleep(0.1)
        speed.config(text=f"Typing Speed:\n{60*len(input.get())/time_elapsed:.2f} Characters/minute\n{60*len(input.get().split(' '))/time_elapsed:.2f}  Words/minute")

def start():
    global running
    input.config(state=NORMAL)
    running = True
    thread = Thread(target=play)
    thread.start()


app = Tk()
app.title("Typing Speed Test")
app.geometry("1600x1000")

canvas = Canvas(app, width=1600, height=1000, bg="#33FFC1",)
canvas.grid(column=0, row=0, columnspan=5, rowspan=4, ipadx=0, ipady=0, padx=0, pady=0,)

header = Label(app, text="Follow the sample text to test your typing speed.", font="Ariel 22 bold", bg="#FFBB33", fg="red", height=1)
header.grid(column=2, row=0, ipadx=0, ipady=0, padx=0, pady=0, sticky="we")

sample = Label(app, text=choice(paragraph), bg="#33DDFF", font="Ariel 14 bold", wraplength=1000, fg="black",)
sample.grid(column=2, row=1, ipadx=0, ipady=0, padx=0, pady=20, sticky="nsew")

input = Entry(app, bg="#33DDFF", font="Ariel 18 bold", fg="black", state=DISABLED)
input.grid(column=2, row=2, ipadx=0, ipady=0, padx=0, pady=20, sticky="nsew")


speed = Label(app, text="Typing Speed:\n0.0 Characters/s\n0.0 Words/s", font="Ariel 18 bold")
speed.grid(column=3, row=1)

reset = Button(app, text="Rest", font="Ariel 22 bold", command=Reset)
reset.grid(column=3, row=3,)

start = Button(app, text="Start", font="Ariel 22 bold", command=start)
start.grid(column=2, row=3,)


app.mainloop()
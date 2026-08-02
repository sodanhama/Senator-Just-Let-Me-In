define s = Character("", color="#fff", what_italic=True)
define crowd = Character("...", color="#8a8a8a")

define daamin = Character(f"Senator Daamin", color="#DEF4C6")
define manan = Character(f"Senator Manan", color="#1C7C54")
define renran = Character(f"Senator Renran", color="#73E2A7")
transform custom_left:
    xcenter 0.2
    yalign 1.0
transform custom_center:
    xcenter 0.5
    yalign 1.0
transform custom_right:
    xcenter 0.8
    yalign 1.0
default approved = True

image bg room = Transform("bg room.png", fit="cover")

init python:
    def approve():
        global approved
        approved = True

    def deny():
        global approved
        approved = False

screen approve_key():
    key "`" action [Function(approve), Return()]
    key "=" action [Function(deny), Return()]

define questions = [
    "I secretly approach you and offer three Hackatime hours, however I get to change your Slack profile for a week. Do you accept or reject my offer?",
    "Do you know the unofficial IKEA mascot of Hack Club? If so, who is it?",
    "Monster or Celsius?",
    "What is your favorite text editor? (Mine is Notepad.)",
    "An anon makes a meta post about you for snoring too loudly. How would you react?",
    "Best YSWS of all time? (It better be one that I organized.)",
    "The average teen consumes ___ mg of caffeine at a hackathon.",
    "What day of the week is it if a cow goes moo and the sky is blue?",
    "Here's a joke: A bug tester walks, jumps, and crawls into a bar, and orders a steak wrapped in cheese. Everything is fine. A normal customer walks into a bar and orders a coffee. The bar explodes. (You can laugh now.)",
    "How many full-sized durians have you consumed in your lifetime?",
    "Every hacker's worst nightmare is merging pull requests, wouldn't you agree?",
    "What is the coolest project you have ever created?",
    "What's the highest number of hours you have logged in one day?",
    "Who is the coolest Hack Clubber you know?",
    ":skulk: or :sparkling_heart:?",
    "Are you Singaporean? (Think carefully.)",
    "Have you ever fallen in public and lost massive amounts of aura? (Speaking from personal experience.)",
    "Are you the type of person to put in a roll of toilet paper under, with the loose end next to the wall? (If you say yes, I hope your pillow is warm on both sides tonight.)",
    "Grrrr.... I don't like the vibe I am getting from you. Tell me a joke to persuade me.",
    "Back in my day, we had to write our code using pen and paper. You should be grateful. (Please explain how grateful you are.)",
    "What song artists do you like?",
    "Are you a Fusion, SolidWorks, or Tinkercad type of person?",
    "You can rest now; this is a free question (could or could not be a trick).",
    "What is the purpose of your visit to Singapore?",
    "What is the capital of Singapore?",
    "Have you visited the Marina Bay Sands?",
    "What do you think you said in your SGAC that made us stop and question you?"
]


label start:

    scene bg airport

    play music "audio/journey.wav"

    "You are a hack clubber."

    s "This is the first time I've travelled abroad."

    "You're excited to explore Singapore."

    "You have to go through immigration and use the MRT to reach the venue."

    scene bg immigration

    play music "audio/regrowth wip.wav"

    "You are at the immigration counter."

    crowd "Looks better than the US immigration counter, I guess."

    "You think it's a good idea to get going as you scan your passport..."

    "However, you are met with a stern rejection message on the display. There seems to be a problem with your SGAC"

    crowd "Uh oh, that's a first."

    "You panic."

    s "Really?"

    show manan at custom_left
    show daamin at custom_center
    show renran at custom_right

    "Three immigration officers appear.You are escorted by a group of three immigration officers."

    "The officers seem familiar: the handsome Manan, the quirky Daamin, and the kind Renran."

    menu:
        "Go along with Manan":
            $ officer = manan
            show manan
        "Go along with Daamin":
            $ officer = daamin
            show daamin
        "Go along with Renran":
            $ officer = renran
            show renran
    officer "Please follow me to the immigration office."
        
    play music "audio/boss battle.wav"
    hide daamin
    hide manan
    hide renran
    if officer == manan:
        show manan at left
    elif officer == daamin:
        show daamin at left
    elif officer == renran:
        show renran at left

    s "What am I gonna do? I need my MRT card to get around Singapore..."

    "His pickup time was scheduled for 10:00 AM, and it was later found out that Hack Club never did the pickup."
    officer "Hmm"


    officer "Hello, welcome to Singapore. May I see your passport and visa?"

    s "Of course you can... what other choice do I have?"

    officer "This is the sketchiest visa I've ever seen. I don't think this is valid."
    
    officer "I'm going to have to ask you some questions to determine if you are a criminal or not. Please answer them truthfully."
    init python:
        import random

    scene bg room
    play music "audio/yeahhhhh yuh.wav"
    if officer == manan:
        show manan at left
    elif officer == daamin:
        show daamin at center
    elif officer == renran:
        show renran at right


    $ selected_questions = random.sample(questions, 10)

    python:
        for q in selected_questions:
            renpy.say(officer, q)
            answer = renpy.input(">")


    show manan at left
    show daamin at center
    show renran at right

    "The officers sit together and discuss your application."

    s "Really? I thought this was my only hope..."

    "You've done nothing wrong."

    s "I can feel the evil glint of the officers' eyes as they look at me."
    scene bg loading
    play music "audio/yeahhhhh yuh.wav"

    hide manan
    hide daamin
    hide renran

    show screen approve_key
    $ renpy.pause(hard=True)
    hide screen approve_key

    if approved:
        show approved
        officer "Congratulations! Your application has been approved."

        s "Thank you so much!"

        "You are given your MRT card and allowed to explore Singapore."
    else:
        show denied
        officer "I'm sorry, but your application has been rejected."

        s "What? Why?"

        "You are escorted back to the airport and sent back home."

    

    return

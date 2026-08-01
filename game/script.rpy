define s = Character("", color="#fff", what_italic=True)
define crowd = Character("...", color="#8a8a8a")

define daamin = Character(f"Senator Daamin", color="#DEF4C6")
define manan = Character(f"Senator Manan", color="#1C7C54")
define renran = Character(f"Senator Renran", color="#73E2A7")

define approved = True
define intent = True

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
    "Du bist gut _____???",
    "Do you like triple t.",
    "What's the highest number of hours you have logged in one day?",
    "Who is the coolest Hack Clubber you know?",
    ":skulk: or :sparkling_heart:?",
    "Are you Singaporean? (Think carefully.)",
    "Fun fact: you are now manually breathing.",
    "Have you ever fallen in public and lost massive amounts of aura? (Speaking from personal experience.)",
    "Are you the type of person to put in a roll of toilet paper under, with the loose end next to the wall? (If you say yes, I hope your pillow is warm on both sides tonight.)",
    "Happy happy haaappyyy, do do do do do dooo",
    "Grrrr.... I don't like the vibe I am getting from you. Tell me a joke to persuade me.",
    "Back in my day, we had to write our code using pen and paper. You should be grateful. (Please explain how grateful you are.)",
    "What song artists do you like?",
    "Are you a Fusion, SolidWorks, or Tinkercad type of person?",
    "You can rest now; this is a free question (could or could not be a trick).",
    "What is the purpose of your visit to Singapore?",
    "What is the capital of Singapore?",
    "How tall is the Rain Vortex at Jewel Changi Airport?",
    "Have you visited the Marina Bay Sands?",
    "What do you think you said in your SGAC that made us stop and question you?"
]


label start:

    scene bg airport

    "You are a hack clubber"

    s "This is the first time I've travelled abroad"

    "You're excited to explore Singapore"

    "You have to go through immigration and use the MRT to mak..."

    scene bg immigration

    "You are at the immigration counter."

    crowd "Better than the US immigration counter in the USA, I guess."

    "You think it's a good idea to get going as you scan your passport..."

    "However, you are met with a stern rejection message on the display."

    crowd "oooohh, that's a first."

    "You panic"

    s "Really?"

    "The first time you've travelled alone, you're met with rejection."

    "You are escorted by a group of three immigration officers."

    "The officers seem familiar: the handsome Manan, the quirky Daamin, and the kind Renran."
    menu:
        "Go along with Manan":
            $ officer = manan
        "Go along with Daamin":
            $ officer = daamin
        "Go along with Renran":
            $ officer = renran

    officer "Please follow me to the immigration office."

    scene bg room

    s "What am I gonna do? I need my MRT card to get around Singapore..."

    "His pickup time was scheduled for 10:00 AM, and it was later found out that Hack Club never did the pickup."
    officer ""

    if officer == daamin:
        show daamin
    elif officer == manan:
        show manan
    elif officer == renran:
        show renran

    officer "Hello, welcome to Singapore. May I see your passport and visa?"

    s "Of course you can... what other choice do I have?"

    officer "This is the sketchiest visa I've ever seen. I don't think this is valid."
    
    init python:
        import random

    scene bg loading

    $ selected_questions = random.sample(questions, 10)

    python:
        for q in selected_questions:
            renpy.say(officer, q)
            answer = renpy.input(">")

    $ approved = renpy.random.choice([True, False])

    show manan
    show daamin
    show renran

    "The officers sit together and discuss your application."

    s "Really? I thought this was my only hope..."

    "You've done nothing wrong."

    s "I can feel the evil glint of the officers' eyes as they look at me."

    "Do you want the application to be approved?"

    menu:
        "Yes":
            $ intent = True
        "No":
            $ intent = False

    if approved == intent:
        show approved
        "SGAC approved"
    else:
        show denied
        "SGAC denied"

    return

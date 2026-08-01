define s = Character("Narrator", color="#fff", what_italics=True)
define approved = True
define crowd = Character("...", color="#8a8a8a")
define daamin = Character(f"Senator Daamin", color="#DEF4C6")
define manan = Character(f"Senator Manan", color="#1C7C54")
define renran = Character(f"Senator Renran", color="#73E2A7")
define officer = renpy.random.choice([daamin, manan, renran])

label start:

    scene bg airport

    "You are a hack clubber"

    "This is the first time you've travelled abroad and you are excited to explore Singapore."

    "You have to go through immigration and use the MRT to mak..."

    scene bg immigration

    "You are at the immigration counter."

    crowd "Better than the US immigration counter in the USA, I guess."

    "You think it's a good idea to get going as you scan your passport..."

    "However, you are met with a stern rejection message on the display."

    crowd "oooohh, that's a first."

    "You panic"



    
    $ officer = renpy.random.choice([daamin, manan, renran])

    if officer == daamin:
        show daamin
    elif officer == manan:
        show manan
    elif officer == renran:
        show renran

    officer "Hello, welcome to Singapore. May I see your passport and visa?"
    
    scene bg room

    scene bg loading

    $ approved = renpy.random.choice([True, False])

    if approved:
        show approved
        "SGAC approved"
    else:
        show denied
        "SGAC denied"

    return

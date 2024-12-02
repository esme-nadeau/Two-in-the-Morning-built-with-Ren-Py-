define e = Character("Eden")
define s = Character("Seneca")
define w = Character("Professor Whitney")

label start:
    $ init_eden = True
    $ init_eden2 = True
    $ init_fridge = True
    $ eden_convo1_comp = False
    $ seneca_convo_prog = False
    $ whitney_convo_prog = False
    $ show_pencils = False
    $ whitney_awake = True

    $ init_whitney = True

    $ whitney_ending = False
    $ seneca_ending = False

    $ has_ed = False
    $ has_pencil = False
    $ has_code = False

    scene bg room_0_email
    with fade
    menu:
        "It's going to be fine.":
            jump start2

label start2:
    menu:
        "I'll just explain that I've been having a really hard semester, and I'm sorry if I totally end up failing this exam or something.":
            jump start3

label start3:
    show screen email1
    menu:
        "Wait... she definitely doesn't know my name. I'm probably the least remarkable person in her class.":
            jump start4

label start4:
    show screen email2
    menu:
        "It's ok, I'll just type my name here and introduce myself. Finally.":
            jump start5

label start5:
    $ username = ""
    call screen email3
    show screen email4
    menu:
        "Perfect. Now I just have to-":
            jump start6

label start6:
    e "[username], what are you doing on your computer? It's two in the morning."
    jump scn_room1

label scn_room1:

    hide screen email4
    hide screen email3
    hide screen email2
    hide screen email1
    scene bg room_1
    call screen room1

label fridge_open:

    if init_eden:
        show edensitting1:
            pos (867, 503)
    "You found an energy drink in Eden's fridge."
    "You put it in your pocket for later."
    $ init_fridge = False
    $ has_ed = True
    jump scn_room1

label eden_convo1:

    $ eden_convo1_comp = True
    show eden neutral
    e "Hey."
    show eden talking
    e "You're up late."
    e "Wanna pull an all-nighter before the most important midterm of the year?"
    show eden laughing
    e "Bold move, but I'm in."
    show eden neutral
    menu:
        "I just can't sleep. I'm too stressed, I guess.":
            jump eden_convo1_2

label eden_convo1_2:
    show eden talking
    e "You're stressed? You'll be fine, [username]. You studied, didn't you?"
    show eden neutral
    menu:
        "I mean, yeah. But none of this stuff comes naturally to me.":
            jump eden_convo1_3

label eden_convo1_3:
    show eden laughing
    e "You always say that. I think you're worrying too much."
    show eden angry
    e "I'm a little annoyed, 'cuz I left my notebook in our classroom after lecture today."
    e "I had some great notes in there! And I was finally gonna learn the Red-Black Tree deletion algorithm in my spare time before the test tomorrow."
    show eden laughing 
    e "I'll have to rely on my superhuman intuition, I guess."
    show eden neutral
    menu:
        "...I can go get it for you.":
            jump eden_convo1_4

label eden_convo1_4:
    show eden talking
    e "Seriously?"
    show eden laughing
    e "You're the best roommate ever! Thanks so much!"
    show eden talking 
    e "While you do that, I'll go take a walk around campus."
    e "See you soon, [username]!"
    $ init_eden = False
    jump scn_room1

label seneca_convo1:

    $ seneca_convo_prog = True
    show seneca neutral
    s "Hey, it's Eden's roommate!"
    menu:
        "It's [username]. But... yeah.":
            jump seneca_convo1_2

label seneca_convo1_2:
    show seneca smiling 
    s "That's right. [username]."
    show seneca neutral
    s "What are ya doing out so late, [username]? We've got a midterm tomorrow."
    menu:
        "I could ask the same of you.":
            jump seneca_convo1_3

label seneca_convo1_3:
    show seneca smiling
    s "Just came back from a party. I'm not worried for the test. I'm not some tryhard like you and Eden."
    show seneca neutral
    s "But seriously, what're you doing out here?"
    menu:
        "Eden left his notebook in our classroom. I'm gonna go get it for him.":
            jump seneca_convo1_4

label seneca_convo1_4:
    show seneca smiling
    s "Haha, classic!"
    show seneca neutral
    s "The computer science building is locked. You're lucky I'm here, I know the passcode."
    show seneca smiling 
    s "Tell you what... I need a pencil for tomorrow's test. Find a pencil for me, and I'll tell you the code."
    menu:
        "Sure. I'll be right back.":
            $ seneca_convo_prog = False
            $ show_pencils = True
            jump scn_room3

label whitney_convo1:

    $ whitney_convo_prog = True
    $ init_whitney = False
    show whitney neutral
    w "...?"
    w "Wait, you're in my class. You sit next to Eden."
    menu:
        "Yeah. My name's [username].":
            jump whitney_convo1_2

label whitney_convo1_2:
    show whitney smiling
    w "Right. Good to meet you."
    show whitney neutral
    w "But what are you doing up? It's two in the morning and you have an exam tomorrow."
    menu:
        "You're GIVING an exam tomorrow...":
            jump whitney_convo1_3

label whitney_convo1_3:
    w "Ugh. I'm still writing it."
    menu:
        "You're still... writing our midterm??":
            jump whitney_convo1_4

label whitney_convo1_4:
    w "Become a professor and you'll understand."
    w "I feel like I'm gonna fall asleep... I just wish I had something to keep me awake."
    show whitney smiling
    w "Good luck on the exam, ok? Don't stay out too late."
    $ whitney_convo_prog = False
    jump scn_room4

label needs_ed:
    show whitneysitting:
        pos (755, 513)
    "Professor Whitney looks tired..."
    jump scn_room4

label whitney_convo2:
    show whitney neutral
    w "...Yes?"
    menu:
        "Give your professor your energy drink.":
            jump whitney_convo2_2
        "Nevermind...":
            jump scn_room4

label whitney_convo2_2:
    show whitney smiling
    w "...Really?"
    w "Thank you so much. You saved me, seriously."
    $ whitney_ending = True
    jump scn_room4

label whitney_convo3:
    show whitney smiling
    w "Thanks again, [username]. I feel better already."
    jump scn_room4

label whitney_is_asleep:
    show whitneysleeping:
        pos (764, 544)
    "She fell asleep."
    "The answer key is right there..."
    menu:
        "Take a picture and send it to Seneca!":
            jump whitney_is_asleep2
        "I'll pretend I didn't see it...":
            jump scn_room4

label whitney_is_asleep2:
    $ seneca_ending = True
    "You took a picture and texted it to Seneca."
    "You feel a little morally bankrupt, but not enough to be truly guilty."
    jump scn_room4

label get_out:
    show whitneysleeping:
        pos (764, 544)
    "Better get out of here before you get caught..."
    jump scn_room4

label scn_room2:

    scene bg room_2
    call screen room2

label pencil_found:
    "You found a pencil!"
    "You put it in your pocket."
    $ show_pencils = False
    $ has_pencil = True
    jump scn_room2

label scn_room3:

    scene bg room_3
    call screen room3

label get_pencil_mes:
    show senecasitting:
        pos (474, 537)
    "Seneca needs a pencil!"
    jump scn_room3

label seneca_convo2:
    $ seneca_convo_prog = True
    show seneca neutral
    s "You found a pencil for me. Thanks, [username]."
    s "Ok, I wrote down the passcode for you. You'll be able to unlock the door now."
    "Seneca gave you a slip of paper with a bunch of 1's and 0's on it."
    $ has_code = True
    show seneca smiling 
    s "It says 'password' in binary. Can you believe these people?"
    s "One more thing..."
    show seneca neutral 
    s "Professor Whitney's desk is right inside."
    show seneca smiling
    s "Let's say, hypothetically, you can find a way to steal the answer key for our midterm..."
    s "Well... just let me know what you find, ok?"
    menu:
        "Ok, Seneca...":
            jump scn_room3

label scn_room4:

    scene bg room_4
    call screen room4

label scn_room5:

    if not whitney_ending:
        $ whitney_awake = False
    scene bg room_5
    call screen room5

label eden_convo2:
    $ init_eden2 = False
    show eden laughing
    e "Beat you to it!"
    show eden talking 
    e "Thanks for unlocking the building for me. I got my notebook, so I'm ready to get some sleep."
    e "What about you?"
    show eden neutral
    menu:
        "Yeah, let's head back to our dorm.":
            if seneca_ending:
                jump endings
            else:
                jump endingn
        "Not yet...":
            jump scn_room5

label eden_convo3:
    show eden talking 
    e "Ready to go yet?"
    show eden neutral
    menu:
        "Yeah, let's head back to our dorm.":
            if seneca_ending:
                jump endings
            else:
                jump endingn
        "Not yet...":
            jump scn_room5

label endingn:
    scene bg room_1
    with fade
    show eden talking
    e "Thanks again."
    show eden laughing
    e "You're a good roommate, y'know? I appreciate you."
    show eden talking
    e "Good luck on the test, ok? See you tomorrow."
    menu:
        "Goodnight, Eden. You too!":
            if whitney_ending:
                jump endingw
            else:
                jump endingn_2

label endingn_2:
    scene bg room_0
    e "Goodnight."
    e "I'm gonna turn the lights off now, ok?"
    scene bg black
    with Dissolve(1.0)
    show screen end_creds
    pause 2.0
    return

label endingw:
    scene bg room_0
    menu:
        "Hey, I got a new email. At two in the morning?":
            jump endingw_2

label endingw_2:
    scene bg room_0_email2
    show screen email5
    menu:
        "Oh. That's... so sweet.":
            jump endingw_3

label endingw_3:
    hide screen email5
    scene bg room_0
    menu: 
        "I think tomorrow is going to be fine, after all.":
            jump endingw_4

label endingw_4:
    e "I'm gonna turn the lights off now, ok?"
    scene bg black
    with Dissolve(1.0)
    show screen end_creds
    pause 2.0
    return

label endings:
    scene bg room_1
    with fade
    show seneca neutral
    s "Hey, [username]."
    show seneca smiling:
        xpos 500
    show eden neutral:
        xpos 400
    s "Hey, [username]'s roommate."
    show seneca neutral
    show eden talking
    e "Very funny, Seneca."
    show eden neutral
    show seneca smiling
    s "Your roommate just made my night a whole lot better, Eden. You're no longer my favorite occupant of room 001."
    show eden laughing 
    show seneca neutral 
    e "Oh really?"
    show seneca phone
    show eden neutral 
    window hide
    pause 1.5
    show eden laughing
    e "No way. The answer key?? You're crazy, [username]. I love it."
    show seneca smiling 
    s "I'll help you guys memorize this if you let me hang out for awhile. You're a lot cooler than my roommate."
    show seneca neutral
    show eden talking 
    e "Are you down, [username]?"
    show eden neutral
    menu:
        "Totally!":
            jump endings_2

label endings_2:
    show eden laughing 
    show seneca phone
    e "Let's get started!"
    scene bg black
    with Dissolve(1.5)
    show screen end_creds
    pause 2.0
    return
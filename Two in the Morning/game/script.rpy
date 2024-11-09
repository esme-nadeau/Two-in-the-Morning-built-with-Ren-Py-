define e = Character("Eden")

label start:
    $ init_eden = True
    $ init_fridge = True
    $ eden_convo1_comp = False
    $ show_pencils = False
    jump scn_room1

label scn_room1:

    scene bg room_1
    call screen room1

label eden_convo1:

    $ eden_convo1_comp = True
    show eden neutral
    e "placeholder dialogue"
    $ init_eden = False
    jump scn_room1

label scn_room2:

    scene bg room_2
    call screen room2

label scn_room3:

    return
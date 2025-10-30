
# ---------- STAGE 3: Exit ----------
def Exit():
    print("DunMaster: Before you is a massive gate on the top of the door you see a symbol that says \"Egress\".\n"
          "DunMaster: And there are blocks on the ground that look like they can be stepped on.\n")
    print("DunMaster: What will you do?\n"
          "[1]  Step on the blocks according to the book you found in the library\n"
          "[2]  Go back to the library")
    answer = ""
    while answer not in ("1", "2"):
        answer = input("> ")
    if answer == "1":
        print("DunMaster: You step on the blocks in the order you found in the book: Up, Left, Up, Right, Right, Up.\n"
              "DunMaster: The gate opens and you step outside into freedom!\n"
              "DunMaster: Congratulations you have escaped the DunDun Dungeon!")
    else:
        print("DunMaster: You go back to the library.\n")
        library()
    exit(0)

# ---------- STAGE 2.2: library search ----------
def library_search():
    print("DunMaster: You search the library.\n"
          "After a while you find a book that seems to describe the symbols on the door it says \"A, B, C, D\".\n"
          "You read the book and learn that the symbols represent a simple code.\n")
    print("DunMaster: Do you search library more or try to open the door?\n"
          "[1]  Search the library more\n"
          "[2]  Try to open the door with symbols")
    answer = ""
    while answer not in ("1", "2"):
        answer = input("> ")
    if answer == "1":
        print("DunMaster: You search the library and find a book that only says \"Egress ↑ ← ↑ → → ↑\" .\n"
              "Maybe you should try the door with symbols?")
        print("DunMaster: Try to enter the code from the book to unlock the door.\n")
        Door_answer = input("DunMaster: Enter the code from the book: ")
        while Door_answer != "ABCD":
            print("DunMaster: Incorrect code.")
            Door_answer = input("DunMaster: Enter the code from the book again: ")
        print("DunMaster: The door unlocks with a satisfying click!")
        Exit()
    else:
        print("DunMaster: You approach the door with symbols but can't decipher them.\n"
              "DunMaster: On the door you see symbols that says BETA, DELTA, GAMMA, ALPHA.\n"
              "DunMaster: Maybe you should try to use the code you found in the library?\n")
        library_door()
        
# ---------- STAGE 2.1: library door ----------
def library_door():
    print("DunMaster: You approach the door with symbols but can't decipher them.\n"
          "DunMaster: On the door you see symbols that says BETA, DELTA, GAMMA, ALPHA.\n"
          "DunMaster: Maybe you should try to search the library for clues?\n")
    print("[1] Use brute force to open the door\n"
          "[2] Search the library for clues\n"
          "[3] Try to enter the code randomly")
    answer = ""
    while answer not in ("1", "2", "3"):
        answer = input("> ")
    if answer == "1":
        print("DunMaster: You try to force the door open but it won't budge.\n"
              "DunMaster: Maybe you should try to search the library for clues?")
        library_search()
    elif answer == "2":
        library_search()
    else:
        tries = 0
        Door_answer = ""
        while Door_answer != "ABCD" and tries < 3:
            Door_answer = input("DunMaster: Enter the code from the book:\n> ")
            tries += 1
            if Door_answer == "ABCD":
                print("DunMaster: The door unlocks with a satisfying click!")
                Exit()
            else:
                print("DunMaster: Incorrect code.")
        if tries >= 3:
            print("DunMaster: Too many dumb answers.")
            library_door()

# ---------- STAGE 2: Library ----------
def library():
    import time
    print("DunMaster: You get to the door.\n"
          "[1]  Grab the handle and open the door\n"
          "[2]  Stare at the door")
    answer = ""
    while answer not in ("1", "2"):
        answer = input("> ")
    if answer == "1":
        print("DunMaster: Before you is a beautiful library filled with thousands of books!")
    else:
        time.sleep(2)
        print("DunMaster: You don't know how doors work?")
        print("DunMaster: Maybe try to open the door?\n"
              "[1]  Grab the handle and open the door\n"
              "[2]  Stare at the door some more")
        answer = ""
        while answer not in ("1", "2"):
            answer = input("> ")
        if answer == "1":
            continue_library()
        else:
            print("DunMaster: You are weird you know that?")
            print("DunMaster: Are you trying to scare the door to open?\n"
                  "[1]  Grab the doorknob and twist it to open the door\n"
                  "[2]  Stare at the door like a maniac")
            answer = ""
            while answer not in ("1", "2"):
                answer = input("> ")
            if answer == "1":
                continue_library()
            else:
                time.sleep(2)
                print("DunMaster: Ehhh, the door opens *by magical power* and you see a huge library full of books. I don't think you ever heard of those.\n")
                continue_library()
def continue_library():
    print("DunMaster: The library has many different types of books that can help you escape\n"
          "DunMaster: At the end of the library you see a door with symbols on it\n")
    print("DunMaster: What will you do?\n"
          "[1] Search the library for clues\n"
          "[2] Walk to the door with symbols")
    answer = ""
    while answer not in ("1", "2"):
        answer = input("> ")
    if answer == "1":
        library_search()
    else:
        library_door()
        
# =============================== #
#       ✧ DUNDUNDUNGEON ✧        #
# =============================== #
print("DunMaster: Welcome to the DunDun Dungeon\n"
      "DunMaster: You need to explore and solve a few puzzles to escape")
Name = input("DunMaster: What is your name?: ")
print(f"DunMaster: Let's begin your journey {Name}!\n")

# ---------- STAGE 1: Intro / dark room ----------
print("DunMaster: You are in a dark room. You can only see a glimmer of light through the door. What will you do?\n"
      "[1]  Go towards the door\n"
      "[2]  Check out the room you are in")
answer = ""
while answer not in ("1", "2"):
    answer = input("> ")
if answer == "1":
    print("DunMaster: You are going towards the door")
    library()
else:
    print("DunMaster: You look around the room. It seems mostly empty.\n"
          "There is a strange scratch on the floor, but nothing else of immediate interest.")

# ---------- STAGE 1.1 : dark room ----------
print("DunMaster: What will you do now?\n"
      "[1]  Go towards the door\n"
      "[2]  Look around the room again")
answer = ""
while answer not in ("1", "2"):
    answer = input("> ")
if answer == "1":
    print("DunMaster: You are going towards the door\n")
    library()
else:
    print("DunMaster: You keep looking. Still nothing. The room is empty, really.\n")

# ---------- STAGE 1.2 : dark room ----------
print("DunMaster: Soo what now?\n"
      "[1]  Go through that door that I told you about twice\n"
      "[2]  Look around the room even more")
answer = ""
while answer not in ("1", "2"):
    answer = input("> ")
if answer == "1":
    print("DunMaster: You are walking towards the door\n")
    library()
else:
    print("DunMaster: IT'S A ROOM AND IT'S EMPTY\n")

# ---------- STAGE 1.3 : dark room ----------
print("DunMaster: ...OK that room is cool and whatever but you need to make progress to escape\n"
      "[1]  You are going through that nice and tempting looking door\n"
      "[2]  You keep looking at the empty room like a lunatic")
answer = ""
while answer not in ("1", "2"):
    answer = input("> ")
if answer == "1":
    print("DunMaster: You are finally going through the door\n")
    library()
else:
    print("DunMaster: Alright... you suddenly feel a magical push and are forced through the door.\n")
    library()
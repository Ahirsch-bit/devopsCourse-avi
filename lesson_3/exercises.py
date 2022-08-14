def question_1():
    try:
        a = 1 / 0
    except ZeroDivisionError:
        a = "You can't divide by 0!"
    print(a)


def question_6(name):
    file = open("words.txt", "a")
    file.write(name + "\n")
    file.close()


def question_7(name):
    question_6(name)
    f = open("words.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()


def question_8():
    f = open("words.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()


from PIL import Image, ImageDraw


def question_10():
    # Create Image object
    im = Image.new('RGB', (90, 90), 'white')

    # Draw line
    draw = ImageDraw.Draw(im)
    draw.ellipse((0, 0, 89, 89), 'green', 'blue')  # made this a little smaller..
    draw.ellipse((25, 20, 35, 30), 'yellow', 'blue')
    draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
    draw.arc((20, 40, 70, 70), 0, 180, 'black')  # draw anarc in black

    im.save('newpic.png','png')
    # Show image
    im.show()


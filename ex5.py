"""A company is looking to hire a typist with writing spped more than 60 word per minute. They asked from you to design
a program that's above 60, their will display to the user he passed the first interview and that company will contact him
later for the second interview. If speed 60 or less then inform him that the company looking only for typist with writing 
above 60 WPM"""

def tiping_input():
    print("whe are hiring a typist with certain writing speed\nyou can cheek yours at https://10fastfingers.com/typing-test/spanish")
    while True:
        try:
            speed = int(input("enter you writing speed"))
            if speed <= 0:
                raise Exception
            return speed
        
        except:
            print("type a valid integer above 0")

def aprove_disaprove(speed,target):
    if speed <= target:
        print("the company looking only for typist with writing above 60 WPM")
    if speed > target:
        print("he user passed the first interview and that company will contact him later for the second interview")


if __name__ == '__main__':
    speed = tiping_input()
    aprove_disaprove(speed, target = 60)

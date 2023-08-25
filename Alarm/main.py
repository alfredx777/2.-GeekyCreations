import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minuites_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\r{minuites_left:02d}:{seconds_left:02d}", end="")
        if minuites_left == 00 and seconds_left == 00:
            print("\rtime's up")
            playsound('alarm.mp3')


def pause():
    input("Press enter to resume.")


def main():
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds

    alarm(total_seconds)

    while True:
        command = input("Pause (p) or resume (r)? ")
        if command == "p":
            pause()
        elif command == "r":
            alarm(total_seconds)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

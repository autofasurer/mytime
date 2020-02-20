import atexit
import arrow
import sys, argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", required = True, help = "Name of the project you want to track your time spent on.")
    args = vars(parser.parse_args())

    starttime = arrow.now('Europe/Brussels')

    atexit.register(exit_handler, starttime=starttime, project=args['project'])

    while True:
        waitforquit = input(f"\033[1;32;40mCurrently timing work on {args['project']}\033[\n\033[0;37;40mType Q to quit\n")
        if waitforquit.lower() == "q":
            sys.exit()

#Funtion to convert the seconds of deltatime (endtime - starttime) to hrs/mins/sec
def format_deltatime(time_in_seconds):
    minutes, seconds = divmod(time_in_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


# Function to run when the program quits.
def exit_handler(starttime, project):
    endtime = arrow.now('Europe/Brussels')
    total_time_spent = format_deltatime((endtime - starttime).seconds)
    endtime = endtime.format('YYYY-MM-DD HH:mm:ss')
    starttime = starttime.format('YYYY-MM-DD HH:mm:ss')
    with open('mytime.txt', 'a+') as timestore:
            timestore.write(f"Work on:\t{project}\nstarted at:\t{starttime}\nended at:\t{endtime}\n")
            timestore.write('___________________________________________________\n' )
            timestore.write(f'Total:\t\t\t\t{total_time_spent}\n')
            timestore.write('===================================================\n\n')


if __name__ == '__main__':
    main()

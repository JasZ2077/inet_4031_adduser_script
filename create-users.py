#!/usr/bin/python3

# INET4031
# Wenyijie Zhao
# March 23 2026 Created
# Modified at the same day.

#Importing os for os.system, where that will let python run commands for us.
#Importing re , regular expression, we can use the match function to identify the pounds so the interpreter knows 
# that these are not the lines to scan.
# import that sys is just for that stdin can work correctly.
import os
import re
import sys

# a main function, where the code will do, as a function .

def main():
    for line in sys.stdin:

        #Regular expression here, with ^ which means starting with, in this case, anything starts with hashtag.
        match = re.match("^#",line)

        #The code splits each line into small pieces, when seeing a colon they separate it. 
        # strip is for getting rid of unnecessary elements, like escape sequences or so
        fields = line.strip().split(':')

        # Or gate and a not gate, or something like that
        # the statement is checking  whether it is a comment (line starting with hashtag above) or numbers of fields
        # the number has to equal to five, else that will be skipped.
        # if the expression turns out to be true, then it will be skipped by continue command.
        # This if statement rely on two variable: match and fields.
        # Has to equal to five, since that is how much categories of info needed from a user to build a profile.
        if match or len(fields) != 5:
            continue

        #Purpose of the next 3 lines: to assign a variable name ( so they can be recalled easily later)
        # and set them into the desired info : username, password, etc. %s %s are a place holder where field[3] and 
        # field [2] will be fitting in, depending on the given input.
        # password info will be put into the fields[1], that's the expected place to find the password
        # gecos, a linux personal info identifier. Last name and first name.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # There can be more than one group. splitting that in case if there are more than one group separated by ","
        groups = fields[4].split(',')

        #Letting user see the interaction, and letting the developers to debug. For visual purposes.
        print("==> Creating account for %s..." % (username))
        # this thing adds user, and make password uninteractive in the beginning, and add gecos and username in the end.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # No significant error on dry run
        # os.system will execute the command above to create users.
        print(cmd)
        os.system(cmd)

        # Letting whoever interacts to know that this function has functioned til this far. for visual purpose and debugging

        print("==> Setting the password for %s..." % (username))
        
	# /bin/echo outpus the strings,n for not auto changing lines and -e to enable \ n, and that double percent s makes it 
        # twice of the input of the parameters, which is password, as you can see the two password param at end
        # pipe operator is just  whatever that is on the left will be sent to usr/bin/sudo,and usr/bin/passwd
        # or that it takes output of the echo send it as input of the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #the system will run cmd to set passwords when uncommented.
        print(cmd)
        os.system(cmd)

        for group in groups:
            # this for statement is trying to assign groups. the if statement is making a base case, since '-'
            # means that there isn't an assignable group for this user.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

# classic stuff
if __name__ == '__main__':
    main()

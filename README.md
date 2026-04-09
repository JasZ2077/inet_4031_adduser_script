# inet_4031_adduser_script
# This is a README!
# READ BEFORE USE

## What it Does:
   1.Reads list of users from .input file with created Python Scripts\
   2.Creates a list of users via Terminal Commands.

## How to Run:
```bash
  python3 create-users.py < create-users.input
```
\
or\
```bash
   ./create-users.py < create-users.input
```
  ( Sudo is not necessary.)\
  (You can choose either one to implement, I recommend the first one)\
  (create-users.imput is the example file given, modify the data within or build one .input file of your own and change the name of the file accordingly)

## Implementation:
 \ 
   Creates User\
   Creates Password\
   Assigns Users to their assigned group.

## Details about Self Creation of document:
 \
   If you want to create a file, with .input ending, that it should strictly follow the fomrat of Username:Password:LastName:Firstname:GroupName1,GroupName2\
   ...groupNamex. The number of colons has to be ** EXACLY 4 ** , otherwise it will fail to operate. Plus *every users should be separated by lines*.

## Verification
 \ Check it via grip command, and check your user in your directory:\
   *grep -r user/etc/ *   \
   Or if you have tput the user in a specific directory, try to locate them and recheck.

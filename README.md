# sleepAce
Switches your pc off at 9pm to promote sleeping habits

## Motivation
I could not find any software which achieved this without either asking for money, or spamming you with adverts. All I want to do is force my pc to switch off at a certain time!

## Implementation
What I want to do can almost be entirely achieved by one command ('rundll32.exe powrprof.dll,SetSuspendState 0,1,0'), but wrapped this in some python to make it a bit more robust (read as tiny bit more robust) and slightly more elegant

This provides functionality to force switching off of PC at 9:00pm. This works in tandem with Task Scheduler to achieve this. It is hacky and has multiple edge cases which can be worked around, but does for my purpose.

# Use:
1) Create a task in Task Scheduler
    1) This should be kicked off at 8:50pm, on the days that you want this enforced (I just use week days)
    1) When created, select Task settings and get it to 'run as soon after as possible'
1) Wait until 9:00pm
1) You will get a pop up, when you click 'ok', your PC will sleep
    1) You can ignore the message, but you will get spammed by more pop ups.
1) Relax, be free. Do what people did before PCs

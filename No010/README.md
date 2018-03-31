### Disclaimer
This is not a precise scheduler, it's supposed to run tasks after a certain amount of milliseconds.</br>
It doesn't guarantee exact time of the run, can be +/- 10ms apparently(because of the sleep precision)
python main.py

###Example output: </br>
1522492604600591 Scheduling a task to be run at: 1522492605600587 </br>
Running Hello World at: 1522492605600622 </br>
Hello world </br>
1522492606603068 Scheduling a task to be run at: 1522492607103055 </br>
1522492606603126 Scheduling a task to be run at: 1522492611603123 </br>
1522492606603161 Scheduling a task to be run at: 1522492607603159 </br>
Running Hello World 2 at: 1522492607103107 </br>
Hello world 2 </br>
Running Hello World at: 1522492607603294 </br>
Hello world </br>
Running Hello World 2 at: 1522492611603258 </br>
Hello world 2 </br>
Scheduler has been stopped </br>
>>> elapsed time 12s </br>

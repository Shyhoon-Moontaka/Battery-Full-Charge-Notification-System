I have used Ubuntu as Linux Os.When I am using laptop,I have noticed that I got notification when the battery is under 20% charge.
But when the battery is charging with adapter & the charge goes up to 80%,then there have no notification comes from Os.
That's why,my laptop battery have gradually drained frequently.I have changed battery 4 times in recent 2 years.
Then I was searching for any snap or apt package/software that gives us proper notification when the battery charge becomes up to 80%.
Unfortunately, I could not found any package for battery notification.
So,I had decided to create my own python script to show notification in proper time.
I have created a virtual environment for the python script with one dependencies that is psutil.It helps the user to know the device information such as battery/charging status.
The script runs after one minutes contineously.There is a built-in package in Ubuntu to show any notification which works on command line.
To execute notification command I have used python subprocess module.It has a run method to serve the execution.
When the battery charge goes up to 80%,the script shows an alert to unplug the adapter from the laptop.
But another challenge comes here.The script could not run as background service.The script runs only when I run it.
To solve this problem,I have used Ubuntu built-in software called Startup Application which runs any script when user logged-in.
Finally,I am happy to solve the issues.

copilot_test.py
This script prints your system uptime in hours. It works on Unix/Linux and Windows systems.

What does copilot_test.py do?
On Unix/Linux: Reads /proc/uptime to display how many hours the system has been running.
On Windows: Uses the net stats srv command to extract the system uptime.
On other systems: Notifies if uptime cannot be determined.
How to Run
Clone this repository (if you haven't already):

bash
git clone https://github.com/pujitha-thota/copilot-demo.git
cd copilot-demo
Run the script with Python:

bash
python copilot_test.py
Make sure you have Python installed (version 3.x).
Example Output
Code
System Uptime: 5.32 hours
or (on Windows):

Code
System Uptime: Statistics since 6/6/2025 7:00:00 AM

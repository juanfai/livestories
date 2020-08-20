# Livestorie's Automation Suite - Developed by Juan Faisal - faisal.juan@gmail.com

Developed with:
  - Python
  - Pytest

# How to run test?

  1. Clone this project
```sh
git clone https://github.com/juanfai/livestories.git
```
  ---------------------------
  	Running test from Console
	
	2.a. Install Python 3, link: https://www.python.org/

	2.b. Install pip, link: https://pypi.org/project/pip/
  
	2.c. Go to the system terminal
 
	2.d. Browse to cloned project's root folder
  
	2.e. Run this command from the console: pip install -r requirements.txt
  
	2.f. Run: pytest . -rxXs -lv --html=./tests/reports/report.html --self-contained-html

  ---------------------------
  	Select environment from console
	  Dev env run: --env dev
	  Qa env run: --env prod
	  Forward Staging env run: --env forward-staging

	  Note: default setting: "forward-staging"

  ---------------------------
  	Select Test Suite
	  Available test suites:
 	    ---

  ---------------------------
  	Browser
	  ---

	  Default: chrome

  ---------------------------
  	Run mode
	  ---

  ---------------------------
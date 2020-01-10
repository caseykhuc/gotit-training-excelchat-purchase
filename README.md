# Selenium WebDriver with python3 Practice

### Task:
- Automate asker's process from signing in account, purchasing an unlimited subscription to the successful state.
- Assert with the appearance of purchase-success modal and increase in session balance

### Note:
- Individual & Small business tab
- Config: freq: 30 days - trial: 0 - sessions: 0 (unlimited)

### Flow:
- Sign in to account
- Navigate to Pricing page
- Invoke Payment modal
- Choose Card ending with 1881 or add another Visa Card --> Submit
- Verify the visible session balance is unlimited

## Install

```git clone https://github.com/khuctrang/gotit-training-excelchat-purchase.git``` Clone project

```virtualenv venv --python=python3``` Create the virtual environment for python3

```source venv/bin/activate```

```pip install -e .``` Install the packages required 

## Running Instruction

```behave``` Run the project with development config

```behave -D APP_STATE=staging``` Run the project with staging config


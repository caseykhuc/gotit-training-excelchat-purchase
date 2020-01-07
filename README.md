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
- Verify the success modal visiability
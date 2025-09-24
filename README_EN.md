# Autosignin
This is an auto sign-in script that helps users automatically complete sign-in actions on specified websites.

## English Version
You are already viewing the English instructions.

## Features
- Auto login to specified websites
- Auto sign-in
- Support multiple accounts
- Save cookies to reduce repeated login
- Can be combined with scheduled tasks for automatic sign-in
- Screenshot feature to verify successful sign-in
- Logs to help confirm script execution

## Tutorial

### Installation
Download the source code to install required dependencies or use the packaged exe file.

### Usage

#### Configuration
Deploy the exe file to the desired folder. On first run, a `config.json` file will be generated in the current directory with the following format:

```json
{
    "handle_login": false,
    "auto_sign_all": true
}
```

- The first option specifies whether to manually log in and save cookies (used during the first login for a website). If selected, log in manually and wait for cookies to be automatically saved. Remember to turn this off for subsequent uses.

- The second option specifies whether to enable automatic login. When enabled, the script will automatically read the URLs from the `urls.txt` file and use the cookies in the `cookies` folder to log in and perform automatic sign-in.

#### Auto Sign-in
After configuring the URLs and obtaining the corresponding cookies, you can set up automatic login/sign-in. Combining with Windows Task Scheduler allows convenient scheduled sign-ins:

  - Press `Windows + R` and run `taskschd.msc` to open Task Scheduler
  - Click **Create Task** on the right and enter the task name
  - Select **Triggers**, click **New**, create a trigger, and set the automatic start time
  - Select **Actions**, click **New**, create a new action, set the action to start a program, and choose the exe file
  - Click OK to save the task and right-click to test run it
  - Note: It is recommended to set the task to retry at least 3 times on failure, run only when connected to the internet, and run immediately if a scheduled run is missed

#### Dependencies
##### Browser Automation
selenium

###### ChromeDriver Management
webdriver-manager

> Note: Chrome browser must be installed

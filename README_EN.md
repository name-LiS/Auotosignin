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

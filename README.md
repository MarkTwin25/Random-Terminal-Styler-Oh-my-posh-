# Random Terminal Styler (Oh-my-posh!)

This project dynamically customizes your Bash terminal on every startup. It uses a Python script to randomly select a theme from a themes.txt file (which includes my favorite themes, but you can add your own), and modifies your .bashrc to apply the new style using Oh-My-Posh.

## Requirements

- Python 3.x
- Bash (WSL or Linux)
- Oh My Posh installed with curl

## Install Oh My Posh with curl:

```bash
curl -s https://ohmyposh.dev/install.sh | bash -s
```

## Installation

1. Clone this repository
	```bash
		git clone [repository]
	```
2. Grant execution permissions to the script
	```bash
		chmod +x auto.py
	```
3. (Optional) If you want to try the srcipt, yo can do:
	```bash
		./auto.py
	```
	then, yo must do:
	```bash
		source ~/.bashrc
	```
	This is to recharge the terminal and yo can see your new bash style.

4. If you want it to switch to a new style every time you start a new terminal, you must add this at the end  to your .bashrc file:
	```
	python3 python3 /absolutePath/auto.py
	```
	Where "absolutePath" is the place where auto.py is.

# MySSH

MySSH is a simple program that allows you to connect to a remote server using SSH smoothly.  
You can personalize it and add shortcuts easily.

## Requirements
- Windows (Tested on 10 & 11)  
- Python 3.10 or later (otherwise replace the `match-case`)

## Usage
### Doskey Alias
Create a doskey file and add a shortcut which executes the `myssh.py` script with (e.g.) `myssh`. [See how to setup permanent doskeys here](https://alanrobson.co/how-to-setup-a-permanent-doskeys-macro-file/).

### Shortcuts
Add new shortcuts inside of the `getServer` function.  
Exmaple:
```python
def getServer(resolvable):
	# add shortcuts
    match resolvable:
		case "ex":
			return "example.com" # or IP e.g.
        case _:
            return resolvable
```

## Preview
![Preview](./img/preview.gif)

## Defaults
`Target` has **no default** value and the script exists if no target is specified.  
`Username` defaults to **"root"**  
`Port` defaults to **"22"**  
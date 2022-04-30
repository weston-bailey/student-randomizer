# Student Randomizer

CLI tool to automate randomly calling on students in class

## Usage

`python3 randomizer.py --make`: creates the random list

`python3 randomizer.py --print`: prints list of random students

`python3 randomizer.py --next`: prints the next student and advances the queue

## Aliases

in `zshrc/bashrc`, add these to run the tool from anywhere.

```shell
# select the next random student
alias sr='python3 ~/< path to clone directory from root >/randomizer.py --next'
# reshuffle the randomized students
alias srm='python3 ~/< path to clone directory from root  >/randomizer.py --make'
```

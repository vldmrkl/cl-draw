# cl-draw
<p align="center"><img src="https://github.com/vldmrkl/cl-draw/blob/main/images/cl-draw-cli.png" alt="program sample output" /></p>

## What's cl-draw?
cl-draw is an assistant tool for draws of Champions League (round of 16) style competitions. The creation of this tool was inspired after [UEFA voided the Champions League 21/22 Round of 16 draw because of technical issues](https://www.uefa.com/uefachampionsleague/news/0270-13f2ac0aff13-74f2ff9e43b1-1000--champions-league-round-of-16-draw-declared-void-and-will-be-red/).

## How to use

### Install dependencies
If you don't have pipenv:
```
pip install --user pipenv
```

Install dependencies from Pipfile:
```
pipenv install
```

### Run
`python main.py`

## How this works
### Input
This program expects an input file named 'teams.json', which has the following structure:
```
{
  "seeded": [
    {
      "team": string,
      "group": string,
      "country": string
    },
    ...
  ],
  "unseeded": [
    {
      "team": string,
      "group": string,
      "country": string
    },
    ...
  ]
}
```

### Rules
The program currently follows UEFA's rules for their Champions League Round of 16 draw. This includes:
* Teams from the same country cannot play each other
* Teams from the same group cannot play each other

import indicoio
indicoio.config.api_key = '54c4e2eef50b6e56b29754bc635a5506'

# single example
indicoio.emotion("I did it. I got into Grad School. Not just any program, but a GREAT program. :-)")

# batch example
print(indicoio.emotion([
    "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
    "Like seriously my life is bleak, I have been unemployed for almost a year."
]))
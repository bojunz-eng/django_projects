import csv  # https://docs.python.org/3/library/csv.html

import datetime
from django.utils import timezone

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        # Replace these comments to

        # Make a new Question and save it
        q = Question(question_text=row[0], pub_date=timezone.now())
        q.save()

        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it
        for c in row[1:]:
            ch = Choice(choice_text=c, votes=0, question=q)
            ch.save()
            
        # Read and review the code for creating and saving Question objects
        # in Tutorial 2

    print("=== Load Complete")
    
    
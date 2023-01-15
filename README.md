# Solution to the assignment

## Firstly, project specific information

This project is using flask + psql and in order to save a lot of extra hassle is dockerized.

Thus, start by:

```
docker-compose up --build
```

Then in order to initialize db run:

```
docker exec wolt_backend python3 -m flask migrate
```

And that shall be it. The application should be now up and running.

If you want to run tests then execute:

```
docker exec wolt_backend python3 -m pytest
```

## Questions from assignment

### Part 1

1. Previously I have had 2 job experiences. During the first one I was very afraid of asking the questions trying to find my way out even, if it was evident that I need some guidence. As a result, I have spent absurd amount of time getting to know the project, solving tasks, etc. On my second position, I wanted to fix all the wrongs and right away I started asking stuff that was not known to me about the project and the way it supposed to work as soon as possible. This has given me a possibility to understand better what supposed to be happening both at and behind the scenes. At the potential new position, I would most certainly choose the second approach of asking the questions, whilst at the same time trying to utilize my technical knowledge to actually get stuff done. Secondly, there are certain things used within the tech stack that I am not 100% familiar with, for instance Flask. Whilst, basic understanding is present - getting to know the framework specifics will take time. Yet again, if potentially I am the suitable candidate - there is still a notice period that can be used as a learning gap. In a free time I would search for relevant resources to help me out starting out with flask. In addition to that, I am always open to the suggestions of type 'what to read'.

2. I believe there is no need for the third party solution in this case as the functionality is somewhat basic and can be implemented from scratch. If I would have chosen a tech stack to build it, I would use django + django rest framework (DRF). Following choice would be made due to multiple reasons. Firstly, DRF + Django is a highly scalable solution as it provides plenty of built in tools to simplify the life of the developer. Sufficient amount of commands provide a handy boiler-plate code that can be used right away (unlike in flask) + it handles quite well database management with premade cli commands that detect migrations, preform them as well as roll them back. Project structure itself is clear as well:

```
.
    ├── ...
    ├── certain app name        # encapsulates certain functionality, let's say user creation
    │   ├── views.py            # Contains business logic
    │   ├── urls.py             # Connects view to url
    │   └── tests               # For the app
    |   └── models.py           # Define relational tables as a Classes (Django's version of SQLAlchemy)
    |   └── ...                 # Rest of functionality will go here, such as utils, validators, signals, etc...
    └── ...
```

Lastly, DRF + Django is a very secure combination. It provides configuration for base permission classes, base hashing for user models and safe SQL queries as it uses ORM.

Notes: I might not know Flask well enough and it might be that some of the solutions mentioned above are also well implemented within it.

3. In growing companies planning is a very important step. Trying to know as much as possible ahead is a difficult task, although if done correctly is a crucial bonus to the development process. In order to make planning easier, goals should be clear - and this should be achieved via careful and thorough communication. After that - changes to design/ solution and implemetation can be done in accordance with the decisions followed from the steps above. Generally, I would say that plenty of solutions should be done natively without the help of 3rd parties, on the other hand, if the time constrains are limited and solution is too complex, proper research should be done on what cloud vendor should be use.

### Part 2

The choice of the technology was Flask, both as a front- and backend as well as psql + psycopg2 as database solution. Logically, the choice was made out of 2 main reasonings:

1. The application is extremely simple, thus there is no need for more complicated frameworks.

2. Secondly, it is the main stack of the automation team that I am not fluent with and I have decided that this simple task is a perfect place and time to practice.

If however, something more complicated would have been requested, I would probably switch out the frontend to be React (in case more complex UI is needed + SPA are proven to be efficient) and kept Flask as API only as it is quite an efficient solution.

Choice of the PSQL was based on the fact relational databases are efficient, well-scalable, has robust set of features, can be integrated into other projects/ services, etc. It is generally speaking a time-proven solution that seems not to go anywhere any time soon.

Unit tests for webhook. This is somewhat interesting one. Not very familiar with the slack webhooks, but I would imagine in case there is a test-channel with test-webhook connected to it - then tests technically could not have been mocked, but it regardless feels incorrect. Thus, couple of rounds of manual testing, seeing how webhook works and implementing mock tests accordingly, seems like a better approach.

### Part 3

I am left with a feeling that some of the questions are not opened to the extent that is needed and part 1.3 question is not understood completely. Hopefully, I will get the chance to discuss it on Tuesday :)

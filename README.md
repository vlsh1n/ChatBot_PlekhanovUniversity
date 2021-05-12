# ChatBot_PlekhanovUniversity

<h3> Telegram Bot for student school of Plekhanov Russian University of Economics </h3>


<i>Start file for this bot is 'app.py' at the root directory of project</i>

<b>
Logic of project:
</b>

Data --> config.py --> There we create env object and take secure data from .env file

Handlers --> errors --> error_handler.py --> There we catch errors and return answers for these errors

Handlers --> users --> All handlers of this project. There we catch commands and messages from private chat with users
and return prepared answer

Keyboards --> All default and inline keyboards

Middlewares --> throttling.py --> Logic for prevent flooding

Static --> Directory with static files for answers

Utils --> Logic for logging, throttling and function to notification admins about starting the bot

app.py --> There we run notification function and run the bot

loader.py --> There we create bot object, choose method for storage data and create dispatcher who
can polling messages and commands from users
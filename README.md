# KaratekaInfoBDWeb
 A web application to enter and view information of Karate athletes of Bangladesh.

How to get CSV files of models:
uri/get_<models>_csv/secret

models = {athletes, clubs, teams, championships, championshipstandings}
secret should be defined in .env file which should be in the root directory (same as manage.py).
secret should be defined as follows: CSV_SECRET = your_secret_key
The views are protected to redirect to the homepage if secret does not match CSV_SECRET from .env.

How to run the scripts:
python manage.py runscript script_name
(script_name should be without .py extension)

Order of running the scripts:
club_load, team_load, athlete_load, championship_load, championshipstanding_load
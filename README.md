# waste_master
Waste Master

## Setup

### Requirements:

- Python 2.7
- virtualenv

### Procedure

- In terminal type `https://github.com/oleaha/waste_master.git` to clone the project
- Create virtualenv: `virtualenv env`
- Activate virtualenv: `source env/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Migrate database: `python manage.py migrate`
- Start project: `python manage.py runserver`

## Server
Project is hosted on heroku, deploy using `git push heroku master`

Link: http://waste-master.herokuapp.com

## API

**POST:**

Send post request to: http://waste-master.herokuapp.com/api/readings/ with Container ID and measurement value
`[{"container":1,"value":123}]`

**LIST:**

Visit http://waste-master.herokuapp.com/api/readings/ to see all listings. Visit http://waste-master.herokuapp.com/api/readings/<container-id> to see all listings for one container


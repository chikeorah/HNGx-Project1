from flask import Flask
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timezone

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class ProjectX(Resource):
  def get(self):
    parser.add_argument("slack_name", location='args')
    parser.add_argument("track", location='args')
    args = parser.parse_args()
    
    projectData = {
        "slack_name": args["slack_name"],
        "current_day": datetime.now().strftime("%A"),
        "utc_time": datetime.now().strftime("%Y-%m-%dT%XZ"),
        "track": args["track"],
        "github_file_url": "https://github.com/chikeorah/HNGx-Project1/blob/main/api.py",
        "github_repo_url": "https://github.com/chikeorah/HNGx-Project1",
        "status_code": 200
        }
    
    return projectData

api.add_resource(ProjectX, '/api/')

if __name__ == "__main__":
  app.run(debug=True)
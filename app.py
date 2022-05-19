from flask import Flask
import linecache
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/",defaults={'file':'file1.txt'})
@app.route("/<string:file>/")
def hello_world(file='file1.txt'):
    if request.method == "GET":
        content = []

        try:
            start = 1 if request.args.get('start') is None else int(request.args.get('start') )
            end = num_lines = sum(1 for line in open(f"resources/{file}.txt",'r',encoding='unicode_escape'))  if request.args.get('end') is None else int(request.args.get('end') )
            for i in range(start,end+1):
                line = linecache.getline(f"resources/{file}.txt", i)
                content.append(line)
                line = None

        except Exception as e:
            content.append(e)
            
        return render_template('base.html',lines = content)



if __name__=="__main__":
    app.run(debug=True)
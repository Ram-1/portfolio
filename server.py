from flask import Flask, render_template,url_for,request,redirect
import csv
app = Flask(__name__,template_folder='template')
print(__name__)

@app.route("/")
def myhome():
  return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name): 
  return render_template(page_name)


def write_to_file(data):
  with open('database.txt','a') as database:
    email=data['email']
    subject=data['subject']
    message=data['message']
    file_write = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
  with open('eggs.csv', 'a',newline='') as csvfile:
    email=data['email']
    subject=data['subject']
    message=data['message']
    csv_writer= csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method=='POST':
    try:
      data=request.form.to_dict()
      write_to_csv(data)
      return redirect('thankyou.html')
    except:
      return 'did not save to database'
  else:
    return 'something went wrong plz try again'

# if __name__ == "__main__":
#   app.run()


# powershell
#     1. activate : venv/scripts/activate.ps1
#     2. run : $env:FLASK_APP = "server.py"
#     3. debuge on: $env:FLASK_ENV = "development"
#     4. when flask module is not found then select python below left-
#         python 3.7.6 (64-bit:conda)
# CMD
#        set FLASK_ENV=development


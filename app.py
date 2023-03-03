from flask import Flask,render_template

app=Flask(__name__)


jobs_list = [{
  'id':1,
  'title':'data sci',
  'location':'delhi',
  'salary':'10,00,000'
}
,{
  'id':2,
  'title':'frontend engineer',
  'location':'pune',
  'salary':'11,00,000'
}
,{
  'id':3,
  'title':'backend engineer',
  'location':'banglore',
  # 'salary':'15,00,000'
},
{
  'id':4,
  'title':'data analyst',
  'location':'Mumbai',
  'salary':'12,00,000'
}
      
      ]


@app.route("/")

def hello_world():
  return render_template('home.html',jobs=jobs_list)



if __name__=='__main__':
  app.run(host='0.0.0.0',debug= True)

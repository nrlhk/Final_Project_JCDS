from flask import Flask, jsonify, request, render_template, url_for, send_from_directory, abort
import requests, json, mysql.connector
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import json, requests
import os, random
import numpy as np

app = Flask(__name__)
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Nurul',
    passwd = '8989',
    database = 'jcds_project'
)
x = mydb.cursor()
x.execute('select * from users')
datauser = x.fetchall()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    df = pd.read_csv('data.csv')
    df = df.dropna()
    dfdummy1 = pd.get_dummies(df['age'])
    dfdummy2 = pd.get_dummies(df['gender'])
    df = pd.concat([dfdummy1, dfdummy2, df], axis = 1)
    df2 = df[['30-34', '35-39', '40-44', '45-49', 'F', 'M', 'approved_conversion']]

    #35-39
    a = df2[df2['30-34'] == 1]
    aF = a[a['F'] == 1]
    aF0 = aF[aF['approved_conversion'] == 0]
    aF0group = aF0['approved_conversion'].count()
    aF_up = aF[aF['approved_conversion'] != 0]
    aF_upgroup = aF_up['approved_conversion'].sum()

    aM = a[a['M'] == 1]
    aM0 = aM[aM['approved_conversion'] == 0]
    aM0group = aF0['approved_conversion'].count()
    aM_up = aM[aM['approved_conversion'] != 0]
    aM_upgroup = aM_up['approved_conversion'].sum()

    #35-39
    b = df2[df2['35-39'] == 1]
    bF = b[b['F'] == 1]
    bF0 = bF[bF['approved_conversion'] == 0]
    bF0group = bF0['approved_conversion'].count()
    bF_up = bF[bF['approved_conversion'] != 0]
    bF_upgroup = bF_up['approved_conversion'].sum()

    bM = b[b['M'] == 1]
    bM0 = bM[bM['approved_conversion'] == 0]
    bM0group = bF0['approved_conversion'].count()
    bM_up = bM[bM['approved_conversion'] != 0]
    bM_upgroup = bM_up['approved_conversion'].sum()

    # 40-44
    c = df2[df2['40-44'] == 1]
    cF = c[c['F'] == 1]
    cF0 = cF[cF['approved_conversion'] == 0]
    cF0group = cF0['approved_conversion'].count()
    cF_up = cF[cF['approved_conversion'] != 0]
    cF_upgroup = cF_up['approved_conversion'].sum()

    cM = c[c['M'] == 1]
    cM0 = cM[cM['approved_conversion'] == 0]
    cM0group = cF0['approved_conversion'].count()
    cM_up = cM[cM['approved_conversion'] != 0]
    cM_upgroup = cM_up['approved_conversion'].sum()

    # 45-49
    d = df2[df2['45-49'] == 1]
    dF = d[d['F'] == 1]
    dF0 = dF[dF['approved_conversion'] == 0]
    dF0group = dF0['approved_conversion'].count()
    dF_up = dF[dF['approved_conversion'] != 0]
    dF_upgroup = dF_up['approved_conversion'].sum()

    dM = d[d['M'] == 1]
    dM0 = dM[dM['approved_conversion'] == 0]
    dM0group = dF0['approved_conversion'].count()
    dM_up = dM[dM['approved_conversion'] != 0]
    dM_upgroup = dM_up['approved_conversion'].sum()

    plt.style.use('ggplot')
    plt.figure(figsize=(20,10))

    plt.subplot(311)
    plt.bar('30 F 0', aF0group, color='#f6a6b2')
    plt.bar('30 F 1up', aF_upgroup, color='#f6a6b2')
    plt.bar('30 M 0', aM0group, color='#99d3f0')
    plt.bar('30 M 1up', aM_upgroup, color='#99d3f0')

    plt.bar('35 F 0', bF0group, color='#f6a6b2')
    plt.bar('35 F 1up', bF_upgroup, color='#f6a6b2')
    plt.bar('35 M 0', bM0group, color='#99d3f0')
    plt.bar('35 M 1up', bM_upgroup, color='#99d3f0')

    plt.bar('40 F 0', cF0group, color='#f6a6b2')
    plt.bar('40 F 1up', cF_upgroup, color='#f6a6b2')
    plt.bar('40 M 0', cM0group, color='#99d3f0')
    plt.bar('40 M 1up', cM_upgroup, color='#99d3f0')

    plt.bar('45 F 0', dF0group, color='#f6a6b2')
    plt.bar('45 F 1up', dF_upgroup, color='#f6a6b2')
    plt.bar('45 M 0', dM0group, color='#99d3f0')
    plt.bar('45 M 1up', dM_upgroup, color='#99d3f0')

    plt.title('Approved Conversion by Age and Gender')
    plt.xlabel('Categories')
    plt.ylabel('Total Number')

    plt.subplot(312)
    df3 = df[['interest1', 'interest2', 'interest3', 'approved_conversion']]
    df31up = df3[df3['approved_conversion'] != 0]
    df31upgroup = df31up.groupby('interest1').sum()
    plt.bar(df31upgroup.index, df31upgroup['approved_conversion'], color='#00c2c7' )
    plt.title('>=1 Conversion by 1st Interest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 1')
    plt.ylabel('Total Number')

    plt.subplot(313)
    df30 = df3[df3['approved_conversion'] == 0]
    df30group = df30.groupby('interest1').count()
    plt.bar(df30group.index, df30group['approved_conversion'], color='#00c2c7' )
    plt.title('0 Conversion by 1st Interest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 1')
    plt.ylabel('Total Number')

    plt.subplots_adjust(
    left=0.06, bottom=0.06, right=0.98, top=0.95,
    wspace=.2, hspace=.5
    )

    address = './storage/grafikconversion1.png'
    urlgrafik ='http://localhost:5000/grafik/grafikconversion1.png'
    plt.savefig(address)
    grafik = urlgrafik

    # Grafik2
    plt.style.use('ggplot')
    plt.figure(figsize=(20,10))
    plt.subplot(411)
    df31upgroup2 = df31up.groupby('interest2').sum()
    plt.bar(df31upgroup2.index, df31upgroup2['approved_conversion'], color='#99d3f0')
    plt.title('>=1 Conversion by 2nd Interest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 2')
    plt.ylabel('Total Number')

    plt.subplot(412)
    df30group2 = df30.groupby('interest2').count()
    plt.bar(df30group2.index, df30group2['approved_conversion'], color='#99d3f0')
    plt.title('0 Conversion by 2ndInterest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 2')
    plt.ylabel('Total Number')

    plt.subplot(413)
    df31upgroup3 = df31up.groupby('interest3').sum()
    plt.bar(df31upgroup3.index, df31upgroup3['approved_conversion'], color='#f6a6b2')
    plt.title('>=1 Conversion by 3rd Interest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 3')
    plt.ylabel('Total Number')

    plt.subplot(414)
    df30group3 = df30.groupby('interest3').count()
    plt.bar(df30group3.index, df30group3['approved_conversion'], color='#f6a6b2')
    plt.title('0 Conversion by 3rd Interest')
    plt.xticks(np.arange(0,66,step=2))
    plt.yticks(np.arange(0,105,step=20))
    plt.xlabel('Interest 3')
    plt.ylabel('Total Number')

    plt.subplots_adjust(
    left=0.06, bottom=0.06, right=0.978, top=0.96,
    wspace=.2, hspace=.90
    )

    address11 = './storage/grafikconversion2.png'
    urlgrafik11 ='http://localhost:5000/grafik/grafikconversion2.png'
    plt.savefig(address11)
    grafik11 = urlgrafik11

    # grafik 3
    df2 = pd.read_csv('german_credit_data.csv')
    dfrisk0 = df2[df2['Risk'] == 'bad']
    dfrisk1 = df2[df2['Risk'] == 'good']

    a1 = dfrisk0.groupby('Age').count()
    a2 = dfrisk1.groupby('Age').count()
    b1 = dfrisk0.groupby('Sex').count()
    b2 = dfrisk1.groupby('Sex').count()

    c1 = dfrisk0.groupby('Job').count()
    c2 = dfrisk1.groupby('Job').count()
    d1 = dfrisk0.groupby('Housing').count()
    d2 = dfrisk1.groupby('Housing').count()
    e1 = dfrisk0.groupby('Credit amount').count()
    e2 = dfrisk1.groupby('Credit amount').count()
    f1 = dfrisk0.groupby('Duration').count()
    f2 = dfrisk1.groupby('Duration').count()
    g1 = dfrisk0.groupby('Purpose').count()
    g2 = dfrisk1.groupby('Purpose').count()

    plt.figure(figsize=(15,7))
    plt.style.use('ggplot')
    plt.suptitle('Credit Risk by Client Profile', size='xx-large')
    plt.subplot(241)
    plt.title('Bad Credit Risk(age)', size='medium')
    plt.bar(a1.index, a1['Risk'], color ='#1475e1', width=.6)
    plt.yticks(np.arange(0,45,step=5))
    plt.xticks(np.arange(20,75,step=10))
    plt.subplot(242)
    plt.title('Good Credit Risk(age)', size='medium')
    plt.bar(a2.index, a2['Risk'], color ='#89baf0', width=.6)
    plt.yticks(np.arange(0,45,step=5))
    plt.xticks(np.arange(20,75,step=10))

    plt.subplot(243)
    plt.title('Bad Credit Risk', size='medium')
    plt.bar(b1.index.values[0], b1.iloc[0]['Risk'], color='#f6a6b2', width=.6)
    plt.bar(b1.index.values[1], b1.iloc[1]['Risk'], color='#99d3f0', width=.6)
    plt.yticks(np.arange(0,550,step=100))
    plt.subplot(244)
    plt.title('Good Credit Risk', size='medium')
    plt.bar(b2.index.values[0], b2.iloc[0]['Risk'], color='#f6a6b2', width=.6)
    plt.bar(b2.index.values[1], b2.iloc[1]['Risk'], color='#99d3f0', width=.6)
    plt.yticks(np.arange(0,550,step=100))

    plt.subplot(245)
    plt.title('Bad Credit Risk(Job)', size='medium')
    plt.bar(c1.index, c1['Risk'], color='#14dce1')
    plt.yticks(np.arange(0,500,step=50))
    plt.xticks(np.arange(0,4,step=1))
    plt.subplot(246)
    plt.title('Good Credit Risk(Job)', size='medium')
    plt.bar(c2.index, c2['Risk'], color='#89edf0')
    plt.yticks(np.arange(0,500,step=50))
    plt.xticks(np.arange(0,4,step=1))

    plt.subplot(247)
    plt.title('Bad Credit Risk(Housing)', size='medium')
    plt.bar(d1.index, d1['Risk'], color='#1475e1')
    plt.yticks(np.arange(0,600,step=50))
    plt.subplot(248)
    plt.title('Good Credit Risk(Housing)', size='medium')
    plt.bar(d2.index, d2['Risk'], color='#89baf0')
    plt.yticks(np.arange(0,600,step=50))

    plt.subplots_adjust(
    left=0.05, bottom=0.07, right=0.98, top=0.90,
    wspace=.25, hspace=.31
    )

    address2 = './storage/grafikcreditrisk.png'
    urlgrafik2 ='http://localhost:5000/grafik/grafikcreditrisk.png'
    plt.savefig(address2)
    grafik2 = urlgrafik2

    newgrafik = {
        'grafik': grafik,
        'grafik11': grafik11,
        'grafik2': grafik2,
    }

    deptid = int(request.form['department'])
    password = int(request.form['password'])

    # Using db in MySQL
    if deptid == 1 and password == datauser[deptid-1][2]:
        return render_template('form.html', data=newgrafik)
    elif deptid == 2 and password == datauser[deptid-1][2]:
        return render_template('ca.html', data=newgrafik)
    else:
        return render_template('2ndlogin.html')

    # Using json file *user.json
    # import json
    # with open('user.json') as datauser:
    #     datauser = json.load(datauser)

    # if deptid == 1 and password == datauser[deptid-1]['pwd']:
    #     return render_template('form.html', data=newgrafik)
    # elif deptid == 2 and password == datauser[deptid-1]['pwd']:
    #     return render_template('ca.html', data=newgrafik)
    # else:
    #     return render_template('2ndlogin.html')


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    age = request.form['age']
    gender = int(request.form['gender'])
    interest1 = int(request.form['interest1'])
    interest2 = int(request.form['interest2'])
    interest3 = int(request.form['interest3'])

    if age == 0:
        age1 = 1
        age2 = 0
        age3 = 0
        age4 = 0
    elif age == 1:
        age1 = 0
        age2 = 1
        age3 = 0
        age4 = 0
    elif age == 2:
        age1 = 0
        age2 = 0
        age3 = 1
        age4 = 0
    else:
        age1 = 0
        age2 = 0
        age3 = 0
        age4 = 1
    
    if gender == 0:
        gender1 = 1
        gender2 = 0
    else:
        gender1 = 0
        gender2 = 1
    
    pred = modeltree.predict([[
        age1, age2, age3, age4, gender1, gender2, 
        interest1, interest2, interest3
        ]])[0]

    if pred == 0:
        pred = 'This audience will not give you conversion/ become active user'
    else:
        pred = 'Cool! she/he is GREAT audience, targetting your campaign for this audience to get active user'

    newdata = {
        'age1': age1,
        'age2': age2,
        'age3': age3,
        'age4': age4,
        'gender1': gender1,
        'gender2': gender2,
        'interest1': interest1,
        'interest2': interest2,
        'interest3': interest3,
        'pred': pred,
    }
    return render_template('hasil.html', data=newdata)

@app.route('/predictCA', methods = ['POST', 'GET'])
def predictCA():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    job = int(request.form['job'])
    housing = int(request.form['housing'])
    creditamount = int(request.form['creditamount'])
    duration = int(request.form['duration'])
    purpose = int(request.form['purpose'])

    pred2 = modellogres.predict([[
        age, sex, job, housing, creditamount, duration, purpose
        ]])[0]
        
    if pred2 == 0:
        pred2 = 'He/ She has BAD Credit RISK'
    else:
        pred2 = 'He/ She has Good Credit RISK, You can approve the application!'
    
    # proba = modellogres.predict_proba([[
    #     age, sex, job, housing, creditamount, duration, purpose
    #     ]])
    # probamax = round(proba[0].max() * 100)

    newdata2 = {
        'age': age,
        'sex': sex,
        'job': job,
        'housing': housing,
        'creditamount': creditamount,
        'duration': duration,
        'purpose': purpose,
        'pred': pred2,
        # 'proba': probamax,
    }
    return render_template('hasilCA.html', data=newdata2)

@app.route('/grafik/<path:x>')
def graph(x):
    return send_from_directory('storage', x)

if __name__ == '__main__':
    modeltree = joblib.load('treemodelforconversion')
    modellogres = joblib.load('logRegGermancredit')
    app.run(debug=True)

# Final_Project_JCDS
Predict facebook audience profile to improve campaign effectiveness and predict client credit risk


Bakground:
Facebook Ad Campaign
•	> 53.6 % marketing campaign tidak menghasilkan approved conversion /active users
•	Biaya yang lebih besar untuk membayar campaign melalui facebook karena target audience terlalu besar (kurang tepat sasaran)
•	Dataset: https://www.kaggle.com/madislemsalu/facebook-ad-campaign

Credit Scoring Prediction for Credit Analyst team
•	Proses manual yang lebih lama dalam menganalisa client risk yang mengajukan kredit 
•	Dataset: https://www.kaggle.com/uciml/german-credit


Solution: Web based Dashboard for Marketing and Credit Analyst team

Marketing Team
•	Report hasil approved conversion dari facebook campaign sebelumnya
•	Prediksi audience facebook seperti apa yang akan signup, install, dan menjadi active user sehingga untuk campaign difacebook selanjutnya bisa menggunakan target tersebut/ target lebih tepat sasaran

Credit Analyst Team
•	Report hasil profile client risk sebelumnya
•	Prediksi apakah client memiliki resiko kredit bad atau good

Dataset Facebook Ad Campaign
•	1143 data, 15 atribut ('ad_id‘, 'reporting_start‘, 'reporting_end‘, 'campaign_id‘, 'fb_campaign_id‘, 'age‘, 'gender‘, 'interest1‘, 'interest2‘, 'interest3‘, 'impressions‘, 'clicks‘, 'spent‘, 'total_conversion‘, 'approved_conversion‘)
•	382 null on target/ approved_conversion
•	Drop null target
•	Use 761 data, 6 atribut ('age‘, 'gender‘, 'interest1‘, 'interest2‘, 'interest3‘, 'approved_conversion‘)
•	Age: 30-34, 35-39, 40-44, 45-49
•	Gender: Female, Male
•	Interest 1/2/3 : 2- 120
•	Approved_conversion: (0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 12, 14, 17, 21,)

Model:
•	Classification
•	Decision Tree
•	90% train, 10% test
•	Score train around 94%

German Credit Dataset
•	1000 data, 11 atribut ('Unnamed: 0‘, 'Age‘, 'Sex‘, 'Job‘, 'Housing‘, 'Saving accounts‘, 'Checking account‘, 'Credit amount‘, 'Duration‘, 'Purpose‘, 'Risk‘,)
•	Null data  on Saving account 183, and Checking account 394: (text - little, moderate, quite rich, rich)
•	Measure 8 atribut, drop saving account and checking account
•	Age (numeric), Sex (text: male, female)
•	Job (numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled)
•	Housing (text: own, rent, or free)
•	Credit amount (numeric, in DM)
•	Duration (numeric, in month)
•	Purpose (text: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others)
•	Risk (text: bad, good)

Model:
•	Classification
•	Logistic Regression
•	90% train, 10% test
•	Scored train 70-71%

Tampilan:
1. Department selection and input password
![Image1](https://user-images.githubusercontent.com/49969892/61648420-99385f80-acd9-11e9-83e0-1341b1db46f0.jpg)
2. Use Marketing and Sales Department to view the report and input prediction
![Image2](https://user-images.githubusercontent.com/49969892/61648423-9b022300-acd9-11e9-95f8-2be782d94a0c.jpg)
3. Result after input prediction
![Image3](https://user-images.githubusercontent.com/49969892/61648424-9c335000-acd9-11e9-991b-2ff92ea3bf44.jpg)
4. Use Credit analyst department to view report and input selection
![Image4](https://user-images.githubusercontent.com/49969892/61648428-9dfd1380-acd9-11e9-9b9c-81a193356912.jpg)
5. Result after input prediction
![Image5](https://user-images.githubusercontent.com/49969892/61648431-9f2e4080-acd9-11e9-8982-9f74e66e9b9d.jpg)






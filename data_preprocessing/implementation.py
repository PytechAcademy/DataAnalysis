import pandas as pd
import datetime
# Load data
df = pd.read_csv('Car details v3.csv')
### Generate EDA report
#from ydata_profiling import ProfileReport
#report = ProfileReport(df)
#report.to_file("EDA.html")
### Remove duplicates
df = df.drop_duplicates(subset=None,keep="first",inplace=False)
print(df.info())
### converting datatype from str to numeric
df["engine"] = df["engine"].str.extract('([^\s]+)').astype("float")
df["mileage"] = df["mileage"].str.extract('([^\s]+)').astype("float")
df["max_power"] = df["max_power"].str.extract('([^\s]+)')
df["max_power"] = df["max_power"][~(df["max_power"] == "bhp")]
df["max_power"] = df["max_power"].astype("float")
#create 'car_age' feature from 'year' column
df["car_age"] = (datetime.datetime.now().year) - (df["year"])
### missing value treatment
## check whether there are null values in the dataset
print(df.isnull().sum())
mean_engine = df['engine'].mean()
df['engine'] = df['engine'].fillna(mean_engine)
mean_mileage = df['mileage'].mean()
df['mileage'] = df['mileage'].replace(0,mean_mileage)
mean_max_power = df['max_power'].astype('float').mean()
df['max_power'] = df['max_power'].replace(0,mean_max_power)
##replace missing values in each categorical column with the most frequent value
#df["seats"] = df["seats"].fillna(df["seats"].value_counts().index[0], inplace = True)
### Outlier treatment -kms driven
Max = df["km_driven"].max()
Min = df["km_driven"].min()
Q1 = df["km_driven"].quantile(0.25)
Q3 = df["km_driven"].quantile(0.75)
IQR = Q3 - Q1
St_max = Q3 + (1.5*IQR)
St_min = Q1 - (1.5*IQR)
print(f"Q1:{Q1},Q3:{Q3},IQR:{IQR},St_max:{St_max},St_min:{St_min},Max:{Max},Min:{Min}")
# treating categorical variables using one hot encoding
df =pd.get_dummies(df,columns=['fuel','seller_type','transmission','owner'],\
                 prefix=['fuel','seller_type','transmission','owner'],drop_first=True)
print(df.info())
# divide dependent and independent variables
y = df["selling_price"]
X=df.drop(columns=['name'],axis=1)
# applying minimax scalar
from sklearn.preprocessing import MinMaxScaler
scalar=MinMaxScaler()
X=scalar.fit_transform(X)

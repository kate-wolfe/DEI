import pandas as pd
import datetime
import pytz
import numpy as np

df = pd.read_csv('/Users/Kate/Desktop/Diversity Audit/finalItem.csv', usecols=['creation_date_gmt', 'location_code', 'price', 'checkout_total', 'material_type_name', 'Buddhism', 'Hinduism', 'Agnosticism & Atheism', 'Islam', 'Class', 'South Asian', 'East Asian & Pacific Islander', 'Abuse & Violence', 'Disabilities & Neurodiversity', 'Mental & Emotional Health', 'Substance Abuse & Addiction', 'LGBTQIA+ & Gender Studies', 'Indigenous', 'Arab & Middle Eastern', 'Hispanic & Latino', 'Equity & Social Issues', 'Black', 'Judaism', 'Multicultural', 'Christianity', 'Diversity', 'bib_record_num', 'Genre', 'Audience'], dtype={'creation_date_gmt':str, 'location_code':str, 'price':float, 'checkout_total':int, 'material_type_name':str, 'Buddhism':int, 'Hinduism':int, 'Agnosticism & Atheism':int, 'Islam':int, 'Class':int, 'South Asian':int, 'East Asian & Pacific Islander':int, 'Abuse & Violence':int, 'Disabilities & Neurodiversity':int, 'Mental & Emotional Health':int, 'Substance Abuse & Addiction':int, 'LGBTQIA+ & Gender Studies':int, 'Indigenous':int, 'Arab & Middle Eastern':int, 'Hispanic & Latino':int, 'Equity & Social Issues':int, 'Black':int, 'Judaism':int, 'Multicultural':int, 'Christianity':int, 'Diversity':str, 'bib_record_num':int, 'Genre':str, 'Audience':str})

divList = ['Buddhism', 'Hinduism', 'Agnosticism & Atheism', 'Islam', 'Class', 'South Asian', 'East Asian & Pacific Islander', 'Abuse & Violence', 'Disabilities & Neurodiversity', 'Mental & Emotional Health', 'Substance Abuse & Addiction', 'LGBTQIA+ & Gender Studies', 'Indigenous', 'Arab & Middle Eastern', 'Hispanic & Latino', 'Equity & Social Issues', 'Black', 'Judaism', 'Multicultural', 'Christianity']

df['Location'] = ['Main' if x[2] == 'm' else 'Outreach' if x[2] == '3' else 'Boudreau' if x[2] == '4' else 'CSQ' if x[2] == '5' else 'Collins' if x[2] == '6' else "O'Connell" if x[2] == '7' else "O'Neill" if x[2] == '8' else 'Valente' if x[2] == '9' else 'Other' for x in df['location_code']]

df['creation_date_gmt'] = pd.to_datetime(df['creation_date_gmt'])
today = datetime.datetime.now(tz=pytz.utc)
df['Age'] = [(today - x).days for x in df['creation_date_gmt']]

dfBud = df.loc[(df['Buddhism'] > 0) & (df['price'] > 0)]
dfBudAvg = dfBud.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfBudAvg['Category'] = 'Buddhism' 

dfHin = df.loc[(df['Hinduism'] > 0) & (df['price'] > 0)]
dfHinAvg = dfHin.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfHinAvg['Category'] = 'Hinduism'

dfAth = df.loc[(df['Agnosticism & Atheism'] > 0) & (df['price'] > 0)]
dfAthAvg = dfAth.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfAthAvg['Category'] = 'Agnosticism & Atheism'

dfIsl = df.loc[(df['Islam'] > 0) & (df['price'] > 0)]
dfIslAvg = dfIsl.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfIslAvg['Category'] = 'Islam'

dfCla = df.loc[(df['Class'] > 0) & (df['price'] > 0)]
dfClaAvg = dfCla.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfClaAvg['Category'] = 'Class'

dfSA = df.loc[(df['South Asian'] > 0) & (df['price'] > 0)]
dfSAAvg = dfSA.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfSAAvg['Category'] = 'South Asian'

dfEA = df.loc[(df['East Asian & Pacific Islander'] > 0) & (df['price'] > 0)]
dfEAAvg = dfEA.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfEAAvg['Category'] = 'East Asian & Pacific Islander'

dfAbu = df.loc[(df['Abuse & Violence'] > 0) & (df['price'] > 0)]
dfAbuAvg = dfAbu.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfAbuAvg['Category'] = 'Abuse & Violence'

dfDis = df.loc[(df['Disabilities & Neurodiversity'] > 0) & (df['price'] > 0)]
dfDisAvg = dfDis.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfDisAvg['Category'] = 'Disabilities & Neurodiversity'

dfMen = df.loc[(df['Mental & Emotional Health'] > 0) & (df['price'] > 0)]
dfMenAvg = dfMen.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfMenAvg['Category'] = 'Mental & Emotional Health'

dfSub = df.loc[(df['Substance Abuse & Addiction'] > 0) & (df['price'] > 0)]
dfSubAvg = dfSub.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfSubAvg['Category'] = 'Substance Abuse & Addiction'

dfLGBT = df.loc[(df['LGBTQIA+ & Gender Studies'] > 0) & (df['price'] > 0)]
dfLGBTAvg = dfLGBT.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfLGBTAvg['Category'] = 'LGBTQIA+ & Gender Studies'

dfInd = df.loc[(df['Indigenous'] > 0) & (df['price'] > 0)]
dfIndAvg = dfInd.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfIndAvg['Category'] = 'Indigenous'

dfArab = df.loc[(df['Arab & Middle Eastern'] > 0) & (df['price'] > 0)]
dfArabAvg = dfArab.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfArabAvg['Category'] = 'Arab & Middle Eastern'

dfHis = df.loc[(df['Hispanic & Latino'] > 0) & (df['price'] > 0)]
dfHisAvg = dfHis.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfHisAvg['Category'] = 'Hispanic & Latino'

dfEqu = df.loc[(df['Equity & Social Issues'] > 0) & (df['price'] > 0)]
dfEquAvg = dfEqu.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfEquAvg['Category'] = 'Equity & Social Issues'

dfBla = df.loc[(df['Black'] > 0) & (df['price'] > 0)]
dfBlaAvg = dfBla.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfBlaAvg['Category'] = 'Black'

dfJud = df.loc[(df['Judaism'] > 0) & (df['price'] > 0)]
dfJudAvg = dfJud.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfJudAvg['Category'] = 'Judaism'

dfMul = df.loc[(df['Multicultural'] > 0) & (df['price'] > 0)]
dfMulAvg = dfMul.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfMulAvg['Category'] = 'Multicultural'

dfChr = df.loc[(df['Christianity'] > 0) & (df['price'] > 0)]
dfChrAvg = dfChr.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfChrAvg['Category'] = 'Christianity'

dfDiv = df.loc[(df['Diversity'] == 'Diverse') & (df['price'] > 0)]
dfDivAvg = dfDiv.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfDivAvg['Category'] = 'Diverse'

dfND = df.loc[(df['Diversity'] == 'Not Diverse') & (df['price'] > 0)]
dfNDAvg = dfND.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])['price', 'checkout_total', 'Age'].mean().reset_index()
dfNDAvg['Category'] = 'Not Diverse'

frames = [dfDivAvg, dfNDAvg, dfBudAvg, dfHinAvg, dfAth, dfIslAvg, dfClaAvg, dfSAAvg, dfEAAvg, dfAbuAvg, dfDisAvg, dfMenAvg, dfSubAvg, dfLGBTAvg, dfIndAvg, dfArabAvg, dfHisAvg, dfEquAvg, dfBlaAvg, dfJudAvg, dfMulAvg, dfChrAvg]

dfAvgs = pd.concat(frames)

dfDisBib = df.groupby(['bib_record_num','Location','Audience','Genre','material_type_name', 'Diversity'])[divList].sum()

dfDisBib[divList] = dfDisBib[divList].astype(bool)
dfDisBib[divList] = dfDisBib[divList].astype(int)

dfTotUnique = dfDisBib.groupby(['Location','Audience','Genre','material_type_name', 'Diversity']).size().reset_index(name='Count')
dfTotUnique = dfTotUnique.rename(columns={'Diversity':'Category'})

dfCount = dfDisBib.groupby(['Location', 'Audience', 'Genre', 'material_type_name'])[divList].sum().reset_index()
dfMelt = pd.melt(dfCount,id_vars=['Location', 'Audience', 'Genre', 'material_type_name'],var_name='Category',value_name='Count')
dfAppend = dfMelt.append(dfTotUnique, ignore_index=True)

dfMerge = pd.merge(dfAppend, dfAvgs, on=['Location', 'Audience', 'Genre', 'material_type_name', 'Category']).reset_index()

dfMerge.to_csv('/Users/Kate/Desktop/Diversity Audit/newAggs2.csv', index=False)
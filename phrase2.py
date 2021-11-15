from numpy.core.numeric import NaN
import pandas as pd
import regex as re

dfLoad1 = pd.read_csv('/Users/Kate/Desktop/Diversity Audit/phraseentry.csv', usecols=['record_num', 'is_permuted', 'index_entry'], dtype={'record_num':int, 'is_permuted': str, 'index_entry': str})
dfLoad2 = pd.read_csv('/Users/Kate/Desktop/Diversity Audit/bibdata.csv', usecols=['record_num', 'material_type_name'], dtype={'record_num': int, 'material_type_name': str})
dfLoad3 = pd.read_csv('/Users/Kate/Desktop/Diversity Audit/itemdata.csv', usecols=['record_num', 'creation_date_gmt', 'call_number_norm', 'location_code', 'price', 'checkout_total'], dtype={'record_num': int, 'creation_date_gmt': str, 'call_number_norm': str, 'location_code': str, 'price': float, 'checkout_total': int}, parse_dates=['creation_date_gmt'], infer_datetime_format=True)
dfLoad4 = pd.read_csv('/Users/Kate/Desktop/Diversity Audit/recordlink.csv', usecols=['bib_record_num', 'item_record_num'], dtype={'bib_record_num': int, 'item_record_num': int})

#Categorize subjects

dfPhraseFull = dfLoad1.loc[dfLoad1['is_permuted'].isnull()].reset_index(drop=True)

dfPhraseFull = dfPhraseFull.drop(['is_permuted'], axis=1)

dfPhrase = dfPhraseFull.drop(['record_num'], axis=1)

dfPhrase = dfPhrase.drop_duplicates(subset=['index_entry'])

buddhismPat = r'(\bzen\b)|(dalai lama)|(buddhis)'
hinduPat = r'(\bhindu(?!(stan|\skush)))|(divali)|(\bholi\b)|(bhagavadgita)|(upanishads)'
agnosPat = r'(agnosticism)|(atheism)|(secularism)'
islamPat = r'((?<!terrorism.*)(islam(?!.*(fundamentalism|terrorism))))|(\bsufi(sm)?)|(ramadan)|(id al (fitr\b)|(\badha\b))|(quran)|(sunnites)|(shiah)|(muslim)|(mosques)|(qawwali)'
classPat = r'(working class)|(social mobility)|(standard of living)|(social classes)|(poor)|(\bcaste\b)|(social stratification)|(classism)'
sasiaPat = r'(south asia)|(indic)|(\bindia\b)|(east indian)|(bengali)|(bangladesh)|(?<!everest.*)(nepal(?!.*everest))|(sri lanka)|(bhutan)'
easiaPat = r'(east asia)|(asian americans)|(?<!everest).*(chin(a(?!\sfictitious)|ese)(?!.*everest))|(japan)|(korea)|(taiwan)|(vietnam)|(cambodia)|(mongolia)|(lao(s|tian))|(myanmar)|(malay)|(thai)|(philippin)|(filipino)|(indonesia)|(polynesia)|(brunei)|(east timor)|(pacific island)|(tibet autonomous)|(hmong)'
abusePat = r'(harassment)|(victims of)|(hate crime)|(internment)|((?<!psychological\s)torture)|(police brutality)|((human|child)\strafficking)|(kidnapping)|(genocide)|((?<!(su)|(herb)|(pest))icide)|(suicide bombers)|(murder)|(\brape)|(bullying)|(aggressiveness)|((?<!(substance|medication|opioid|oxycodone|cocaine|marijuana|opium|phetamine|drug|morphine|heroin))\sabuse)|(violent crimes)|((?<!non)violence)|(crimes against)'
disablPat = r'((?<!recordings for people.*)disabilit)|(blind)|(deaf)|(terminally ill)|(amputees)|(patients)|(aspergers)|(neurobehavioral)|(neuropsychology)|(neurodiversity)|(brain variation)|(personality disorder)|(autis(m|tic))'
mentalPat = r'(phobias)|(mentally ill)|(acceptance)|(anxiety)|(compulsive)|(schizophrenia)|(eating disorders)|(mental (health|illness|healing))|(resilience personality)|(suicid)|(self (esteem|confidence|realization|perception|actualization|management|destructive|control))|(emotional problems)|(mindfulness)|(depressi(?!ons))|(stress (psychology|disorder))|(psychic trauma)'
addictPat = r'(gamblers)|(drug use)|(substance|medication|opioid|oxycodone|cocaine|marijuana|opium|phetamine|drug|morphine|heroin)\sabuse|(alcoholi(?!c beverages))|(binge drinking)|((?<!relationship\s)addiction)|(addicts)'
lgbtPat = r'(sexual minorities)|(gender)|(asexual)|(bisexual)|(gay(s|\b(?!(head|john))))|(intersex)|(homosexual)|(lesbian)|(stonewall riots)|(masculinity)|(femininity)'
indigPat = r'(indigenous)|(aboriginal)|(american indian)|((?<!east(ern)\s)\bindians(?!\sbaseball))|(apache)|(cherokee)|(navajo)|(trail of tears)|(aztecs)|(indian art)|(maya(s|n))|(ojibwa)|(iroquois)|(nez perce)|(shoshoni)|(pueblo indian)|(seminole)|(eskimos)|(inuit)|(inca(s|n))|(algonquia?n)|(arctic peoples)|(aleut)'
arabPat = r'(\barab)|(afghan(?!\swar))|(?<!k2.*)(pakistan(?!.*k2))|(middle east)|(palestin)|(bedouin)|(israel)|(saudi)|(yemen)|(iraq(?!\swar))|(\biran\b)|(egypt(?!ologists))|(leban(on|ese))|(qatar)|(syria)|(turkey\b)'
hispPat = r'(hispanic)|(?<!new\s)(mexic)|(latin america)|(cuba(?!n\smissile))|(puerto ric)|(dominican)|(el salvador)|(salvadoran)|(argentin)|(bolivia)|(chile)|(colombia)|(costa rica)|(ecuador)|(equatorial guinea)|(guatemala)|(hondura)|(nicaragua)|(panama)|(paragua)|(peru)|(spain)|(spaniard)|(spanish)|(urugua)|(venezuela)|(brazil)|(guiana)|(guadaloup)|(martinique)|(saint barthelemy)|(saint martin)'
equityPat = r'(sexual harassment)|(((islamo)|(xeno)|(trans))phobia)|(persecution)|(activis)|(racial profiling)|(ku klux klan)|(eugenics)|(social psychology)|(social status)|(political prisoners)|(race awareness)|(equality)|(immigra)|(feminis)|(womens rights)|(sexism)|((?<!fugitives from )justice(?!(s of the peace)|(\s(league|society|donald))))|(racism)|(colorism)|(suffrag)|(sex role)|(social (change)|(movements)|(problems)|(reformers)|(responsibilit)|(conditions))|(sustainable development)|(environmental)|(poverty)|(abortion)|(((pro choice)|(labor)|(gay liberation)|(anti nazi)|(black lives matter))\smovement)|((human|civil) rights)|(prejudice)|(protest movements)|(homeless)|(public (health|welfare))|(discrimination)|(refugee)'
blackPat = r'(men black)|(\bafro)|(haiti)|(blacks(?!mith))|(africa)|(black (nationalism|panther party|power|muslim|lives))|(harlem renaissance)|(abolition)|(segregation)|(?<!(rome)|(italy)|(egypt)).*(slave(s|(ry))(?!(rome)|(egypt)|(italy)))|(slave trade)|(emancipation)|(underground railroad)|(apartheid)'
jewPat = r'(jews)|(jewish)|(judaism)|(holocaust)|(hanukkah)|(purim)|(passover)|(zionis)|(hasid)|(antisemitism)|(rosh hashanah)|(yom kippur)|(sabbath(?!day))|(sukkot)|(pentateuch)|(synagogue)|(yiddish)'
multiPat = r'(multicultural)|(interracial)|(cross cultural)|(diasporas)|((?<!sexual\s)minorities)|(ethnic identity)|((race|ethnic) relations)|(racially mixed)|(bilingual)|(passing identity)' 
chrisPat = r'(shaker)|(new testament)|(protestant)|(bibl(e|ical))|(nativity)|(adventis)|(mormon)|(baptist)|(catholic)|(methodis)|(pentecost)|(episcopal)|(lutheran)|(clergy)|(church)|(evangelicalism)|(christianity)|(easter\b)|(christmas)|(noahs ark)|(christian(?!.*\d{4}))'

BUDcomp = re.compile(buddhismPat)
HINDUcomp = re.compile(hinduPat)
AGNOScomp = re.compile(agnosPat)
ISLAMcomp = re.compile(islamPat)
CLASScomp = re.compile(classPat)
SASIAcomp = re.compile(sasiaPat)
EASIAcomp = re.compile(easiaPat)
ABUSEcomp = re.compile(abusePat)
DISABLcomp = re.compile(disablPat)
MENTALcomp = re.compile(mentalPat)
ADDICTcomp = re.compile(addictPat)
LGBTcomp = re.compile(lgbtPat)
INDIGcomp = re.compile(indigPat)
ARABcomp = re.compile(arabPat)
HISPcomp = re.compile(hispPat)
EQUITYcomp = re.compile(equityPat)
BLACKcomp = re.compile(blackPat)
JEWcomp = re.compile(jewPat)
MULTIcomp = re.compile(multiPat)
CHRIScomp = re.compile(chrisPat)

dfPhrase['Buddhism'] = [int(bool(BUDcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Hinduism'] = [int(bool(HINDUcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Agnosticism & Atheism'] = [int(bool(AGNOScomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Islam'] = [int(bool(ISLAMcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Class'] = [int(bool(CLASScomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['South Asian'] = [int(bool(SASIAcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['East Asian & Pacific Islander'] = [int(bool(EASIAcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Abuse & Violence'] = [int(bool(ABUSEcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Disabilities & Neurodiversity'] = [int(bool(DISABLcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Mental & Emotional Health'] = [int(bool(MENTALcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Substance Abuse & Addiction'] = [int(bool(ADDICTcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['LGBTQIA+ & Gender Studies'] = [int(bool(LGBTcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Indigenous'] = [int(bool(INDIGcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Arab & Middle Eastern'] = [int(bool(ARABcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Hispanic & Latino'] = [int(bool(HISPcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Equity & Social Issues'] = [int(bool(EQUITYcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Black'] = [int(bool(BLACKcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Judaism'] = [int(bool(JEWcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Multicultural'] = [int(bool(MULTIcomp.search(x))) for x in dfPhrase['index_entry']]
dfPhrase['Christianity'] = [int(bool(CHRIScomp.search(x))) for x in dfPhrase['index_entry']]

#dfPhrase.to_csv('/Users/Kate/Desktop/Diversity Audit/phraseBools.csv', index=False)

#Set up bib records

dfBib = dfLoad2.replace({'material_type_name':{'BLU-RAY':'Movie', 'DVD OR VCD':'Movie', 'JUV READALONG':'Book', 'BOOK':'Book', 'LARGE PRINT':'Book', 'PLAYAWAY AUDIOBOOK':'Audiobook', 'SPOKEN CD':'Audiobook'}})

dfBib = dfBib.loc[dfBib['material_type_name'].isin(['Book','Movie','Audiobook'])].reset_index(drop=True)

#Set up final item data table
#First, merge phrase entry dfs with each other

newPhrase = pd.merge(dfPhraseFull, dfPhrase, how='inner', on='index_entry')

#Second, merge phrase with bib record. Then condense.

bibSubjects = pd.merge(newPhrase, dfBib, how='inner', on='record_num')

bibSubjects = bibSubjects.drop(['index_entry'], axis=1)

bibSubjectsCond = bibSubjects.groupby(['record_num','material_type_name']).sum().reset_index()

divList = ['Buddhism', 'Hinduism', 'Agnosticism & Atheism', 'Islam', 'Class', 'South Asian', 'East Asian & Pacific Islander', 'Abuse & Violence', 'Disabilities & Neurodiversity', 'Mental & Emotional Health', 'Substance Abuse & Addiction', 'LGBTQIA+ & Gender Studies', 'Indigenous', 'Arab & Middle Eastern', 'Hispanic & Latino', 'Equity & Social Issues', 'Black', 'Judaism', 'Multicultural', 'Christianity']
bibSubjectsCond['Diversity'] = ['Diverse' if bibSubjectsCond[divList].iloc[x].sum() > 0 else 'Not Diverse' for x in range(len(bibSubjectsCond['Buddhism']))]


#At this point you could try to use highest count in category to assign a primary category.

#Merge bib with record link

recLink = pd.merge(bibSubjectsCond, dfLoad4, how='inner', left_on='record_num', right_on='bib_record_num').reset_index()

#Now merge this info with item data

newItem = pd.merge(dfLoad3, recLink, how='inner', left_on='record_num', right_on='item_record_num').reset_index()


nfPat = r'((.*\d\d\d.*)|(.*poetry.*)|(^jb.*))'
NFcomp = re.compile(nfPat)
newItem['Genre'] = ['Nonfiction' if NFcomp.search(x) else 'Fiction' for x in newItem['call_number_norm'].astype(str)]

newItem = newItem[newItem['location_code'].apply (lambda x: len(str(x)) > 3)]

locs = newItem.filter(['location_code'], axis=1)
locs = locs.drop_duplicates(subset=['location_code'])
locs['Audience'] = ['Juv' if x[3] == 'j' else 'YA' if x[3] == 'y' else 'Adult' for x in locs['location_code']]

finalItem = pd.merge(newItem, locs, how='inner', on='location_code')

finalItem.to_csv('/Users/Kate/Desktop/Diversity Audit/finalItem.csv', index=False)
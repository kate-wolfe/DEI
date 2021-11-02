import pandas as pd
import regex as re

df = pd.read_csv('/Users/Kate/Desktop/MergeAll.csv', dtype={'Subject':'str','Occurrences':'int','Interactions':'int'})

buddhismPat = r'(\bzen\b)|(dalai lama)|(buddhis)'
hinduPat = r'(\bhindu(?!(stan|\skush)))|(divali)|(\bholi\b)|(bhagavadgita)|(upanishads)'
agnosPat = r'(agnosticism)|(atheism)|(secularism)'
islamPat = r'(^\b(?!\w*terrorism)\w*(islam(?!.*(fundamentalism|terrorism))))|(\bsufi(sm)?)|(ramadan)|(id al fitr)|(quran)|(sunnites)|(shiah)|(muslim)|(mosques)|(qawwali)'
classPat = r'(working class)|(social mobility)|(standard of living)|(social classes)|(poor)|(\bcaste\b)|(social stratification)|(classism)'
sasiaPat = r'(south asia)|(indic)|(^\b(?!\w*k2)\w*(pakistan(?!.*k2)))|(\bindia\b)|(bengali)|(afghan(?!\swar))|(bangladesh)|(nepal)|(sri lanka)|(bhutan)'
easiaPat = r'(east asia)|(asian americans)|(chin(a(?!\sfictitious)|ese))|(japan)|(korea)|(taiwan)|(vietnam)|(cambodia)|(mongolia)|(lao(s|tian))|(myanmar)|(malay)|(thai)|(philippin)|(indonesia)|(polynesia)|(brunei)|(east timor)|(pacific island)|(tibet autonomous)|(hmong)'
abusePat = r'(bullying)|(aggressiveness)|((?<!(substance|medication|opioid|oxycodone|cocaine|marijuana|opium|phetamine|drug|morphine|heroin))\sabuse)|(violent crimes)|(violence)|(violence against)'
disablPat = r'((?<!recordings for people.*)disabilit)|(blind)|(deaf)|(terminally ill)|(amputees)|(patients)|(aspergers)|(neurobehavioral)|(neuropsychology)|(neurodiversity)|(brain variation)|(personality disorder)|(autis(m|tic))'
mentalPat = r'(acceptance)|(anxiety)|(compulsive disorder)|(schizophrenia)|(eating disorders)|(mental (health)|(illness)|healing)|(resilience personality)|(suicid)|(self (esteem|confidence|realization|perception|actualization|management|destructive|control))|(emotional problems)|(mindfulness)|(depressi)|(stress (psychology|disorder|psychology))|(psychic trauma)'
addictPat = r'(gamblers)|(drug use)|(substance|medication|opioid|oxycodone|cocaine|marijuana|opium|phetamine|drug|morphine|heroin)\sabuse|(alcoholi(?<!c beverages))|(binge drinking)|(addiction)'
lgbtPat = r'(sexual minorities)|(gender)|(asexual)|(bisexual)|(gay(s|\b(?!(head|john))))|(intersex)|(homosexual)|(lesbian)|(stonewall riots)|(masculinity)|(femininity)'
indigPat = r'(indigenous)|(aboriginal)|((?<!east\s)\bindians(?!\sbaseball))|(apache)|(cherokee)|(navajo)|(trail of tears)|(aztecs)|(indian art)|(maya(s|n))|(ojibwa)|(iroquois)|(nez perce)|(shoshoni)|(pueblo indian)|(seminole)|(eskimos)|(inuit)|(inca(s|n))|(algonquia?n)|(arctic peoples)|(aleut)'
arabPat = r'(\barab)|(middle east)|(palestin)|(bedouin)|(israel)|(saudi)|(yemen)|(iraq(?!\swar))|(iran)|(egypt(?!ologists))|(leban(on|ese))|(qatar)|(syria)|(turkey\b)'
hispPat = r'(hispanic)|(?<!new\s)(mexic)|(latin america)|(cuba(?!n\smissile))|(puerto ric)|(dominican)|(el salvador)|(salvadoran)|(argentin)|(bolivia)|(chile)|(colombia)|(costa rica)|(ecuador)|(equatorial guinea)|(guatemala)|(hondura)|(nicaragua)|(panama)|(paragua)|(peru)|(spain)|(spaniard)|(spanish)|(urugua)|(venezuela)|(brazil)|(guiana)|(guadaloup)|(haiti)|(martinique)|(saint barthelemy)|(saint martin)'
equityPat = r'(equality)|(immigra)|(feminis)|(womens rights)|(sexism)|(?<!fugitives from )justice(?!(s of the peace)|(\s(league|society|donald)))|(racism)|(suffrag)|(sex role)|(social (change)|(movements)|(problems)|(reformers)|(responsibilit))|(sustainable development)|(environmental)|(poverty)|(abortion)|((human|civil) rights)|(prejudice)|(protest movements)|(homeless)|(public (health|welfare))|(discrimination)|(refugee)'
blackPat = r'(\bafro)|(blacks(?!mith))|(africa)|(black (nationalism|panther party|power|muslim|lives))|(harlem renaissance)|(abolition)|(segregation)|(slavery)|(underground railroad)|(apartheid)'
jewPat = r'(jews)|(judaism)|(hanukkah)|(purim)|(passover)|(zionis)|(hasidism)|(antisemitism)|(rosh hashanah)|(yom kippur)|(sabbath)|(sukkot)|(pentateuch)|(synagogue)'
multiPat = r'(multicultural)|(cross cultural)|(diasporas)|(minorities)|(ethnic identity)|((race|ethnic) relations)|(racially mixed)|(bilingual)' 
chrisPat = r'(protestant)|(bible)|(nativity)|(adventis)|(mormon)|(baptist)|(catholic)|(methodis)|(pentecost)|(episcopal)|(lutheran)|(clergy)|(church)|(evangelicalism)|(christianity)|(easter)|(christmas)'

BUDcomp = re.compile(buddhismPat, flags=re.IGNORECASE)
HINDUcomp = re.compile(hinduPat, flags=re.IGNORECASE)
AGNOScomp = re.compile(agnosPat, flags=re.IGNORECASE)
ISLAMcomp = re.compile(islamPat, flags=re.IGNORECASE)
CLASScomp = re.compile(classPat, flags=re.IGNORECASE)
SASIAcomp = re.compile(sasiaPat, flags=re.IGNORECASE)
EASIAcomp = re.compile(easiaPat, flags=re.IGNORECASE)
ABUSEcomp = re.compile(abusePat, flags=re.IGNORECASE)
DISABLcomp = re.compile(disablPat, flags=re.IGNORECASE)
MENTALcomp = re.compile(mentalPat, flags=re.IGNORECASE)
ADDICTcomp = re.compile(addictPat, flags=re.IGNORECASE)
LGBTcomp = re.compile(lgbtPat, flags=re.IGNORECASE)
INDIGcomp = re.compile(indigPat, flags=re.IGNORECASE)
ARABcomp = re.compile(arabPat, flags=re.IGNORECASE)
HISPcomp = re.compile(hispPat, flags=re.IGNORECASE)
EQUITYcomp = re.compile(equityPat, flags=re.IGNORECASE)
BLACKcomp = re.compile(blackPat, flags=re.IGNORECASE)
JEWcomp = re.compile(jewPat, flags=re.IGNORECASE)
MULTIcomp = re.compile(multiPat, flags=re.IGNORECASE)
CHRIScomp = re.compile(chrisPat, flags=re.IGNORECASE)

df['Buddhism'] = [bool(BUDcomp.search(x)) for x in df['Subject']]
df['Hinduism'] = [bool(HINDUcomp.search(x)) for x in df['Subject']]
df['Agnosticism & Atheism'] = [bool(AGNOScomp.search(x)) for x in df['Subject']]
df['Islam'] = [bool(ISLAMcomp.search(x)) for x in df['Subject']]
df['Class'] = [bool(CLASScomp.search(x)) for x in df['Subject']]
df['South Asian'] = [bool(SASIAcomp.search(x)) for x in df['Subject']]
df['East Asian & Pacific Islander'] = [bool(EASIAcomp.search(x)) for x in df['Subject']]
df['Abuse & Violence'] = [bool(ABUSEcomp.search(x)) for x in df['Subject']]
df['Disabilities & Neurodiversity'] = [bool(DISABLcomp.search(x)) for x in df['Subject']]
df['Mental & Emotional Health'] = [bool(MENTALcomp.search(x)) for x in df['Subject']]
df['Substance Abuse & Addiction'] = [bool(ADDICTcomp.search(x)) for x in df['Subject']]
df['LGBTQIA+ & Gender Studies'] = [bool(LGBTcomp.search(x)) for x in df['Subject']]
df['Indigenous'] = [bool(INDIGcomp.search(x)) for x in df['Subject']]
df['Arab & Middle Eastern'] = [bool(ARABcomp.search(x)) for x in df['Subject']]
df['Hispanic & Latino'] = [bool(HISPcomp.search(x)) for x in df['Subject']]
df['Equity & Social Issues'] = [bool(EQUITYcomp.search(x)) for x in df['Subject']]
df['Black'] = [bool(BLACKcomp.search(x)) for x in df['Subject']]
df['Judaism'] = [bool(JEWcomp.search(x)) for x in df['Subject']]
df['Multicultural'] = [bool(MULTIcomp.search(x)) for x in df['Subject']]
df['Christianity'] = [bool(CHRIScomp.search(x)) for x in df['Subject']]

df.to_csv('/Users/Kate/Desktop/upsetdataALL.csv', index=False)
from numpy.core.numeric import NaN
import pandas as pd
import regex as re

dfLoad = pd.read_csv('/Users/Kate/Desktop/PhraseEntry.csv', usecols=['is_permuted', 'index_entry'], dtype={'record_num': int, 'is_permuted': str, 'index_entry': str})

df = dfLoad.loc[dfLoad['is_permuted'].isnull()].reset_index(drop=True)

df = df.drop(['is_permuted'], axis=1)

df = df.drop_duplicates(subset=['index_entry'])

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
addictPat = r'(gamblers)|(drug use)|(substance|medication|opioid|oxycodone|cocaine|marijuana|opium|phetamine|drug|morphine|heroin)\sabuse|(alcoholi(?!c beverages))|(binge drinking)|((?!relationship\s)addiction)|(addicts)'
lgbtPat = r'(sexual minorities)|(gender)|(asexual)|(bisexual)|(gay(s|\b(?!(head|john))))|(intersex)|(homosexual)|(lesbian)|(stonewall riots)|(masculinity)|(femininity)'
indigPat = r'(indigenous)|(aboriginal)|(american indian)|((?<!east(ern)\s)\bindians(?!\sbaseball))|(apache)|(cherokee)|(navajo)|(trail of tears)|(aztecs)|(indian art)|(maya(s|n))|(ojibwa)|(iroquois)|(nez perce)|(shoshoni)|(pueblo indian)|(seminole)|(eskimos)|(inuit)|(inca(s|n))|(algonquia?n)|(arctic peoples)|(aleut)'
arabPat = r'(\barab)|(afghan(?!\swar))|(?<!k2.*)(pakistan(?!.*k2))|(middle east)|(palestin)|(bedouin)|(israel)|(saudi)|(yemen)|(iraq(?!\swar))|(\biran\b)|(egypt(?!ologists))|(leban(on|ese))|(qatar)|(syria)|(turkey\b)'
hispPat = r'(hispanic)|(?<!new\s)(mexic)|(latin america)|(cuba(?!n\smissile))|(puerto ric)|(dominican)|(el salvador)|(salvadoran)|(argentin)|(bolivia)|(chile)|(colombia)|(costa rica)|(ecuador)|(equatorial guinea)|(guatemala)|(hondura)|(nicaragua)|(panama)|(paragua)|(peru)|(spain)|(spaniard)|(spanish)|(urugua)|(venezuela)|(brazil)|(guiana)|(guadaloup)|(martinique)|(saint barthelemy)|(saint martin)'
equityPat = r'(sexual harassment)|(((islamo)|(xeno)|(trans))phobia)|(persecution)|(activis)|(racial profiling)|(ku klux klan)|(eugenics)|(social psychology)|(social status)|(political prisoners)|(race awareness)|(equality)|(immigra)|(feminis)|(womens rights)|(sexism)|((?<!fugitives from )justice(?!(s of the peace)|(\s(league|society|donald))))|(racism)|(colorism)|(suffrag)|(sex role)|(social (change)|(movements)|(problems)|(reformers)|(responsibilit)|(conditions))|(sustainable development)|(environmental)|(poverty)|(abortion)|(((pro choice)|(labor)|(gay liberation)|(anti nazi)|(black lives matter))\smovement)|((human|civil) rights)|(prejudice)|(protest movements)|(homeless)|(public (health|welfare))|(discrimination)|(refugee)'
blackPat = r'(men black)|(\bafro)|(haiti)|(blacks(?!mith))|(africa)|(black (nationalism|panther party|power|muslim|lives))|(harlem renaissance)|(abolition)|(segregation)|(?<!(rome)|(italy)|(egypt)).*(slave(s|(ry))(?!(rome)|(egypt)|(italy)))|(slave trade)|(emancipation)|(underground railroad)|(apartheid)'
jewPat = r'(jews)|(jewish)|(judaism)|(holocaust)|(hanukkah)|(purim)|(passover)|(zionis)|(hasid)|(antisemitism)|(rosh hashanah)|(yom kippur)|(sabbath(?!day))|(sukkot)|(pentateuch)|(synagogue)|(yiddish)'
multiPat = r'(multicultural)|(interracial)|(cross cultural)|(diasporas)|((?<!sexual\s)minorities)|(ethnic identity)|((race|ethnic) relations)|(racially mixed)|(bilingual)|(passing identity)' 
chrisPat = r'(shaker)|(new testament)|(protestant)|(bibl(e|ical))|(nativity)|(adventis)|(mormon)|(baptist)|(catholic)|(methodis)|(pentecost)|(episcopal)|(lutheran)|(clergy)|(church)|(evangelicalism)|(christianity)|(easter\b)|(christmas)|(noahs ark)|(christian(?!.*\d{4}))'

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

df['Buddhism'] = [bool(BUDcomp.search(x)) for x in df['index_entry']]
df['Hinduism'] = [bool(HINDUcomp.search(x)) for x in df['index_entry']]
df['Agnosticism & Atheism'] = [bool(AGNOScomp.search(x)) for x in df['index_entry']]
df['Islam'] = [bool(ISLAMcomp.search(x)) for x in df['index_entry']]
df['Class'] = [bool(CLASScomp.search(x)) for x in df['index_entry']]
df['South Asian'] = [bool(SASIAcomp.search(x)) for x in df['index_entry']]
df['East Asian & Pacific Islander'] = [bool(EASIAcomp.search(x)) for x in df['index_entry']]
df['Abuse & Violence'] = [bool(ABUSEcomp.search(x)) for x in df['index_entry']]
df['Disabilities & Neurodiversity'] = [bool(DISABLcomp.search(x)) for x in df['index_entry']]
df['Mental & Emotional Health'] = [bool(MENTALcomp.search(x)) for x in df['index_entry']]
df['Substance Abuse & Addiction'] = [bool(ADDICTcomp.search(x)) for x in df['index_entry']]
df['LGBTQIA+ & Gender Studies'] = [bool(LGBTcomp.search(x)) for x in df['index_entry']]
df['Indigenous'] = [bool(INDIGcomp.search(x)) for x in df['index_entry']]
df['Arab & Middle Eastern'] = [bool(ARABcomp.search(x)) for x in df['index_entry']]
df['Hispanic & Latino'] = [bool(HISPcomp.search(x)) for x in df['index_entry']]
df['Equity & Social Issues'] = [bool(EQUITYcomp.search(x)) for x in df['index_entry']]
df['Black'] = [bool(BLACKcomp.search(x)) for x in df['index_entry']]
df['Judaism'] = [bool(JEWcomp.search(x)) for x in df['index_entry']]
df['Multicultural'] = [bool(MULTIcomp.search(x)) for x in df['index_entry']]
df['Christianity'] = [bool(CHRIScomp.search(x)) for x in df['index_entry']]

df.to_csv('/Users/Kate/Desktop/phraseBools.csv', index=False)

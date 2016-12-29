#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import petrarch_ud, PETRglobals, PETRreader, utilities, codecs

config = utilities._get_data('data/config/', 'PETR_config.ini')
print("reading config")
PETRreader.parse_Config(config)
print("reading dicts")
petrarch_ud.read_dictionaries()
fout_report = codecs.open("test_report.txt","w",encoding='utf8') #opens test report file for writing
fout_report.write("Text@ Parse Tree@ Expected Encoding as per Petrarch@ Result from Petrarch2 @Verbs @Nouns\n")
def parse_parser(parse):
    phrase_dict = {}
    for line in parse.splitlines():
        line = line.split("_")
        num = line[0][:2].strip()
        str = line[0][2:].strip()
        phrase_dict[num]=str
        #print(num)
        #print(str)
    return phrase_dict	
def parse_verb_noun(strs,phrase_dict):
    str_out = ""
    str_arr = str(strs).strip("{").split(",")
    print("Verb/Noun") 
    print("Printing Verbs/Noun")
    for x in str_arr:
        str_num = x.find(":")		
        str_out = str_out + ", " + phrase_dict[x[:str_num].strip()]
        #print(phrase_dict[verb[:verb_num].strip()])
    fout_report.write("@"+ str_out[1:])
    return
def test1():
    text="""Arnor is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test2': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test2']['sents']['0']:
            print(return_dict['test2']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test2']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test2 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test2 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test2']['sents']['0']:
        verbs=return_dict['test2']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test2']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test2']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test2():
    text="""Arnor is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test3': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test3']['sents']['0']:
            print(return_dict['test3']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test3']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test3 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test3 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test3']['sents']['0']:
        verbs=return_dict['test3']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test3']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test3']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test3():
    text="""Dagolath's first Deputy Prime Minister Telemar left for 
Minas Tirith on Wednesday for meetings of the joint transport 
committee with Arnor, the Dagolathi news agency reported. 
"""
    parse="""1	Dagolath	_	PROPN	PROPN	_	4	nmod:poss
2	's	_	PART	PART	_	1	case
3	first	_	ADJ	ADJ	_	4	amod
4	Deputy	_	NOUN	NOUN	_	7	compound
5	Prime	_	PROPN	PROPN	_	6	compound
6	Minister	_	PROPN	PROPN	_	7	compound
7	Telemar	_	PROPN	PROPN	_	8	nsubj
8	left	_	VERB	VERB	_	0	root
9	for	_	ADP	ADP	_	11	case
10	Minas	_	PROPN	PROPN	_	11	compound
11	Tirith	_	PROPN	PROPN	_	8	nmod
12	on	_	ADP	ADP	_	13	case
13	Wednesday	_	PROPN	PROPN	_	8	nmod
14	for	_	ADP	ADP	_	15	case
15	meetings	_	NOUN	NOUN	_	8	nmod
16	of	_	ADP	ADP	_	20	case
17	the	_	DET	DET	_	20	det
18	joint	_	ADJ	ADJ	_	20	amod
19	transport	_	NOUN	NOUN	_	20	compound
20	committee	_	NOUN	NOUN	_	15	nmod
21	with	_	ADP	ADP	_	22	case
22	Arnor	_	PROPN	PROPN	_	20	nmod
23	,	_	PUNCT	PUNCT	_	20	punct
24	the	_	DET	DET	_	27	det
25	Dagolathi	_	PROPN	PROPN	_	27	compound
26	news	_	NOUN	NOUN	_	27	compound
27	agency	_	NOUN	NOUN	_	20	nmod
28	reported	_	VERB	VERB	_	27	acl
29	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test4': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test4']['sents']['0']:
            print(return_dict['test4']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")@ " + str(return_dict['test4']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")@ noevent  " )
            print("test4 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")@ noeventexception \n " )
        print("test4 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test4']['sents']['0']:
        verbs=return_dict['test4']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test4']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test4']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test4():
    text="""Caras Galadhon's new mayor left yesterday for Minas Tirith for meetings of 
the joint transport committee with Arnor. 
"""
    parse="""1	Caras	_	PROPN	PROPN	_	2	name
2	Galadhon	_	PROPN	PROPN	_	5	nmod:poss
3	's	_	PART	PART	_	2	case
4	new	_	ADJ	ADJ	_	5	amod
5	mayor	_	NOUN	NOUN	_	6	nsubj
6	left	_	VERB	VERB	_	0	root
7	yesterday	_	NOUN	NOUN	_	6	dobj
8	for	_	ADP	ADP	_	10	case
9	Minas	_	PROPN	PROPN	_	10	compound
10	Tirith	_	PROPN	PROPN	_	6	nmod
11	for	_	ADP	ADP	_	12	case
12	meetings	_	NOUN	NOUN	_	6	nmod
13	of	_	ADP	ADP	_	17	case
14	the	_	DET	DET	_	17	det
15	joint	_	ADJ	ADJ	_	17	amod
16	transport	_	NOUN	NOUN	_	17	compound
17	committee	_	NOUN	NOUN	_	12	nmod
18	with	_	ADP	ADP	_	19	case
19	Arnor	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test5': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test5']['sents']['0']:
            print(return_dict['test5']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")@ " + str(return_dict['test5']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")@ noevent  " )
            print("test5 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")@ noeventexception \n " )
        print("test5 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test5']['sents']['0']:
        verbs=return_dict['test5']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test5']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test5']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test5():
    text="""Arnor is about to restore fxll diplomatic ties with Gondor almost 
five years after volleyball crowds burned down its embassy,  a senior 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	25	nsubj
2	is	_	VERB	VERB	_	25	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	fxll	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	5	nmod
14	after	_	ADP	ADP	_	16	case
15	volleyball	_	ADJ	ADJ	_	16	amod
16	crowds	_	NOUN	NOUN	_	8	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	20	case
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	,	_	PUNCT	PUNCT	_	25	punct
22	a	_	DET	DET	_	24	det
23	senior	_	ADJ	ADJ	_	24	amod
24	official	_	NOUN	NOUN	_	25	nsubj
25	said	_	VERB	VERB	_	0	root
26	on	_	ADP	ADP	_	27	case
27	Saturday	_	PROPN	PROPN	_	25	nmod
28	.	_	PUNCT	PUNCT	_	25	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test6': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test6']['sents']['0']:
            print(return_dict['test6']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test6']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test6 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test6 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test6']['sents']['0']:
        verbs=return_dict['test6']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test6']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test6']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test6():
    text="""An Eriadorian was shot dead in Osgiliath, the state's fiercest foe. 
"""
    parse="""1	An	_	DET	DET	_	2	det
2	Eriadorian	_	NOUN	NOUN	_	4	nsubj
3	was	_	AUX	AUX	_	4	aux
4	shot	_	VERB	VERB	_	0	root
5	dead	_	ADJ	ADJ	_	4	dobj
6	in	_	ADP	ADP	_	7	case
7	Osgiliath	_	PROPN	PROPN	_	4	nmod
8	,	_	PUNCT	PUNCT	_	4	punct
9	the	_	DET	DET	_	10	det
10	state	_	NOUN	NOUN	_	13	nmod:poss
11	's	_	PART	PART	_	10	case
12	fiercest	_	ADJ	ADJ	_	13	amod
13	foe	_	NOUN	NOUN	_	4	nmod
14	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test7': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"224\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test7']['sents']['0']:
            print(return_dict['test7']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"224\")@ " + str(return_dict['test7']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"224\")@ noevent  " )
            print("test7 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"224\")@ noeventexception \n " )
        print("test7 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test7']['sents']['0']:
        verbs=return_dict['test7']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test7']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test7']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test7():
    text="""The Calenardhon government condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday and promised aid to the affected Ithilen villages. 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	condemned	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
15	and	_	CONJ	CONJ	_	4	cc
16	promised	_	VERB	VERB	_	4	conj
17	aid	_	NOUN	NOUN	_	16	dobj
18	to	_	ADP	ADP	_	22	case
19	the	_	DET	DET	_	22	det
20	affected	_	VERB	VERB	_	22	amod
21	Ithilen	_	NOUN	NOUN	_	22	compound
22	villages	_	NOUN	NOUN	_	17	nmod
23	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test8': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test8']['sents']['0']:
            print(return_dict['test8']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ " + str(return_dict['test8']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ noevent  " )
            print("test8 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ noeventexception \n " )
        print("test8 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test8']['sents']['0']:
        verbs=return_dict['test8']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test8']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test8']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test8():
    text="""Arnor believes Dagolath and Osgiliath can cope with a decrease in vital 
water from the mighty Entwash river when a major dam is filled next 
month. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	believes	_	VERB	VERB	_	0	root
3	Dagolath	_	PROPN	PROPN	_	2	dobj
4	and	_	CONJ	CONJ	_	3	cc
5	Osgiliath	_	PROPN	PROPN	_	3	conj
6	can	_	AUX	AUX	_	7	aux
7	cope	_	VERB	VERB	_	2	conj
8	with	_	ADP	ADP	_	10	case
9	a	_	DET	DET	_	10	det
10	decrease	_	NOUN	NOUN	_	7	nmod
11	in	_	ADP	ADP	_	13	case
12	vital	_	ADJ	ADJ	_	13	amod
13	water	_	NOUN	NOUN	_	10	nmod
14	from	_	ADP	ADP	_	18	case
15	the	_	DET	DET	_	18	det
16	mighty	_	PROPN	PROPN	_	17	compound
17	Entwash	_	PROPN	PROPN	_	18	compound
18	river	_	NOUN	NOUN	_	13	nmod
19	when	_	ADV	ADV	_	24	mark
20	a	_	DET	DET	_	22	det
21	major	_	ADJ	ADJ	_	22	amod
22	dam	_	NOUN	NOUN	_	24	nsubj
23	is	_	AUX	AUX	_	24	aux
24	filled	_	VERB	VERB	_	18	advcl
25	next	_	ADJ	ADJ	_	26	amod
26	month	_	NOUN	NOUN	_	24	dobj
27	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test9': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950107'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test9']['sents']['0']:
            print(return_dict['test9']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")@ " + str(return_dict['test9']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")@ noevent  " )
            print("test9 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")@ noeventexception \n " )
        print("test9 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test9']['sents']['0']:
        verbs=return_dict['test9']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test9']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test9']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test9():
    text="""The ambassadors of Arnor, Osgiliath and Gondor presented 
credentials to Ithilen's president on Wednesday in a further 
show of support to his government by their countries. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	ambassadors	_	NOUN	NOUN	_	9	nsubj
3	of	_	ADP	ADP	_	4	case
4	Arnor	_	PROPN	PROPN	_	2	nmod
5	,	_	PUNCT	PUNCT	_	4	punct
6	Osgiliath	_	PROPN	PROPN	_	4	conj
7	and	_	CONJ	CONJ	_	4	cc
8	Gondor	_	PROPN	PROPN	_	4	conj
9	presented	_	VERB	VERB	_	0	root
10	credentials	_	NOUN	NOUN	_	9	dobj
11	to	_	ADP	ADP	_	14	case
12	Ithilen	_	PROPN	PROPN	_	14	nmod:poss
13	's	_	PART	PART	_	12	case
14	president	_	PROPN	PROPN	_	10	nmod
15	on	_	ADP	ADP	_	16	case
16	Wednesday	_	PROPN	PROPN	_	9	nmod
17	in	_	ADP	ADP	_	20	case
18	a	_	DET	DET	_	20	det
19	further	_	ADJ	ADJ	_	20	amod
20	show	_	NOUN	NOUN	_	9	nmod
21	of	_	ADP	ADP	_	22	case
22	support	_	NOUN	NOUN	_	20	nmod
23	to	_	ADP	ADP	_	25	case
24	his	_	PRON	PRON	_	25	nmod:poss
25	government	_	NOUN	NOUN	_	22	nmod
26	by	_	ADP	ADP	_	28	case
27	their	_	PRON	PRON	_	28	nmod:poss
28	countries	_	NOUN	NOUN	_	9	nmod
29	.	_	PUNCT	PUNCT	_	9	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test10': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950108'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test10']['sents']['0']:
            print(return_dict['test10']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ " + str(return_dict['test10']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ noevent  " )
            print("test10 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ noeventexception \n " )
        print("test10 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test10']['sents']['0']:
        verbs=return_dict['test10']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test10']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test10']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test10():
    text="""Gondor's Prime Minister Falastur noted that Cirith Ungol regretted Eriador's 
refusal to talk to Calenardhon leader Calimehtar. 
"""
    parse="""1	Gondor	_	PROPN	PROPN	_	5	nmod:poss
2	's	_	PART	PART	_	1	case
3	Prime	_	PROPN	PROPN	_	4	compound
4	Minister	_	PROPN	PROPN	_	5	compound
5	Falastur	_	PROPN	PROPN	_	6	nsubj
6	noted	_	VERB	VERB	_	0	root
7	that	_	SCONJ	SCONJ	_	10	mark
8	Cirith	_	PROPN	PROPN	_	9	name
9	Ungol	_	PROPN	PROPN	_	10	nsubj
10	regretted	_	VERB	VERB	_	6	ccomp
11	Eriador	_	PROPN	PROPN	_	10	dobj
12	's	_	PART	PART	_	11	case
13	refusal	_	ADJ	ADJ	_	10	xcomp
14	to	_	PART	PART	_	15	mark
15	talk	_	VERB	VERB	_	13	xcomp
16	to	_	ADP	ADP	_	18	case
17	Calenardhon	_	PROPN	PROPN	_	18	compound
18	leader	_	NOUN	NOUN	_	15	nmod
19	Calimehtar	_	PROPN	PROPN	_	18	vocative
20	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test11': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950110'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONGOV\", u\"MORMIL\", u\"115\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test11']['sents']['0']:
            print(return_dict['test11']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONGOV\", u\"MORMIL\", u\"115\")@ " + str(return_dict['test11']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONGOV\", u\"MORMIL\", u\"115\")@ noevent  " )
            print("test11 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONGOV\", u\"MORMIL\", u\"115\")@ noeventexception \n " )
        print("test11 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test11']['sents']['0']:
        verbs=return_dict['test11']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test11']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test11']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test11():
    text="""Bree Prime Minister Romendacil will meet Eriadori and Calenardhon 
leaders during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	6	nsubj
5	will	_	AUX	AUX	_	6	aux
6	meet	_	VERB	VERB	_	0	root
7	Eriadori	_	PROPN	PROPN	_	6	dobj
8	and	_	CONJ	CONJ	_	7	cc
9	Calenardhon	_	PROPN	PROPN	_	7	conj
10	leaders	_	NOUN	NOUN	_	6	dobj
11	during	_	ADP	ADP	_	15	case
12	a	_	DET	DET	_	15	det
13	brief	_	ADJ	ADJ	_	15	amod
14	private	_	ADJ	ADJ	_	15	amod
15	visit	_	NOUN	NOUN	_	6	nmod
16	to	_	ADP	ADP	_	17	case
17	Eriador	_	PROPN	PROPN	_	15	nmod
18	starting	_	VERB	VERB	_	15	acl
19	on	_	ADP	ADP	_	20	case
20	Sunday	_	PROPN	PROPN	_	18	nmod
21	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test12': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test12']['sents']['0']:
            print(return_dict['test12']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")@ " + str(return_dict['test12']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")@ noevent  " )
            print("test12 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")@ noeventexception \n " )
        print("test12 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test12']['sents']['0']:
        verbs=return_dict['test12']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test12']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test12']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test12():
    text="""Eriador expressed hopes on Thursday that Osgiliath, the state's 
fiercest foe, could be drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	2	nsubj
2	expressed	_	VERB	VERB	_	0	root
3	hopes	_	NOUN	NOUN	_	2	dobj
4	on	_	ADP	ADP	_	5	case
5	Thursday	_	PROPN	PROPN	_	2	nmod
6	that	_	ADP	ADP	_	7	case
7	Osgiliath	_	PROPN	PROPN	_	2	nmod
8	,	_	PUNCT	PUNCT	_	7	punct
9	the	_	DET	DET	_	10	det
10	state	_	NOUN	NOUN	_	13	nmod:poss
11	's	_	PART	PART	_	10	case
12	fiercest	_	ADJ	ADJ	_	13	amod
13	foe	_	NOUN	NOUN	_	7	appos
14	,	_	PUNCT	PUNCT	_	2	punct
15	could	_	AUX	AUX	_	17	aux
16	be	_	AUX	AUX	_	17	aux
17	drawn	_	VERB	VERB	_	2	parataxis
18	into	_	ADP	ADP	_	21	case
19	the	_	DET	DET	_	21	det
20	peace	_	NOUN	NOUN	_	21	compound
21	process	_	NOUN	NOUN	_	17	nmod
22	by	_	ADP	ADP	_	24	case
23	its	_	PRON	PRON	_	24	nmod:poss
24	resumption	_	NOUN	NOUN	_	21	nmod
25	of	_	ADP	ADP	_	27	case
26	diplomatic	_	ADJ	ADJ	_	27	amod
27	ties	_	NOUN	NOUN	_	24	nmod
28	with	_	ADP	ADP	_	29	case
29	Gondor	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test13': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"024\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test13']['sents']['0']:
            print(return_dict['test13']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"024\")@ " + str(return_dict['test13']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"024\")@ noevent  " )
            print("test13 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"024\")@ noeventexception \n " )
        print("test13 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test13']['sents']['0']:
        verbs=return_dict['test13']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test13']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test13']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test13():
    text="""Arnor on Thursday signed an 800 million ducat trade protocol
for 1990 with Dagolath, its biggest trading partner, officials said. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	nsubj
2	on	_	ADP	ADP	_	3	case
3	Thursday	_	PROPN	PROPN	_	1	nmod
4	signed	_	VERB	VERB	_	22	advcl
5	an	_	DET	DET	_	10	det
6	800	_	NUM	NUM	_	7	compound
7	million	_	NUM	NUM	_	8	nummod
8	ducat	_	NOUN	NOUN	_	10	compound
9	trade	_	NOUN	NOUN	_	10	compound
10	protocol	_	NOUN	NOUN	_	4	dobj
11	for	_	ADP	ADP	_	12	case
12	1990	_	NUM	NUM	_	10	nmod
13	with	_	ADP	ADP	_	14	case
14	Dagolath	_	PROPN	PROPN	_	10	nmod
15	,	_	PUNCT	PUNCT	_	14	punct
16	its	_	PRON	PRON	_	19	nmod:poss
17	biggest	_	ADJ	ADJ	_	19	amod
18	trading	_	NOUN	NOUN	_	19	compound
19	partner	_	NOUN	NOUN	_	14	conj
20	,	_	PUNCT	PUNCT	_	22	punct
21	officials	_	NOUN	NOUN	_	22	nsubj
22	said	_	VERB	VERB	_	0	root
23	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test14': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test14']['sents']['0']:
            print(return_dict['test14']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ " + str(return_dict['test14']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ noevent  " )
            print("test14 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ noeventexception \n " )
        print("test14 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test14']['sents']['0']:
        verbs=return_dict['test14']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test14']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test14']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test14():
    text="""Ithilen's militia vowed on Thursday to wage war on the Rohans until that 
group yielded ground seized in six days of fighting.
"""
    parse="""1	Ithilen	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	militia	_	NOUN	NOUN	_	4	nsubj
4	vowed	_	VERB	VERB	_	0	root
5	on	_	ADP	ADP	_	6	case
6	Thursday	_	PROPN	PROPN	_	4	nmod
7	to	_	PART	PART	_	8	mark
8	wage	_	VERB	VERB	_	4	advcl
9	war	_	NOUN	NOUN	_	8	dobj
10	on	_	ADP	ADP	_	12	case
11	the	_	DET	DET	_	12	det
12	Rohans	_	PROPN	PROPN	_	8	nmod
13	until	_	ADP	ADP	_	15	case
14	that	_	DET	DET	_	15	det
15	group	_	NOUN	NOUN	_	8	nmod
16	yielded	_	VERB	VERB	_	15	acl
17	ground	_	NOUN	NOUN	_	16	dobj
18	seized	_	VERB	VERB	_	17	acl
19	in	_	ADP	ADP	_	21	case
20	six	_	NUM	NUM	_	21	nummod
21	days	_	NOUN	NOUN	_	18	nmod
22	of	_	ADP	ADP	_	23	case
23	fighting	_	NOUN	NOUN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test15': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950114'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"ROH\", u\"173\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test15']['sents']['0']:
            print(return_dict['test15']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"ROH\", u\"173\")@ " + str(return_dict['test15']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"ROH\", u\"173\")@ noevent  " )
            print("test15 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"ROH\", u\"173\")@ noeventexception \n " )
        print("test15 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test15']['sents']['0']:
        verbs=return_dict['test15']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test15']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test15']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test15():
    text="""Arnor signed an accord on Thursday to supply Gondor with some 
50,000 tonnes of wheat, worth 11.8 million ducats, an Arnorian 
embassy spokesman said.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	signed	_	VERB	VERB	_	0	root
3	an	_	DET	DET	_	4	det
4	accord	_	NOUN	NOUN	_	2	dobj
5	on	_	ADP	ADP	_	6	case
6	Thursday	_	PROPN	PROPN	_	2	nmod
7	to	_	PART	PART	_	8	mark
8	supply	_	VERB	VERB	_	2	advcl
9	Gondor	_	PROPN	PROPN	_	8	dobj
10	with	_	ADP	ADP	_	13	case
11	some	_	DET	DET	_	13	det
12	50,000	_	NUM	NUM	_	13	nummod
13	tonnes	_	NOUN	NOUN	_	8	nmod
14	of	_	ADP	ADP	_	15	case
15	wheat	_	NOUN	NOUN	_	13	nmod
16	,	_	PUNCT	PUNCT	_	13	punct
17	worth	_	ADJ	ADJ	_	20	amod
18	11.8	_	NUM	NUM	_	19	compound
19	million	_	NUM	NUM	_	20	nummod
20	ducats	_	NOUN	NOUN	_	13	nmod
21	,	_	PUNCT	PUNCT	_	20	punct
22	an	_	DET	DET	_	25	det
23	Arnorian	_	ADJ	ADJ	_	25	amod
24	embassy	_	NOUN	NOUN	_	25	compound
25	spokesman	_	NOUN	NOUN	_	20	appos
26	said	_	VERB	VERB	_	25	acl
27	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test16': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950115'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test16']['sents']['0']:
            print(return_dict['test16']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ " + str(return_dict['test16']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ noevent  " )
            print("test16 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ noeventexception \n " )
        print("test16 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test16']['sents']['0']:
        verbs=return_dict['test16']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test16']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test16']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test16():
    text="""Fornost President Umbardacil has again appealed for peace in Ithilen in 
a message to the spiritial leader of the war-torn nation's influential 
Douzu community.
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	2	compound
2	President	_	PROPN	PROPN	_	3	compound
3	Umbardacil	_	PROPN	PROPN	_	6	nsubj
4	has	_	AUX	AUX	_	6	aux
5	again	_	ADV	ADV	_	6	advmod
6	appealed	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	8	case
8	peace	_	NOUN	NOUN	_	6	nmod
9	in	_	ADP	ADP	_	10	case
10	Ithilen	_	PROPN	PROPN	_	6	nmod
11	in	_	ADP	ADP	_	13	case
12	a	_	DET	DET	_	13	det
13	message	_	NOUN	NOUN	_	6	nmod
14	to	_	ADP	ADP	_	17	case
15	the	_	DET	DET	_	17	det
16	spiritial	_	ADJ	ADJ	_	17	amod
17	leader	_	NOUN	NOUN	_	13	nmod
18	of	_	ADP	ADP	_	25	case
19	the	_	DET	DET	_	21	det
20	war-torn	_	ADJ	ADJ	_	21	amod
21	nation	_	NOUN	NOUN	_	25	nmod:poss
22	's	_	PART	PART	_	21	case
23	influential	_	ADJ	ADJ	_	25	amod
24	Douzu	_	PROPN	PROPN	_	25	compound
25	community	_	NOUN	NOUN	_	17	nmod
26	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test17': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950116'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITH\", u\"095\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test17']['sents']['0']:
            print(return_dict['test17']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITH\", u\"095\")@ " + str(return_dict['test17']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITH\", u\"095\")@ noevent  " )
            print("test17 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITH\", u\"095\")@ noeventexception \n " )
        print("test17 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test17']['sents']['0']:
        verbs=return_dict['test17']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test17']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test17']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test17():
    text="""Bree President Romendacil arrived in Gondor on Monday on his first 
official foreign visit since pro-restoration demonstrators 
in Eymn Muil were crushed last June.
"""
    parse="""1	Bree	_	PROPN	PROPN	_	2	compound
2	President	_	PROPN	PROPN	_	3	compound
3	Romendacil	_	PROPN	PROPN	_	22	nsubj
4	arrived	_	VERB	VERB	_	3	acl
5	in	_	ADP	ADP	_	6	case
6	Gondor	_	PROPN	PROPN	_	4	nmod
7	on	_	ADP	ADP	_	8	case
8	Monday	_	PROPN	PROPN	_	4	nmod
9	on	_	ADP	ADP	_	14	case
10	his	_	PRON	PRON	_	14	nmod:poss
11	first	_	ADJ	ADJ	_	14	amod
12	official	_	ADJ	ADJ	_	14	amod
13	foreign	_	ADJ	ADJ	_	14	amod
14	visit	_	NOUN	NOUN	_	4	nmod
15	since	_	ADP	ADP	_	17	case
16	pro-restoration	_	NOUN	NOUN	_	17	compound
17	demonstrators	_	NOUN	NOUN	_	14	nmod
18	in	_	ADP	ADP	_	20	case
19	Eymn	_	PROPN	PROPN	_	20	compound
20	Muil	_	PROPN	PROPN	_	17	nmod
21	were	_	AUX	AUX	_	22	aux
22	crushed	_	VERB	VERB	_	0	root
23	last	_	ADJ	ADJ	_	24	amod
24	June	_	PROPN	PROPN	_	22	dobj
25	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test18': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950117'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test18']['sents']['0']:
            print(return_dict['test18']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")@ " + str(return_dict['test18']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")@ noevent  " )
            print("test18 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")@ noeventexception \n " )
        print("test18 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test18']['sents']['0']:
        verbs=return_dict['test18']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test18']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test18']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test18():
    text="""Calenardhon urged Bree on Monday to help win a greater role for 
it in forthcoming peace talks.
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	urged	_	VERB	VERB	_	0	root
3	Bree	_	PROPN	PROPN	_	2	dobj
4	on	_	ADP	ADP	_	5	case
5	Monday	_	PROPN	PROPN	_	2	nmod
6	to	_	PART	PART	_	7	mark
7	help	_	VERB	VERB	_	2	advcl
8	win	_	VERB	VERB	_	7	xcomp
9	a	_	DET	DET	_	11	det
10	greater	_	ADJ	ADJ	_	11	amod
11	role	_	NOUN	NOUN	_	8	dobj
12	for	_	ADP	ADP	_	13	case
13	it	_	PRON	PRON	_	11	nmod
14	in	_	ADP	ADP	_	17	case
15	forthcoming	_	ADJ	ADJ	_	17	amod
16	peace	_	NOUN	NOUN	_	17	compound
17	talks	_	NOUN	NOUN	_	8	nmod
18	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test19': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test19']['sents']['0']:
            print(return_dict['test19']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"102\")@ " + str(return_dict['test19']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"102\")@ noevent  " )
            print("test19 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"102\")@ noeventexception \n " )
        print("test19 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test19']['sents']['0']:
        verbs=return_dict['test19']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test19']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test19']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test19():
    text="""Arnor's foreign minister, in remarks published on Monday, urged 
Eriador to respond to Gondor's proposals on elections.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	nmod:poss
2	's	_	PART	PART	_	1	case
3	foreign	_	ADJ	ADJ	_	4	amod
4	minister	_	NOUN	NOUN	_	8	nsubj
5	,	_	PUNCT	PUNCT	_	8	punct
6	in	_	ADP	ADP	_	7	case
7	remarks	_	NOUN	NOUN	_	8	nmod
8	published	_	VERB	VERB	_	0	root
9	on	_	ADP	ADP	_	10	case
10	Monday	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	urged	_	VERB	VERB	_	8	advcl
13	Eriador	_	PROPN	PROPN	_	12	dobj
14	to	_	PART	PART	_	15	mark
15	respond	_	VERB	VERB	_	12	xcomp
16	to	_	ADP	ADP	_	19	case
17	Gondor	_	PROPN	PROPN	_	19	nmod:poss
18	's	_	PART	PART	_	17	case
19	proposals	_	NOUN	NOUN	_	15	nmod
20	on	_	ADP	ADP	_	21	case
21	elections	_	NOUN	NOUN	_	15	nmod
22	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test20': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950119'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test20']['sents']['0']:
            print(return_dict['test20']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")@ " + str(return_dict['test20']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")@ noevent  " )
            print("test20 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")@ noeventexception \n " )
        print("test20 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test20']['sents']['0']:
        verbs=return_dict['test20']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test20']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test20']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test20():
    text="""Eriador's death toll has risen in the dispute with  Osgiliath, the state's 
fiercest foe. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	4	nmod:poss
2	's	_	PART	PART	_	1	case
3	death	_	NOUN	NOUN	_	4	compound
4	toll	_	NOUN	NOUN	_	6	nsubj
5	has	_	AUX	AUX	_	6	aux
6	risen	_	VERB	VERB	_	0	root
7	in	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	dispute	_	NOUN	NOUN	_	6	nmod
10	with	_	ADP	ADP	_	11	case
11	Osgiliath	_	PROPN	PROPN	_	6	nmod
12	,	_	PUNCT	PUNCT	_	6	punct
13	the	_	DET	DET	_	14	det
14	state	_	NOUN	NOUN	_	17	nmod:poss
15	's	_	PART	PART	_	14	case
16	fiercest	_	ADJ	ADJ	_	17	amod
17	foe	_	NOUN	NOUN	_	6	nmod
18	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test21': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test21']['sents']['0']:
            print(return_dict['test21']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ " + str(return_dict['test21']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ noevent  " )
            print("test21 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ noeventexception \n " )
        print("test21 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test21']['sents']['0']:
        verbs=return_dict['test21']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test21']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test21']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test21():
    text="""Eriador's death and injury toll has risen in the dispute with Osgiliath, the state's 
fiercest foe. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	death	_	NOUN	NOUN	_	8	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	injury	_	NOUN	NOUN	_	6	compound
6	toll	_	NOUN	NOUN	_	3	conj
7	has	_	AUX	AUX	_	8	aux
8	risen	_	VERB	VERB	_	0	root
9	in	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	dispute	_	NOUN	NOUN	_	8	nmod
12	with	_	ADP	ADP	_	13	case
13	Osgiliath	_	PROPN	PROPN	_	11	nmod
14	,	_	PUNCT	PUNCT	_	8	punct
15	the	_	DET	DET	_	16	det
16	state	_	NOUN	NOUN	_	19	nmod:poss
17	's	_	PART	PART	_	16	case
18	fiercest	_	ADJ	ADJ	_	19	amod
19	foe	_	NOUN	NOUN	_	8	nmod
20	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test22': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test22']['sents']['0']:
            print(return_dict['test22']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ " + str(return_dict['test22']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ noevent  " )
            print("test22 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\")@ noeventexception \n " )
        print("test22 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test22']['sents']['0']:
        verbs=return_dict['test22']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test22']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test22']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test22():
    text="""Eriador's death and injury toll has risen in the dispute with Osgiliath, the state's 
fiercest foe. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	death	_	NOUN	NOUN	_	8	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	injury	_	NOUN	NOUN	_	6	compound
6	toll	_	NOUN	NOUN	_	3	conj
7	has	_	AUX	AUX	_	8	aux
8	risen	_	VERB	VERB	_	0	root
9	in	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	dispute	_	NOUN	NOUN	_	8	nmod
12	with	_	ADP	ADP	_	13	case
13	Osgiliath	_	PROPN	PROPN	_	11	nmod
14	,	_	PUNCT	PUNCT	_	8	punct
15	the	_	DET	DET	_	16	det
16	state	_	NOUN	NOUN	_	19	nmod:poss
17	's	_	PART	PART	_	16	case
18	fiercest	_	ADJ	ADJ	_	19	amod
19	foe	_	NOUN	NOUN	_	8	nmod
20	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test23': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\"),(u\"&quot;INJURY TOLL&quot;\", u\"OSG\", u\"223\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test23']['sents']['0']:
            print(return_dict['test23']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\"),(u\"&quot;INJURY TOLL&quot;\", u\"OSG\", u\"223\")@ " + str(return_dict['test23']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\"),(u\"&quot;INJURY TOLL&quot;\", u\"OSG\", u\"223\")@ noevent  " )
            print("test23 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"223\"),(u\"&quot;INJURY TOLL&quot;\", u\"OSG\", u\"223\")@ noeventexception \n " )
        print("test23 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test23']['sents']['0']:
        verbs=return_dict['test23']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test23']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test23']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test23():
    text="""Eriador's death total has risen in the dispute with  Osgiliath, the state's 
fiercest foe. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	death	_	NOUN	NOUN	_	6	nsubj
4	total	_	ADJ	ADJ	_	3	amod
5	has	_	AUX	AUX	_	6	aux
6	risen	_	VERB	VERB	_	0	root
7	in	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	dispute	_	NOUN	NOUN	_	6	nmod
10	with	_	ADP	ADP	_	11	case
11	Osgiliath	_	PROPN	PROPN	_	6	nmod
12	,	_	PUNCT	PUNCT	_	6	punct
13	the	_	DET	DET	_	14	det
14	state	_	NOUN	NOUN	_	17	nmod:poss
15	's	_	PART	PART	_	14	case
16	fiercest	_	ADJ	ADJ	_	17	amod
17	foe	_	NOUN	NOUN	_	6	nmod
18	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test24': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"224\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test24']['sents']['0']:
            print(return_dict['test24']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"224\")@ " + str(return_dict['test24']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"224\")@ noevent  " )
            print("test24 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"224\")@ noeventexception \n " )
        print("test24 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test24']['sents']['0']:
        verbs=return_dict['test24']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test24']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test24']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test24():
    text="""Eriador's death and injury total has risen in the dispute with Osgiliath, the state's 
fiercest foe. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	death	_	NOUN	NOUN	_	8	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	injury	_	NOUN	NOUN	_	6	compound
6	total	_	NOUN	NOUN	_	3	conj
7	has	_	AUX	AUX	_	8	aux
8	risen	_	VERB	VERB	_	0	root
9	in	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	dispute	_	NOUN	NOUN	_	8	nmod
12	with	_	ADP	ADP	_	13	case
13	Osgiliath	_	PROPN	PROPN	_	11	nmod
14	,	_	PUNCT	PUNCT	_	8	punct
15	the	_	DET	DET	_	16	det
16	state	_	NOUN	NOUN	_	19	nmod:poss
17	's	_	PART	PART	_	16	case
18	fiercest	_	ADJ	ADJ	_	19	amod
19	foe	_	NOUN	NOUN	_	8	nmod
20	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test25': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test25']['sents']['0']:
            print(return_dict['test25']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test25']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test25 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test25 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test25']['sents']['0']:
        verbs=return_dict['test25']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test25']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test25']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test25():
    text="""Gondor and Osgiliath have postponed their meeting after a 
hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Gondor	_	PROPN	PROPN	_	5	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Osgiliath	_	PROPN	PROPN	_	1	conj
4	have	_	AUX	AUX	_	5	aux
5	postponed	_	VERB	VERB	_	0	root
6	their	_	PRON	PRON	_	7	nmod:poss
7	meeting	_	NOUN	NOUN	_	5	dobj
8	after	_	ADP	ADP	_	10	case
9	a	_	DET	DET	_	10	det
10	hafling	_	NOUN	NOUN	_	7	nmod
11	was	_	AUX	AUX	_	12	aux
12	reported	_	VERB	VERB	_	5	advcl
13	on	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	pass	_	NOUN	NOUN	_	12	nmod
16	of	_	ADP	ADP	_	18	case
17	Cirith	_	PROPN	PROPN	_	18	compound
18	Ungol	_	PROPN	PROPN	_	15	nmod
19	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test26': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test26']['sents']['0']:
            print(return_dict['test26']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")@ " + str(return_dict['test26']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")@ noevent  " )
            print("test26 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")@ noeventexception \n " )
        print("test26 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test26']['sents']['0']:
        verbs=return_dict['test26']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test26']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test26']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test26():
    text="""Gondor and Osgiliath have delayed their meeting after a 
hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Gondor	_	PROPN	PROPN	_	5	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Osgiliath	_	PROPN	PROPN	_	1	conj
4	have	_	AUX	AUX	_	5	aux
5	delayed	_	VERB	VERB	_	0	root
6	their	_	PRON	PRON	_	7	nmod:poss
7	meeting	_	NOUN	NOUN	_	5	dobj
8	after	_	ADP	ADP	_	10	case
9	a	_	DET	DET	_	10	det
10	hafling	_	NOUN	NOUN	_	7	nmod
11	was	_	AUX	AUX	_	12	aux
12	reported	_	VERB	VERB	_	5	advcl
13	on	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	pass	_	NOUN	NOUN	_	12	nmod
16	of	_	ADP	ADP	_	18	case
17	Cirith	_	PROPN	PROPN	_	18	compound
18	Ungol	_	PROPN	PROPN	_	15	nmod
19	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test27': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test27']['sents']['0']:
            print(return_dict['test27']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ " + str(return_dict['test27']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noevent  " )
            print("test27 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noeventexception \n " )
        print("test27 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test27']['sents']['0']:
        verbs=return_dict['test27']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test27']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test27']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test27():
    text="""Gondor and Osgiliath have downplayed their meeting after a 
hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Gondor	_	PROPN	PROPN	_	5	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Osgiliath	_	PROPN	PROPN	_	1	conj
4	have	_	AUX	AUX	_	5	aux
5	downplayed	_	VERB	VERB	_	0	root
6	their	_	PRON	PRON	_	7	nmod:poss
7	meeting	_	NOUN	NOUN	_	5	dobj
8	after	_	ADP	ADP	_	10	case
9	a	_	DET	DET	_	10	det
10	hafling	_	NOUN	NOUN	_	7	nmod
11	was	_	AUX	AUX	_	12	aux
12	reported	_	VERB	VERB	_	5	advcl
13	on	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	pass	_	NOUN	NOUN	_	12	nmod
16	of	_	ADP	ADP	_	18	case
17	Cirith	_	PROPN	PROPN	_	18	compound
18	Ungol	_	PROPN	PROPN	_	15	nmod
19	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test28': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test28']['sents']['0']:
            print(return_dict['test28']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ " + str(return_dict['test28']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noevent  " )
            print("test28 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noeventexception \n " )
        print("test28 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test28']['sents']['0']:
        verbs=return_dict['test28']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test28']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test28']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test28():
    text="""It has been noted that Gondor and Osgiliath have delayed their meeting after a hafling was reported on the pass
"""
    parse="""1	It	_	PRON	PRON	_	4	nsubj
2	has	_	AUX	AUX	_	4	aux
3	been	_	AUX	AUX	_	4	aux
4	noted	_	VERB	VERB	_	0	root
5	that	_	SCONJ	SCONJ	_	10	mark
6	Gondor	_	PROPN	PROPN	_	10	nsubj
7	and	_	CONJ	CONJ	_	6	cc
8	Osgiliath	_	PROPN	PROPN	_	6	conj
9	have	_	AUX	AUX	_	10	aux
10	delayed	_	VERB	VERB	_	4	ccomp
11	their	_	PRON	PRON	_	12	nmod:poss
12	meeting	_	NOUN	NOUN	_	10	dobj
13	after	_	ADP	ADP	_	15	case
14	a	_	DET	DET	_	15	det
15	hafling	_	NOUN	NOUN	_	10	nmod
16	was	_	AUX	AUX	_	17	aux
17	reported	_	VERB	VERB	_	15	acl:relcl
18	on	_	ADP	ADP	_	20	case
19	the	_	DET	DET	_	20	det
20	pass	_	NOUN	NOUN	_	17	nmod
21	of	_	ADP	ADP	_	23	case
22	Cirith	_	PROPN	PROPN	_	23	compound
23	Ungol	_	PROPN	PROPN	_	20	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test29': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test29']['sents']['0']:
            print(return_dict['test29']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ " + str(return_dict['test29']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noevent  " )
            print("test29 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")@ noeventexception \n " )
        print("test29 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test29']['sents']['0']:
        verbs=return_dict['test29']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test29']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test29']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test29():
    text="""Soldiers from Gondor have cordoned off the roads leading into Mordor along the pass 
of Cirith Ungol.
"""
    parse="""1	Soldiers	_	NOUN	NOUN	_	5	nsubj
2	from	_	ADP	ADP	_	3	case
3	Gondor	_	PROPN	PROPN	_	1	nmod
4	have	_	AUX	AUX	_	5	aux
5	cordoned	_	VERB	VERB	_	0	root
6	off	_	ADP	ADP	_	8	case
7	the	_	DET	DET	_	8	det
8	roads	_	NOUN	NOUN	_	5	nmod
9	leading	_	VERB	VERB	_	8	acl
10	into	_	ADP	ADP	_	11	case
11	Mordor	_	PROPN	PROPN	_	9	nmod
12	along	_	ADP	ADP	_	14	case
13	the	_	DET	DET	_	14	det
14	pass	_	NOUN	NOUN	_	9	nmod
15	of	_	ADP	ADP	_	17	case
16	Cirith	_	PROPN	PROPN	_	17	compound
17	Ungol	_	PROPN	PROPN	_	14	nmod
18	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test30': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1721\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test30']['sents']['0']:
            print(return_dict['test30']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1721\")@ " + str(return_dict['test30']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1721\")@ noevent  " )
            print("test30 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1721\")@ noeventexception \n " )
        print("test30 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test30']['sents']['0']:
        verbs=return_dict['test30']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test30']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test30']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test30():
    text="""Soldiers from Gondor wire tapped all communication links leading into Mordor along the 
pass of Cirith Ungol.
"""
    parse="""1	Soldiers	_	NOUN	NOUN	_	5	nsubj
2	from	_	ADP	ADP	_	4	case
3	Gondor	_	PROPN	PROPN	_	4	compound
4	wire	_	NOUN	NOUN	_	1	nmod
5	tapped	_	VERB	VERB	_	0	root
6	all	_	DET	DET	_	8	det
7	communication	_	NOUN	NOUN	_	8	compound
8	links	_	NOUN	NOUN	_	5	dobj
9	leading	_	VERB	VERB	_	8	acl
10	into	_	ADP	ADP	_	11	case
11	Mordor	_	PROPN	PROPN	_	9	nmod
12	along	_	ADP	ADP	_	14	case
13	the	_	DET	DET	_	14	det
14	pass	_	NOUN	NOUN	_	9	nmod
15	of	_	ADP	ADP	_	17	case
16	Cirith	_	PROPN	PROPN	_	17	compound
17	Ungol	_	PROPN	PROPN	_	14	nmod
18	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test31': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1711\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test31']['sents']['0']:
            print(return_dict['test31']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1711\")@ " + str(return_dict['test31']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1711\")@ noevent  " )
            print("test31 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"1711\")@ noeventexception \n " )
        print("test31 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test31']['sents']['0']:
        verbs=return_dict['test31']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test31']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test31']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test31():
    text="""Soldiers from Gondor will not wire tap the communication links leading into Mordor along  
the pass of Cirith Ungol.
"""
    parse="""1	Soldiers	_	NOUN	NOUN	_	0	root
2	from	_	ADP	ADP	_	7	case
3	Gondor	_	PROPN	PROPN	_	7	nmod:poss
4	will	_	AUX	AUX	_	7	aux
5	not	_	PART	PART	_	7	neg
6	wire	_	NOUN	NOUN	_	7	compound
7	tap	_	NOUN	NOUN	_	1	nmod
8	the	_	DET	DET	_	10	det
9	communication	_	NOUN	NOUN	_	10	compound
10	links	_	NOUN	NOUN	_	11	nsubj
11	leading	_	VERB	VERB	_	7	acl:relcl
12	into	_	ADP	ADP	_	13	case
13	Mordor	_	PROPN	PROPN	_	11	nmod
14	along	_	ADP	ADP	_	16	case
15	the	_	DET	DET	_	16	det
16	pass	_	NOUN	NOUN	_	11	nmod
17	of	_	ADP	ADP	_	19	case
18	Cirith	_	PROPN	PROPN	_	19	compound
19	Ungol	_	PROPN	PROPN	_	16	nmod
20	.	_	PUNCT	PUNCT	_	1	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test32': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"081\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test32']['sents']['0']:
            print(return_dict['test32']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"081\")@ " + str(return_dict['test32']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"081\")@ noevent  " )
            print("test32 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"081\")@ noeventexception \n " )
        print("test32 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test32']['sents']['0']:
        verbs=return_dict['test32']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test32']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test32']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test32():
    text="""Soldiers from Gondor have cordoned off for construction the roads leading into Mordor 
along the pass of Cirith Ungol.
"""
    parse="""1	Soldiers	_	NOUN	NOUN	_	5	nsubj
2	from	_	ADP	ADP	_	3	case
3	Gondor	_	PROPN	PROPN	_	1	nmod
4	have	_	AUX	AUX	_	5	aux
5	cordoned	_	VERB	VERB	_	0	root
6	off	_	ADP	ADP	_	5	compound:prt
7	for	_	ADP	ADP	_	8	case
8	construction	_	NOUN	NOUN	_	5	nmod
9	the	_	DET	DET	_	10	det
10	roads	_	NOUN	NOUN	_	11	nsubj
11	leading	_	VERB	VERB	_	8	acl
12	into	_	ADP	ADP	_	13	case
13	Mordor	_	PROPN	PROPN	_	11	nmod
14	along	_	ADP	ADP	_	16	case
15	the	_	DET	DET	_	16	det
16	pass	_	NOUN	NOUN	_	11	nmod
17	of	_	ADP	ADP	_	19	case
18	Cirith	_	PROPN	PROPN	_	19	compound
19	Ungol	_	PROPN	PROPN	_	16	nmod
20	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test33': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"071\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test33']['sents']['0']:
            print(return_dict['test33']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"071\")@ " + str(return_dict['test33']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"071\")@ noevent  " )
            print("test33 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GONMIL\", u\"MOR\", u\"071\")@ noeventexception \n " )
        print("test33 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test33']['sents']['0']:
        verbs=return_dict['test33']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test33']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test33']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test33():
    text="""Arnor cleric is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	compound
2	cleric	_	NOUN	NOUN	_	3	nsubj
3	is	_	VERB	VERB	_	0	root
4	about	_	ADV	ADV	_	6	advmod
5	to	_	PART	PART	_	6	mark
6	restore	_	VERB	VERB	_	3	advcl
7	full	_	ADJ	ADJ	_	9	amod
8	diplomatic	_	ADJ	ADJ	_	9	amod
9	ties	_	NOUN	NOUN	_	6	dobj
10	with	_	ADP	ADP	_	11	case
11	Gondor	_	PROPN	PROPN	_	9	nmod
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	16	nmod:npmod
15	after	_	ADP	ADP	_	16	case
16	crowds	_	NOUN	NOUN	_	6	nmod
17	trashed	_	VERB	VERB	_	16	acl
18	its	_	PRON	PRON	_	19	nmod:poss
19	embassy	_	NOUN	NOUN	_	17	dobj
20	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test34': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNREL\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test34']['sents']['0']:
            print(return_dict['test34']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNREL\", u\"GON\", u\"064\")@ " + str(return_dict['test34']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNREL\", u\"GON\", u\"064\")@ noevent  " )
            print("test34 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNREL\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test34 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test34']['sents']['0']:
        verbs=return_dict['test34']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test34']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test34']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test34():
    text="""MSF Arnor is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy.
"""
    parse="""1	MSF	_	PROPN	PROPN	_	2	compound
2	Arnor	_	PROPN	PROPN	_	3	nsubj
3	is	_	VERB	VERB	_	0	root
4	about	_	ADV	ADV	_	6	advmod
5	to	_	PART	PART	_	6	mark
6	restore	_	VERB	VERB	_	3	advcl
7	full	_	ADJ	ADJ	_	9	amod
8	diplomatic	_	ADJ	ADJ	_	9	amod
9	ties	_	NOUN	NOUN	_	6	dobj
10	with	_	ADP	ADP	_	11	case
11	Gondor	_	PROPN	PROPN	_	9	nmod
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	16	nmod:npmod
15	after	_	ADP	ADP	_	16	case
16	crowds	_	NOUN	NOUN	_	6	nmod
17	trashed	_	VERB	VERB	_	16	acl
18	its	_	PRON	PRON	_	19	nmod:poss
19	embassy	_	NOUN	NOUN	_	17	dobj
20	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test35': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test35']['sents']['0']:
            print(return_dict['test35']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARN\", u\"GON\", u\"064\")@ " + str(return_dict['test35']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test35 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test35 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test35']['sents']['0']:
        verbs=return_dict['test35']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test35']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test35']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test35():
    text="""An MSF Arnor diplomat is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy.
"""
    parse="""1	An	_	DET	DET	_	4	det
2	MSF	_	PROPN	PROPN	_	3	compound
3	Arnor	_	PROPN	PROPN	_	4	compound
4	diplomat	_	NOUN	NOUN	_	5	nsubj
5	is	_	VERB	VERB	_	0	root
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	almost	_	ADV	ADV	_	15	advmod
15	five	_	NUM	NUM	_	16	nummod
16	years	_	NOUN	NOUN	_	18	nmod:npmod
17	after	_	ADP	ADP	_	18	case
18	crowds	_	NOUN	NOUN	_	8	nmod
19	trashed	_	VERB	VERB	_	18	acl
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	19	dobj
22	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test36': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARNGOV\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test36']['sents']['0']:
            print(return_dict['test36']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARNGOV\", u\"GON\", u\"064\")@ " + str(return_dict['test36']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARNGOV\", u\"GON\", u\"064\")@ noevent  " )
            print("test36 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGOARNGOV\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test36 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test36']['sents']['0']:
        verbs=return_dict['test36']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test36']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test36']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test36():
    text="""Arnor is about to restore full diplomatic ties with the Gondor main opposition group 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	14	case
10	the	_	DET	DET	_	14	det
11	Gondor	_	PROPN	PROPN	_	14	compound
12	main	_	ADJ	ADJ	_	13	amod
13	opposition	_	NOUN	NOUN	_	14	compound
14	group	_	NOUN	NOUN	_	8	nmod
15	almost	_	ADV	ADV	_	16	advmod
16	five	_	NUM	NUM	_	17	nummod
17	years	_	NOUN	NOUN	_	19	nmod:npmod
18	after	_	ADP	ADP	_	19	case
19	crowds	_	NOUN	NOUN	_	5	nmod
20	trashed	_	VERB	VERB	_	19	acl
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	20	dobj
23	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test37': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test37']['sents']['0']:
            print(return_dict['test37']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ " + str(return_dict['test37']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noevent  " )
            print("test37 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noeventexception \n " )
        print("test37 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test37']['sents']['0']:
        verbs=return_dict['test37']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test37']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test37']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test37():
    text="""Arnor is about to restore full diplomatic ties with Gondor's government 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	12	case
10	Gondor	_	PROPN	PROPN	_	12	nmod:poss
11	's	_	PART	PART	_	10	case
12	government	_	NOUN	NOUN	_	8	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	five	_	NUM	NUM	_	15	nummod
15	years	_	NOUN	NOUN	_	17	nmod:npmod
16	after	_	ADP	ADP	_	17	case
17	crowds	_	NOUN	NOUN	_	5	nmod
18	trashed	_	VERB	VERB	_	17	acl
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	18	dobj
21	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test38': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGOV\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test38']['sents']['0']:
            print(return_dict['test38']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGOV\", u\"064\")@ " + str(return_dict['test38']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGOV\", u\"064\")@ noevent  " )
            print("test38 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGOV\", u\"064\")@ noeventexception \n " )
        print("test38 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test38']['sents']['0']:
        verbs=return_dict['test38']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test38']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test38']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test38():
    text="""Arnor is about to restore full diplomatic ties with Gondor's main opposition group 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	14	case
10	Gondor	_	PROPN	PROPN	_	14	nmod:poss
11	's	_	PART	PART	_	10	case
12	main	_	ADJ	ADJ	_	14	amod
13	opposition	_	NOUN	NOUN	_	14	compound
14	group	_	NOUN	NOUN	_	8	nmod
15	almost	_	ADV	ADV	_	16	advmod
16	five	_	NUM	NUM	_	17	nummod
17	years	_	NOUN	NOUN	_	19	nmod:npmod
18	after	_	ADP	ADP	_	19	case
19	crowds	_	NOUN	NOUN	_	5	nmod
20	trashed	_	VERB	VERB	_	19	acl
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	20	dobj
23	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test39': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test39']['sents']['0']:
            print(return_dict['test39']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ " + str(return_dict['test39']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noevent  " )
            print("test39 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noeventexception \n " )
        print("test39 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test39']['sents']['0']:
        verbs=return_dict['test39']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test39']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test39']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test39():
    text="""Human rights activists in Arnor are about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy.
"""
    parse="""1	Human	_	ADJ	ADJ	_	3	amod
2	rights	_	NOUN	NOUN	_	3	compound
3	activists	_	NOUN	NOUN	_	0	root
4	in	_	ADP	ADP	_	5	case
5	Arnor	_	PROPN	PROPN	_	3	nmod
6	are	_	VERB	VERB	_	3	acl
7	about	_	ADV	ADV	_	9	advmod
8	to	_	PART	PART	_	9	mark
9	restore	_	VERB	VERB	_	6	advcl
10	full	_	ADJ	ADJ	_	12	amod
11	diplomatic	_	ADJ	ADJ	_	12	amod
12	ties	_	NOUN	NOUN	_	9	dobj
13	with	_	ADP	ADP	_	14	case
14	Gondor	_	PROPN	PROPN	_	12	nmod
15	almost	_	ADV	ADV	_	16	advmod
16	five	_	NUM	NUM	_	17	nummod
17	years	_	NOUN	NOUN	_	19	nmod:npmod
18	after	_	ADP	ADP	_	19	case
19	crowds	_	NOUN	NOUN	_	9	nmod
20	trashed	_	VERB	VERB	_	19	acl
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	20	dobj
23	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test40': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNOPP\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test40']['sents']['0']:
            print(return_dict['test40']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNOPP\", u\"GON\", u\"064\")@ " + str(return_dict['test40']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNOPP\", u\"GON\", u\"064\")@ noevent  " )
            print("test40 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNOPP\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test40 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test40']['sents']['0']:
        verbs=return_dict['test40']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test40']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test40']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test40():
    text="""Arnor is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test41': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test41']['sents']['0']:
            print(return_dict['test41']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")@ " + str(return_dict['test41']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")@ noevent  " )
            print("test41 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")@ noeventexception \n " )
        print("test41 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test41']['sents']['0']:
        verbs=return_dict['test41']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test41']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test41']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test41():
    text="""The Calenardhon government condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	condemned	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test42': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test42']['sents']['0']:
            print(return_dict['test42']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ " + str(return_dict['test42']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noevent  " )
            print("test42 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noeventexception \n " )
        print("test42 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test42']['sents']['0']:
        verbs=return_dict['test42']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test42']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test42']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test42():
    text="""Arnor security officials are about to restore full diplomatic 
ties with Gondor police. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	compound
2	security	_	NOUN	NOUN	_	3	compound
3	officials	_	NOUN	NOUN	_	0	root
4	are	_	VERB	VERB	_	3	acl
5	about	_	ADV	ADV	_	7	advmod
6	to	_	PART	PART	_	7	mark
7	restore	_	VERB	VERB	_	4	advcl
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	7	dobj
11	with	_	ADP	ADP	_	13	case
12	Gondor	_	PROPN	PROPN	_	13	compound
13	police	_	NOUN	NOUN	_	10	nmod
14	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test43': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"GONCOP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test43']['sents']['0']:
            print(return_dict['test43']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"GONCOP\", u\"064\")@ " + str(return_dict['test43']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"GONCOP\", u\"064\")@ noevent  " )
            print("test43 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"GONCOP\", u\"064\")@ noeventexception \n " )
        print("test43 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test43']['sents']['0']:
        verbs=return_dict['test43']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test43']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test43']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test43():
    text="""White House security officials are about to restore full diplomatic 
ties with Minas Tirith border police. 
"""
    parse="""1	White	_	PROPN	PROPN	_	2	compound
2	House	_	PROPN	PROPN	_	0	root
3	security	_	NOUN	NOUN	_	4	compound
4	officials	_	NOUN	NOUN	_	2	list
5	are	_	VERB	VERB	_	2	acl
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	16	case
13	Minas	_	PROPN	PROPN	_	14	compound
14	Tirith	_	PROPN	PROPN	_	16	compound
15	border	_	NOUN	NOUN	_	16	compound
16	police	_	NOUN	NOUN	_	11	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test44': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GONCOP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test44']['sents']['0']:
            print(return_dict['test44']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GONCOP\", u\"064\")@ " + str(return_dict['test44']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GONCOP\", u\"064\")@ noevent  " )
            print("test44 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GONCOP\", u\"064\")@ noeventexception \n " )
        print("test44 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test44']['sents']['0']:
        verbs=return_dict['test44']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test44']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test44']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test44():
    text="""The Calenardhon government condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	condemned	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test45': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test45']['sents']['0']:
            print(return_dict['test45']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ " + str(return_dict['test45']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ noevent  " )
            print("test45 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ noeventexception \n " )
        print("test45 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test45']['sents']['0']:
        verbs=return_dict['test45']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test45']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test45']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test45():
    text="""The Calenardhon government condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	condemned	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test46': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test46']['sents']['0']:
            print(return_dict['test46']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ " + str(return_dict['test46']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ noevent  " )
            print("test46 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALLEG\", u\"OSGMIL\", u\"122\")@ noeventexception \n " )
        print("test46 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test46']['sents']['0']:
        verbs=return_dict['test46']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test46']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test46']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test46():
    text="""The Calenardhon Ministry of Silly Walks condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	Ministry	_	PROPN	PROPN	_	6	nsubj
4	of	_	ADP	ADP	_	5	case
5	Silly	_	PROPN	PROPN	_	3	nmod
6	Walks	_	VERB	VERB	_	0	root
7	condemned	_	VERB	VERB	_	6	xcomp
8	an	_	DET	DET	_	9	det
9	attack	_	NOUN	NOUN	_	7	dobj
10	by	_	ADP	ADP	_	12	case
11	Osgiliath	_	PROPN	PROPN	_	12	compound
12	soldiers	_	NOUN	NOUN	_	9	nmod
13	in	_	ADP	ADP	_	15	case
14	south	_	ADJ	ADJ	_	15	amod
15	Ithilen	_	PROPN	PROPN	_	9	nmod
16	on	_	ADP	ADP	_	17	case
17	Thursday	_	PROPN	PROPN	_	7	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test47': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test47']['sents']['0']:
            print(return_dict['test47']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ " + str(return_dict['test47']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noevent  " )
            print("test47 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noeventexception \n " )
        print("test47 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test47']['sents']['0']:
        verbs=return_dict['test47']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test47']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test47']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test47():
    text="""The Calenardhon Minister of Silly Walks condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	6	nsubj
4	of	_	ADP	ADP	_	5	case
5	Silly	_	PROPN	PROPN	_	3	nmod
6	Walks	_	VERB	VERB	_	0	root
7	condemned	_	VERB	VERB	_	6	xcomp
8	an	_	DET	DET	_	9	det
9	attack	_	NOUN	NOUN	_	7	dobj
10	by	_	ADP	ADP	_	12	case
11	Osgiliath	_	PROPN	PROPN	_	12	compound
12	soldiers	_	NOUN	NOUN	_	9	nmod
13	in	_	ADP	ADP	_	15	case
14	south	_	ADJ	ADJ	_	15	amod
15	Ithilen	_	PROPN	PROPN	_	9	nmod
16	on	_	ADP	ADP	_	17	case
17	Thursday	_	PROPN	PROPN	_	7	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test48': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test48']['sents']['0']:
            print(return_dict['test48']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ " + str(return_dict['test48']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noevent  " )
            print("test48 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\")@ noeventexception \n " )
        print("test48 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test48']['sents']['0']:
        verbs=return_dict['test48']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test48']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test48']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test48():
    text="""The human rights activists of Amnesty International are about to restore 
full diplomatic ties with Gondor. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	human	_	ADJ	ADJ	_	4	amod
3	rights	_	NOUN	NOUN	_	4	compound
4	activists	_	NOUN	NOUN	_	0	root
5	of	_	ADP	ADP	_	7	case
6	Amnesty	_	PROPN	PROPN	_	7	compound
7	International	_	PROPN	PROPN	_	4	nmod
8	are	_	VERB	VERB	_	4	acl
9	about	_	ADV	ADV	_	11	advmod
10	to	_	PART	PART	_	11	mark
11	restore	_	VERB	VERB	_	8	advcl
12	full	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	11	dobj
15	with	_	ADP	ADP	_	16	case
16	Gondor	_	PROPN	PROPN	_	14	nmod
17	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test49': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGMOPP\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test49']['sents']['0']:
            print(return_dict['test49']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGMOPP\", u\"GON\", u\"064\")@ " + str(return_dict['test49']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGMOPP\", u\"GON\", u\"064\")@ noevent  " )
            print("test49 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"NGMOPP\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test49 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test49']['sents']['0']:
        verbs=return_dict['test49']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test49']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test49']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test49():
    text="""Washington security officials are about to restore full diplomatic 
ties with Gondor. 
"""
    parse="""1	Washington	_	PROPN	PROPN	_	3	compound
2	security	_	NOUN	NOUN	_	3	compound
3	officials	_	NOUN	NOUN	_	0	root
4	are	_	VERB	VERB	_	3	acl
5	about	_	ADV	ADV	_	7	advmod
6	to	_	PART	PART	_	7	mark
7	restore	_	VERB	VERB	_	4	advcl
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	7	dobj
11	with	_	ADP	ADP	_	12	case
12	Gondor	_	PROPN	PROPN	_	10	nmod
13	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test50': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test50']['sents']['0']:
            print(return_dict['test50']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ " + str(return_dict['test50']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ noevent  " )
            print("test50 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test50 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test50']['sents']['0']:
        verbs=return_dict['test50']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test50']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test50']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test50():
    text="""White House security officials are about to restore full diplomatic 
ties with Gondor. 
"""
    parse="""1	White	_	PROPN	PROPN	_	2	compound
2	House	_	PROPN	PROPN	_	0	root
3	security	_	NOUN	NOUN	_	4	compound
4	officials	_	NOUN	NOUN	_	2	list
5	are	_	VERB	VERB	_	2	acl
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test51': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test51']['sents']['0']:
            print(return_dict['test51']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ " + str(return_dict['test51']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ noevent  " )
            print("test51 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test51 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test51']['sents']['0']:
        verbs=return_dict['test51']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test51']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test51']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test51():
    text="""The Quibbler government newspaper is about to restore full diplomatic 
ties with Gondor now. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	Quibbler	_	PROPN	PROPN	_	4	compound
3	government	_	NOUN	NOUN	_	4	compound
4	newspaper	_	NOUN	NOUN	_	5	nsubj
5	is	_	VERB	VERB	_	0	root
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	now	_	ADV	ADV	_	8	advmod
15	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test52': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HGWGOVMED\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test52']['sents']['0']:
            print(return_dict['test52']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HGWGOVMED\", u\"GON\", u\"064\")@ " + str(return_dict['test52']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HGWGOVMED\", u\"GON\", u\"064\")@ noevent  " )
            print("test52 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HGWGOVMED\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test52 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test52']['sents']['0']:
        verbs=return_dict['test52']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test52']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test52']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test52():
    text="""Arnor is about to restore full diplomatic ties with Gondor's main opposition groups 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	14	case
10	Gondor	_	PROPN	PROPN	_	14	nmod:poss
11	's	_	PART	PART	_	10	case
12	main	_	ADJ	ADJ	_	14	amod
13	opposition	_	NOUN	NOUN	_	14	compound
14	groups	_	NOUN	NOUN	_	8	nmod
15	almost	_	ADV	ADV	_	16	advmod
16	five	_	NUM	NUM	_	17	nummod
17	years	_	NOUN	NOUN	_	5	nmod
18	after	_	ADP	ADP	_	19	case
19	crowds	_	NOUN	NOUN	_	17	nmod
20	trashed	_	VERB	VERB	_	19	acl
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	20	dobj
23	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test53': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test53']['sents']['0']:
            print(return_dict['test53']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ " + str(return_dict['test53']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noevent  " )
            print("test53 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONMOP\", u\"064\")@ noeventexception \n " )
        print("test53 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test53']['sents']['0']:
        verbs=return_dict['test53']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test53']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test53']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test53():
    text="""Arnor is about to restore full diplomatic ties with Gondor's golden geese 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	13	case
10	Gondor	_	PROPN	PROPN	_	13	nmod:poss
11	's	_	PART	PART	_	10	case
12	golden	_	ADJ	ADJ	_	13	amod
13	geese	_	NOUN	NOUN	_	8	nmod
14	almost	_	ADV	ADV	_	15	advmod
15	five	_	NUM	NUM	_	16	nummod
16	years	_	NOUN	NOUN	_	18	nmod:npmod
17	after	_	ADP	ADP	_	18	case
18	crowds	_	NOUN	NOUN	_	5	nmod
19	trashed	_	VERB	VERB	_	18	acl
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	19	dobj
22	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test54': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGGS\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test54']['sents']['0']:
            print(return_dict['test54']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGGS\", u\"064\")@ " + str(return_dict['test54']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGGS\", u\"064\")@ noevent  " )
            print("test54 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GONGGS\", u\"064\")@ noeventexception \n " )
        print("test54 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test54']['sents']['0']:
        verbs=return_dict['test54']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test54']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test54']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test54():
    text="""Arnor is about to restore full diplomatic ties with Gondor's polices 
almost five years after crowds trashed its embassy.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	12	case
10	Gondor	_	PROPN	PROPN	_	12	nmod:poss
11	's	_	PART	PART	_	10	case
12	polices	_	NOUN	NOUN	_	8	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	five	_	NUM	NUM	_	15	nummod
15	years	_	NOUN	NOUN	_	5	nmod
16	after	_	ADP	ADP	_	17	case
17	crowds	_	NOUN	NOUN	_	15	nmod
18	trashed	_	VERB	VERB	_	17	acl
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	18	dobj
21	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test55': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test55']['sents']['0']:
            print(return_dict['test55']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test55']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test55 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test55 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test55']['sents']['0']:
        verbs=return_dict['test55']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test55']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test55']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test55():
    text="""West German world government activists are about to restore 
full diplomatic ties with human rights activists of Gonzo GMO. 
"""
    parse="""1	West	_	ADV	ADV	_	2	advmod
2	German	_	ADJ	ADJ	_	5	amod
3	world	_	NOUN	NOUN	_	5	compound
4	government	_	NOUN	NOUN	_	5	compound
5	activists	_	NOUN	NOUN	_	0	root
6	are	_	VERB	VERB	_	5	acl
7	about	_	ADV	ADV	_	9	advmod
8	to	_	PART	PART	_	9	mark
9	restore	_	VERB	VERB	_	6	advcl
10	full	_	ADJ	ADJ	_	12	amod
11	diplomatic	_	ADJ	ADJ	_	12	amod
12	ties	_	NOUN	NOUN	_	9	dobj
13	with	_	ADP	ADP	_	16	case
14	human	_	ADJ	ADJ	_	16	amod
15	rights	_	NOUN	NOUN	_	16	compound
16	activists	_	NOUN	NOUN	_	12	nmod
17	of	_	ADP	ADP	_	19	case
18	Gonzo	_	PROPN	PROPN	_	19	compound
19	GMO	_	PROPN	PROPN	_	16	nmod
20	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test56': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test56']['sents']['0']:
            print(return_dict['test56']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")@ " + str(return_dict['test56']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")@ noevent  " )
            print("test56 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")@ noeventexception \n " )
        print("test56 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test56']['sents']['0']:
        verbs=return_dict['test56']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test56']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test56']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test56():
    text="""White House security officials are about to restore full diplomatic 
ties with Gondor and Arnor. 
"""
    parse="""1	White	_	PROPN	PROPN	_	2	compound
2	House	_	PROPN	PROPN	_	0	root
3	security	_	NOUN	NOUN	_	4	compound
4	officials	_	NOUN	NOUN	_	2	list
5	are	_	VERB	VERB	_	2	acl
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	and	_	CONJ	CONJ	_	13	cc
15	Arnor	_	PROPN	PROPN	_	13	conj
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test57': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test57']['sents']['0']:
            print(return_dict['test57']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ " + str(return_dict['test57']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ noevent  " )
            print("test57 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ noeventexception \n " )
        print("test57 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test57']['sents']['0']:
        verbs=return_dict['test57']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test57']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test57']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test57():
    text="""Arnor former security officials are about to restore full diplomatic 
ties with former Gondor prosecutors. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	compound
2	former	_	ADJ	ADJ	_	4	amod
3	security	_	NOUN	NOUN	_	4	compound
4	officials	_	NOUN	NOUN	_	0	root
5	are	_	VERB	VERB	_	4	acl
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	15	case
13	former	_	ADJ	ADJ	_	15	amod
14	Gondor	_	PROPN	PROPN	_	15	compound
15	prosecutors	_	NOUN	NOUN	_	11	nmod
16	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test58': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNELI\", u\"GONELI\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test58']['sents']['0']:
            print(return_dict['test58']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNELI\", u\"GONELI\", u\"064\")@ " + str(return_dict['test58']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNELI\", u\"GONELI\", u\"064\")@ noevent  " )
            print("test58 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNELI\", u\"GONELI\", u\"064\")@ noeventexception \n " )
        print("test58 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test58']['sents']['0']:
        verbs=return_dict['test58']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test58']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test58']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test58():
    text="""Former security officials in White House are about to restore full 
diplomatic ties with former Minas Tirith border police. 
"""
    parse="""1	Former	_	ADJ	ADJ	_	3	amod
2	security	_	NOUN	NOUN	_	3	compound
3	officials	_	NOUN	NOUN	_	0	root
4	in	_	ADP	ADP	_	6	case
5	White	_	PROPN	PROPN	_	6	compound
6	House	_	PROPN	PROPN	_	3	nmod
7	are	_	VERB	VERB	_	3	acl
8	about	_	ADV	ADV	_	10	advmod
9	to	_	PART	PART	_	10	mark
10	restore	_	VERB	VERB	_	7	advcl
11	full	_	ADJ	ADJ	_	13	amod
12	diplomatic	_	ADJ	ADJ	_	13	amod
13	ties	_	NOUN	NOUN	_	10	dobj
14	with	_	ADP	ADP	_	19	case
15	former	_	ADJ	ADJ	_	19	amod
16	Minas	_	PROPN	PROPN	_	17	compound
17	Tirith	_	PROPN	PROPN	_	19	compound
18	border	_	NOUN	NOUN	_	19	compound
19	police	_	NOUN	NOUN	_	13	nmod
20	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test59': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOVELI\", u\"GONELI\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test59']['sents']['0']:
            print(return_dict['test59']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOVELI\", u\"GONELI\", u\"064\")@ " + str(return_dict['test59']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOVELI\", u\"GONELI\", u\"064\")@ noevent  " )
            print("test59 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOVELI\", u\"GONELI\", u\"064\")@ noeventexception \n " )
        print("test59 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test59']['sents']['0']:
        verbs=return_dict['test59']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test59']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test59']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test59():
    text="""Old foes Gondor and Osgiliath have renewed diplomatic ties after a 
12-year break in a step that holds advantages for both major 
powers. 
"""
    parse="""1	Old	_	ADJ	ADJ	_	2	amod
2	foes	_	NOUN	NOUN	_	0	root
3	Gondor	_	PROPN	PROPN	_	7	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	Osgiliath	_	PROPN	PROPN	_	3	conj
6	have	_	AUX	AUX	_	7	aux
7	renewed	_	VERB	VERB	_	2	acl:relcl
8	diplomatic	_	ADJ	ADJ	_	9	amod
9	ties	_	NOUN	NOUN	_	7	dobj
10	after	_	ADP	ADP	_	13	case
11	a	_	DET	DET	_	13	det
12	12-year	_	NUM	NUM	_	13	nummod
13	break	_	NOUN	NOUN	_	7	nmod
14	in	_	ADP	ADP	_	16	case
15	a	_	DET	DET	_	16	det
16	step	_	NOUN	NOUN	_	13	nmod
17	that	_	PRON	PRON	_	18	nsubj
18	holds	_	VERB	VERB	_	16	acl:relcl
19	advantages	_	NOUN	NOUN	_	18	dobj
20	for	_	ADP	ADP	_	23	case
21	both	_	DET	DET	_	23	det
22	major	_	ADJ	ADJ	_	23	amod
23	powers	_	NOUN	NOUN	_	18	nmod
24	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test60': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test60']['sents']['0']:
            print(return_dict['test60']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")@ " + str(return_dict['test60']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")@ noevent  " )
            print("test60 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test60 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test60']['sents']['0']:
        verbs=return_dict['test60']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test60']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test60']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test60():
    text="""Mordor, Rohan, Fornost and Bree welcomed their resumption of formal 
diplomatic ties with Osgiliath after a 12-year rift. 
"""
    parse="""1	Mordor	_	PROPN	PROPN	_	8	vocative
2	,	_	PUNCT	PUNCT	_	1	punct
3	Rohan	_	PROPN	PROPN	_	1	conj
4	,	_	PUNCT	PUNCT	_	1	punct
5	Fornost	_	PROPN	PROPN	_	1	conj
6	and	_	CONJ	CONJ	_	1	cc
7	Bree	_	PROPN	PROPN	_	1	conj
8	welcomed	_	VERB	VERB	_	0	root
9	their	_	PRON	PRON	_	10	nmod:poss
10	resumption	_	NOUN	NOUN	_	8	dobj
11	of	_	ADP	ADP	_	14	case
12	formal	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	10	nmod
15	with	_	ADP	ADP	_	16	case
16	Osgiliath	_	PROPN	PROPN	_	14	nmod
17	after	_	ADP	ADP	_	20	case
18	a	_	DET	DET	_	20	det
19	12-year	_	NUM	NUM	_	20	nummod
20	rift	_	NOUN	NOUN	_	8	nmod
21	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test61': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test61']['sents']['0']:
            print(return_dict['test61']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ " + str(return_dict['test61']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noevent  " )
            print("test61 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test61 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test61']['sents']['0']:
        verbs=return_dict['test61']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test61']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test61']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test61():
    text="""Fornost and Gondor welcome a resumption of formal diplomatic ties with  
Osgiliath after a 12-year rift, the primary official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	24	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Gondor	_	PROPN	PROPN	_	1	conj
4	welcome	_	INTJ	INTJ	_	6	discourse
5	a	_	DET	DET	_	6	det
6	resumption	_	NOUN	NOUN	_	1	conj
7	of	_	ADP	ADP	_	10	case
8	formal	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	6	nmod
11	with	_	ADP	ADP	_	12	case
12	Osgiliath	_	PROPN	PROPN	_	10	nmod
13	after	_	ADP	ADP	_	16	case
14	a	_	DET	DET	_	16	det
15	12-year	_	NUM	NUM	_	16	nummod
16	rift	_	NOUN	NOUN	_	6	nmod
17	,	_	PUNCT	PUNCT	_	24	punct
18	the	_	DET	DET	_	22	det
19	primary	_	ADJ	ADJ	_	22	amod
20	official	_	ADJ	ADJ	_	22	amod
21	news	_	NOUN	NOUN	_	22	compound
22	agency	_	NOUN	NOUN	_	16	appos
23	WFNA	_	PROPN	PROPN	_	24	nsubj
24	said	_	VERB	VERB	_	0	root
25	on	_	ADP	ADP	_	26	case
26	Thursday	_	PROPN	PROPN	_	24	nmod
27	.	_	PUNCT	PUNCT	_	24	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test62': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test62']['sents']['0']:
            print(return_dict['test62']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test62']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test62 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test62 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test62']['sents']['0']:
        verbs=return_dict['test62']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test62']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test62']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test62():
    text="""Fornost welcomed a resumption of formal diplomatic ties between Gondor 
and Osgiliath after a 12-year rift, the primary official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	a	_	DET	DET	_	4	det
4	resumption	_	NOUN	NOUN	_	2	dobj
5	of	_	ADP	ADP	_	8	case
6	formal	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	4	nmod
9	between	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	and	_	CONJ	CONJ	_	10	cc
12	Osgiliath	_	PROPN	PROPN	_	10	conj
13	after	_	ADP	ADP	_	16	case
14	a	_	DET	DET	_	16	det
15	12-year	_	NUM	NUM	_	16	nummod
16	rift	_	NOUN	NOUN	_	2	nmod
17	,	_	PUNCT	PUNCT	_	16	punct
18	the	_	DET	DET	_	22	det
19	primary	_	ADJ	ADJ	_	22	amod
20	official	_	ADJ	ADJ	_	22	amod
21	news	_	NOUN	NOUN	_	22	compound
22	agency	_	NOUN	NOUN	_	16	appos
23	WFNA	_	PROPN	PROPN	_	24	nsubj
24	said	_	VERB	VERB	_	22	acl:relcl
25	on	_	ADP	ADP	_	26	case
26	Thursday	_	PROPN	PROPN	_	24	nmod
27	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test63': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test63']['sents']['0']:
            print(return_dict['test63']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test63']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test63 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test63 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test63']['sents']['0']:
        verbs=return_dict['test63']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test63']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test63']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test63():
    text="""Osgiliath welcomed the resumption of formal  diplomatic ties with 
Mordor, Rohan, Fornost and Bree after a 12-year rift. 
"""
    parse="""1	Osgiliath	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	the	_	DET	DET	_	4	det
4	resumption	_	NOUN	NOUN	_	2	dobj
5	of	_	ADP	ADP	_	8	case
6	formal	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	4	nmod
9	with	_	ADP	ADP	_	10	case
10	Mordor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	10	punct
12	Rohan	_	PROPN	PROPN	_	10	conj
13	,	_	PUNCT	PUNCT	_	10	punct
14	Fornost	_	PROPN	PROPN	_	10	conj
15	and	_	CONJ	CONJ	_	10	cc
16	Bree	_	PROPN	PROPN	_	10	conj
17	after	_	ADP	ADP	_	20	case
18	a	_	DET	DET	_	20	det
19	12-year	_	NUM	NUM	_	20	nummod
20	rift	_	NOUN	NOUN	_	2	nmod
21	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test64': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test64']['sents']['0']:
            print(return_dict['test64']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")@ " + str(return_dict['test64']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")@ noevent  " )
            print("test64 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")@ noeventexception \n " )
        print("test64 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test64']['sents']['0']:
        verbs=return_dict['test64']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test64']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test64']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test64():
    text="""Fornost and Gondor welcomed a resumption of formal diplomatic ties
between Eriador and Osgiliath after a 12-year rift, the official news
agency WFNA said on Thursday . 
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	4	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Gondor	_	PROPN	PROPN	_	1	conj
4	welcomed	_	VERB	VERB	_	0	root
5	a	_	DET	DET	_	6	det
6	resumption	_	NOUN	NOUN	_	4	dobj
7	of	_	ADP	ADP	_	10	case
8	formal	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	6	nmod
11	between	_	ADP	ADP	_	12	case
12	Eriador	_	PROPN	PROPN	_	10	nmod
13	and	_	CONJ	CONJ	_	12	cc
14	Osgiliath	_	PROPN	PROPN	_	12	conj
15	after	_	ADP	ADP	_	18	case
16	a	_	DET	DET	_	18	det
17	12-year	_	NUM	NUM	_	18	nummod
18	rift	_	NOUN	NOUN	_	6	nmod
19	,	_	PUNCT	PUNCT	_	18	punct
20	the	_	DET	DET	_	23	det
21	official	_	ADJ	ADJ	_	23	amod
22	news	_	NOUN	NOUN	_	23	compound
23	agency	_	NOUN	NOUN	_	18	appos
24	WFNA	_	PROPN	PROPN	_	25	nsubj
25	said	_	VERB	VERB	_	23	acl:relcl
26	on	_	ADP	ADP	_	27	case
27	Thursday	_	PROPN	PROPN	_	25	nmod
28	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test65': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test65']['sents']['0']:
            print(return_dict['test65']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ " + str(return_dict['test65']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noevent  " )
            print("test65 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test65 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test65']['sents']['0']:
        verbs=return_dict['test65']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test65']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test65']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test65():
    text="""Mordor, Rohan, Fornost and Bree welcomed a resumption of formal 
diplomatic ties between Gondor and Osgiliath after a 12-year rift, the 
official news agency WFNA said on Thursday . 
"""
    parse="""1	Mordor	_	PROPN	PROPN	_	8	nsubj
2	,	_	PUNCT	PUNCT	_	1	punct
3	Rohan	_	PROPN	PROPN	_	1	conj
4	,	_	PUNCT	PUNCT	_	1	punct
5	Fornost	_	PROPN	PROPN	_	1	conj
6	and	_	CONJ	CONJ	_	1	cc
7	Bree	_	PROPN	PROPN	_	1	conj
8	welcomed	_	VERB	VERB	_	0	root
9	a	_	DET	DET	_	10	det
10	resumption	_	NOUN	NOUN	_	8	dobj
11	of	_	ADP	ADP	_	14	case
12	formal	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	10	nmod
15	between	_	ADP	ADP	_	16	case
16	Gondor	_	PROPN	PROPN	_	14	nmod
17	and	_	CONJ	CONJ	_	16	cc
18	Osgiliath	_	PROPN	PROPN	_	16	conj
19	after	_	ADP	ADP	_	22	case
20	a	_	DET	DET	_	22	det
21	12-year	_	NUM	NUM	_	22	nummod
22	rift	_	NOUN	NOUN	_	10	nmod
23	,	_	PUNCT	PUNCT	_	22	punct
24	the	_	DET	DET	_	27	det
25	official	_	ADJ	ADJ	_	27	amod
26	news	_	NOUN	NOUN	_	27	compound
27	agency	_	NOUN	NOUN	_	22	appos
28	WFNA	_	PROPN	PROPN	_	29	nsubj
29	said	_	VERB	VERB	_	27	acl:relcl
30	on	_	ADP	ADP	_	31	case
31	Thursday	_	PROPN	PROPN	_	29	nmod
32	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test66': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test66']['sents']['0']:
            print(return_dict['test66']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ " + str(return_dict['test66']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noevent  " )
            print("test66 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test66 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test66']['sents']['0']:
        verbs=return_dict['test66']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test66']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test66']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test66():
    text="""Mordor, the Shire, Fornost and Bree welcomed a resumption of formal 
diplomatic ties between Minas Tirith and Osgiliath after a 12-year rift, 
the official news agency WFNA said on Thursday. 
"""
    parse="""1	Mordor	_	PROPN	PROPN	_	31	nsubj
2	,	_	PUNCT	PUNCT	_	1	punct
3	the	_	DET	DET	_	4	det
4	Shire	_	PROPN	PROPN	_	1	conj
5	,	_	PUNCT	PUNCT	_	1	punct
6	Fornost	_	PROPN	PROPN	_	1	conj
7	and	_	CONJ	CONJ	_	1	cc
8	Bree	_	PROPN	PROPN	_	4	conj
9	welcomed	_	VERB	VERB	_	8	acl
10	a	_	DET	DET	_	11	det
11	resumption	_	NOUN	NOUN	_	9	dobj
12	of	_	ADP	ADP	_	15	case
13	formal	_	ADJ	ADJ	_	15	amod
14	diplomatic	_	ADJ	ADJ	_	15	amod
15	ties	_	NOUN	NOUN	_	11	nmod
16	between	_	ADP	ADP	_	18	case
17	Minas	_	PROPN	PROPN	_	18	compound
18	Tirith	_	PROPN	PROPN	_	15	nmod
19	and	_	CONJ	CONJ	_	18	cc
20	Osgiliath	_	PROPN	PROPN	_	18	conj
21	after	_	ADP	ADP	_	24	case
22	a	_	DET	DET	_	24	det
23	12-year	_	NUM	NUM	_	24	nummod
24	rift	_	NOUN	NOUN	_	11	nmod
25	,	_	PUNCT	PUNCT	_	31	punct
26	the	_	DET	DET	_	29	det
27	official	_	ADJ	ADJ	_	29	amod
28	news	_	NOUN	NOUN	_	29	compound
29	agency	_	NOUN	NOUN	_	24	appos
30	WFNA	_	PROPN	PROPN	_	31	nsubj
31	said	_	VERB	VERB	_	0	root
32	on	_	ADP	ADP	_	33	case
33	Thursday	_	PROPN	PROPN	_	31	nmod
34	.	_	PUNCT	PUNCT	_	31	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test67': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test67']['sents']['0']:
            print(return_dict['test67']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ " + str(return_dict['test67']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noevent  " )
            print("test67 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test67 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test67']['sents']['0']:
        verbs=return_dict['test67']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test67']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test67']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test67():
    text="""Lawmakers in Fornost and Gondor welcomed a resumption of formal diplomatic ties
with Eriador. 
"""
    parse="""1	Lawmakers	_	NOUN	NOUN	_	6	nsubj
2	in	_	ADP	ADP	_	3	case
3	Fornost	_	PROPN	PROPN	_	1	nmod
4	and	_	CONJ	CONJ	_	3	cc
5	Gondor	_	PROPN	PROPN	_	3	conj
6	welcomed	_	VERB	VERB	_	0	root
7	a	_	DET	DET	_	8	det
8	resumption	_	NOUN	NOUN	_	6	dobj
9	of	_	ADP	ADP	_	12	case
10	formal	_	ADJ	ADJ	_	12	amod
11	diplomatic	_	ADJ	ADJ	_	12	amod
12	ties	_	NOUN	NOUN	_	8	nmod
13	with	_	ADP	ADP	_	14	case
14	Eriador	_	PROPN	PROPN	_	12	nmod
15	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test68': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test68']['sents']['0']:
            print(return_dict['test68']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")@ " + str(return_dict['test68']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")@ noevent  " )
            print("test68 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")@ noeventexception \n " )
        print("test68 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test68']['sents']['0']:
        verbs=return_dict['test68']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test68']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test68']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test68():
    text="""Lawmakers and officials in Fornost and Gondor welcomed a resumption of formal diplomatic ties
with Eriador. 
"""
    parse="""1	Lawmakers	_	NOUN	NOUN	_	8	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	officials	_	NOUN	NOUN	_	1	conj
4	in	_	ADP	ADP	_	5	case
5	Fornost	_	PROPN	PROPN	_	1	nmod
6	and	_	CONJ	CONJ	_	5	cc
7	Gondor	_	PROPN	PROPN	_	5	conj
8	welcomed	_	VERB	VERB	_	0	root
9	a	_	DET	DET	_	10	det
10	resumption	_	NOUN	NOUN	_	8	dobj
11	of	_	ADP	ADP	_	14	case
12	formal	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	10	nmod
15	with	_	ADP	ADP	_	16	case
16	Eriador	_	PROPN	PROPN	_	14	nmod
17	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test69': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test69']['sents']['0']:
            print(return_dict['test69']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")@ " + str(return_dict['test69']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")@ noevent  " )
            print("test69 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")@ noeventexception \n " )
        print("test69 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test69']['sents']['0']:
        verbs=return_dict['test69']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test69']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test69']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test69():
    text="""The Shire is about to restore full diplomatic ties with Lorien almost 
five years after crowds burned down its embassy. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Shire	_	PROPN	PROPN	_	3	nsubj
3	is	_	VERB	VERB	_	0	root
4	about	_	ADV	ADV	_	6	advmod
5	to	_	PART	PART	_	6	mark
6	restore	_	VERB	VERB	_	3	advcl
7	full	_	ADJ	ADJ	_	9	amod
8	diplomatic	_	ADJ	ADJ	_	9	amod
9	ties	_	NOUN	NOUN	_	6	dobj
10	with	_	ADP	ADP	_	11	case
11	Lorien	_	PROPN	PROPN	_	9	nmod
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	16	nmod:npmod
15	after	_	ADP	ADP	_	16	case
16	crowds	_	NOUN	NOUN	_	6	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	20	case
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test70': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test70']['sents']['0']:
            print(return_dict['test70']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")@ " + str(return_dict['test70']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")@ noevent  " )
            print("test70 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")@ noeventexception \n " )
        print("test70 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test70']['sents']['0']:
        verbs=return_dict['test70']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test70']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test70']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test70():
    text="""Fornost and the evil awful Gondor welcomed a resumption of formal diplomatic  
ties with Osgiliath after a 12-year rift, the official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	26	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	the	_	DET	DET	_	6	det
4	evil	_	ADJ	ADJ	_	6	amod
5	awful	_	ADJ	ADJ	_	6	amod
6	Gondor	_	PROPN	PROPN	_	1	conj
7	welcomed	_	VERB	VERB	_	5	parataxis
8	a	_	DET	DET	_	9	det
9	resumption	_	NOUN	NOUN	_	7	dobj
10	of	_	ADP	ADP	_	13	case
11	formal	_	ADJ	ADJ	_	13	amod
12	diplomatic	_	ADJ	ADJ	_	13	amod
13	ties	_	NOUN	NOUN	_	9	nmod
14	with	_	ADP	ADP	_	15	case
15	Osgiliath	_	PROPN	PROPN	_	13	nmod
16	after	_	ADP	ADP	_	19	case
17	a	_	DET	DET	_	19	det
18	12-year	_	NUM	NUM	_	19	nummod
19	rift	_	NOUN	NOUN	_	7	nmod
20	,	_	PUNCT	PUNCT	_	26	punct
21	the	_	DET	DET	_	24	det
22	official	_	ADJ	ADJ	_	24	amod
23	news	_	NOUN	NOUN	_	24	compound
24	agency	_	NOUN	NOUN	_	19	appos
25	WFNA	_	PROPN	PROPN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	28	case
28	Thursday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test71': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test71']['sents']['0']:
            print(return_dict['test71']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ " + str(return_dict['test71']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noevent  " )
            print("test71 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test71 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test71']['sents']['0']:
        verbs=return_dict['test71']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test71']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test71']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test71():
    text="""Evil Mordor, the awful Fornost, and good Gondor welcomed a resumption of formal   
diplomatic ties with Osgiliath after a 12-year rift, the official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Evil	_	ADJ	ADJ	_	2	amod
2	Mordor	_	PROPN	PROPN	_	30	nsubj
3	,	_	PUNCT	PUNCT	_	2	punct
4	the	_	DET	DET	_	6	det
5	awful	_	ADJ	ADJ	_	6	amod
6	Fornost	_	PROPN	PROPN	_	2	conj
7	,	_	PUNCT	PUNCT	_	2	punct
8	and	_	CONJ	CONJ	_	2	cc
9	good	_	ADJ	ADJ	_	10	amod
10	Gondor	_	PROPN	PROPN	_	11	nsubj
11	welcomed	_	VERB	VERB	_	2	parataxis
12	a	_	DET	DET	_	13	det
13	resumption	_	NOUN	NOUN	_	11	dobj
14	of	_	ADP	ADP	_	17	case
15	formal	_	ADJ	ADJ	_	17	amod
16	diplomatic	_	ADJ	ADJ	_	17	amod
17	ties	_	NOUN	NOUN	_	13	nmod
18	with	_	ADP	ADP	_	19	case
19	Osgiliath	_	PROPN	PROPN	_	13	nmod
20	after	_	ADP	ADP	_	23	case
21	a	_	DET	DET	_	23	det
22	12-year	_	NUM	NUM	_	23	nummod
23	rift	_	NOUN	NOUN	_	11	nmod
24	,	_	PUNCT	PUNCT	_	30	punct
25	the	_	DET	DET	_	28	det
26	official	_	ADJ	ADJ	_	28	amod
27	news	_	NOUN	NOUN	_	28	compound
28	agency	_	NOUN	NOUN	_	23	appos
29	WFNA	_	PROPN	PROPN	_	30	nsubj
30	said	_	VERB	VERB	_	0	root
31	on	_	ADP	ADP	_	32	case
32	Thursday	_	PROPN	PROPN	_	30	nmod
33	.	_	PUNCT	PUNCT	_	30	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test72': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test72']['sents']['0']:
            print(return_dict['test72']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ " + str(return_dict['test72']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noevent  " )
            print("test72 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test72 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test72']['sents']['0']:
        verbs=return_dict['test72']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test72']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test72']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test72():
    text="""Arnor, Calenardhon and the evil awful Gondor welcomed a resumption of formal diplomatic  
ties with Osgiliath after a 12-year rift, the official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	28	nsubj
2	,	_	PUNCT	PUNCT	_	1	punct
3	Calenardhon	_	PROPN	PROPN	_	1	conj
4	and	_	CONJ	CONJ	_	1	cc
5	the	_	DET	DET	_	8	det
6	evil	_	ADJ	ADJ	_	8	amod
7	awful	_	ADJ	ADJ	_	8	amod
8	Gondor	_	PROPN	PROPN	_	1	conj
9	welcomed	_	VERB	VERB	_	7	parataxis
10	a	_	DET	DET	_	11	det
11	resumption	_	NOUN	NOUN	_	9	dobj
12	of	_	ADP	ADP	_	15	case
13	formal	_	ADJ	ADJ	_	15	amod
14	diplomatic	_	ADJ	ADJ	_	15	amod
15	ties	_	NOUN	NOUN	_	11	nmod
16	with	_	ADP	ADP	_	17	case
17	Osgiliath	_	PROPN	PROPN	_	15	nmod
18	after	_	ADP	ADP	_	21	case
19	a	_	DET	DET	_	21	det
20	12-year	_	NUM	NUM	_	21	nummod
21	rift	_	NOUN	NOUN	_	9	nmod
22	,	_	PUNCT	PUNCT	_	28	punct
23	the	_	DET	DET	_	26	det
24	official	_	ADJ	ADJ	_	26	amod
25	news	_	NOUN	NOUN	_	26	compound
26	agency	_	NOUN	NOUN	_	21	appos
27	WFNA	_	PROPN	PROPN	_	28	nsubj
28	said	_	VERB	VERB	_	0	root
29	on	_	ADP	ADP	_	30	case
30	Thursday	_	PROPN	PROPN	_	28	nmod
31	.	_	PUNCT	PUNCT	_	28	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test73': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test73']['sents']['0']:
            print(return_dict['test73']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ " + str(return_dict['test73']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noevent  " )
            print("test73 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test73 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test73']['sents']['0']:
        verbs=return_dict['test73']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test73']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test73']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test73():
    text="""Calenardhon and the evil Arnor awful Gondor welcomed a resumption of formal diplomatic  
ties with Osgiliath after a 12-year rift, the official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	27	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	the	_	DET	DET	_	5	det
4	evil	_	ADJ	ADJ	_	5	amod
5	Arnor	_	PROPN	PROPN	_	1	conj
6	awful	_	ADJ	ADJ	_	7	amod
7	Gondor	_	PROPN	PROPN	_	8	nsubj
8	welcomed	_	VERB	VERB	_	4	parataxis
9	a	_	DET	DET	_	10	det
10	resumption	_	NOUN	NOUN	_	8	dobj
11	of	_	ADP	ADP	_	14	case
12	formal	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	10	nmod
15	with	_	ADP	ADP	_	16	case
16	Osgiliath	_	PROPN	PROPN	_	14	nmod
17	after	_	ADP	ADP	_	20	case
18	a	_	DET	DET	_	20	det
19	12-year	_	NUM	NUM	_	20	nummod
20	rift	_	NOUN	NOUN	_	8	nmod
21	,	_	PUNCT	PUNCT	_	27	punct
22	the	_	DET	DET	_	25	det
23	official	_	ADJ	ADJ	_	25	amod
24	news	_	NOUN	NOUN	_	25	compound
25	agency	_	NOUN	NOUN	_	20	appos
26	WFNA	_	PROPN	PROPN	_	27	nsubj
27	said	_	VERB	VERB	_	0	root
28	on	_	ADP	ADP	_	29	case
29	Thursday	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	27	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test74': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test74']['sents']['0']:
            print(return_dict['test74']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")@ " + str(return_dict['test74']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")@ noevent  " )
            print("test74 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test74 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test74']['sents']['0']:
        verbs=return_dict['test74']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test74']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test74']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test74():
    text="""The lions and the evil awful Gondor welcomed a resumption of formal diplomatic  
ties with Osgiliath after a 12-year rift, the primary official news agency WFNA said 
on Thursday. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	lions	_	NOUN	NOUN	_	8	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	the	_	DET	DET	_	7	det
5	evil	_	ADJ	ADJ	_	7	amod
6	awful	_	ADJ	ADJ	_	7	amod
7	Gondor	_	PROPN	PROPN	_	2	conj
8	welcomed	_	VERB	VERB	_	0	root
9	a	_	DET	DET	_	10	det
10	resumption	_	NOUN	NOUN	_	8	dobj
11	of	_	ADP	ADP	_	14	case
12	formal	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	10	nmod
15	with	_	ADP	ADP	_	16	case
16	Osgiliath	_	PROPN	PROPN	_	14	nmod
17	after	_	ADP	ADP	_	20	case
18	a	_	DET	DET	_	20	det
19	12-year	_	NUM	NUM	_	20	nummod
20	rift	_	NOUN	NOUN	_	8	nmod
21	,	_	PUNCT	PUNCT	_	28	punct
22	the	_	DET	DET	_	26	det
23	primary	_	ADJ	ADJ	_	26	amod
24	official	_	ADJ	ADJ	_	26	amod
25	news	_	NOUN	NOUN	_	26	compound
26	agency	_	NOUN	NOUN	_	20	appos
27	WFNA	_	PROPN	PROPN	_	28	nsubj
28	said	_	VERB	VERB	_	26	acl:relcl
29	on	_	ADP	ADP	_	30	case
30	Thursday	_	PROPN	PROPN	_	28	nmod
31	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test75': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test75']['sents']['0']:
            print(return_dict['test75']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test75']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test75 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test75 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test75']['sents']['0']:
        verbs=return_dict['test75']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test75']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test75']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test75():
    text="""Lions, tigers, and Gondor welcomed a resumption of formal diplomatic ties  
with Osgiliath after a 12-year rift, the primary official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Lions	_	NOUN	NOUN	_	27	ccomp
2	,	_	PUNCT	PUNCT	_	1	punct
3	tigers	_	PROPN	PROPN	_	1	appos
4	,	_	PUNCT	PUNCT	_	1	punct
5	and	_	CONJ	CONJ	_	1	cc
6	Gondor	_	PROPN	PROPN	_	7	nsubj
7	welcomed	_	VERB	VERB	_	1	appos
8	a	_	DET	DET	_	9	det
9	resumption	_	NOUN	NOUN	_	7	dobj
10	of	_	ADP	ADP	_	13	case
11	formal	_	ADJ	ADJ	_	13	amod
12	diplomatic	_	ADJ	ADJ	_	13	amod
13	ties	_	NOUN	NOUN	_	9	nmod
14	with	_	ADP	ADP	_	15	case
15	Osgiliath	_	PROPN	PROPN	_	13	nmod
16	after	_	ADP	ADP	_	19	case
17	a	_	DET	DET	_	19	det
18	12-year	_	NUM	NUM	_	19	nummod
19	rift	_	NOUN	NOUN	_	7	nmod
20	,	_	PUNCT	PUNCT	_	27	punct
21	the	_	DET	DET	_	25	det
22	primary	_	ADJ	ADJ	_	25	amod
23	official	_	ADJ	ADJ	_	25	amod
24	news	_	NOUN	NOUN	_	25	compound
25	agency	_	NOUN	NOUN	_	19	appos
26	WFNA	_	PROPN	PROPN	_	27	nsubj
27	said	_	VERB	VERB	_	0	root
28	on	_	ADP	ADP	_	29	case
29	Thursday	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	27	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test76': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test76']['sents']['0']:
            print(return_dict['test76']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test76']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test76 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test76 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test76']['sents']['0']:
        verbs=return_dict['test76']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test76']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test76']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test76():
    text="""Ithilen's awful and evil minister Calimehtar warned of the Prince of 
Dol Amroth. 
"""
    parse="""1	Ithilen	_	PROPN	PROPN	_	6	nmod:poss
2	's	_	PART	PART	_	1	case
3	awful	_	ADJ	ADJ	_	6	amod
4	and	_	CONJ	CONJ	_	3	cc
5	evil	_	ADJ	ADJ	_	3	conj
6	minister	_	NOUN	NOUN	_	7	compound
7	Calimehtar	_	PROPN	PROPN	_	8	nsubj
8	warned	_	VERB	VERB	_	0	root
9	of	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	Prince	_	PROPN	PROPN	_	8	nmod
12	of	_	ADP	ADP	_	14	case
13	Dol	_	PROPN	PROPN	_	14	compound
14	Amroth	_	PROPN	PROPN	_	11	nmod
15	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test77': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test77']['sents']['0']:
            print(return_dict['test77']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ " + str(return_dict['test77']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ noevent  " )
            print("test77 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ noeventexception \n " )
        print("test77 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test77']['sents']['0']:
        verbs=return_dict['test77']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test77']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test77']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test77():
    text="""Fornost and Gondor welcomed a resumption of formal diplomatic ties with  
Osgiliath after a 12-year rift, the official news agency WFNA said 
on Thursday. 
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	4	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	Gondor	_	PROPN	PROPN	_	1	conj
4	welcomed	_	VERB	VERB	_	0	root
5	a	_	DET	DET	_	6	det
6	resumption	_	NOUN	NOUN	_	4	dobj
7	of	_	ADP	ADP	_	10	case
8	formal	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	6	nmod
11	with	_	ADP	ADP	_	12	case
12	Osgiliath	_	PROPN	PROPN	_	10	nmod
13	after	_	ADP	ADP	_	16	case
14	a	_	DET	DET	_	16	det
15	12-year	_	NUM	NUM	_	16	nummod
16	rift	_	NOUN	NOUN	_	6	nmod
17	,	_	PUNCT	PUNCT	_	16	punct
18	the	_	DET	DET	_	21	det
19	official	_	ADJ	ADJ	_	21	amod
20	news	_	NOUN	NOUN	_	21	compound
21	agency	_	NOUN	NOUN	_	16	appos
22	WFNA	_	PROPN	PROPN	_	23	nsubj
23	said	_	VERB	VERB	_	21	acl:relcl
24	on	_	ADP	ADP	_	25	case
25	Thursday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test78': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test78']['sents']['0']:
            print(return_dict['test78']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ " + str(return_dict['test78']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noevent  " )
            print("test78 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")@ noeventexception \n " )
        print("test78 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test78']['sents']['0']:
        verbs=return_dict['test78']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test78']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test78']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test78():
    text="""Ithilen's awful and cool minister Calimehtar warned of the Prince of 
Dol Amroth. 
"""
    parse="""1	Ithilen	_	PROPN	PROPN	_	6	nmod:poss
2	's	_	PART	PART	_	1	case
3	awful	_	ADJ	ADJ	_	6	amod
4	and	_	CONJ	CONJ	_	3	cc
5	cool	_	ADJ	ADJ	_	3	conj
6	minister	_	NOUN	NOUN	_	7	compound
7	Calimehtar	_	PROPN	PROPN	_	8	nsubj
8	warned	_	VERB	VERB	_	0	root
9	of	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	Prince	_	PROPN	PROPN	_	8	nmod
12	of	_	ADP	ADP	_	14	case
13	Dol	_	PROPN	PROPN	_	14	compound
14	Amroth	_	PROPN	PROPN	_	11	nmod
15	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test79': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test79']['sents']['0']:
            print(return_dict['test79']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ " + str(return_dict['test79']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ noevent  " )
            print("test79 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITHGOV\", u\"DOL\", u\"160\")@ noeventexception \n " )
        print("test79 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test79']['sents']['0']:
        verbs=return_dict['test79']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test79']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test79']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test79():
    text="""Ithilen's sheep and goats of Gondor warned of the Prince of Dol_Amroth. 
"""
    parse="""1	Ithilen	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	sheep	_	NOUN	NOUN	_	8	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	goats	_	NOUN	NOUN	_	3	conj
6	of	_	ADP	ADP	_	7	case
7	Gondor	_	PROPN	PROPN	_	5	nmod
8	warned	_	VERB	VERB	_	0	root
9	of	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	Prince	_	PROPN	PROPN	_	8	nmod
12	of	_	ADP	ADP	_	13	case
13	Dol_Amroth	_	PROPN	PROPN	_	11	nmod
14	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test80': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test80']['sents']['0']:
            print(return_dict['test80']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")@ " + str(return_dict['test80']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")@ noevent  " )
            print("test80 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")@ noeventexception \n " )
        print("test80 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test80']['sents']['0']:
        verbs=return_dict['test80']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test80']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test80']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test80():
    text="""Ithilen and the government of Gondor warned their populations about the Prince of Dol_Amroth. 
"""
    parse="""1	Ithilen	_	ADJ	ADJ	_	0	root
2	and	_	CONJ	CONJ	_	1	cc
3	the	_	DET	DET	_	4	det
4	government	_	NOUN	NOUN	_	7	nsubj
5	of	_	ADP	ADP	_	6	case
6	Gondor	_	PROPN	PROPN	_	4	nmod
7	warned	_	VERB	VERB	_	1	conj
8	their	_	PRON	PRON	_	9	nmod:poss
9	populations	_	NOUN	NOUN	_	7	dobj
10	about	_	ADP	ADP	_	12	case
11	the	_	DET	DET	_	12	det
12	Prince	_	PROPN	PROPN	_	9	nmod
13	of	_	ADP	ADP	_	14	case
14	Dol_Amroth	_	PROPN	PROPN	_	12	nmod
15	.	_	PUNCT	PUNCT	_	1	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test81': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test81']['sents']['0']:
            print(return_dict['test81']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ " + str(return_dict['test81']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ noevent  " )
            print("test81 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ noeventexception \n " )
        print("test81 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test81']['sents']['0']:
        verbs=return_dict['test81']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test81']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test81']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test81():
    text="""Ithilen and the government of Gondor warned their Ent populations about the Prince of Dol_Amroth. 
"""
    parse="""1	Ithilen	_	ADJ	ADJ	_	0	root
2	and	_	CONJ	CONJ	_	1	cc
3	the	_	DET	DET	_	4	det
4	government	_	NOUN	NOUN	_	7	nsubj
5	of	_	ADP	ADP	_	6	case
6	Gondor	_	PROPN	PROPN	_	4	nmod
7	warned	_	VERB	VERB	_	1	conj
8	their	_	PRON	PRON	_	10	nmod:poss
9	Ent	_	ADJ	ADJ	_	10	amod
10	populations	_	NOUN	NOUN	_	7	dobj
11	about	_	ADP	ADP	_	13	case
12	the	_	DET	DET	_	13	det
13	Prince	_	PROPN	PROPN	_	10	nmod
14	of	_	ADP	ADP	_	15	case
15	Dol_Amroth	_	PROPN	PROPN	_	13	nmod
16	.	_	PUNCT	PUNCT	_	1	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test82': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test82']['sents']['0']:
            print(return_dict['test82']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ " + str(return_dict['test82']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ noevent  " )
            print("test82 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")@ noeventexception \n " )
        print("test82 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test82']['sents']['0']:
        verbs=return_dict['test82']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test82']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test82']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test82():
    text="""Neither Galadriel nor Gollum boycotted the parade supporting Gondor 
on Saturday. 
"""
    parse="""1	Neither	_	CONJ	CONJ	_	5	cc
2	Galadriel	_	PROPN	PROPN	_	5	nsubj
3	nor	_	CONJ	CONJ	_	2	cc
4	Gollum	_	PROPN	PROPN	_	2	conj
5	boycotted	_	VERB	VERB	_	0	root
6	the	_	DET	DET	_	7	det
7	parade	_	NOUN	NOUN	_	5	dobj
8	supporting	_	VERB	VERB	_	7	acl
9	Gondor	_	PROPN	PROPN	_	8	dobj
10	on	_	ADP	ADP	_	11	case
11	Saturday	_	PROPN	PROPN	_	8	nmod
12	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test83': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test83']['sents']['0']:
            print(return_dict['test83']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")@ " + str(return_dict['test83']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")@ noevent  " )
            print("test83 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")@ noeventexception \n " )
        print("test83 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test83']['sents']['0']:
        verbs=return_dict['test83']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test83']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test83']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test83():
    text="""The Calenardhon government condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday and promised aid to the affected Ithilen villages. 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	condemned	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
15	and	_	CONJ	CONJ	_	4	cc
16	promised	_	VERB	VERB	_	4	conj
17	aid	_	NOUN	NOUN	_	16	dobj
18	to	_	ADP	ADP	_	22	case
19	the	_	DET	DET	_	22	det
20	affected	_	VERB	VERB	_	22	amod
21	Ithilen	_	NOUN	NOUN	_	22	compound
22	villages	_	NOUN	NOUN	_	17	nmod
23	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test84': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test84']['sents']['0']:
            print(return_dict['test84']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ " + str(return_dict['test84']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ noevent  " )
            print("test84 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")@ noeventexception \n " )
        print("test84 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test84']['sents']['0']:
        verbs=return_dict['test84']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test84']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test84']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test84():
    text="""Danish media and government warned at the Gondor of the Prince of Dol Amroth. 
"""
    parse="""1	Danish	_	ADJ	ADJ	_	2	amod
2	media	_	NOUN	NOUN	_	5	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	government	_	NOUN	NOUN	_	2	conj
5	warned	_	VERB	VERB	_	0	root
6	at	_	ADP	ADP	_	8	case
7	the	_	DET	DET	_	8	det
8	Gondor	_	PROPN	PROPN	_	5	nmod
9	of	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	Prince	_	PROPN	PROPN	_	8	nmod
12	of	_	ADP	ADP	_	14	case
13	Dol	_	PROPN	PROPN	_	14	compound
14	Amroth	_	PROPN	PROPN	_	11	nmod
15	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test85': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test85']['sents']['0']:
            print(return_dict['test85']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")@ " + str(return_dict['test85']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")@ noevent  " )
            print("test85 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")@ noeventexception \n " )
        print("test85 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test85']['sents']['0']:
        verbs=return_dict['test85']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test85']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test85']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test85():
    text=""""""
    parse="""1	The	_	DET	DET	_	3	det
2	Danish	_	ADJ	ADJ	_	3	amod
3	media	_	NOUN	NOUN	_	6	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	government	_	NOUN	NOUN	_	3	conj
6	warned	_	VERB	VERB	_	0	root
7	the	_	DET	DET	_	8	det
8	population	_	NOUN	NOUN	_	6	dobj
9	of	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	of	_	ADP	ADP	_	13	case
12	the	_	DET	DET	_	13	det
13	Prince	_	PROPN	PROPN	_	10	nmod
14	of	_	ADP	ADP	_	16	case
15	Dol	_	PROPN	PROPN	_	16	compound
16	Amroth	_	PROPN	PROPN	_	13	nmod
17	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test86': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test86']['sents']['0']:
            print(return_dict['test86']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")@ " + str(return_dict['test86']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")@ noevent  " )
            print("test86 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")@ noeventexception \n " )
        print("test86 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test86']['sents']['0']:
        verbs=return_dict['test86']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test86']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test86']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test86():
    text="""The Danish Islamist media and government warned at the Gondor of the Prince of Dol Amroth. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	Danish	_	PROPN	PROPN	_	3	compound
3	Islamist	_	PROPN	PROPN	_	4	compound
4	media	_	NOUN	NOUN	_	7	nsubj
5	and	_	CONJ	CONJ	_	4	cc
6	government	_	NOUN	NOUN	_	4	conj
7	warned	_	VERB	VERB	_	0	root
8	at	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	Gondor	_	PROPN	PROPN	_	7	nmod
11	of	_	ADP	ADP	_	13	case
12	the	_	DET	DET	_	13	det
13	Prince	_	PROPN	PROPN	_	10	nmod
14	of	_	ADP	ADP	_	16	case
15	Dol	_	PROPN	PROPN	_	16	compound
16	Amroth	_	PROPN	PROPN	_	13	nmod
17	.	_	PUNCT	PUNCT	_	7	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test87': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test87']['sents']['0']:
            print(return_dict['test87']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")@ " + str(return_dict['test87']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")@ noevent  " )
            print("test87 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")@ noeventexception \n " )
        print("test87 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test87']['sents']['0']:
        verbs=return_dict['test87']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test87']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test87']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test87():
    text="""Frodo said he has deep satisfaction toward Gondor and Arnor's Elrond, 
and Gondor's dramatic cooperation and its eye-catching development are of 
great significance to the region and even the entire world, he noted. 
"""
    parse="""1	Frodo	_	PROPN	PROPN	_	2	nsubj
2	said	_	VERB	VERB	_	0	root
3	he	_	PRON	PRON	_	4	nsubj
4	has	_	VERB	VERB	_	2	ccomp
5	deep	_	ADJ	ADJ	_	6	amod
6	satisfaction	_	NOUN	NOUN	_	4	dobj
7	toward	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	6	nmod
9	and	_	CONJ	CONJ	_	8	cc
10	Arnor	_	PROPN	PROPN	_	12	nmod:poss
11	's	_	PART	PART	_	10	case
12	Elrond	_	PROPN	PROPN	_	8	conj
13	,	_	PUNCT	PUNCT	_	8	punct
14	and	_	CONJ	CONJ	_	8	cc
15	Gondor	_	PROPN	PROPN	_	18	nmod:poss
16	's	_	PART	PART	_	15	case
17	dramatic	_	ADJ	ADJ	_	18	amod
18	cooperation	_	NOUN	NOUN	_	8	conj
19	and	_	CONJ	CONJ	_	18	cc
20	its	_	PRON	PRON	_	22	nmod:poss
21	eye-catching	_	ADJ	ADJ	_	22	amod
22	development	_	NOUN	NOUN	_	18	conj
23	are	_	VERB	VERB	_	22	acl
24	of	_	ADP	ADP	_	26	case
25	great	_	ADJ	ADJ	_	26	amod
26	significance	_	NOUN	NOUN	_	23	nmod
27	to	_	ADP	ADP	_	29	case
28	the	_	DET	DET	_	29	det
29	region	_	NOUN	NOUN	_	26	nmod
30	and	_	CONJ	CONJ	_	29	cc
31	even	_	ADV	ADV	_	34	advmod
32	the	_	DET	DET	_	34	det
33	entire	_	ADJ	ADJ	_	34	amod
34	world	_	NOUN	NOUN	_	29	conj
35	,	_	PUNCT	PUNCT	_	34	punct
36	he	_	PRON	PRON	_	37	nsubj
37	noted	_	VERB	VERB	_	34	acl:relcl
38	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test88': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20000423'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test88']['sents']['0']:
            print(return_dict['test88']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")@ " + str(return_dict['test88']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")@ noevent  " )
            print("test88 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")@ noeventexception \n " )
        print("test88 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test88']['sents']['0']:
        verbs=return_dict['test88']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test88']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test88']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test88():
    text="""The Calenardhon government issue condemned an attack by Osgiliath soldiers 
in south Ithilen on Thursday and promised raids to the affected Ithilen villages. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	Calenardhon	_	PROPN	PROPN	_	4	compound
3	government	_	NOUN	NOUN	_	4	compound
4	issue	_	NOUN	NOUN	_	5	nsubj
5	condemned	_	VERB	VERB	_	0	root
6	an	_	DET	DET	_	7	det
7	attack	_	NOUN	NOUN	_	5	dobj
8	by	_	ADP	ADP	_	10	case
9	Osgiliath	_	PROPN	PROPN	_	10	compound
10	soldiers	_	NOUN	NOUN	_	5	nmod
11	in	_	ADP	ADP	_	13	case
12	south	_	ADJ	ADJ	_	13	amod
13	Ithilen	_	PROPN	PROPN	_	10	nmod
14	on	_	ADP	ADP	_	15	case
15	Thursday	_	PROPN	PROPN	_	5	nmod
16	and	_	CONJ	CONJ	_	5	cc
17	promised	_	VERB	VERB	_	5	conj
18	raids	_	NOUN	NOUN	_	17	dobj
19	to	_	ADP	ADP	_	23	case
20	the	_	DET	DET	_	23	det
21	affected	_	VERB	VERB	_	23	amod
22	Ithilen	_	NOUN	NOUN	_	23	compound
23	villages	_	NOUN	NOUN	_	18	nmod
24	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test89': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test89']['sents']['0']:
            print(return_dict['test89']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")@ " + str(return_dict['test89']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")@ noevent  " )
            print("test89 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")@ noeventexception \n " )
        print("test89 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test89']['sents']['0']:
        verbs=return_dict['test89']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test89']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test89']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test89():
    text="""The Calenardhon government chided an attack by Osgiliath soldiers 
in south Ithilen on Thursday and ousted the affected Ithilen villages. 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Calenardhon	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	chided	_	VERB	VERB	_	0	root
5	an	_	DET	DET	_	6	det
6	attack	_	NOUN	NOUN	_	4	dobj
7	by	_	ADP	ADP	_	9	case
8	Osgiliath	_	PROPN	PROPN	_	9	compound
9	soldiers	_	NOUN	NOUN	_	4	nmod
10	in	_	ADP	ADP	_	12	case
11	south	_	ADJ	ADJ	_	12	amod
12	Ithilen	_	PROPN	PROPN	_	4	nmod
13	on	_	ADP	ADP	_	14	case
14	Thursday	_	PROPN	PROPN	_	4	nmod
15	and	_	CONJ	CONJ	_	4	cc
16	ousted	_	VERB	VERB	_	4	conj
17	the	_	DET	DET	_	20	det
18	affected	_	ADJ	ADJ	_	20	amod
19	Ithilen	_	NOUN	NOUN	_	20	compound
20	villages	_	NOUN	NOUN	_	16	dobj
21	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test90': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test90']['sents']['0']:
            print(return_dict['test90']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")@ " + str(return_dict['test90']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")@ noevent  " )
            print("test90 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")@ noeventexception \n " )
        print("test90 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test90']['sents']['0']:
        verbs=return_dict['test90']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test90']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test90']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test90():
    text="""And Eriador has called for a boycott against Osgiliath, the state's fiercest foe. 
"""
    parse="""1	And	_	CONJ	CONJ	_	15	cc
2	Eriador	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	called	_	VERB	VERB	_	0	root
5	for	_	ADP	ADP	_	7	case
6	a	_	DET	DET	_	7	det
7	boycott	_	NOUN	NOUN	_	4	nmod
8	against	_	ADP	ADP	_	9	case
9	Osgiliath	_	PROPN	PROPN	_	7	nmod
10	,	_	PUNCT	PUNCT	_	15	punct
11	the	_	DET	DET	_	12	det
12	state	_	NOUN	NOUN	_	15	nmod:poss
13	's	_	PART	PART	_	12	case
14	fiercest	_	ADJ	ADJ	_	15	amod
15	foe	_	NOUN	NOUN	_	4	nmod
16	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test91': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"096\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test91']['sents']['0']:
            print(return_dict['test91']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"096\")@ " + str(return_dict['test91']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"096\")@ noevent  " )
            print("test91 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"OSG\", u\"096\")@ noeventexception \n " )
        print("test91 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test91']['sents']['0']:
        verbs=return_dict['test91']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test91']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test91']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test91():
    text="""Resumption of ties between Arnor and Gondor may spur reconciliation 
between Calenardhon and Gondor, and Gondor and Dagolath, the Osgiliath
newspaper al-Raya said on Friday. 
"""
    parse="""1	Resumption	_	NOUN	NOUN	_	9	nsubj
2	of	_	ADP	ADP	_	3	case
3	ties	_	NOUN	NOUN	_	1	nmod
4	between	_	ADP	ADP	_	5	case
5	Arnor	_	PROPN	PROPN	_	3	nmod
6	and	_	CONJ	CONJ	_	5	cc
7	Gondor	_	PROPN	PROPN	_	5	conj
8	may	_	AUX	AUX	_	9	aux
9	spur	_	VERB	VERB	_	0	root
10	reconciliation	_	NOUN	NOUN	_	9	dobj
11	between	_	ADP	ADP	_	12	case
12	Calenardhon	_	PROPN	PROPN	_	10	nmod
13	and	_	CONJ	CONJ	_	12	cc
14	Gondor	_	PROPN	PROPN	_	12	conj
15	,	_	PUNCT	PUNCT	_	12	punct
16	and	_	CONJ	CONJ	_	12	cc
17	Gondor	_	PROPN	PROPN	_	12	conj
18	and	_	CONJ	CONJ	_	12	cc
19	Dagolath	_	PROPN	PROPN	_	12	conj
20	,	_	PUNCT	PUNCT	_	12	punct
21	the	_	DET	DET	_	23	det
22	Osgiliath	_	PROPN	PROPN	_	23	compound
23	newspaper	_	NOUN	NOUN	_	12	conj
24	al-Raya	_	PROPN	PROPN	_	25	nsubj
25	said	_	VERB	VERB	_	23	acl:relcl
26	on	_	ADP	ADP	_	27	case
27	Friday	_	PROPN	PROPN	_	25	nmod
28	.	_	PUNCT	PUNCT	_	9	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test92': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20000423'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test92']['sents']['0']:
            print(return_dict['test92']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")@ " + str(return_dict['test92']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")@ noevent  " )
            print("test92 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")@ noeventexception \n " )
        print("test92 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test92']['sents']['0']:
        verbs=return_dict['test92']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test92']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test92']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test92():
    text="""Clerics and lawmakers believe Dagolath and Osgiliath can cope with a decrease in vital 
water from the mighty Entwash river when a major dam is filled next 
month. 
"""
    parse="""1	Clerics	_	NOUN	NOUN	_	4	nsubj
2	and	_	CONJ	CONJ	_	1	cc
3	lawmakers	_	NOUN	NOUN	_	1	conj
4	believe	_	VERB	VERB	_	0	root
5	Dagolath	_	PROPN	PROPN	_	4	dobj
6	and	_	CONJ	CONJ	_	5	cc
7	Osgiliath	_	PROPN	PROPN	_	5	conj
8	can	_	AUX	AUX	_	9	aux
9	cope	_	VERB	VERB	_	4	conj
10	with	_	ADP	ADP	_	12	case
11	a	_	DET	DET	_	12	det
12	decrease	_	NOUN	NOUN	_	9	nmod
13	in	_	ADP	ADP	_	15	case
14	vital	_	ADJ	ADJ	_	15	amod
15	water	_	NOUN	NOUN	_	12	nmod
16	from	_	ADP	ADP	_	20	case
17	the	_	DET	DET	_	20	det
18	mighty	_	PROPN	PROPN	_	19	compound
19	Entwash	_	PROPN	PROPN	_	20	compound
20	river	_	NOUN	NOUN	_	15	nmod
21	when	_	ADV	ADV	_	26	mark
22	a	_	DET	DET	_	24	det
23	major	_	ADJ	ADJ	_	24	amod
24	dam	_	NOUN	NOUN	_	26	nsubj
25	is	_	AUX	AUX	_	26	aux
26	filled	_	VERB	VERB	_	20	advcl
27	next	_	ADJ	ADJ	_	28	amod
28	month	_	NOUN	NOUN	_	26	dobj
29	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test93': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950107'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test93']['sents']['0']:
            print(return_dict['test93']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")@ " + str(return_dict['test93']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")@ noevent  " )
            print("test93 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")@ noeventexception \n " )
        print("test93 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test93']['sents']['0']:
        verbs=return_dict['test93']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test93']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test93']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test93():
    text="""The Nasgul said on Friday that an arms embargo against Mordor would not 
work and warned that a blockade of the Bay of Belfalas would harm all  
countries of the region. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Nasgul	_	PROPN	PROPN	_	3	nsubj
3	said	_	VERB	VERB	_	0	root
4	on	_	ADP	ADP	_	5	case
5	Friday	_	PROPN	PROPN	_	3	nmod
6	that	_	SCONJ	SCONJ	_	14	mark
7	an	_	DET	DET	_	9	det
8	arms	_	NOUN	NOUN	_	9	compound
9	embargo	_	NOUN	NOUN	_	14	nsubj
10	against	_	ADP	ADP	_	11	case
11	Mordor	_	PROPN	PROPN	_	9	nmod
12	would	_	AUX	AUX	_	14	aux
13	not	_	PART	PART	_	14	neg
14	work	_	VERB	VERB	_	3	advcl
15	and	_	CONJ	CONJ	_	14	cc
16	warned	_	VERB	VERB	_	14	conj
17	that	_	DET	DET	_	19	det:predet
18	a	_	DET	DET	_	19	det
19	blockade	_	NOUN	NOUN	_	16	dobj
20	of	_	ADP	ADP	_	22	case
21	the	_	DET	DET	_	22	det
22	Bay	_	PROPN	PROPN	_	19	nmod
23	of	_	ADP	ADP	_	24	case
24	Belfalas	_	PROPN	PROPN	_	22	nmod
25	would	_	AUX	AUX	_	26	aux
26	harm	_	VERB	VERB	_	14	conj
27	all	_	DET	DET	_	28	det
28	countries	_	NOUN	NOUN	_	26	dobj
29	of	_	ADP	ADP	_	31	case
30	the	_	DET	DET	_	31	det
31	region	_	NOUN	NOUN	_	28	nmod
32	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test94': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950105'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"###\", u\"MOR\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test94']['sents']['0']:
            print(return_dict['test94']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"###\", u\"MOR\", u\"023\")@ " + str(return_dict['test94']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"###\", u\"MOR\", u\"023\")@ noevent  " )
            print("test94 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"###\", u\"MOR\", u\"023\")@ noeventexception \n " )
        print("test94 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test94']['sents']['0']:
        verbs=return_dict['test94']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test94']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test94']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test94():
    text="""The information ministry of Gondor and the Nasgul said on Friday that an arms 
embargo against the Mordor police would not work and warned that a blockade of 
the Bay of Belfalas would harm all countries of the region. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	information	_	NOUN	NOUN	_	34	nsubj
3	ministry	_	PROPN	PROPN	_	9	nsubj
4	of	_	ADP	ADP	_	5	case
5	Gondor	_	PROPN	PROPN	_	2	nmod
6	and	_	CONJ	CONJ	_	5	cc
7	the	_	DET	DET	_	8	det
8	Nasgul	_	PROPN	PROPN	_	5	conj
9	said	_	VERB	VERB	_	2	acl:relcl
10	on	_	ADP	ADP	_	11	case
11	Friday	_	PROPN	PROPN	_	9	nmod
12	that	_	SCONJ	SCONJ	_	22	mark
13	an	_	DET	DET	_	15	det
14	arms	_	NOUN	NOUN	_	15	compound
15	embargo	_	NOUN	NOUN	_	22	nsubj
16	against	_	ADP	ADP	_	19	case
17	the	_	DET	DET	_	19	det
18	Mordor	_	PROPN	PROPN	_	19	compound
19	police	_	NOUN	NOUN	_	15	nmod
20	would	_	AUX	AUX	_	22	aux
21	not	_	PART	PART	_	22	neg
22	work	_	VERB	VERB	_	9	advcl
23	and	_	CONJ	CONJ	_	22	cc
24	warned	_	VERB	VERB	_	22	conj
25	that	_	DET	DET	_	27	det:predet
26	a	_	DET	DET	_	27	det
27	blockade	_	NOUN	NOUN	_	24	dobj
28	of	_	ADP	ADP	_	30	case
29	the	_	DET	DET	_	30	det
30	Bay	_	PROPN	PROPN	_	27	nmod
31	of	_	ADP	ADP	_	32	case
32	Belfalas	_	PROPN	PROPN	_	30	nmod
33	would	_	AUX	AUX	_	34	aux
34	harm	_	VERB	VERB	_	0	root
35	all	_	DET	DET	_	36	det
36	countries	_	NOUN	NOUN	_	34	dobj
37	of	_	ADP	ADP	_	39	case
38	the	_	DET	DET	_	39	det
39	region	_	NOUN	NOUN	_	36	nmod
40	.	_	PUNCT	PUNCT	_	34	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test95': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950105'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test95']['sents']['0']:
            print(return_dict['test95']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")@ " + str(return_dict['test95']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")@ noevent  " )
            print("test95 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")@ noeventexception \n " )
        print("test95 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test95']['sents']['0']:
        verbs=return_dict['test95']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test95']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test95']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test95():
    text="""White House security officials are about to restore full diplomatic 
ties with Gondor and Arnor. 
"""
    parse="""1	White	_	PROPN	PROPN	_	2	compound
2	House	_	PROPN	PROPN	_	0	root
3	security	_	NOUN	NOUN	_	4	compound
4	officials	_	NOUN	NOUN	_	2	list
5	are	_	VERB	VERB	_	2	acl
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	and	_	CONJ	CONJ	_	13	cc
15	Arnor	_	PROPN	PROPN	_	13	conj
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test96': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test96']['sents']['0']:
            print(return_dict['test96']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ " + str(return_dict['test96']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ noevent  " )
            print("test96 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")@ noeventexception \n " )
        print("test96 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test96']['sents']['0']:
        verbs=return_dict['test96']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test96']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test96']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test96():
    text="""The ambassadors of Arnor, Osgiliath and Gondor presented their 
credentials to Ithilen's president on Wednesday in a further 
show of support to his government by their countries. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	ambassadors	_	NOUN	NOUN	_	9	nsubj
3	of	_	ADP	ADP	_	4	case
4	Arnor	_	PROPN	PROPN	_	2	nmod
5	,	_	PUNCT	PUNCT	_	4	punct
6	Osgiliath	_	PROPN	PROPN	_	4	conj
7	and	_	CONJ	CONJ	_	4	cc
8	Gondor	_	PROPN	PROPN	_	4	conj
9	presented	_	VERB	VERB	_	0	root
10	their	_	PRON	PRON	_	11	nmod:poss
11	credentials	_	NOUN	NOUN	_	9	dobj
12	to	_	ADP	ADP	_	15	case
13	Ithilen	_	PROPN	PROPN	_	15	nmod:poss
14	's	_	PART	PART	_	13	case
15	president	_	PROPN	PROPN	_	11	nmod
16	on	_	ADP	ADP	_	17	case
17	Wednesday	_	PROPN	PROPN	_	15	nmod
18	in	_	ADP	ADP	_	21	case
19	a	_	DET	DET	_	21	det
20	further	_	ADJ	ADJ	_	21	amod
21	show	_	NOUN	NOUN	_	9	nmod
22	of	_	ADP	ADP	_	23	case
23	support	_	NOUN	NOUN	_	21	nmod
24	to	_	ADP	ADP	_	26	case
25	his	_	PRON	PRON	_	26	nmod:poss
26	government	_	NOUN	NOUN	_	23	nmod
27	by	_	ADP	ADP	_	29	case
28	their	_	PRON	PRON	_	29	nmod:poss
29	countries	_	NOUN	NOUN	_	9	nmod
30	.	_	PUNCT	PUNCT	_	9	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test97': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950108'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test97']['sents']['0']:
            print(return_dict['test97']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ " + str(return_dict['test97']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ noevent  " )
            print("test97 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")@ noeventexception \n " )
        print("test97 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test97']['sents']['0']:
        verbs=return_dict['test97']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test97']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test97']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test97():
    text="""The Philippines and the European Union (EU) agree that territorial disputes in the South China Sea should be resolved through international arbitration.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	10	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	the	_	DET	DET	_	9	det
5	European	_	PROPN	PROPN	_	6	compound
6	Union	_	PROPN	PROPN	_	9	compound
7	-LRB-	_	PROPN	PROPN	_	9	compound
8	EU	_	PROPN	PROPN	_	9	compound
9	-RRB-	_	PROPN	PROPN	_	2	conj
10	agree	_	VERB	VERB	_	0	root
11	that	_	SCONJ	SCONJ	_	21	mark
12	territorial	_	ADJ	ADJ	_	13	amod
13	disputes	_	NOUN	NOUN	_	21	nsubj
14	in	_	ADP	ADP	_	18	case
15	the	_	DET	DET	_	18	det
16	South	_	PROPN	PROPN	_	18	compound
17	China	_	PROPN	PROPN	_	18	compound
18	Sea	_	PROPN	PROPN	_	13	nmod
19	should	_	AUX	AUX	_	21	aux
20	be	_	AUX	AUX	_	21	aux
21	resolved	_	VERB	VERB	_	10	ccomp
22	through	_	ADP	ADP	_	24	case
23	international	_	ADJ	ADJ	_	24	amod
24	arbitration	_	NOUN	NOUN	_	21	nmod
25	.	_	PUNCT	PUNCT	_	10	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test98': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test98']['sents']['0']:
            print(return_dict['test98']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")@ " + str(return_dict['test98']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")@ noevent  " )
            print("test98 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")@ noeventexception \n " )
        print("test98 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test98']['sents']['0']:
        verbs=return_dict['test98']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test98']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test98']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test98():
    text="""The Philippines and France agree that territorial disputes should be resolved through international arbitration.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	5	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	France	_	PROPN	PROPN	_	2	conj
5	agree	_	VERB	VERB	_	0	root
6	that	_	SCONJ	SCONJ	_	11	mark
7	territorial	_	ADJ	ADJ	_	8	amod
8	disputes	_	NOUN	NOUN	_	11	nsubj
9	should	_	AUX	AUX	_	11	aux
10	be	_	AUX	AUX	_	11	aux
11	resolved	_	VERB	VERB	_	5	ccomp
12	through	_	ADP	ADP	_	14	case
13	international	_	ADJ	ADJ	_	14	amod
14	arbitration	_	NOUN	NOUN	_	11	nmod
15	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test99': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test99']['sents']['0']:
            print(return_dict['test99']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ " + str(return_dict['test99']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ noevent  " )
            print("test99 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ noeventexception \n " )
        print("test99 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test99']['sents']['0']:
        verbs=return_dict['test99']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test99']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test99']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test99():
    text="""The Philippines and the Central African Republic agree that territorial disputes should be resolved through international arbitration.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	8	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	the	_	DET	DET	_	7	det
5	Central	_	PROPN	PROPN	_	7	compound
6	African	_	PROPN	PROPN	_	7	compound
7	Republic	_	PROPN	PROPN	_	2	conj
8	agree	_	VERB	VERB	_	0	root
9	that	_	SCONJ	SCONJ	_	14	mark
10	territorial	_	ADJ	ADJ	_	11	amod
11	disputes	_	NOUN	NOUN	_	14	nsubj
12	should	_	AUX	AUX	_	14	aux
13	be	_	AUX	AUX	_	14	aux
14	resolved	_	VERB	VERB	_	8	ccomp
15	through	_	ADP	ADP	_	17	case
16	international	_	ADJ	ADJ	_	17	amod
17	arbitration	_	NOUN	NOUN	_	14	nmod
18	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test100': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test100']['sents']['0']:
            print(return_dict['test100']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")@ " + str(return_dict['test100']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")@ noevent  " )
            print("test100 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")@ noeventexception \n " )
        print("test100 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test100']['sents']['0']:
        verbs=return_dict['test100']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test100']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test100']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test100():
    text="""The Philippines and France agree that territorial disputes in the South China Sea should be resolved through international arbitration.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	5	nsubj
3	and	_	CONJ	CONJ	_	2	cc
4	France	_	PROPN	PROPN	_	2	conj
5	agree	_	VERB	VERB	_	0	root
6	that	_	SCONJ	SCONJ	_	16	mark
7	territorial	_	ADJ	ADJ	_	8	amod
8	disputes	_	NOUN	NOUN	_	16	nsubj
9	in	_	ADP	ADP	_	13	case
10	the	_	DET	DET	_	13	det
11	South	_	PROPN	PROPN	_	13	compound
12	China	_	PROPN	PROPN	_	13	compound
13	Sea	_	PROPN	PROPN	_	8	nmod
14	should	_	AUX	AUX	_	16	aux
15	be	_	AUX	AUX	_	16	aux
16	resolved	_	VERB	VERB	_	5	ccomp
17	through	_	ADP	ADP	_	19	case
18	international	_	ADJ	ADJ	_	19	amod
19	arbitration	_	NOUN	NOUN	_	16	nmod
20	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test101': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test101']['sents']['0']:
            print(return_dict['test101']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ " + str(return_dict['test101']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ noevent  " )
            print("test101 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")@ noeventexception \n " )
        print("test101 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test101']['sents']['0']:
        verbs=return_dict['test101']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test101']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test101']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test101():
    text="""Eriador agrees with the Philippines and France that territorial disputes should be resolved through international arbitration.
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	2	nsubj
2	agrees	_	VERB	VERB	_	0	root
3	with	_	ADP	ADP	_	5	case
4	the	_	DET	DET	_	5	det
5	Philippines	_	PROPN	PROPN	_	2	nmod
6	and	_	CONJ	CONJ	_	5	cc
7	France	_	PROPN	PROPN	_	5	conj
8	that	_	DET	DET	_	10	det
9	territorial	_	ADJ	ADJ	_	10	amod
10	disputes	_	NOUN	NOUN	_	13	nsubj
11	should	_	AUX	AUX	_	13	aux
12	be	_	AUX	AUX	_	13	aux
13	resolved	_	VERB	VERB	_	2	conj
14	through	_	ADP	ADP	_	16	case
15	international	_	ADJ	ADJ	_	16	amod
16	arbitration	_	NOUN	NOUN	_	13	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test102': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test102']['sents']['0']:
            print(return_dict['test102']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")@ " + str(return_dict['test102']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")@ noevent  " )
            print("test102 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")@ noeventexception \n " )
        print("test102 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test102']['sents']['0']:
        verbs=return_dict['test102']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test102']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test102']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test102():
    text="""Sam Gamgee will be renewing his gardener's license in Michel Delving.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	5	nsubj
3	will	_	AUX	AUX	_	5	aux
4	be	_	AUX	AUX	_	5	aux
5	renewing	_	VERB	VERB	_	0	root
6	his	_	PRON	PRON	_	7	nmod:poss
7	gardener	_	NOUN	NOUN	_	9	nmod:poss
8	's	_	PART	PART	_	7	case
9	license	_	NOUN	NOUN	_	5	dobj
10	in	_	ADP	ADP	_	12	case
11	Michel	_	PROPN	PROPN	_	12	compound
12	Delving	_	PROPN	PROPN	_	9	nmod
13	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test103': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test103']['sents']['0']:
            print(return_dict['test103']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ " + str(return_dict['test103']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ noevent  " )
            print("test103 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ noeventexception \n " )
        print("test103 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test103']['sents']['0']:
        verbs=return_dict['test103']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test103']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test103']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test103():
    text="""Sam Gamgee will be renewing his gardener's license in Michel Delving.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	5	nsubj
3	will	_	AUX	AUX	_	5	aux
4	be	_	AUX	AUX	_	5	aux
5	renewing	_	VERB	VERB	_	0	root
6	his	_	PRON	PRON	_	7	nmod:poss
7	gardener	_	NOUN	NOUN	_	9	nmod:poss
8	's	_	PART	PART	_	7	case
9	license	_	NOUN	NOUN	_	5	dobj
10	in	_	ADP	ADP	_	12	case
11	Michel	_	PROPN	PROPN	_	12	compound
12	Delving	_	PROPN	PROPN	_	9	nmod
13	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test104': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080119'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test104']['sents']['0']:
            print(return_dict['test104']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ " + str(return_dict['test104']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ noevent  " )
            print("test104 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")@ noeventexception \n " )
        print("test104 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test104']['sents']['0']:
        verbs=return_dict['test104']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test104']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test104']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test104():
    text="""Hamfast Gamgee has rescheduled his annual mushroom hunting trip in the White Downs.
"""
    parse="""1	Hamfast	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	rescheduled	_	VERB	VERB	_	0	root
5	his	_	PRON	PRON	_	7	nmod:poss
6	annual	_	ADJ	ADJ	_	7	amod
7	mushroom	_	NOUN	NOUN	_	4	dobj
8	hunting	_	VERB	VERB	_	7	acl
9	trip	_	NOUN	NOUN	_	8	dobj
10	in	_	ADP	ADP	_	13	case
11	the	_	DET	DET	_	13	det
12	White	_	PROPN	PROPN	_	13	compound
13	Downs	_	PROPN	PROPN	_	8	nmod
14	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test105': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test105']['sents']['0']:
            print(return_dict['test105']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ " + str(return_dict['test105']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ noevent  " )
            print("test105 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ noeventexception \n " )
        print("test105 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test105']['sents']['0']:
        verbs=return_dict['test105']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test105']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test105']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test105():
    text="""Hamfast Gamgee has criticized the recent closure of guest houses in Bree.
"""
    parse="""1	Hamfast	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	criticized	_	VERB	VERB	_	0	root
5	the	_	DET	DET	_	7	det
6	recent	_	ADJ	ADJ	_	7	amod
7	closure	_	NOUN	NOUN	_	4	dobj
8	of	_	ADP	ADP	_	10	case
9	guest	_	NOUN	NOUN	_	10	compound
10	houses	_	NOUN	NOUN	_	7	nmod
11	in	_	ADP	ADP	_	12	case
12	Bree	_	PROPN	PROPN	_	4	nmod
13	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test106': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"121\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test106']['sents']['0']:
            print(return_dict['test106']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"121\")@ " + str(return_dict['test106']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"121\")@ noevent  " )
            print("test106 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"121\")@ noeventexception \n " )
        print("test106 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test106']['sents']['0']:
        verbs=return_dict['test106']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test106']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test106']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test106():
    text="""Hamfast Gamgee has criticized the recent closure of guest houses in Michel Delving.
"""
    parse="""1	Hamfast	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	criticized	_	VERB	VERB	_	0	root
5	the	_	DET	DET	_	7	det
6	recent	_	ADJ	ADJ	_	7	amod
7	closure	_	NOUN	NOUN	_	4	dobj
8	of	_	ADP	ADP	_	10	case
9	guest	_	NOUN	NOUN	_	10	compound
10	houses	_	NOUN	NOUN	_	7	nmod
11	in	_	ADP	ADP	_	13	case
12	Michel	_	PROPN	PROPN	_	13	compound
13	Delving	_	PROPN	PROPN	_	10	nmod
14	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test107': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121225'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test107']['sents']['0']:
            print(return_dict['test107']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")@ " + str(return_dict['test107']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")@ noevent  " )
            print("test107 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")@ noeventexception \n " )
        print("test107 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test107']['sents']['0']:
        verbs=return_dict['test107']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test107']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test107']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test107():
    text="""Hamfast Gamgee has arranged for the reopening of guest houses in Bree.
"""
    parse="""1	Hamfast	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	arranged	_	VERB	VERB	_	0	root
5	for	_	ADP	ADP	_	7	case
6	the	_	DET	DET	_	7	det
7	reopening	_	NOUN	NOUN	_	4	nmod
8	of	_	ADP	ADP	_	10	case
9	guest	_	NOUN	NOUN	_	10	compound
10	houses	_	NOUN	NOUN	_	7	nmod
11	in	_	ADP	ADP	_	12	case
12	Bree	_	PROPN	PROPN	_	4	nmod
13	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test108': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"031\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test108']['sents']['0']:
            print(return_dict['test108']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"031\")@ " + str(return_dict['test108']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"031\")@ noevent  " )
            print("test108 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"BRE\", u\"031\")@ noeventexception \n " )
        print("test108 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test108']['sents']['0']:
        verbs=return_dict['test108']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test108']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test108']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test108():
    text="""Hamfast Gamgee has rescheduled his annual mushroom hunting trip in the White Downs.
"""
    parse="""1	Hamfast	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	rescheduled	_	VERB	VERB	_	0	root
5	his	_	PRON	PRON	_	7	nmod:poss
6	annual	_	ADJ	ADJ	_	7	amod
7	mushroom	_	NOUN	NOUN	_	4	dobj
8	hunting	_	VERB	VERB	_	7	acl
9	trip	_	NOUN	NOUN	_	8	dobj
10	in	_	ADP	ADP	_	13	case
11	the	_	DET	DET	_	13	det
12	White	_	PROPN	PROPN	_	13	compound
13	Downs	_	PROPN	PROPN	_	8	nmod
14	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test109': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20140104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test109']['sents']['0']:
            print(return_dict['test109']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ " + str(return_dict['test109']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ noevent  " )
            print("test109 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"SHR\", u\"082\")@ noeventexception \n " )
        print("test109 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test109']['sents']['0']:
        verbs=return_dict['test109']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test109']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test109']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test109():
    text="""Sam Gamgee has marched very close to the border with Mordor.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	marched	_	VERB	VERB	_	0	root
5	very	_	ADV	ADV	_	6	advmod
6	close	_	ADJ	ADJ	_	4	xcomp
7	to	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	border	_	NOUN	NOUN	_	6	nmod
10	with	_	ADP	ADP	_	11	case
11	Mordor	_	PROPN	PROPN	_	9	nmod
12	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test110': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MOR\", u\"181\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test110']['sents']['0']:
            print(return_dict['test110']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MOR\", u\"181\")@ " + str(return_dict['test110']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MOR\", u\"181\")@ noevent  " )
            print("test110 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MOR\", u\"181\")@ noeventexception \n " )
        print("test110 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test110']['sents']['0']:
        verbs=return_dict['test110']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test110']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test110']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test110():
    text="""Sam Gamgee met a bunch of Morgul Orcs.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	name
2	Gamgee	_	PROPN	PROPN	_	3	nsubj
3	met	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	5	det
5	bunch	_	NOUN	NOUN	_	3	dobj
6	of	_	ADP	ADP	_	8	case
7	Morgul	_	PROPN	PROPN	_	8	compound
8	Orcs	_	PROPN	PROPN	_	5	nmod
9	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test111': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test111']['sents']['0']:
            print(return_dict['test111']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")@ " + str(return_dict['test111']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")@ noevent  " )
            print("test111 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")@ noeventexception \n " )
        print("test111 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test111']['sents']['0']:
        verbs=return_dict['test111']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test111']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test111']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test111():
    text="""Sam Gamgee has overcome the animosity of the Morgul Orcs, which is no small feat.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	overcome	_	VERB	VERB	_	0	root
5	the	_	DET	DET	_	6	det
6	animosity	_	NOUN	NOUN	_	4	dobj
7	of	_	ADP	ADP	_	10	case
8	the	_	DET	DET	_	10	det
9	Morgul	_	PROPN	PROPN	_	10	compound
10	Orcs	_	PROPN	PROPN	_	6	nmod
11	,	_	PUNCT	PUNCT	_	10	punct
12	which	_	PRON	PRON	_	13	nsubj
13	is	_	VERB	VERB	_	10	acl:relcl
14	no	_	DET	DET	_	16	neg
15	small	_	ADJ	ADJ	_	16	amod
16	feat	_	NOUN	NOUN	_	13	dobj
17	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test112': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100110'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"036\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test112']['sents']['0']:
            print(return_dict['test112']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"036\")@ " + str(return_dict['test112']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"036\")@ noevent  " )
            print("test112 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"036\")@ noeventexception \n " )
        print("test112 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test112']['sents']['0']:
        verbs=return_dict['test112']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test112']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test112']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test112():
    text="""Sam Gamgee has begun to question whether he really has much of a future with the
Morgul Orcs.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	begun	_	VERB	VERB	_	0	root
5	to	_	ADP	ADP	_	6	case
6	question	_	NOUN	NOUN	_	4	nmod
7	whether	_	SCONJ	SCONJ	_	10	mark
8	he	_	PRON	PRON	_	10	nsubj
9	really	_	ADV	ADV	_	10	advmod
10	has	_	VERB	VERB	_	4	advcl
11	much	_	ADJ	ADJ	_	10	dobj
12	of	_	ADP	ADP	_	14	case
13	a	_	DET	DET	_	14	det
14	future	_	NOUN	NOUN	_	11	nmod
15	with	_	ADP	ADP	_	18	case
16	the	_	DET	DET	_	18	det
17	Morgul	_	PROPN	PROPN	_	18	compound
18	Orcs	_	PROPN	PROPN	_	14	nmod
19	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test113': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"212\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test113']['sents']['0']:
            print(return_dict['test113']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"212\")@ " + str(return_dict['test113']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"212\")@ noevent  " )
            print("test113 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ORCHOB\", u\"MRGORC\", u\"212\")@ noeventexception \n " )
        print("test113 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test113']['sents']['0']:
        verbs=return_dict['test113']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test113']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test113']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test113():
    text="""Sam Gamgee halted his march towards further adventures in the vicinity of Cirith Ungol.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	name
2	Gamgee	_	PROPN	PROPN	_	3	nsubj
3	halted	_	VERB	VERB	_	0	root
4	his	_	PRON	PRON	_	3	dobj
5	march	_	PROPN	PROPN	_	3	dobj
6	towards	_	ADP	ADP	_	8	case
7	further	_	ADJ	ADJ	_	8	amod
8	adventures	_	NOUN	NOUN	_	3	nmod
9	in	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	vicinity	_	NOUN	NOUN	_	3	nmod
12	of	_	ADP	ADP	_	14	case
13	Cirith	_	PROPN	PROPN	_	14	compound
14	Ungol	_	PROPN	PROPN	_	11	nmod
15	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test114': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MORMIL\", u\"192\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test114']['sents']['0']:
            print(return_dict['test114']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MORMIL\", u\"192\")@ " + str(return_dict['test114']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MORMIL\", u\"192\")@ noevent  " )
            print("test114 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBMIL\", u\"MORMIL\", u\"192\")@ noeventexception \n " )
        print("test114 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test114']['sents']['0']:
        verbs=return_dict['test114']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test114']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test114']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test114():
    text="""Sam Gamgee has reasserted friendship with the gardening license raj of Michel Delving.
"""
    parse="""1	Sam	_	PROPN	PROPN	_	2	compound
2	Gamgee	_	PROPN	PROPN	_	4	nsubj
3	has	_	AUX	AUX	_	4	aux
4	reasserted	_	VERB	VERB	_	0	root
5	friendship	_	NOUN	NOUN	_	4	dobj
6	with	_	ADP	ADP	_	10	case
7	the	_	DET	DET	_	10	det
8	gardening	_	NOUN	NOUN	_	9	compound
9	license	_	NOUN	NOUN	_	10	compound
10	raj	_	NOUN	NOUN	_	5	nmod
11	of	_	ADP	ADP	_	13	case
12	Michel	_	PROPN	PROPN	_	13	compound
13	Delving	_	PROPN	PROPN	_	10	nmod
14	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test115': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121231'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test115']['sents']['0']:
            print(return_dict['test115']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")@ " + str(return_dict['test115']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")@ noevent  " )
            print("test115 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")@ noeventexception \n " )
        print("test115 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test115']['sents']['0']:
        verbs=return_dict['test115']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test115']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test115']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test115():
    text="""Smeagol is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Smeagol	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test116': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19951101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test116']['sents']['0']:
            print(return_dict['test116']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ " + str(return_dict['test116']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ noevent  " )
            print("test116 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test116 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test116']['sents']['0']:
        verbs=return_dict['test116']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test116']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test116']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test116():
    text="""Arnor  is about to restore full diplomatic ties with Slinker almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Slinker	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test117': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19951101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test117']['sents']['0']:
            print(return_dict['test117']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ " + str(return_dict['test117']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ noevent  " )
            print("test117 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ noeventexception \n " )
        print("test117 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test117']['sents']['0']:
        verbs=return_dict['test117']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test117']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test117']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test117():
    text="""Stinker is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Stinker	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test118': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test118']['sents']['0']:
            print(return_dict['test118']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test118']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test118 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test118 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test118']['sents']['0']:
        verbs=return_dict['test118']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test118']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test118']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test118():
    text="""Arnor  is about to restore full diplomatic ties with Slinker almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Slinker	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test119': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19980101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test119']['sents']['0']:
            print(return_dict['test119']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ " + str(return_dict['test119']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ noevent  " )
            print("test119 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBGOV\", u\"064\")@ noeventexception \n " )
        print("test119 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test119']['sents']['0']:
        verbs=return_dict['test119']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test119']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test119']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test119():
    text="""Smeagol is about to restore full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Smeagol	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test120': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test120']['sents']['0']:
            print(return_dict['test120']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ " + str(return_dict['test120']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ noevent  " )
            print("test120 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOBGOV\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test120 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test120']['sents']['0']:
        verbs=return_dict['test120']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test120']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test120']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test120():
    text="""Arnor is about to restore full diplomatic ties with Slinker almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Slinker	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test121': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20010101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBREB\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test121']['sents']['0']:
            print(return_dict['test121']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBREB\", u\"064\")@ " + str(return_dict['test121']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBREB\", u\"064\")@ noevent  " )
            print("test121 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"HOBREB\", u\"064\")@ noeventexception \n " )
        print("test121 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test121']['sents']['0']:
        verbs=return_dict['test121']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test121']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test121']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test121():
    text="""Zimbabwe is about to restore full diplomatic ties with Slinker almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Zimbabwe	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Slinker	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test122': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19781223'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"RHO\", u\"HOB\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test122']['sents']['0']:
            print(return_dict['test122']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"RHO\", u\"HOB\", u\"064\")@ " + str(return_dict['test122']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"RHO\", u\"HOB\", u\"064\")@ noevent  " )
            print("test122 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"RHO\", u\"HOB\", u\"064\")@ noeventexception \n " )
        print("test122 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test122']['sents']['0']:
        verbs=return_dict['test122']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test122']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test122']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test122():
    text="""Arnor is about to restore full diplomatic ties with Zimbabwe almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	23	nsubj
2	is	_	VERB	VERB	_	23	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Zimbabwe	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	5	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test123': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20010101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"ZBW\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test123']['sents']['0']:
            print(return_dict['test123']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"ZBW\", u\"064\")@ " + str(return_dict['test123']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"ZBW\", u\"064\")@ noevent  " )
            print("test123 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"ZBW\", u\"064\")@ noeventexception \n " )
        print("test123 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test123']['sents']['0']:
        verbs=return_dict['test123']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test123']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test123']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test123():
    text="""An investigation determined that the amount of radioactivity that seeped from a 
valve was less than half a microcurie, or less than what one would find in a 
50-pound bag of lawn fertilizer, a senior illiterate university professor said. 
"""
    parse="""1	An	_	DET	DET	_	2	det
2	investigation	_	NOUN	NOUN	_	3	nsubj
3	determined	_	VERB	VERB	_	0	root
4	that	_	SCONJ	SCONJ	_	6	mark
5	the	_	DET	DET	_	6	det
6	amount	_	NOUN	NOUN	_	3	dobj
7	of	_	ADP	ADP	_	8	case
8	radioactivity	_	NOUN	NOUN	_	6	nmod
9	that	_	PRON	PRON	_	10	nsubj
10	seeped	_	VERB	VERB	_	6	acl:relcl
11	from	_	ADP	ADP	_	13	case
12	a	_	DET	DET	_	13	det
13	valve	_	NOUN	NOUN	_	10	nmod
14	was	_	VERB	VERB	_	13	acl
15	less	_	ADJ	ADJ	_	14	xcomp
16	than	_	ADP	ADP	_	19	case
17	half	_	DET	DET	_	19	det:predet
18	a	_	DET	DET	_	19	det
19	microcurie	_	NOUN	NOUN	_	15	nmod
20	,	_	PUNCT	PUNCT	_	15	punct
21	or	_	CONJ	CONJ	_	15	cc
22	less	_	ADJ	ADJ	_	15	conj
23	than	_	SCONJ	SCONJ	_	24	case
24	what	_	PRON	PRON	_	22	nmod
25	one	_	PRON	PRON	_	27	nsubj
26	would	_	AUX	AUX	_	27	aux
27	find	_	VERB	VERB	_	24	acl:relcl
28	in	_	ADP	ADP	_	31	case
29	a	_	DET	DET	_	31	det
30	50-pound	_	ADJ	ADJ	_	31	amod
31	bag	_	NOUN	NOUN	_	27	nmod
32	of	_	ADP	ADP	_	34	case
33	lawn	_	NOUN	NOUN	_	34	compound
34	fertilizer	_	NOUN	NOUN	_	31	nmod
35	,	_	PUNCT	PUNCT	_	31	punct
36	a	_	DET	DET	_	40	det
37	senior	_	ADJ	ADJ	_	40	amod
38	illiterate	_	ADJ	ADJ	_	39	amod
39	university	_	NOUN	NOUN	_	40	compound
40	professor	_	NOUN	NOUN	_	31	nmod
41	said	_	VERB	VERB	_	40	acl
42	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test124': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080801'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test124']['sents']['0']:
            print(return_dict['test124']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test124']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test124 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test124 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test124']['sents']['0']:
        verbs=return_dict['test124']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test124']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test124']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test124():
    text="""A Pakistani woman believed linked to Al-Qaeda who shot at US military officers 
while in detention in Afghanistan was extradited Monday to the United States 
where she faces trial for her actions, a US attorney said. 
"""
    parse="""1	A	_	DET	DET	_	3	det
2	Pakistani	_	ADJ	ADJ	_	3	amod
3	woman	_	NOUN	NOUN	_	4	nsubj
4	believed	_	VERB	VERB	_	37	ccomp
5	linked	_	VERB	VERB	_	4	xcomp
6	to	_	ADP	ADP	_	7	case
7	Al-Qaeda	_	PROPN	PROPN	_	5	nmod
8	who	_	PRON	PRON	_	9	nsubj
9	shot	_	VERB	VERB	_	7	acl:relcl
10	at	_	ADP	ADP	_	13	case
11	US	_	PROPN	PROPN	_	13	compound
12	military	_	ADJ	ADJ	_	13	amod
13	officers	_	NOUN	NOUN	_	9	nmod
14	while	_	SCONJ	SCONJ	_	20	mark
15	in	_	ADP	ADP	_	16	case
16	detention	_	NOUN	NOUN	_	20	nmod
17	in	_	ADP	ADP	_	18	case
18	Afghanistan	_	PROPN	PROPN	_	16	nmod
19	was	_	AUX	AUX	_	20	aux
20	extradited	_	VERB	VERB	_	13	acl
21	Monday	_	PROPN	PROPN	_	20	dobj
22	to	_	ADP	ADP	_	25	case
23	the	_	DET	DET	_	25	det
24	United	_	PROPN	PROPN	_	25	compound
25	States	_	PROPN	PROPN	_	21	nmod
26	where	_	ADV	ADV	_	28	advmod
27	she	_	PRON	PRON	_	28	nsubj
28	faces	_	VERB	VERB	_	20	advcl
29	trial	_	NOUN	NOUN	_	28	dobj
30	for	_	ADP	ADP	_	32	case
31	her	_	PRON	PRON	_	32	nmod:poss
32	actions	_	NOUN	NOUN	_	29	nmod
33	,	_	PUNCT	PUNCT	_	37	punct
34	a	_	DET	DET	_	36	det
35	US	_	PROPN	PROPN	_	36	compound
36	attorney	_	NOUN	NOUN	_	37	nsubj
37	said	_	VERB	VERB	_	0	root
38	.	_	PUNCT	PUNCT	_	37	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test125': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080804'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test125']['sents']['0']:
            print(return_dict['test125']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")@ " + str(return_dict['test125']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")@ noevent  " )
            print("test125 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")@ noeventexception \n " )
        print("test125 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test125']['sents']['0']:
        verbs=return_dict['test125']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test125']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test125']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test125():
    text="""A Pakistani woman believed linked to Al-Qaeda who shot at US military officers 
while in detention in Afghanistan was extradited Monday to the United States 
where she faces trial for her actions, a US attorney said. 
"""
    parse="""1	A	_	DET	DET	_	3	det
2	Pakistani	_	ADJ	ADJ	_	3	amod
3	woman	_	NOUN	NOUN	_	4	nsubj
4	believed	_	VERB	VERB	_	37	ccomp
5	linked	_	VERB	VERB	_	4	xcomp
6	to	_	ADP	ADP	_	7	case
7	Al-Qaeda	_	PROPN	PROPN	_	5	nmod
8	who	_	PRON	PRON	_	9	nsubj
9	shot	_	VERB	VERB	_	7	acl:relcl
10	at	_	ADP	ADP	_	13	case
11	US	_	PROPN	PROPN	_	13	compound
12	military	_	ADJ	ADJ	_	13	amod
13	officers	_	NOUN	NOUN	_	9	nmod
14	while	_	SCONJ	SCONJ	_	20	mark
15	in	_	ADP	ADP	_	16	case
16	detention	_	NOUN	NOUN	_	20	nmod
17	in	_	ADP	ADP	_	18	case
18	Afghanistan	_	PROPN	PROPN	_	16	nmod
19	was	_	AUX	AUX	_	20	aux
20	extradited	_	VERB	VERB	_	13	acl
21	Monday	_	PROPN	PROPN	_	20	dobj
22	to	_	ADP	ADP	_	25	case
23	the	_	DET	DET	_	25	det
24	United	_	PROPN	PROPN	_	25	compound
25	States	_	PROPN	PROPN	_	21	nmod
26	where	_	ADV	ADV	_	28	advmod
27	she	_	PRON	PRON	_	28	nsubj
28	faces	_	VERB	VERB	_	20	advcl
29	trial	_	NOUN	NOUN	_	28	dobj
30	for	_	ADP	ADP	_	32	case
31	her	_	PRON	PRON	_	32	nmod:poss
32	actions	_	NOUN	NOUN	_	29	nmod
33	,	_	PUNCT	PUNCT	_	37	punct
34	a	_	DET	DET	_	36	det
35	US	_	PROPN	PROPN	_	36	compound
36	attorney	_	NOUN	NOUN	_	37	nsubj
37	said	_	VERB	VERB	_	0	root
38	.	_	PUNCT	PUNCT	_	37	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test126': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080804'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test126']['sents']['0']:
            print(return_dict['test126']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")@ " + str(return_dict['test126']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")@ noevent  " )
            print("test126 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")@ noeventexception \n " )
        print("test126 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test126']['sents']['0']:
        verbs=return_dict['test126']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test126']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test126']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test126():
    text="""On improvement of primary health and Gondor's health centres, he said
government proposed to take up the issue with the World Bank in a phased manner
with priority being assigned to states with low health indices. 
"""
    parse="""1	On	_	ADP	ADP	_	2	case
2	improvement	_	NOUN	NOUN	_	13	nmod
3	of	_	ADP	ADP	_	5	case
4	primary	_	ADJ	ADJ	_	5	amod
5	health	_	NOUN	NOUN	_	2	nmod
6	and	_	CONJ	CONJ	_	5	cc
7	Gondor	_	PROPN	PROPN	_	10	nmod:poss
8	's	_	PART	PART	_	7	case
9	health	_	NOUN	NOUN	_	10	compound
10	centres	_	NOUN	NOUN	_	5	conj
11	,	_	PUNCT	PUNCT	_	13	punct
12	he	_	PRON	PRON	_	13	nsubj
13	said	_	VERB	VERB	_	0	root
14	government	_	NOUN	NOUN	_	15	nsubj
15	proposed	_	VERB	VERB	_	13	ccomp
16	to	_	PART	PART	_	17	mark
17	take	_	VERB	VERB	_	15	xcomp
18	up	_	ADP	ADP	_	17	compound:prt
19	the	_	DET	DET	_	20	det
20	issue	_	NOUN	NOUN	_	17	nmod
21	with	_	ADP	ADP	_	24	case
22	the	_	DET	DET	_	24	det
23	World	_	PROPN	PROPN	_	24	compound
24	Bank	_	PROPN	PROPN	_	20	nmod
25	in	_	ADP	ADP	_	28	case
26	a	_	DET	DET	_	28	det
27	phased	_	VERB	VERB	_	28	amod
28	manner	_	NOUN	NOUN	_	17	nmod
29	with	_	ADP	ADP	_	30	case
30	priority	_	NOUN	NOUN	_	28	nmod
31	being	_	AUX	AUX	_	32	aux
32	assigned	_	VERB	VERB	_	30	acl
33	to	_	PART	PART	_	34	mark
34	states	_	VERB	VERB	_	32	xcomp
35	with	_	ADP	ADP	_	38	case
36	low	_	ADJ	ADJ	_	38	amod
37	health	_	NOUN	NOUN	_	38	compound
38	indices	_	NOUN	NOUN	_	34	nmod
39	.	_	PUNCT	PUNCT	_	13	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test127': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test127']['sents']['0']:
            print(return_dict['test127']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test127']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test127 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test127 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test127']['sents']['0']:
        verbs=return_dict['test127']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test127']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test127']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test127():
    text="""South Korea's women have grabbed gold in the team's section since then, while 
their male counterparts are on the verge of completing a hat-trick, having 
triumphed in 2000 and 2004. 
"""
    parse="""1	South	_	PROPN	PROPN	_	2	compound
2	Korea	_	PROPN	PROPN	_	4	nmod:poss
3	's	_	PART	PART	_	2	case
4	women	_	NOUN	NOUN	_	6	nsubj
5	have	_	AUX	AUX	_	6	aux
6	grabbed	_	VERB	VERB	_	0	root
7	gold	_	ADJ	ADJ	_	6	dobj
8	in	_	ADP	ADP	_	12	case
9	the	_	DET	DET	_	10	det
10	team	_	NOUN	NOUN	_	12	nmod:poss
11	's	_	PART	PART	_	10	case
12	section	_	NOUN	NOUN	_	7	nmod
13	since	_	ADP	ADP	_	14	case
14	then	_	ADV	ADV	_	6	nmod
15	,	_	PUNCT	PUNCT	_	6	punct
16	while	_	SCONJ	SCONJ	_	20	mark
17	their	_	PRON	PRON	_	19	nmod:poss
18	male	_	NOUN	NOUN	_	19	compound
19	counterparts	_	NOUN	NOUN	_	20	nsubj
20	are	_	VERB	VERB	_	6	advcl
21	on	_	ADP	ADP	_	23	case
22	the	_	DET	DET	_	23	det
23	verge	_	NOUN	NOUN	_	20	nmod
24	of	_	SCONJ	SCONJ	_	25	mark
25	completing	_	VERB	VERB	_	23	acl
26	a	_	DET	DET	_	27	det
27	hat-trick	_	NOUN	NOUN	_	25	dobj
28	,	_	PUNCT	PUNCT	_	27	punct
29	having	_	AUX	AUX	_	30	aux
30	triumphed	_	VERB	VERB	_	27	acl:relcl
31	in	_	ADP	ADP	_	32	case
32	2000	_	NUM	NUM	_	30	nmod
33	and	_	CONJ	CONJ	_	32	cc
34	2004	_	NUM	NUM	_	32	conj
35	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test128': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080804'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test128']['sents']['0']:
            print(return_dict['test128']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test128']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test128 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test128 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test128']['sents']['0']:
        verbs=return_dict['test128']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test128']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test128']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test128():
    text="""An explosion sent a wall of flame through the school dormitory just as the 
girls, aged from eight to 16, were getting up for morning prayers, one of the 
girls said. 
"""
    parse="""1	An	_	DET	DET	_	2	det
2	explosion	_	NOUN	NOUN	_	24	nsubj
3	sent	_	VERB	VERB	_	2	acl
4	a	_	DET	DET	_	5	det
5	wall	_	NOUN	NOUN	_	3	dobj
6	of	_	ADP	ADP	_	7	case
7	flame	_	NOUN	NOUN	_	5	nmod
8	through	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	school	_	NOUN	NOUN	_	3	nmod
11	dormitory	_	ADV	ADV	_	12	advmod
12	just	_	ADV	ADV	_	15	advmod
13	as	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	girls	_	NOUN	NOUN	_	5	nmod
16	,	_	PUNCT	PUNCT	_	15	punct
17	aged	_	ADJ	ADJ	_	15	amod
18	from	_	ADP	ADP	_	19	case
19	eight	_	NUM	NUM	_	17	nmod
20	to	_	ADP	ADP	_	21	case
21	16	_	NUM	NUM	_	19	nmod
22	,	_	PUNCT	PUNCT	_	34	punct
23	were	_	AUX	AUX	_	24	aux
24	getting	_	VERB	VERB	_	34	advcl
25	up	_	ADP	ADP	_	24	compound:prt
26	for	_	ADP	ADP	_	28	case
27	morning	_	NOUN	NOUN	_	28	compound
28	prayers	_	NOUN	NOUN	_	24	nmod
29	,	_	PUNCT	PUNCT	_	34	punct
30	one	_	NUM	NUM	_	34	nsubj
31	of	_	ADP	ADP	_	33	case
32	the	_	DET	DET	_	33	det
33	girls	_	NOUN	NOUN	_	30	nmod
34	said	_	VERB	VERB	_	0	root
35	.	_	PUNCT	PUNCT	_	34	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test129': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080801'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test129']['sents']['0']:
            print(return_dict['test129']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test129']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test129 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test129 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test129']['sents']['0']:
        verbs=return_dict['test129']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test129']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test129']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test129():
    text="""Grahame Russell, who lost his son Philip when one of the four suicide bombers 
detonated a device on a bus in central London, said:`` A lot of families' 
ideas were included in the design; it's very different. 
"""
    parse="""1	Grahame	_	PROPN	PROPN	_	2	compound
2	Russell	_	PROPN	PROPN	_	26	iobj
3	,	_	PUNCT	PUNCT	_	2	punct
4	who	_	PRON	PRON	_	5	nsubj
5	lost	_	VERB	VERB	_	2	acl:relcl
6	his	_	PRON	PRON	_	7	nmod:poss
7	son	_	NOUN	NOUN	_	5	dobj
8	Philip	_	PROPN	PROPN	_	7	appos
9	when	_	ADV	ADV	_	10	advmod
10	one	_	NUM	NUM	_	5	nmod
11	of	_	ADP	ADP	_	15	case
12	the	_	DET	DET	_	15	det
13	four	_	NUM	NUM	_	14	nummod
14	suicide	_	NOUN	NOUN	_	15	compound
15	bombers	_	NOUN	NOUN	_	10	nmod
16	detonated	_	VERB	VERB	_	15	acl
17	a	_	DET	DET	_	18	det
18	device	_	NOUN	NOUN	_	16	dobj
19	on	_	ADP	ADP	_	21	case
20	a	_	DET	DET	_	21	det
21	bus	_	NOUN	NOUN	_	16	nmod
22	in	_	ADP	ADP	_	24	case
23	central	_	ADJ	ADJ	_	24	amod
24	London	_	PROPN	PROPN	_	21	nmod
25	,	_	PUNCT	PUNCT	_	26	punct
26	said	_	VERB	VERB	_	0	root
27	:	_	PUNCT	PUNCT	_	26	punct
28	``	_	VERB	VERB	_	26	ccomp
29	A	_	DET	DET	_	30	det
30	lot	_	NOUN	NOUN	_	28	dobj
31	of	_	ADP	ADP	_	32	case
32	families	_	NOUN	NOUN	_	30	nmod
33	'	_	PUNCT	PUNCT	_	32	punct
34	ideas	_	NOUN	NOUN	_	36	nsubj
35	were	_	AUX	AUX	_	36	aux
36	included	_	VERB	VERB	_	5	parataxis
37	in	_	ADP	ADP	_	39	case
38	the	_	DET	DET	_	39	det
39	design	_	NOUN	NOUN	_	36	nmod
40	;	_	PUNCT	PUNCT	_	26	punct
41	it	_	PRON	PRON	_	44	nsubj
42	's	_	VERB	VERB	_	44	aux
43	very	_	ADV	ADV	_	44	advmod
44	different	_	ADJ	ADJ	_	26	parataxis
45	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test130': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080801'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test130']['sents']['0']:
            print(return_dict['test130']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test130']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test130 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test130 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test130']['sents']['0']:
        verbs=return_dict['test130']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test130']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test130']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test130():
    text="""The park is to be jointly managed by the government and local communities, with 
assistance from Birdlife International and the Australian state of New South 
Wales. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	park	_	NOUN	NOUN	_	3	nsubj
3	is	_	VERB	VERB	_	0	root
4	to	_	PART	PART	_	7	mark
5	be	_	AUX	AUX	_	7	aux
6	jointly	_	ADV	ADV	_	7	advmod
7	managed	_	VERB	VERB	_	3	advcl
8	by	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	government	_	NOUN	NOUN	_	7	nmod
11	and	_	CONJ	CONJ	_	10	cc
12	local	_	ADJ	ADJ	_	13	amod
13	communities	_	NOUN	NOUN	_	10	conj
14	,	_	PUNCT	PUNCT	_	7	punct
15	with	_	ADP	ADP	_	16	case
16	assistance	_	NOUN	NOUN	_	7	nmod
17	from	_	ADP	ADP	_	19	case
18	Birdlife	_	PROPN	PROPN	_	19	compound
19	International	_	PROPN	PROPN	_	16	nmod
20	and	_	CONJ	CONJ	_	19	cc
21	the	_	DET	DET	_	23	det
22	Australian	_	ADJ	ADJ	_	23	amod
23	state	_	NOUN	NOUN	_	19	conj
24	of	_	ADP	ADP	_	27	case
25	New	_	PROPN	PROPN	_	27	compound
26	South	_	PROPN	PROPN	_	27	compound
27	Wales	_	PROPN	PROPN	_	23	nmod
28	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test131': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080801'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test131']['sents']['0']:
            print(return_dict['test131']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test131']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test131 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test131 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test131']['sents']['0']:
        verbs=return_dict['test131']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test131']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test131']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test131():
    text="""China's coal mines are among the most dangerous in the world, with safety 
standards often ignored in the quest for profits and the drive to meet demand 
for coal-- the source of about 70 percent of China's energy. 
"""
    parse="""1	China	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	coal	_	NOUN	NOUN	_	18	nsubj
4	mines	_	PRON	PRON	_	5	nsubj
5	are	_	VERB	VERB	_	3	acl:relcl
6	among	_	ADP	ADP	_	9	case
7	the	_	DET	DET	_	9	det
8	most	_	ADV	ADV	_	9	advmod
9	dangerous	_	ADJ	ADJ	_	3	acl:relcl
10	in	_	ADP	ADP	_	12	case
11	the	_	DET	DET	_	12	det
12	world	_	NOUN	NOUN	_	9	nmod
13	,	_	PUNCT	PUNCT	_	18	punct
14	with	_	ADP	ADP	_	16	case
15	safety	_	NOUN	NOUN	_	16	compound
16	standards	_	NOUN	NOUN	_	18	nsubj
17	often	_	ADV	ADV	_	18	advmod
18	ignored	_	VERB	VERB	_	0	root
19	in	_	ADP	ADP	_	21	case
20	the	_	DET	DET	_	21	det
21	quest	_	NOUN	NOUN	_	18	nmod
22	for	_	ADP	ADP	_	23	case
23	profits	_	NOUN	NOUN	_	21	nmod
24	and	_	CONJ	CONJ	_	23	cc
25	the	_	DET	DET	_	26	det
26	drive	_	NOUN	NOUN	_	23	conj
27	to	_	PART	PART	_	28	mark
28	meet	_	VERB	VERB	_	26	acl
29	demand	_	NOUN	NOUN	_	28	dobj
30	for	_	ADP	ADP	_	31	case
31	coal	_	NOUN	NOUN	_	29	nmod
32	--	_	PUNCT	PUNCT	_	18	punct
33	the	_	DET	DET	_	34	det
34	source	_	NOUN	NOUN	_	18	conj
35	of	_	ADP	ADP	_	38	case
36	about	_	ADV	ADV	_	37	advmod
37	70	_	NUM	NUM	_	38	nummod
38	percent	_	NOUN	NOUN	_	34	nmod
39	of	_	ADP	ADP	_	42	case
40	China	_	PROPN	PROPN	_	42	nmod:poss
41	's	_	PART	PART	_	40	case
42	energy	_	NOUN	NOUN	_	38	nmod
43	.	_	PUNCT	PUNCT	_	18	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test132': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080801'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test132']['sents']['0']:
            print(return_dict['test132']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test132']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test132 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test132 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test132']['sents']['0']:
        verbs=return_dict['test132']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test132']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test132']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test132():
    text="""They issued a joint statement calling for a continued expansion of the 
International Monetary Fund's reserves and a shake-up of countries' 
representation and voting rights on that and other Bretton Woods institutions. 
"""
    parse="""1	They	_	PRON	PRON	_	2	nsubj
2	issued	_	VERB	VERB	_	0	root
3	a	_	DET	DET	_	5	det
4	joint	_	ADJ	ADJ	_	5	amod
5	statement	_	NOUN	NOUN	_	2	dobj
6	calling	_	VERB	VERB	_	5	acl
7	for	_	ADP	ADP	_	10	case
8	a	_	DET	DET	_	10	det
9	continued	_	VERB	VERB	_	10	amod
10	expansion	_	NOUN	NOUN	_	6	nmod
11	of	_	ADP	ADP	_	17	case
12	the	_	DET	DET	_	15	det
13	International	_	PROPN	PROPN	_	15	compound
14	Monetary	_	PROPN	PROPN	_	15	compound
15	Fund	_	PROPN	PROPN	_	17	nmod:poss
16	's	_	PART	PART	_	15	case
17	reserves	_	NOUN	NOUN	_	10	nmod
18	and	_	CONJ	CONJ	_	17	cc
19	a	_	DET	DET	_	20	det
20	shake-up	_	NOUN	NOUN	_	17	conj
21	of	_	ADP	ADP	_	22	case
22	countries	_	NOUN	NOUN	_	20	nmod
23	'	_	PUNCT	PUNCT	_	22	punct
24	representation	_	NOUN	NOUN	_	22	conj
25	and	_	CONJ	CONJ	_	24	cc
26	voting	_	NOUN	NOUN	_	27	compound
27	rights	_	NOUN	NOUN	_	24	conj
28	on	_	ADP	ADP	_	29	case
29	that	_	PRON	PRON	_	24	nmod
30	and	_	CONJ	CONJ	_	29	cc
31	other	_	ADJ	ADJ	_	34	amod
32	Bretton	_	PROPN	PROPN	_	33	compound
33	Woods	_	PROPN	PROPN	_	34	compound
34	institutions	_	NOUN	NOUN	_	29	conj
35	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test133': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20090101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test133']['sents']['0']:
            print(return_dict['test133']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test133']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test133 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test133 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test133']['sents']['0']:
        verbs=return_dict['test133']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test133']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test133']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test133():
    text="""President Ilham Aliyev and President of the European Commission Jose Manuel Barroso held 
a one-on-one meeting on June 14.
"""
    parse="""1	President	_	PROPN	PROPN	_	3	compound
2	Ilham	_	PROPN	PROPN	_	3	compound
3	Aliyev	_	PROPN	PROPN	_	13	nsubj
4	and	_	CONJ	CONJ	_	3	cc
5	President	_	PROPN	PROPN	_	3	conj
6	of	_	ADP	ADP	_	12	case
7	the	_	DET	DET	_	12	det
8	European	_	PROPN	PROPN	_	12	compound
9	Commission	_	PROPN	PROPN	_	12	compound
10	Jose	_	PROPN	PROPN	_	12	compound
11	Manuel	_	PROPN	PROPN	_	12	compound
12	Barroso	_	PROPN	PROPN	_	3	conj
13	held	_	VERB	VERB	_	0	root
14	a	_	DET	DET	_	16	det
15	one-on-one	_	ADJ	ADJ	_	16	amod
16	meeting	_	NOUN	NOUN	_	13	dobj
17	on	_	ADP	ADP	_	18	case
18	June	_	PROPN	PROPN	_	13	nmod
19	14	_	NUM	NUM	_	18	nummod
20	.	_	PUNCT	PUNCT	_	13	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test134': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080804'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test134']['sents']['0']:
            print(return_dict['test134']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test134']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test134 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test134 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test134']['sents']['0']:
        verbs=return_dict['test134']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test134']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test134']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test134():
    text="""Abubakar also directed Zuokumor to ensure that there is adequate police presence in all 
the polling units and collation centres in the state.
"""
    parse="""1	Abubakar	_	PROPN	PROPN	_	3	nsubj
2	also	_	ADV	ADV	_	3	advmod
3	directed	_	VERB	VERB	_	0	root
4	Zuokumor	_	PROPN	PROPN	_	3	dobj
5	to	_	PART	PART	_	6	mark
6	ensure	_	VERB	VERB	_	3	xcomp
7	that	_	SCONJ	SCONJ	_	9	mark
8	there	_	PRON	PRON	_	9	expl
9	is	_	VERB	VERB	_	6	ccomp
10	adequate	_	ADJ	ADJ	_	12	amod
11	police	_	NOUN	NOUN	_	12	compound
12	presence	_	NOUN	NOUN	_	9	dobj
13	in	_	ADP	ADP	_	17	case
14	all	_	DET	DET	_	17	det:predet
15	the	_	DET	DET	_	17	det
16	polling	_	NOUN	NOUN	_	17	compound
17	units	_	NOUN	NOUN	_	9	nmod
18	and	_	CONJ	CONJ	_	17	cc
19	collation	_	NOUN	NOUN	_	20	compound
20	centres	_	NOUN	NOUN	_	17	conj
21	in	_	ADP	ADP	_	23	case
22	the	_	DET	DET	_	23	det
23	state	_	NOUN	NOUN	_	20	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test135': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080804'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test135']['sents']['0']:
            print(return_dict['test135']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test135']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test135 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test135 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test135']['sents']['0']:
        verbs=return_dict['test135']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test135']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test135']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test135():
    text="""Gryffindor's head Minerva McGonagall left for the Ministry of 
Magic on Wednesday for meetings of the joint OWL standards 
committee with Albus Dumbledore, Luna Lovegood's news agency reported. 
"""
    parse="""1	Gryffindor	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	head	_	NOUN	NOUN	_	5	compound
4	Minerva	_	PROPN	PROPN	_	5	name
5	McGonagall	_	PROPN	PROPN	_	6	nsubj
6	left	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	Ministry	_	PROPN	PROPN	_	6	nmod
10	of	_	ADP	ADP	_	11	case
11	Magic	_	PROPN	PROPN	_	9	nmod
12	on	_	ADP	ADP	_	13	case
13	Wednesday	_	PROPN	PROPN	_	6	nmod
14	for	_	ADP	ADP	_	15	case
15	meetings	_	NOUN	NOUN	_	6	nmod
16	of	_	ADP	ADP	_	21	case
17	the	_	DET	DET	_	21	det
18	joint	_	ADJ	ADJ	_	21	amod
19	OWL	_	PROPN	PROPN	_	21	compound
20	standards	_	NOUN	NOUN	_	21	compound
21	committee	_	NOUN	NOUN	_	15	nmod
22	with	_	ADP	ADP	_	24	case
23	Albus	_	PROPN	PROPN	_	24	compound
24	Dumbledore	_	PROPN	PROPN	_	21	nmod
25	,	_	PUNCT	PUNCT	_	6	punct
26	Luna	_	NOUN	NOUN	_	6	nmod
27	Lovegood	_	PROPN	PROPN	_	30	nmod:poss
28	's	_	PART	PART	_	27	case
29	news	_	NOUN	NOUN	_	30	compound
30	agency	_	NOUN	NOUN	_	6	nmod
31	reported	_	VERB	VERB	_	6	advcl
32	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test136': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"032\"),(u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test136']['sents']['0']:
            print(return_dict['test136']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"032\"),(u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ " + str(return_dict['test136']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"032\"),(u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ noevent  " )
            print("test136 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"032\"),(u\"&quot;THE MINISTRY OF MAGIC&quot;\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ noeventexception \n " )
        print("test136 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test136']['sents']['0']:
        verbs=return_dict['test136']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test136']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test136']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test136():
    text="""Gryffindor's head Minerva McGonagall left for Minas Tirith on Wednesday for meetings of 
the joint OWL standards committee with Albus Dumbledore, Luna Lovegood's news agency reported. 
"""
    parse="""1	Gryffindor	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	head	_	NOUN	NOUN	_	5	compound
4	Minerva	_	PROPN	PROPN	_	5	name
5	McGonagall	_	PROPN	PROPN	_	6	nsubj
6	left	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	9	case
8	Minas	_	PROPN	PROPN	_	9	compound
9	Tirith	_	PROPN	PROPN	_	6	nmod
10	on	_	ADP	ADP	_	11	case
11	Wednesday	_	PROPN	PROPN	_	6	nmod
12	for	_	ADP	ADP	_	13	case
13	meetings	_	NOUN	NOUN	_	6	nmod
14	of	_	ADP	ADP	_	19	case
15	the	_	DET	DET	_	19	det
16	joint	_	ADJ	ADJ	_	19	amod
17	OWL	_	PROPN	PROPN	_	19	compound
18	standards	_	NOUN	NOUN	_	19	compound
19	committee	_	NOUN	NOUN	_	13	nmod
20	with	_	ADP	ADP	_	22	case
21	Albus	_	PROPN	PROPN	_	22	compound
22	Dumbledore	_	PROPN	PROPN	_	19	nmod
23	,	_	PUNCT	PUNCT	_	22	punct
24	Luna	_	NOUN	NOUN	_	22	list
25	Lovegood	_	PROPN	PROPN	_	28	nmod:poss
26	's	_	PART	PART	_	25	case
27	news	_	NOUN	NOUN	_	28	compound
28	agency	_	NOUN	NOUN	_	29	nsubj
29	reported	_	VERB	VERB	_	19	acl
30	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test137': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"GON\", u\"032\"),(u\"GON\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test137']['sents']['0']:
            print(return_dict['test137']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"GON\", u\"032\"),(u\"GON\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ " + str(return_dict['test137']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"GON\", u\"032\"),(u\"GON\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ noevent  " )
            print("test137 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"GON\", u\"032\"),(u\"GON\", u\"&quot;GRYFFINDOR HEAD MINERVA MCGONAGALL&quot;\", u\"033\")@ noeventexception \n " )
        print("test137 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test137']['sents']['0']:
        verbs=return_dict['test137']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test137']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test137']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test137():
    text="""Gryffindor's head Minerva McGonagall left for the Ministry of 
Magic on Wednesday for meetings of the joint OWL standards 
committee with Albus Dumbledore, Luna Lovegood's news agency reported. 
"""
    parse="""1	Gryffindor	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	head	_	NOUN	NOUN	_	5	compound
4	Minerva	_	PROPN	PROPN	_	5	name
5	McGonagall	_	PROPN	PROPN	_	6	nsubj
6	left	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	Ministry	_	PROPN	PROPN	_	6	nmod
10	of	_	ADP	ADP	_	11	case
11	Magic	_	PROPN	PROPN	_	9	nmod
12	on	_	ADP	ADP	_	13	case
13	Wednesday	_	PROPN	PROPN	_	6	nmod
14	for	_	ADP	ADP	_	15	case
15	meetings	_	NOUN	NOUN	_	6	nmod
16	of	_	ADP	ADP	_	21	case
17	the	_	DET	DET	_	21	det
18	joint	_	ADJ	ADJ	_	21	amod
19	OWL	_	PROPN	PROPN	_	21	compound
20	standards	_	NOUN	NOUN	_	21	compound
21	committee	_	NOUN	NOUN	_	15	nmod
22	with	_	ADP	ADP	_	24	case
23	Albus	_	PROPN	PROPN	_	24	compound
24	Dumbledore	_	PROPN	PROPN	_	21	nmod
25	,	_	PUNCT	PUNCT	_	6	punct
26	Luna	_	NOUN	NOUN	_	6	nmod
27	Lovegood	_	PROPN	PROPN	_	30	nmod:poss
28	's	_	PART	PART	_	27	case
29	news	_	NOUN	NOUN	_	30	compound
30	agency	_	NOUN	NOUN	_	6	nmod
31	reported	_	VERB	VERB	_	6	advcl
32	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test138': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test138']['sents']['0']:
            print(return_dict['test138']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test138']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test138 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test138 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test138']['sents']['0']:
        verbs=return_dict['test138']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test138']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test138']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test138():
    text="""Gryffindor's head Minerva McGonagall left for the Ministry of 
Magic on Wednesday for meetings of the joint OWL standards 
committee with Albus Dumbledore, Luna Lovegood's news agency reported. 
"""
    parse="""1	Gryffindor	_	PROPN	PROPN	_	3	nmod:poss
2	's	_	PART	PART	_	1	case
3	head	_	NOUN	NOUN	_	5	compound
4	Minerva	_	PROPN	PROPN	_	5	name
5	McGonagall	_	PROPN	PROPN	_	6	nsubj
6	left	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	Ministry	_	PROPN	PROPN	_	6	nmod
10	of	_	ADP	ADP	_	11	case
11	Magic	_	PROPN	PROPN	_	9	nmod
12	on	_	ADP	ADP	_	13	case
13	Wednesday	_	PROPN	PROPN	_	6	nmod
14	for	_	ADP	ADP	_	15	case
15	meetings	_	NOUN	NOUN	_	6	nmod
16	of	_	ADP	ADP	_	21	case
17	the	_	DET	DET	_	21	det
18	joint	_	ADJ	ADJ	_	21	amod
19	OWL	_	PROPN	PROPN	_	21	compound
20	standards	_	NOUN	NOUN	_	21	compound
21	committee	_	NOUN	NOUN	_	15	nmod
22	with	_	ADP	ADP	_	24	case
23	Albus	_	PROPN	PROPN	_	24	compound
24	Dumbledore	_	PROPN	PROPN	_	21	nmod
25	,	_	PUNCT	PUNCT	_	6	punct
26	Luna	_	NOUN	NOUN	_	6	nmod
27	Lovegood	_	PROPN	PROPN	_	30	nmod:poss
28	's	_	PART	PART	_	27	case
29	news	_	NOUN	NOUN	_	30	compound
30	agency	_	NOUN	NOUN	_	6	nmod
31	reported	_	VERB	VERB	_	6	advcl
32	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test139': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test139']['sents']['0']:
            print(return_dict['test139']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test139']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test139 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test139 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test139']['sents']['0']:
        verbs=return_dict['test139']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test139']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test139']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test139():
    text="""The Kuwait government is about to restore full diplomatic ties with Libya almost 
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Kuwait	_	PROPN	PROPN	_	3	compound
3	government	_	NOUN	NOUN	_	4	nsubj
4	is	_	VERB	VERB	_	22	ccomp
5	about	_	ADV	ADV	_	7	advmod
6	to	_	PART	PART	_	7	mark
7	restore	_	VERB	VERB	_	4	advcl
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	7	dobj
11	with	_	ADP	ADP	_	12	case
12	Libya	_	PROPN	PROPN	_	10	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	crowds	_	NOUN	NOUN	_	15	nsubj
15	trashed	_	VERB	VERB	_	7	advcl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	22	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	22	nsubj
22	said	_	VERB	VERB	_	0	root
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test140': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"KUWGOV\", u\"LBY\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test140']['sents']['0']:
            print(return_dict['test140']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"KUWGOV\", u\"LBY\", u\"064\")@ " + str(return_dict['test140']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"KUWGOV\", u\"LBY\", u\"064\")@ noevent  " )
            print("test140 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"KUWGOV\", u\"LBY\", u\"064\")@ noeventexception \n " )
        print("test140 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test140']['sents']['0']:
        verbs=return_dict['test140']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test140']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test140']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test140():
    text="""The KU basketball team is about to restore full diplomatic ties with Libya almost 
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	KU	_	PROPN	PROPN	_	4	compound
3	basketball	_	NOUN	NOUN	_	4	compound
4	team	_	NOUN	NOUN	_	5	nsubj
5	is	_	VERB	VERB	_	23	ccomp
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Libya	_	PROPN	PROPN	_	11	nmod
14	almost	_	ADV	ADV	_	15	advmod
15	crowds	_	NOUN	NOUN	_	16	nsubj
16	trashed	_	VERB	VERB	_	8	advcl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	23	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	23	nsubj
23	said	_	VERB	VERB	_	0	root
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	23	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test141': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test141']['sents']['0']:
            print(return_dict['test141']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ " + str(return_dict['test141']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ noevent  " )
            print("test141 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ noeventexception \n " )
        print("test141 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test141']['sents']['0']:
        verbs=return_dict['test141']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test141']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test141']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test141():
    text="""The K.U. basketball team is about to restore full diplomatic ties with Libya almost 
crowds trashed its embassy. 
"""
    parse="""1	The	_	DET	DET	_	4	det
2	K.U.	_	NOUN	NOUN	_	3	compound
3	basketball	_	NOUN	NOUN	_	4	compound
4	team	_	NOUN	NOUN	_	5	nsubj
5	is	_	VERB	VERB	_	0	root
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	full	_	ADJ	ADJ	_	11	amod
10	diplomatic	_	ADJ	ADJ	_	11	amod
11	ties	_	NOUN	NOUN	_	8	dobj
12	with	_	ADP	ADP	_	13	case
13	Libya	_	PROPN	PROPN	_	11	nmod
14	almost	_	ADV	ADV	_	16	advmod
15	crowds	_	NOUN	NOUN	_	16	nsubj
16	trashed	_	VERB	VERB	_	8	advcl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test142': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test142']['sents']['0']:
            print(return_dict['test142']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ " + str(return_dict['test142']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ noevent  " )
            print("test142 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USAEDU\", u\"LBY\", u\"064\")@ noeventexception \n " )
        print("test142 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test142']['sents']['0']:
        verbs=return_dict['test142']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test142']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test142']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test142():
    text="""The Australian government is about to restore full diplomatic ties with Libya almost 
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Australian	_	ADJ	ADJ	_	3	amod
3	government	_	NOUN	NOUN	_	4	nsubj
4	is	_	VERB	VERB	_	22	ccomp
5	about	_	ADV	ADV	_	7	advmod
6	to	_	PART	PART	_	7	mark
7	restore	_	VERB	VERB	_	4	advcl
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	7	dobj
11	with	_	ADP	ADP	_	12	case
12	Libya	_	PROPN	PROPN	_	10	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	crowds	_	NOUN	NOUN	_	15	nsubj
15	trashed	_	VERB	VERB	_	7	advcl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	22	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	22	nsubj
22	said	_	VERB	VERB	_	0	root
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test143': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"AUSGOV\", u\"LBY\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test143']['sents']['0']:
            print(return_dict['test143']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"AUSGOV\", u\"LBY\", u\"064\")@ " + str(return_dict['test143']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"AUSGOV\", u\"LBY\", u\"064\")@ noevent  " )
            print("test143 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"AUSGOV\", u\"LBY\", u\"064\")@ noeventexception \n " )
        print("test143 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test143']['sents']['0']:
        verbs=return_dict['test143']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test143']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test143']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test143():
    text="""The AU is about to restore full diplomatic ties with Libya almost 
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	The	_	DET	DET	_	2	det
2	AU	_	PROPN	PROPN	_	3	nsubj
3	is	_	VERB	VERB	_	21	ccomp
4	about	_	ADV	ADV	_	6	advmod
5	to	_	PART	PART	_	6	mark
6	restore	_	VERB	VERB	_	3	advcl
7	full	_	ADJ	ADJ	_	9	amod
8	diplomatic	_	ADJ	ADJ	_	9	amod
9	ties	_	NOUN	NOUN	_	6	dobj
10	with	_	ADP	ADP	_	11	case
11	Libya	_	PROPN	PROPN	_	9	nmod
12	almost	_	ADV	ADV	_	14	advmod
13	crowds	_	NOUN	NOUN	_	14	nsubj
14	trashed	_	VERB	VERB	_	6	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	21	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	21	nsubj
21	said	_	VERB	VERB	_	0	root
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	21	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test144': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"IGOAFR\", u\"LBY\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test144']['sents']['0']:
            print(return_dict['test144']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"IGOAFR\", u\"LBY\", u\"064\")@ " + str(return_dict['test144']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"IGOAFR\", u\"LBY\", u\"064\")@ noevent  " )
            print("test144 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"IGOAFR\", u\"LBY\", u\"064\")@ noeventexception \n " )
        print("test144 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test144']['sents']['0']:
        verbs=return_dict['test144']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test144']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test144']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test144():
    text="""The Hermit Kingdom fired two artillery shells at New Zealand on Thursday.
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Hermit	_	PROPN	PROPN	_	3	compound
3	Kingdom	_	PROPN	PROPN	_	4	nsubj
4	fired	_	VERB	VERB	_	0	root
5	two	_	NUM	NUM	_	7	nummod
6	artillery	_	NOUN	NOUN	_	7	compound
7	shells	_	NOUN	NOUN	_	4	dobj
8	at	_	ADP	ADP	_	10	case
9	New	_	PROPN	PROPN	_	10	compound
10	Zealand	_	PROPN	PROPN	_	7	nmod
11	on	_	ADP	ADP	_	12	case
12	Thursday	_	PROPN	PROPN	_	4	nmod
13	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test145': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"NZE\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test145']['sents']['0']:
            print(return_dict['test145']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"NZE\", u\"194\")@ " + str(return_dict['test145']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"NZE\", u\"194\")@ noevent  " )
            print("test145 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"NZE\", u\"194\")@ noeventexception \n " )
        print("test145 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test145']['sents']['0']:
        verbs=return_dict['test145']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test145']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test145']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test145():
    text="""The Hermit Kingdom fired two artillery shells at Zealand on Thursday.
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Hermit	_	PROPN	PROPN	_	3	compound
3	Kingdom	_	PROPN	PROPN	_	4	nsubj
4	fired	_	VERB	VERB	_	0	root
5	two	_	NUM	NUM	_	7	nummod
6	artillery	_	NOUN	NOUN	_	7	compound
7	shells	_	NOUN	NOUN	_	4	dobj
8	at	_	ADP	ADP	_	9	case
9	Zealand	_	PROPN	PROPN	_	7	nmod
10	on	_	ADP	ADP	_	11	case
11	Thursday	_	PROPN	PROPN	_	4	nmod
12	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test146': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"DNK\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test146']['sents']['0']:
            print(return_dict['test146']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"DNK\", u\"194\")@ " + str(return_dict['test146']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"DNK\", u\"194\")@ noevent  " )
            print("test146 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"DNK\", u\"194\")@ noeventexception \n " )
        print("test146 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test146']['sents']['0']:
        verbs=return_dict['test146']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test146']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test146']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test146():
    text="""The United States on Thursday fired two artillery shells at Seoul.
"""
    parse="""1	The	_	DET	DET	_	3	det
2	United	_	PROPN	PROPN	_	3	compound
3	States	_	PROPN	PROPN	_	6	nsubj
4	on	_	ADP	ADP	_	5	case
5	Thursday	_	PROPN	PROPN	_	3	nmod
6	fired	_	VERB	VERB	_	0	root
7	two	_	NUM	NUM	_	9	nummod
8	artillery	_	NOUN	NOUN	_	9	compound
9	shells	_	NOUN	NOUN	_	6	dobj
10	at	_	ADP	ADP	_	11	case
11	Seoul	_	PROPN	PROPN	_	9	nmod
12	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test147': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USA\", u\"KOR\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test147']['sents']['0']:
            print(return_dict['test147']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USA\", u\"KOR\", u\"194\")@ " + str(return_dict['test147']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USA\", u\"KOR\", u\"194\")@ noevent  " )
            print("test147 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"USA\", u\"KOR\", u\"194\")@ noeventexception \n " )
        print("test147 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test147']['sents']['0']:
        verbs=return_dict['test147']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test147']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test147']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test147():
    text="""North Korea on Thursday fired two artillery shells near a naval vessel from South Korea 
on a routine patrol of an area south of the two nations’ disputed maritime boundary in the Yellow Sea, according to reports.
"""
    parse="""1	North	_	PROPN	PROPN	_	2	compound
2	Korea	_	PROPN	PROPN	_	5	nsubj
3	on	_	ADP	ADP	_	4	case
4	Thursday	_	PROPN	PROPN	_	2	nmod
5	fired	_	VERB	VERB	_	0	root
6	two	_	NUM	NUM	_	8	nummod
7	artillery	_	NOUN	NOUN	_	8	compound
8	shells	_	NOUN	NOUN	_	5	dobj
9	near	_	ADP	ADP	_	12	case
10	a	_	DET	DET	_	12	det
11	naval	_	ADJ	ADJ	_	12	amod
12	vessel	_	NOUN	NOUN	_	5	nmod
13	from	_	ADP	ADP	_	15	case
14	South	_	PROPN	PROPN	_	15	compound
15	Korea	_	PROPN	PROPN	_	12	nmod
16	on	_	ADP	ADP	_	19	case
17	a	_	DET	DET	_	19	det
18	routine	_	ADJ	ADJ	_	19	amod
19	patrol	_	NOUN	NOUN	_	5	nmod
20	of	_	ADP	ADP	_	23	case
21	an	_	DET	DET	_	23	det
22	area	_	NOUN	NOUN	_	23	compound
23	south	_	NOUN	NOUN	_	19	nmod
24	of	_	ADP	ADP	_	27	case
25	the	_	DET	DET	_	27	det
26	two	_	NUM	NUM	_	27	nummod
27	nations	_	NOUN	NOUN	_	23	nmod
28	'	_	PUNCT	PUNCT	_	27	punct
29	disputed	_	VERB	VERB	_	5	advcl
30	maritime	_	ADJ	ADJ	_	31	amod
31	boundary	_	NOUN	NOUN	_	29	dobj
32	in	_	ADP	ADP	_	35	case
33	the	_	DET	DET	_	35	det
34	Yellow	_	ADJ	ADJ	_	35	amod
35	Sea	_	NOUN	NOUN	_	31	nmod
36	,	_	PUNCT	PUNCT	_	29	punct
37	according	_	VERB	VERB	_	29	conj
38	to	_	PART	PART	_	39	mark
39	reports	_	VERB	VERB	_	37	xcomp
40	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test148': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test148']['sents']['0']:
            print(return_dict['test148']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ " + str(return_dict['test148']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noevent  " )
            print("test148 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noeventexception \n " )
        print("test148 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test148']['sents']['0']:
        verbs=return_dict['test148']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test148']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test148']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test148():
    text="""Pyongyang on Thursday fired two artillery shells at Seoul.
"""
    parse="""1	Pyongyang	_	VERB	VERB	_	0	root
2	on	_	ADP	ADP	_	3	case
3	Thursday	_	PROPN	PROPN	_	1	nmod
4	fired	_	VERB	VERB	_	1	advcl
5	two	_	NUM	NUM	_	7	nummod
6	artillery	_	NOUN	NOUN	_	7	compound
7	shells	_	NOUN	NOUN	_	4	dobj
8	at	_	ADP	ADP	_	9	case
9	Seoul	_	PROPN	PROPN	_	7	nmod
10	.	_	PUNCT	PUNCT	_	1	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test149': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test149']['sents']['0']:
            print(return_dict['test149']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ " + str(return_dict['test149']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noevent  " )
            print("test149 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noeventexception \n " )
        print("test149 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test149']['sents']['0']:
        verbs=return_dict['test149']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test149']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test149']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test149():
    text="""The Hermit Kingdom fired two artillery shells at Seoul on Thursday.
"""
    parse="""1	The	_	DET	DET	_	3	det
2	Hermit	_	PROPN	PROPN	_	3	compound
3	Kingdom	_	PROPN	PROPN	_	4	nsubj
4	fired	_	VERB	VERB	_	0	root
5	two	_	NUM	NUM	_	7	nummod
6	artillery	_	NOUN	NOUN	_	7	compound
7	shells	_	NOUN	NOUN	_	4	dobj
8	at	_	ADP	ADP	_	9	case
9	Seoul	_	PROPN	PROPN	_	7	nmod
10	on	_	ADP	ADP	_	11	case
11	Thursday	_	PROPN	PROPN	_	4	nmod
12	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test150': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test150']['sents']['0']:
            print(return_dict['test150']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ " + str(return_dict['test150']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noevent  " )
            print("test150 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PRK\", u\"KOR\", u\"194\")@ noeventexception \n " )
        print("test150 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test150']['sents']['0']:
        verbs=return_dict['test150']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test150']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test150']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test150():
    text="""Ethiopia has broken relations with Libya almost five years after crowds 
trashed its embassy. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	broken	_	VERB	VERB	_	0	root
4	relations	_	NOUN	NOUN	_	3	dobj
5	with	_	ADP	ADP	_	6	case
6	Libya	_	PROPN	PROPN	_	3	nmod
7	almost	_	ADV	ADV	_	8	advmod
8	five	_	NUM	NUM	_	9	nummod
9	years	_	NOUN	NOUN	_	3	nmod
10	after	_	ADP	ADP	_	11	case
11	crowds	_	NOUN	NOUN	_	9	nmod
12	trashed	_	VERB	VERB	_	3	advcl
13	its	_	PRON	PRON	_	14	nmod:poss
14	embassy	_	NOUN	NOUN	_	12	dobj
15	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test151': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test151']['sents']['0']:
            print(return_dict['test151']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ " + str(return_dict['test151']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noevent  " )
            print("test151 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noeventexception \n " )
        print("test151 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test151']['sents']['0']:
        verbs=return_dict['test151']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test151']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test151']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test151():
    text="""Ethiopia has broken down relations with Libya almost five years after crowds 
trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	broken	_	VERB	VERB	_	0	root
4	down	_	ADP	ADP	_	3	compound:prt
5	relations	_	NOUN	NOUN	_	3	nmod
6	with	_	ADP	ADP	_	7	case
7	Libya	_	PROPN	PROPN	_	3	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	3	nmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	10	nmod
13	trashed	_	VERB	VERB	_	3	advcl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	,	_	PUNCT	PUNCT	_	15	punct
17	a	_	DET	DET	_	19	det
18	senior	_	ADJ	ADJ	_	19	amod
19	official	_	NOUN	NOUN	_	15	appos
20	said	_	VERB	VERB	_	19	acl
21	on	_	ADP	ADP	_	22	case
22	Saturday	_	PROPN	PROPN	_	20	nmod
23	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test152': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test152']['sents']['0']:
            print(return_dict['test152']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ " + str(return_dict['test152']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noevent  " )
            print("test152 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noeventexception \n " )
        print("test152 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test152']['sents']['0']:
        verbs=return_dict['test152']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test152']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test152']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test152():
    text="""Ethiopia will break relations with Libya almost five years after crowds 
trashed its embassy.
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	break	_	VERB	VERB	_	0	root
4	relations	_	NOUN	NOUN	_	3	dobj
5	with	_	ADP	ADP	_	6	case
6	Libya	_	PROPN	PROPN	_	3	nmod
7	almost	_	ADV	ADV	_	8	advmod
8	five	_	NUM	NUM	_	9	nummod
9	years	_	NOUN	NOUN	_	3	nmod
10	after	_	ADP	ADP	_	11	case
11	crowds	_	NOUN	NOUN	_	9	nmod
12	trashed	_	VERB	VERB	_	3	advcl
13	its	_	PRON	PRON	_	14	nmod:poss
14	embassy	_	NOUN	NOUN	_	12	dobj
15	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test153': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test153']['sents']['0']:
            print(return_dict['test153']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ " + str(return_dict['test153']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noevent  " )
            print("test153 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noeventexception \n " )
        print("test153 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test153']['sents']['0']:
        verbs=return_dict['test153']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test153']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test153']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test153():
    text="""Ethiopia broken down a treaty with Libya's  almost five years after 
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	broken	_	VERB	VERB	_	21	advcl
3	down	_	ADP	ADP	_	5	case
4	a	_	DET	DET	_	5	det
5	treaty	_	NOUN	NOUN	_	2	nmod
6	with	_	ADP	ADP	_	11	case
7	Libya	_	PROPN	PROPN	_	11	nmod:poss
8	's	_	PART	PART	_	7	case
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	5	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	21	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	21	nsubj
21	said	_	VERB	VERB	_	0	root
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	21	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test154': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test154']['sents']['0']:
            print(return_dict['test154']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ " + str(return_dict['test154']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ noevent  " )
            print("test154 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ noeventexception \n " )
        print("test154 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test154']['sents']['0']:
        verbs=return_dict['test154']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test154']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test154']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test154():
    text="""Ethiopia broken down a treaty with Libya's  almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	broken	_	VERB	VERB	_	21	advcl
3	down	_	ADP	ADP	_	5	case
4	a	_	DET	DET	_	5	det
5	treaty	_	NOUN	NOUN	_	2	nmod
6	with	_	ADP	ADP	_	11	case
7	Libya	_	PROPN	PROPN	_	11	nmod:poss
8	's	_	PART	PART	_	7	case
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	5	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	21	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	21	nsubj
21	said	_	VERB	VERB	_	0	root
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	21	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test155': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test155']['sents']['0']:
            print(return_dict['test155']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ " + str(return_dict['test155']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ noevent  " )
            print("test155 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"161\")@ noeventexception \n " )
        print("test155 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test155']['sents']['0']:
        verbs=return_dict['test155']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test155']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test155']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test155():
    text="""Ethiopia is acting strangely with Libya almost five years after  
crowds trashed its embassy. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	is	_	AUX	AUX	_	3	aux
3	acting	_	VERB	VERB	_	0	root
4	strangely	_	ADV	ADV	_	3	advmod
5	with	_	ADP	ADP	_	6	case
6	Libya	_	PROPN	PROPN	_	3	nmod
7	almost	_	ADV	ADV	_	8	advmod
8	five	_	NUM	NUM	_	9	nummod
9	years	_	NOUN	NOUN	_	3	nmod
10	after	_	ADP	ADP	_	11	case
11	crowds	_	NOUN	NOUN	_	9	nmod
12	trashed	_	VERB	VERB	_	3	advcl
13	its	_	PRON	PRON	_	14	nmod:poss
14	embassy	_	NOUN	NOUN	_	12	dobj
15	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test156': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test156']['sents']['0']:
            print(return_dict['test156']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ " + str(return_dict['test156']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ noevent  " )
            print("test156 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ noeventexception \n " )
        print("test156 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test156']['sents']['0']:
        verbs=return_dict['test156']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test156']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test156']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test156():
    text="""Ethiopia has acted oddly with respect to Libya almost five years after  
crowds trashed its embassy
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	acted	_	VERB	VERB	_	0	root
4	oddly	_	ADV	ADV	_	3	advmod
5	with	_	ADP	ADP	_	6	case
6	respect	_	NOUN	NOUN	_	3	nmod
7	to	_	ADP	ADP	_	8	case
8	Libya	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test157': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test157']['sents']['0']:
            print(return_dict['test157']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ " + str(return_dict['test157']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ noevent  " )
            print("test157 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"100\")@ noeventexception \n " )
        print("test157 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test157']['sents']['0']:
        verbs=return_dict['test157']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test157']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test157']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test157():
    text="""Ethiopia indicated it would act now with Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	indicated	_	VERB	VERB	_	0	root
3	it	_	PRON	PRON	_	5	nsubj
4	would	_	AUX	AUX	_	5	aux
5	act	_	VERB	VERB	_	2	ccomp
6	now	_	ADV	ADV	_	5	advmod
7	with	_	ADP	ADP	_	8	case
8	Libya	_	PROPN	PROPN	_	5	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	5	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test158': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test158']['sents']['0']:
            print(return_dict['test158']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ " + str(return_dict['test158']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ noevent  " )
            print("test158 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ noeventexception \n " )
        print("test158 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test158']['sents']['0']:
        verbs=return_dict['test158']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test158']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test158']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test158():
    text="""Ethiopia indicated it would acting now  with Libya's  almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	indicated	_	VERB	VERB	_	0	root
3	it	_	PRON	PRON	_	5	nsubj
4	would	_	AUX	AUX	_	5	aux
5	acting	_	VERB	VERB	_	2	ccomp
6	now	_	ADV	ADV	_	5	advmod
7	with	_	ADP	ADP	_	12	case
8	Libya	_	PROPN	PROPN	_	12	nmod:poss
9	's	_	PART	PART	_	8	case
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	5	nmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	12	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test159': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test159']['sents']['0']:
            print(return_dict['test159']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ " + str(return_dict['test159']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ noevent  " )
            print("test159 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1010\")@ noeventexception \n " )
        print("test159 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test159']['sents']['0']:
        verbs=return_dict['test159']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test159']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test159']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test159():
    text="""Ethiopia indicated it should have acted against Libya almost five years after  
crowds trashed its embassy. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	indicated	_	VERB	VERB	_	0	root
3	it	_	PRON	PRON	_	6	nsubj
4	should	_	AUX	AUX	_	6	aux
5	have	_	AUX	AUX	_	6	aux
6	acted	_	VERB	VERB	_	2	ccomp
7	against	_	ADP	ADP	_	8	case
8	Libya	_	PROPN	PROPN	_	6	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	6	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	6	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test160': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1011\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test160']['sents']['0']:
            print(return_dict['test160']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1011\")@ " + str(return_dict['test160']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1011\")@ noevent  " )
            print("test160 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1011\")@ noeventexception \n " )
        print("test160 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test160']['sents']['0']:
        verbs=return_dict['test160']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test160']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test160']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test160():
    text="""Ethiopia act on a resolution  with Libya's  almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	act	_	VERB	VERB	_	21	advcl
3	on	_	ADP	ADP	_	5	case
4	a	_	DET	DET	_	5	det
5	resolution	_	NOUN	NOUN	_	2	nmod
6	with	_	ADP	ADP	_	11	case
7	Libya	_	PROPN	PROPN	_	11	nmod:poss
8	's	_	PART	PART	_	7	case
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	2	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	21	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	21	nsubj
21	said	_	VERB	VERB	_	0	root
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	21	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test161': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test161']['sents']['0']:
            print(return_dict['test161']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ " + str(return_dict['test161']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noevent  " )
            print("test161 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noeventexception \n " )
        print("test161 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test161']['sents']['0']:
        verbs=return_dict['test161']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test161']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test161']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test161():
    text="""Ethiopia is acting on a resolution with Libya's  almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	is	_	AUX	AUX	_	3	aux
3	acting	_	VERB	VERB	_	0	root
4	on	_	ADP	ADP	_	6	case
5	a	_	DET	DET	_	6	det
6	resolution	_	NOUN	NOUN	_	3	nmod
7	with	_	ADP	ADP	_	12	case
8	Libya	_	PROPN	PROPN	_	12	nmod:poss
9	's	_	PART	PART	_	8	case
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	3	nmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	12	nmod
15	trashed	_	VERB	VERB	_	3	advcl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test162': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test162']['sents']['0']:
            print(return_dict['test162']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ " + str(return_dict['test162']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noevent  " )
            print("test162 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noeventexception \n " )
        print("test162 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test162']['sents']['0']:
        verbs=return_dict['test162']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test162']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test162']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test162():
    text="""Ethiopia acted on a resolution against Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	acted	_	VERB	VERB	_	0	root
3	on	_	ADP	ADP	_	5	case
4	a	_	DET	DET	_	5	det
5	resolution	_	NOUN	NOUN	_	2	nmod
6	against	_	ADP	ADP	_	7	case
7	Libya	_	PROPN	PROPN	_	2	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	12	nmod:npmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	2	nmod
13	trashed	_	VERB	VERB	_	12	acl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	,	_	PUNCT	PUNCT	_	15	punct
17	a	_	DET	DET	_	19	det
18	senior	_	ADJ	ADJ	_	19	amod
19	official	_	NOUN	NOUN	_	15	appos
20	said	_	VERB	VERB	_	19	acl
21	on	_	ADP	ADP	_	22	case
22	Saturday	_	PROPN	PROPN	_	20	nmod
23	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test163': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test163']['sents']['0']:
            print(return_dict['test163']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ " + str(return_dict['test163']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noevent  " )
            print("test163 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"102\")@ noeventexception \n " )
        print("test163 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test163']['sents']['0']:
        verbs=return_dict['test163']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test163']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test163']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test163():
    text="""Ethiopia will act on some programs with Libya  almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	act	_	VERB	VERB	_	0	root
4	on	_	ADP	ADP	_	6	case
5	some	_	DET	DET	_	6	det
6	programs	_	NOUN	NOUN	_	3	nmod
7	with	_	ADP	ADP	_	8	case
8	Libya	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test164': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test164']['sents']['0']:
            print(return_dict['test164']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ " + str(return_dict['test164']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ noevent  " )
            print("test164 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ noeventexception \n " )
        print("test164 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test164']['sents']['0']:
        verbs=return_dict['test164']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test164']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test164']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test164():
    text="""Ethiopia acted on some programs with Libya almost five years after  
crowds trashed its embassy. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	acted	_	VERB	VERB	_	0	root
3	on	_	ADP	ADP	_	5	case
4	some	_	DET	DET	_	5	det
5	programs	_	NOUN	NOUN	_	2	nmod
6	with	_	ADP	ADP	_	7	case
7	Libya	_	PROPN	PROPN	_	2	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	12	nmod:npmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	2	nmod
13	trashed	_	VERB	VERB	_	12	acl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test165': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test165']['sents']['0']:
            print(return_dict['test165']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ " + str(return_dict['test165']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ noevent  " )
            print("test165 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"103\")@ noeventexception \n " )
        print("test165 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test165']['sents']['0']:
        verbs=return_dict['test165']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test165']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test165']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test165():
    text="""Ethiopia broken down with Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	broken	_	VERB	VERB	_	0	root
3	down	_	ADV	ADV	_	2	advmod
4	with	_	ADP	ADP	_	5	case
5	Libya	_	PROPN	PROPN	_	2	nmod
6	almost	_	ADV	ADV	_	7	advmod
7	five	_	NUM	NUM	_	8	nummod
8	years	_	NOUN	NOUN	_	10	nmod:npmod
9	after	_	ADP	ADP	_	10	case
10	crowds	_	NOUN	NOUN	_	2	nmod
11	trashed	_	VERB	VERB	_	10	acl
12	its	_	PRON	PRON	_	13	nmod:poss
13	embassy	_	NOUN	NOUN	_	11	dobj
14	,	_	PUNCT	PUNCT	_	13	punct
15	a	_	DET	DET	_	17	det
16	senior	_	ADJ	ADJ	_	17	amod
17	official	_	NOUN	NOUN	_	13	appos
18	said	_	VERB	VERB	_	17	acl
19	on	_	ADP	ADP	_	20	case
20	Saturday	_	PROPN	PROPN	_	18	nmod
21	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test166': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test166']['sents']['0']:
            print(return_dict['test166']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ " + str(return_dict['test166']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noevent  " )
            print("test166 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"1717\")@ noeventexception \n " )
        print("test166 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test166']['sents']['0']:
        verbs=return_dict['test166']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test166']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test166']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test166():
    text="""Ethiopia is about to depart from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	is	_	VERB	VERB	_	0	root
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	depart	_	VERB	VERB	_	2	advcl
6	from	_	ADP	ADP	_	7	case
7	Libya	_	PROPN	PROPN	_	5	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	12	nmod:npmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	5	nmod
13	trashed	_	VERB	VERB	_	5	advcl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	,	_	PUNCT	PUNCT	_	15	punct
17	a	_	DET	DET	_	19	det
18	senior	_	ADJ	ADJ	_	19	amod
19	official	_	NOUN	NOUN	_	15	appos
20	said	_	VERB	VERB	_	19	acl
21	on	_	ADP	ADP	_	22	case
22	Saturday	_	PROPN	PROPN	_	20	nmod
23	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test167': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test167']['sents']['0']:
            print(return_dict['test167']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ " + str(return_dict['test167']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noevent  " )
            print("test167 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noeventexception \n " )
        print("test167 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test167']['sents']['0']:
        verbs=return_dict['test167']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test167']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test167']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test167():
    text="""Ethiopia departs from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	departs	_	VERB	VERB	_	0	root
3	from	_	ADP	ADP	_	4	case
4	Libya	_	PROPN	PROPN	_	2	nmod
5	almost	_	ADV	ADV	_	6	advmod
6	five	_	NUM	NUM	_	7	nummod
7	years	_	NOUN	NOUN	_	9	nmod:npmod
8	after	_	ADP	ADP	_	9	case
9	crowds	_	NOUN	NOUN	_	2	nmod
10	trashed	_	VERB	VERB	_	2	advcl
11	its	_	PRON	PRON	_	12	nmod:poss
12	embassy	_	NOUN	NOUN	_	10	dobj
13	,	_	PUNCT	PUNCT	_	12	punct
14	a	_	DET	DET	_	16	det
15	senior	_	ADJ	ADJ	_	16	amod
16	official	_	NOUN	NOUN	_	12	appos
17	said	_	VERB	VERB	_	16	acl
18	on	_	ADP	ADP	_	19	case
19	Saturday	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test168': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test168']['sents']['0']:
            print(return_dict['test168']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ " + str(return_dict['test168']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noevent  " )
            print("test168 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noeventexception \n " )
        print("test168 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test168']['sents']['0']:
        verbs=return_dict['test168']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test168']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test168']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test168():
    text="""Ethiopia departed from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	departed	_	VERB	VERB	_	0	root
3	from	_	ADP	ADP	_	4	case
4	Libya	_	PROPN	PROPN	_	2	nmod
5	almost	_	ADV	ADV	_	6	advmod
6	five	_	NUM	NUM	_	7	nummod
7	years	_	NOUN	NOUN	_	9	nmod:npmod
8	after	_	ADP	ADP	_	9	case
9	crowds	_	NOUN	NOUN	_	2	nmod
10	trashed	_	VERB	VERB	_	2	advcl
11	its	_	PRON	PRON	_	12	nmod:poss
12	embassy	_	NOUN	NOUN	_	10	dobj
13	,	_	PUNCT	PUNCT	_	12	punct
14	a	_	DET	DET	_	16	det
15	senior	_	ADJ	ADJ	_	16	amod
16	official	_	NOUN	NOUN	_	12	appos
17	said	_	VERB	VERB	_	16	acl
18	on	_	ADP	ADP	_	19	case
19	Saturday	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test169': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test169']['sents']['0']:
            print(return_dict['test169']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ " + str(return_dict['test169']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noevent  " )
            print("test169 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"032\")@ noeventexception \n " )
        print("test169 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test169']['sents']['0']:
        verbs=return_dict['test169']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test169']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test169']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test169():
    text="""Ethiopia departx from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	compound
2	departx	_	PROPN	PROPN	_	17	nsubj
3	from	_	ADP	ADP	_	4	case
4	Libya	_	PROPN	PROPN	_	2	nmod
5	almost	_	ADV	ADV	_	6	advmod
6	five	_	NUM	NUM	_	7	nummod
7	years	_	NOUN	NOUN	_	9	nmod:npmod
8	after	_	ADP	ADP	_	9	case
9	crowds	_	NOUN	NOUN	_	2	nmod
10	trashed	_	VERB	VERB	_	9	acl
11	its	_	PRON	PRON	_	12	nmod:poss
12	embassy	_	NOUN	NOUN	_	10	dobj
13	,	_	PUNCT	PUNCT	_	17	punct
14	a	_	DET	DET	_	16	det
15	senior	_	ADJ	ADJ	_	16	amod
16	official	_	NOUN	NOUN	_	17	nsubj
17	said	_	VERB	VERB	_	0	root
18	on	_	ADP	ADP	_	19	case
19	Saturday	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	17	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test170': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test170']['sents']['0']:
            print(return_dict['test170']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test170']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test170 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test170 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test170']['sents']['0']:
        verbs=return_dict['test170']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test170']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test170']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test170():
    text="""Ethiopia departes from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	departes	_	VERB	VERB	_	0	root
3	from	_	ADP	ADP	_	4	case
4	Libya	_	PROPN	PROPN	_	2	nmod
5	almost	_	ADV	ADV	_	6	advmod
6	five	_	NUM	NUM	_	7	nummod
7	years	_	NOUN	NOUN	_	9	nmod:npmod
8	after	_	ADP	ADP	_	9	case
9	crowds	_	NOUN	NOUN	_	2	nmod
10	trashed	_	VERB	VERB	_	2	advcl
11	its	_	PRON	PRON	_	12	nmod:poss
12	embassy	_	NOUN	NOUN	_	10	dobj
13	,	_	PUNCT	PUNCT	_	12	punct
14	a	_	DET	DET	_	16	det
15	senior	_	ADJ	ADJ	_	16	amod
16	official	_	NOUN	NOUN	_	12	appos
17	said	_	VERB	VERB	_	16	acl
18	on	_	ADP	ADP	_	19	case
19	Saturday	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test171': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test171']['sents']['0']:
            print(return_dict['test171']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test171']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test171 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test171 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test171']['sents']['0']:
        verbs=return_dict['test171']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test171']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test171']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test171():
    text="""Ethiopia deplored from Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	deplored	_	VERB	VERB	_	0	root
3	from	_	ADP	ADP	_	4	case
4	Libya	_	PROPN	PROPN	_	2	nmod
5	almost	_	ADV	ADV	_	6	advmod
6	five	_	NUM	NUM	_	7	nummod
7	years	_	NOUN	NOUN	_	9	nmod:npmod
8	after	_	ADP	ADP	_	9	case
9	crowds	_	NOUN	NOUN	_	2	nmod
10	trashed	_	VERB	VERB	_	2	advcl
11	its	_	PRON	PRON	_	12	nmod:poss
12	embassy	_	NOUN	NOUN	_	10	dobj
13	,	_	PUNCT	PUNCT	_	12	punct
14	a	_	DET	DET	_	16	det
15	senior	_	ADJ	ADJ	_	16	amod
16	official	_	NOUN	NOUN	_	12	appos
17	said	_	VERB	VERB	_	16	acl
18	on	_	ADP	ADP	_	19	case
19	Saturday	_	PROPN	PROPN	_	17	nmod
20	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test172': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test172']['sents']['0']:
            print(return_dict['test172']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"122\")@ " + str(return_dict['test172']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"122\")@ noevent  " )
            print("test172 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"122\")@ noeventexception \n " )
        print("test172 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test172']['sents']['0']:
        verbs=return_dict['test172']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test172']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test172']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test172():
    text="""Ethiopia indicated it deplored Libya almost five years after  
crowds trashed its embassy, a senior official said on Saturday. 
"""
    parse="""1	Ethiopia	_	PROPN	PROPN	_	2	nsubj
2	indicated	_	VERB	VERB	_	0	root
3	it	_	PRON	PRON	_	4	nsubj
4	deplored	_	VERB	VERB	_	2	ccomp
5	Libya	_	PROPN	PROPN	_	4	dobj
6	almost	_	ADV	ADV	_	7	advmod
7	five	_	NUM	NUM	_	8	nummod
8	years	_	NOUN	NOUN	_	10	nmod:npmod
9	after	_	ADP	ADP	_	10	case
10	crowds	_	NOUN	NOUN	_	4	nmod
11	trashed	_	VERB	VERB	_	10	acl
12	its	_	PRON	PRON	_	13	nmod:poss
13	embassy	_	NOUN	NOUN	_	11	dobj
14	,	_	PUNCT	PUNCT	_	13	punct
15	a	_	DET	DET	_	17	det
16	senior	_	ADJ	ADJ	_	17	amod
17	official	_	NOUN	NOUN	_	13	appos
18	said	_	VERB	VERB	_	17	acl
19	on	_	ADP	ADP	_	20	case
20	Saturday	_	PROPN	PROPN	_	18	nmod
21	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test173': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"123\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test173']['sents']['0']:
            print(return_dict['test173']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"123\")@ " + str(return_dict['test173']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"123\")@ noevent  " )
            print("test173 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ETH\", u\"LBY\", u\"123\")@ noeventexception \n " )
        print("test173 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test173']['sents']['0']:
        verbs=return_dict['test173']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test173']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test173']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test173():
    text="""Gollum was seen to break into an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	3	nsubj
2	was	_	AUX	AUX	_	3	aux
3	seen	_	VERB	VERB	_	0	root
4	to	_	PART	PART	_	5	mark
5	break	_	VERB	VERB	_	3	xcomp
6	into	_	ADP	ADP	_	10	case
7	an	_	DET	DET	_	10	det
8	anti-	_	ADJ	ADJ	_	10	amod
9	Gondor	_	NOUN	NOUN	_	10	compound
10	parade	_	NOUN	NOUN	_	5	nmod
11	on	_	ADP	ADP	_	12	case
12	Saturday	_	PROPN	PROPN	_	5	nmod
13	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test174': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test174']['sents']['0']:
            print(return_dict['test174']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ " + str(return_dict['test174']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ noevent  " )
            print("test174 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ noeventexception \n " )
        print("test174 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test174']['sents']['0']:
        verbs=return_dict['test174']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test174']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test174']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test174():
    text="""Gollum abandoned an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	abandoned	_	VERB	VERB	_	0	root
3	an	_	DET	DET	_	6	det
4	anti-	_	ADJ	ADJ	_	6	amod
5	Gondor	_	NOUN	NOUN	_	6	compound
6	parade	_	NOUN	NOUN	_	2	dobj
7	on	_	ADP	ADP	_	8	case
8	Saturday	_	PROPN	PROPN	_	2	nmod
9	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test175': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test175']['sents']['0']:
            print(return_dict['test175']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ " + str(return_dict['test175']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ noevent  " )
            print("test175 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test175 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test175']['sents']['0']:
        verbs=return_dict['test175']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test175']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test175']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test175():
    text="""Gollum will bargain for asylum in Gondor, AFP reported. 
"""
    parse="""1	Gollum	_	NOUN	NOUN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	bargain	_	VERB	VERB	_	0	root
4	for	_	ADP	ADP	_	5	case
5	asylum	_	NOUN	NOUN	_	3	nmod
6	in	_	ADP	ADP	_	7	case
7	Gondor	_	PROPN	PROPN	_	3	nmod
8	,	_	PUNCT	PUNCT	_	3	punct
9	AFP	_	PROPN	PROPN	_	10	nsubj
10	reported	_	VERB	VERB	_	3	advcl
11	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test176': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174K\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test176']['sents']['0']:
            print(return_dict['test176']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174K\")@ " + str(return_dict['test176']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174K\")@ noevent  " )
            print("test176 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174K\")@ noeventexception \n " )
        print("test176 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test176']['sents']['0']:
        verbs=return_dict['test176']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test176']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test176']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test176():
    text="""Gollum will bargain foreign asylum in Gondor, AFP reported. 
"""
    parse="""1	Gollum	_	NOUN	NOUN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	bargain	_	VERB	VERB	_	0	root
4	foreign	_	ADJ	ADJ	_	5	amod
5	asylum	_	NOUN	NOUN	_	3	dobj
6	in	_	ADP	ADP	_	7	case
7	Gondor	_	PROPN	PROPN	_	3	nmod
8	,	_	PUNCT	PUNCT	_	3	punct
9	AFP	_	PROPN	PROPN	_	10	nsubj
10	reported	_	VERB	VERB	_	3	advcl
11	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test177': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174L\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test177']['sents']['0']:
            print(return_dict['test177']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174L\")@ " + str(return_dict['test177']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174L\")@ noevent  " )
            print("test177 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"174L\")@ noeventexception \n " )
        print("test177 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test177']['sents']['0']:
        verbs=return_dict['test177']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test177']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test177']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test177():
    text="""Gollum was known to break into an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	3	nsubj
2	was	_	AUX	AUX	_	3	aux
3	known	_	VERB	VERB	_	0	root
4	to	_	PART	PART	_	5	mark
5	break	_	VERB	VERB	_	3	xcomp
6	into	_	ADP	ADP	_	10	case
7	an	_	DET	DET	_	10	det
8	anti-	_	ADJ	ADJ	_	10	amod
9	Gondor	_	NOUN	NOUN	_	10	compound
10	parade	_	NOUN	NOUN	_	5	nmod
11	on	_	ADP	ADP	_	12	case
12	Saturday	_	PROPN	PROPN	_	5	nmod
13	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test178': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test178']['sents']['0']:
            print(return_dict['test178']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ " + str(return_dict['test178']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ noevent  " )
            print("test178 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"1717\")@ noeventexception \n " )
        print("test178 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test178']['sents']['0']:
        verbs=return_dict['test178']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test178']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test178']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test178():
    text="""Gollum was in an accord with an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	was	_	VERB	VERB	_	0	root
3	in	_	ADP	ADP	_	5	case
4	an	_	DET	DET	_	5	det
5	accord	_	NOUN	NOUN	_	2	nmod
6	with	_	ADP	ADP	_	10	case
7	an	_	DET	DET	_	10	det
8	anti-	_	ADJ	ADJ	_	10	amod
9	Gondor	_	NOUN	NOUN	_	10	compound
10	parade	_	NOUN	NOUN	_	2	nmod
11	on	_	ADP	ADP	_	12	case
12	Saturday	_	PROPN	PROPN	_	2	nmod
13	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test179': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ @ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test179']['sents']['0']:
            print(return_dict['test179']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ @ " + str(return_dict['test179']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ @ noevent  " )
            print("test179 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ @ noeventexception \n " )
        print("test179 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test179']['sents']['0']:
        verbs=return_dict['test179']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test179']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test179']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test179():
    text="""Ithilen's palace guard militia was freed from Barad-dur after that 
group yielded ground seized in six days of fighting.
"""
    parse="""1	Ithilen	_	PROPN	PROPN	_	5	nmod:poss
2	's	_	PART	PART	_	1	case
3	palace	_	NOUN	NOUN	_	4	compound
4	guard	_	NOUN	NOUN	_	5	compound
5	militia	_	NOUN	NOUN	_	7	nsubj
6	was	_	AUX	AUX	_	7	aux
7	freed	_	VERB	VERB	_	0	root
8	from	_	ADP	ADP	_	9	case
9	Barad-dur	_	PROPN	PROPN	_	7	nmod
10	after	_	ADP	ADP	_	12	case
11	that	_	DET	DET	_	12	det
12	group	_	NOUN	NOUN	_	7	nmod
13	yielded	_	VERB	VERB	_	7	advcl
14	ground	_	NOUN	NOUN	_	13	dobj
15	seized	_	VERB	VERB	_	14	acl
16	in	_	ADP	ADP	_	18	case
17	six	_	NUM	NUM	_	18	nummod
18	days	_	NOUN	NOUN	_	15	nmod
19	of	_	ADP	ADP	_	20	case
20	fighting	_	NOUN	NOUN	_	18	nmod
21	.	_	PUNCT	PUNCT	_	7	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test180': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950114'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"ITH\", u\"066\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test180']['sents']['0']:
            print(return_dict['test180']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"ITH\", u\"066\")@ " + str(return_dict['test180']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"ITH\", u\"066\")@ noevent  " )
            print("test180 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MOR\", u\"ITH\", u\"066\")@ noeventexception \n " )
        print("test180 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test180']['sents']['0']:
        verbs=return_dict['test180']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test180']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test180']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test180():
    text="""Fornost President Umbardacil has again appealed for peace in Ithilen state-run television in 
a message to the spiritual leader of the war-torn nation's influential 
Douzu community
"""
    parse="""1	Fornost	_	PROPN	PROPN	_	2	compound
2	President	_	PROPN	PROPN	_	3	compound
3	Umbardacil	_	PROPN	PROPN	_	6	nsubj
4	has	_	AUX	AUX	_	6	aux
5	again	_	ADV	ADV	_	6	advmod
6	appealed	_	VERB	VERB	_	0	root
7	for	_	ADP	ADP	_	8	case
8	peace	_	NOUN	NOUN	_	6	nmod
9	in	_	ADP	ADP	_	12	case
10	Ithilen	_	ADJ	ADJ	_	12	amod
11	state-run	_	NOUN	NOUN	_	12	compound
12	television	_	NOUN	NOUN	_	6	nmod
13	in	_	ADP	ADP	_	15	case
14	a	_	DET	DET	_	15	det
15	message	_	NOUN	NOUN	_	6	nmod
16	to	_	ADP	ADP	_	19	case
17	the	_	DET	DET	_	19	det
18	spiritual	_	ADJ	ADJ	_	19	amod
19	leader	_	NOUN	NOUN	_	15	nmod
20	of	_	ADP	ADP	_	27	case
21	the	_	DET	DET	_	23	det
22	war-torn	_	ADJ	ADJ	_	23	amod
23	nation	_	NOUN	NOUN	_	27	nmod:poss
24	's	_	PART	PART	_	23	case
25	influential	_	ADJ	ADJ	_	27	amod
26	Douzu	_	PROPN	PROPN	_	27	compound
27	community	_	NOUN	NOUN	_	19	nmod
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test181': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950116'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITHTV\", u\"095\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test181']['sents']['0']:
            print(return_dict['test181']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITHTV\", u\"095\")@ " + str(return_dict['test181']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITHTV\", u\"095\")@ noevent  " )
            print("test181 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"FORGOV\", u\"ITHTV\", u\"095\")@ noeventexception \n " )
        print("test181 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test181']['sents']['0']:
        verbs=return_dict['test181']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test181']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test181']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test181():
    text="""Gollum was seen to break in an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	3	nsubj
2	was	_	AUX	AUX	_	3	aux
3	seen	_	VERB	VERB	_	0	root
4	to	_	PART	PART	_	5	mark
5	break	_	VERB	VERB	_	3	xcomp
6	in	_	ADP	ADP	_	10	case
7	an	_	DET	DET	_	10	det
8	anti-	_	ADJ	ADJ	_	10	amod
9	Gondor	_	NOUN	NOUN	_	10	compound
10	parade	_	NOUN	NOUN	_	5	nmod
11	on	_	ADP	ADP	_	12	case
12	Saturday	_	PROPN	PROPN	_	5	nmod
13	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test182': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"HOB\", u\"075\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test182']['sents']['0']:
            print(return_dict['test182']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"HOB\", u\"075\")@ " + str(return_dict['test182']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"HOB\", u\"075\")@ noevent  " )
            print("test182 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"HOB\", u\"075\")@ noeventexception \n " )
        print("test182 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test182']['sents']['0']:
        verbs=return_dict['test182']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test182']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test182']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test182():
    text="""Gollum abandoned efforts to stop an anti- Gondor parade on Saturday. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	abandoned	_	VERB	VERB	_	0	root
3	efforts	_	NOUN	NOUN	_	2	dobj
4	to	_	PART	PART	_	5	mark
5	stop	_	VERB	VERB	_	3	acl
6	an	_	DET	DET	_	9	det
7	anti-	_	ADJ	ADJ	_	9	amod
8	Gondor	_	NOUN	NOUN	_	9	compound
9	parade	_	NOUN	NOUN	_	5	dobj
10	on	_	ADP	ADP	_	11	case
11	Saturday	_	PROPN	PROPN	_	5	nmod
12	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test183': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test183']['sents']['0']:
            print(return_dict['test183']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ " + str(return_dict['test183']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ noevent  " )
            print("test183 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test183 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test183']['sents']['0']:
        verbs=return_dict['test183']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test183']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test183']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test183():
    text="""Gollum allowed that Mordor isn't a really pleasant place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	allowed	_	VERB	VERB	_	0	root
3	that	_	SCONJ	SCONJ	_	10	mark
4	Mordor	_	PROPN	PROPN	_	10	nsubj
5	is	_	VERB	VERB	_	10	cop
6	n't	_	PART	PART	_	10	neg
7	a	_	DET	DET	_	10	det
8	really	_	ADV	ADV	_	9	advmod
9	pleasant	_	ADJ	ADJ	_	10	amod
10	place	_	NOUN	NOUN	_	2	ccomp
11	to	_	PART	PART	_	12	mark
12	visit	_	VERB	VERB	_	10	acl
13	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test184': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test184']['sents']['0']:
            print(return_dict['test184']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ " + str(return_dict['test184']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ noevent  " )
            print("test184 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ noeventexception \n " )
        print("test184 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test184']['sents']['0']:
        verbs=return_dict['test184']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test184']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test184']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test184():
    text="""Gollum allowed that Mordor isn't a real pleasant place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	allowed	_	VERB	VERB	_	0	root
3	that	_	SCONJ	SCONJ	_	10	mark
4	Mordor	_	PROPN	PROPN	_	10	nsubj
5	is	_	VERB	VERB	_	10	cop
6	n't	_	PART	PART	_	10	neg
7	a	_	DET	DET	_	10	det
8	real	_	ADJ	ADJ	_	10	amod
9	pleasant	_	ADJ	ADJ	_	10	amod
10	place	_	NOUN	NOUN	_	2	ccomp
11	to	_	PART	PART	_	12	mark
12	visit	_	VERB	VERB	_	10	acl
13	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test185': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test185']['sents']['0']:
            print(return_dict['test185']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ " + str(return_dict['test185']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ noevent  " )
            print("test185 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"024\")@ noeventexception \n " )
        print("test185 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test185']['sents']['0']:
        verbs=return_dict['test185']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test185']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test185']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test185():
    text="""Gollum allowed that Mordor isn't a real easy or pleasant place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	allowed	_	VERB	VERB	_	0	root
3	that	_	SCONJ	SCONJ	_	12	mark
4	Mordor	_	PROPN	PROPN	_	12	nsubj
5	is	_	VERB	VERB	_	12	advcl
6	n't	_	PART	PART	_	12	neg
7	a	_	DET	DET	_	12	det
8	real	_	ADJ	ADJ	_	12	amod
9	easy	_	ADJ	ADJ	_	12	amod
10	or	_	CONJ	CONJ	_	9	cc
11	pleasant	_	ADJ	ADJ	_	9	conj
12	place	_	NOUN	NOUN	_	2	ccomp
13	to	_	PART	PART	_	14	mark
14	visit	_	VERB	VERB	_	12	acl
15	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test186': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test186']['sents']['0']:
            print(return_dict['test186']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ " + str(return_dict['test186']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noevent  " )
            print("test186 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noeventexception \n " )
        print("test186 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test186']['sents']['0']:
        verbs=return_dict['test186']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test186']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test186']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test186():
    text="""Gollum recently allowed that Mordor isn't a such neat place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	3	nsubj
2	recently	_	ADV	ADV	_	3	advmod
3	allowed	_	VERB	VERB	_	0	root
4	that	_	SCONJ	SCONJ	_	11	mark
5	Mordor	_	PROPN	PROPN	_	11	nsubj
6	is	_	VERB	VERB	_	11	cop
7	n't	_	PART	PART	_	11	neg
8	a	_	DET	DET	_	11	det
9	such	_	ADJ	ADJ	_	11	amod
10	neat	_	ADJ	ADJ	_	11	amod
11	place	_	NOUN	NOUN	_	3	ccomp
12	to	_	PART	PART	_	13	mark
13	visit	_	VERB	VERB	_	11	acl
14	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test187': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"025\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test187']['sents']['0']:
            print(return_dict['test187']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"025\")@ " + str(return_dict['test187']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"025\")@ noevent  " )
            print("test187 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"025\")@ noeventexception \n " )
        print("test187 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test187']['sents']['0']:
        verbs=return_dict['test187']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test187']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test187']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test187():
    text="""Gollum recently did allow that Mordor isn't a such neat place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	4	nsubj
2	recently	_	ADV	ADV	_	4	advmod
3	did	_	AUX	AUX	_	4	aux
4	allow	_	VERB	VERB	_	0	root
5	that	_	SCONJ	SCONJ	_	12	mark
6	Mordor	_	PROPN	PROPN	_	12	nsubj
7	is	_	VERB	VERB	_	12	cop
8	n't	_	PART	PART	_	12	neg
9	a	_	DET	DET	_	12	det
10	such	_	ADJ	ADJ	_	12	amod
11	neat	_	ADJ	ADJ	_	12	amod
12	place	_	NOUN	NOUN	_	4	ccomp
13	to	_	PART	PART	_	14	mark
14	visit	_	VERB	VERB	_	12	acl
15	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test188': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test188']['sents']['0']:
            print(return_dict['test188']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ " + str(return_dict['test188']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noevent  " )
            print("test188 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noeventexception \n " )
        print("test188 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test188']['sents']['0']:
        verbs=return_dict['test188']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test188']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test188']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test188():
    text="""Gollum allowed that Mordor isn't the neatest place to visit. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	nsubj
2	allowed	_	VERB	VERB	_	0	root
3	that	_	SCONJ	SCONJ	_	9	mark
4	Mordor	_	PROPN	PROPN	_	9	nsubj
5	is	_	VERB	VERB	_	9	cop
6	n't	_	PART	PART	_	9	neg
7	the	_	DET	DET	_	9	det
8	neatest	_	ADJ	ADJ	_	9	amod
9	place	_	NOUN	NOUN	_	2	ccomp
10	to	_	PART	PART	_	11	mark
11	visit	_	VERB	VERB	_	9	acl
12	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test189': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"027\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test189']['sents']['0']:
            print(return_dict['test189']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"027\")@ " + str(return_dict['test189']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"027\")@ noevent  " )
            print("test189 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"027\")@ noeventexception \n " )
        print("test189 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test189']['sents']['0']:
        verbs=return_dict['test189']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test189']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test189']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test189():
    text="""Gollum in recent days did allow that Mordor isn't the neat or cool place to visit. 
"""
    parse="""1	Gollum	_	VERB	VERB	_	6	csubj
2	in	_	ADP	ADP	_	4	case
3	recent	_	ADJ	ADJ	_	4	amod
4	days	_	NOUN	NOUN	_	1	nmod
5	did	_	AUX	AUX	_	6	aux
6	allow	_	VERB	VERB	_	0	root
7	that	_	SCONJ	SCONJ	_	15	mark
8	Mordor	_	PROPN	PROPN	_	15	nsubj
9	is	_	VERB	VERB	_	15	advcl
10	n't	_	PART	PART	_	15	neg
11	the	_	DET	DET	_	15	det
12	neat	_	ADJ	ADJ	_	15	amod
13	or	_	CONJ	CONJ	_	12	cc
14	cool	_	ADJ	ADJ	_	12	conj
15	place	_	NOUN	NOUN	_	6	ccomp
16	to	_	PART	PART	_	17	mark
17	visit	_	VERB	VERB	_	15	acl
18	.	_	PUNCT	PUNCT	_	6	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test190': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test190']['sents']['0']:
            print(return_dict['test190']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ " + str(return_dict['test190']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noevent  " )
            print("test190 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"MOR\", u\"080\")@ noeventexception \n " )
        print("test190 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test190']['sents']['0']:
        verbs=return_dict['test190']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test190']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test190']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test190():
    text="""Gollum centre of a diplomatic row between Radagast the Brown called on 
Gondor late Sunday to be allowed to leave Lorien by elves. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	compound
2	centre	_	NOUN	NOUN	_	0	root
3	of	_	ADP	ADP	_	6	case
4	a	_	DET	DET	_	6	det
5	diplomatic	_	ADJ	ADJ	_	6	amod
6	row	_	NOUN	NOUN	_	2	nmod
7	between	_	ADP	ADP	_	8	case
8	Radagast	_	PROPN	PROPN	_	6	nmod
9	the	_	DET	DET	_	10	det
10	Brown	_	PROPN	PROPN	_	11	nsubj
11	called	_	VERB	VERB	_	6	acl
12	on	_	ADP	ADP	_	13	case
13	Gondor	_	PROPN	PROPN	_	11	nmod
14	late	_	ADV	ADV	_	15	advmod
15	Sunday	_	PROPN	PROPN	_	11	nmod
16	to	_	PART	PART	_	18	mark
17	be	_	AUX	AUX	_	18	aux
18	allowed	_	VERB	VERB	_	11	advcl
19	to	_	PART	PART	_	20	mark
20	leave	_	VERB	VERB	_	18	xcomp
21	Lorien	_	PROPN	PROPN	_	20	dobj
22	by	_	ADP	ADP	_	23	case
23	elves	_	PROPN	PROPN	_	20	nmod
24	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test191': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"095\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test191']['sents']['0']:
            print(return_dict['test191']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"095\")@ " + str(return_dict['test191']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"095\")@ noevent  " )
            print("test191 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"095\")@ noeventexception \n " )
        print("test191 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test191']['sents']['0']:
        verbs=return_dict['test191']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test191']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test191']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test191():
    text="""Gollum centre of a diplomatic row between Radagast the Brown called immediately for  
Gondor late Sunday to be allowed to leave Lorien by elves. 
"""
    parse="""1	Gollum	_	PROPN	PROPN	_	2	compound
2	centre	_	NOUN	NOUN	_	11	nsubj
3	of	_	ADP	ADP	_	6	case
4	a	_	DET	DET	_	6	det
5	diplomatic	_	ADJ	ADJ	_	6	amod
6	row	_	NOUN	NOUN	_	2	nmod
7	between	_	ADP	ADP	_	8	case
8	Radagast	_	PROPN	PROPN	_	6	nmod
9	the	_	DET	DET	_	10	det
10	Brown	_	PROPN	PROPN	_	8	appos
11	called	_	VERB	VERB	_	0	root
12	immediately	_	ADV	ADV	_	11	advmod
13	for	_	ADP	ADP	_	14	case
14	Gondor	_	PROPN	PROPN	_	11	nmod
15	late	_	ADV	ADV	_	16	advmod
16	Sunday	_	PROPN	PROPN	_	11	nmod
17	to	_	PART	PART	_	19	mark
18	be	_	AUX	AUX	_	19	aux
19	allowed	_	VERB	VERB	_	11	advcl
20	to	_	PART	PART	_	21	mark
21	leave	_	VERB	VERB	_	19	xcomp
22	Lorien	_	PROPN	PROPN	_	21	dobj
23	by	_	ADP	ADP	_	24	case
24	elves	_	PROPN	PROPN	_	21	nmod
25	.	_	PUNCT	PUNCT	_	11	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test192': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"096\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test192']['sents']['0']:
            print(return_dict['test192']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"096\")@ " + str(return_dict['test192']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"096\")@ noevent  " )
            print("test192 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"HOB\", u\"GON\", u\"096\")@ noeventexception \n " )
        print("test192 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test192']['sents']['0']:
        verbs=return_dict['test192']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test192']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test192']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test192():
    text="""Mordor will be hosting Osgiliath to celebrate Tabaski with Eriador
next week at Cirith Ungol. 
"""
    parse="""1	Mordor	_	NOUN	NOUN	_	4	nsubj
2	will	_	AUX	AUX	_	4	aux
3	be	_	AUX	AUX	_	4	aux
4	hosting	_	VERB	VERB	_	0	root
5	Osgiliath	_	PROPN	PROPN	_	4	dobj
6	to	_	PART	PART	_	7	mark
7	celebrate	_	VERB	VERB	_	4	xcomp
8	Tabaski	_	PROPN	PROPN	_	7	dobj
9	with	_	ADP	ADP	_	10	case
10	Eriador	_	PROPN	PROPN	_	8	nmod
11	next	_	ADJ	ADJ	_	12	amod
12	week	_	NOUN	NOUN	_	7	nmod
13	at	_	ADP	ADP	_	15	case
14	Cirith	_	PROPN	PROPN	_	15	compound
15	Ungol	_	PROPN	PROPN	_	7	nmod
16	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test193': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MORMIL\", u\"MOR\", u\"042\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test193']['sents']['0']:
            print(return_dict['test193']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MORMIL\", u\"MOR\", u\"042\")@ " + str(return_dict['test193']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MORMIL\", u\"MOR\", u\"042\")@ noevent  " )
            print("test193 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"MORMIL\", u\"MOR\", u\"042\")@ noeventexception \n " )
        print("test193 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test193']['sents']['0']:
        verbs=return_dict['test193']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test193']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test193']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test193():
    text="""Mordor will be hosting Osgiliath to celebrate May Day with Eriador
next week at Cirith Ungol. 
"""
    parse="""1	Mordor	_	NOUN	NOUN	_	4	nsubj
2	will	_	AUX	AUX	_	4	aux
3	be	_	AUX	AUX	_	4	aux
4	hosting	_	VERB	VERB	_	0	root
5	Osgiliath	_	PROPN	PROPN	_	4	dobj
6	to	_	PART	PART	_	7	mark
7	celebrate	_	VERB	VERB	_	4	xcomp
8	May	_	PROPN	PROPN	_	9	compound
9	Day	_	PROPN	PROPN	_	7	dobj
10	with	_	ADP	ADP	_	11	case
11	Eriador	_	PROPN	PROPN	_	9	nmod
12	next	_	ADJ	ADJ	_	13	amod
13	week	_	NOUN	NOUN	_	7	nmod:tmod
14	at	_	ADP	ADP	_	16	case
15	Cirith	_	PROPN	PROPN	_	16	compound
16	Ungol	_	PROPN	PROPN	_	7	nmod
17	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test194': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"MOR\", u\"046\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test194']['sents']['0']:
            print(return_dict['test194']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"MOR\", u\"046\")@ " + str(return_dict['test194']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"MOR\", u\"046\")@ noevent  " )
            print("test194 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ERI\", u\"MOR\", u\"046\")@ noeventexception \n " )
        print("test194 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test194']['sents']['0']:
        verbs=return_dict['test194']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test194']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test194']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test194():
    text="""Arnor has celebrated Eid at Osgiliath with Gondor after a 
hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	celebrated	_	VERB	VERB	_	0	root
4	Eid	_	PROPN	PROPN	_	3	dobj
5	at	_	ADP	ADP	_	6	case
6	Osgiliath	_	PROPN	PROPN	_	3	nmod
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	after	_	ADP	ADP	_	11	case
10	a	_	DET	DET	_	11	det
11	hafling	_	NOUN	NOUN	_	3	nmod
12	was	_	AUX	AUX	_	13	aux
13	reported	_	VERB	VERB	_	3	advcl
14	on	_	ADP	ADP	_	16	case
15	the	_	DET	DET	_	16	det
16	pass	_	NOUN	NOUN	_	13	nmod
17	of	_	ADP	ADP	_	19	case
18	Cirith	_	PROPN	PROPN	_	19	compound
19	Ungol	_	PROPN	PROPN	_	16	nmod
20	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test195': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test195']['sents']['0']:
            print(return_dict['test195']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ " + str(return_dict['test195']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ noevent  " )
            print("test195 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ noeventexception \n " )
        print("test195 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test195']['sents']['0']:
        verbs=return_dict['test195']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test195']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test195']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test195():
    text="""Arnor has celebrated Iftar in Osgiliath with the leaders of Gondor after leaving Eriador 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	celebrated	_	VERB	VERB	_	0	root
4	Iftar	_	PROPN	PROPN	_	3	dobj
5	in	_	ADP	ADP	_	6	case
6	Osgiliath	_	PROPN	PROPN	_	3	nmod
7	with	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	leaders	_	NOUN	NOUN	_	3	nmod
10	of	_	ADP	ADP	_	11	case
11	Gondor	_	PROPN	PROPN	_	9	nmod
12	after	_	SCONJ	SCONJ	_	13	mark
13	leaving	_	VERB	VERB	_	3	advcl
14	Eriador	_	PROPN	PROPN	_	13	dobj
15	when	_	ADV	ADV	_	19	mark
16	a	_	DET	DET	_	17	det
17	hafling	_	NOUN	NOUN	_	19	nsubj
18	was	_	AUX	AUX	_	19	aux
19	reported	_	VERB	VERB	_	13	advcl
20	on	_	ADP	ADP	_	22	case
21	the	_	DET	DET	_	22	det
22	pass	_	NOUN	NOUN	_	19	nmod
23	of	_	ADP	ADP	_	25	case
24	Cirith	_	PROPN	PROPN	_	25	compound
25	Ungol	_	PROPN	PROPN	_	22	nmod
26	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test196': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"045\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test196']['sents']['0']:
            print(return_dict['test196']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"045\")@ " + str(return_dict['test196']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"045\")@ noevent  " )
            print("test196 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"045\")@ noeventexception \n " )
        print("test196 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test196']['sents']['0']:
        verbs=return_dict['test196']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test196']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test196']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test196():
    text="""Arnor has celebrated Iftar at Osgiliath with the parliament of Gondor in Eriador 
after a hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	celebrated	_	VERB	VERB	_	0	root
4	Iftar	_	PROPN	PROPN	_	3	dobj
5	at	_	ADP	ADP	_	6	case
6	Osgiliath	_	PROPN	PROPN	_	3	nmod
7	with	_	ADP	ADP	_	9	case
8	the	_	DET	DET	_	9	det
9	parliament	_	NOUN	NOUN	_	3	nmod
10	of	_	ADP	ADP	_	11	case
11	Gondor	_	PROPN	PROPN	_	9	nmod
12	in	_	ADP	ADP	_	13	case
13	Eriador	_	PROPN	PROPN	_	3	nmod
14	after	_	ADP	ADP	_	16	case
15	a	_	DET	DET	_	16	det
16	hafling	_	NOUN	NOUN	_	3	nmod
17	was	_	AUX	AUX	_	18	aux
18	reported	_	VERB	VERB	_	3	advcl
19	on	_	ADP	ADP	_	21	case
20	the	_	DET	DET	_	21	det
21	pass	_	NOUN	NOUN	_	18	nmod
22	of	_	ADP	ADP	_	24	case
23	Cirith	_	PROPN	PROPN	_	24	compound
24	Ungol	_	PROPN	PROPN	_	21	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test197': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"044\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test197']['sents']['0']:
            print(return_dict['test197']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"044\")@ " + str(return_dict['test197']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"044\")@ noevent  " )
            print("test197 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"044\")@ noeventexception \n " )
        print("test197 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test197']['sents']['0']:
        verbs=return_dict['test197']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test197']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test197']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test197():
    text="""Arnor has celebrated Eid at United Arab Emirates with Gondor after a 
hafling was reported on the pass of Cirith Ungol. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	celebrated	_	VERB	VERB	_	0	root
4	Eid	_	PROPN	PROPN	_	3	dobj
5	at	_	ADP	ADP	_	8	case
6	United	_	PROPN	PROPN	_	8	compound
7	Arab	_	PROPN	PROPN	_	8	compound
8	Emirates	_	PROPN	PROPN	_	3	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	3	nmod
11	after	_	ADP	ADP	_	13	case
12	a	_	DET	DET	_	13	det
13	hafling	_	NOUN	NOUN	_	3	nmod
14	was	_	AUX	AUX	_	15	aux
15	reported	_	VERB	VERB	_	3	advcl
16	on	_	ADP	ADP	_	18	case
17	the	_	DET	DET	_	18	det
18	pass	_	NOUN	NOUN	_	15	nmod
19	of	_	ADP	ADP	_	21	case
20	Cirith	_	PROPN	PROPN	_	21	compound
21	Ungol	_	PROPN	PROPN	_	18	nmod
22	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test198': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test198']['sents']['0']:
            print(return_dict['test198']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ " + str(return_dict['test198']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ noevent  " )
            print("test198 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"043\")@ noeventexception \n " )
        print("test198 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test198']['sents']['0']:
        verbs=return_dict['test198']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test198']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test198']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test198():
    text="""Gondor launched a new bombing and shelling offensive against besieged 
Osgiliath during the night following daylight raids in which 
Arnor spokesmen said 54 civilians were killed or injured. 
"""
    parse="""1	Gondor	_	PROPN	PROPN	_	2	nsubj
2	launched	_	VERB	VERB	_	0	root
3	a	_	DET	DET	_	5	det
4	new	_	ADJ	ADJ	_	5	amod
5	bombing	_	NOUN	NOUN	_	2	dobj
6	and	_	CONJ	CONJ	_	2	cc
7	shelling	_	VERB	VERB	_	2	conj
8	offensive	_	ADJ	ADJ	_	7	dobj
9	against	_	ADP	ADP	_	11	case
10	besieged	_	ADJ	ADJ	_	11	amod
11	Osgiliath	_	PROPN	PROPN	_	7	nmod
12	during	_	ADP	ADP	_	14	case
13	the	_	DET	DET	_	14	det
14	night	_	NOUN	NOUN	_	7	nmod
15	following	_	VERB	VERB	_	17	amod
16	daylight	_	NOUN	NOUN	_	17	compound
17	raids	_	NOUN	NOUN	_	8	nmod
18	in	_	ADP	ADP	_	21	case
19	which	_	DET	DET	_	21	det
20	Arnor	_	PROPN	PROPN	_	21	compound
21	spokesmen	_	NOUN	NOUN	_	17	nmod
22	said	_	VERB	VERB	_	21	acl
23	54	_	NUM	NUM	_	24	nummod
24	civilians	_	NOUN	NOUN	_	26	nsubj
25	were	_	AUX	AUX	_	26	aux
26	killed	_	VERB	VERB	_	22	ccomp
27	or	_	CONJ	CONJ	_	26	cc
28	injured	_	VERB	VERB	_	26	conj
29	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test199': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19820727'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"223\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test199']['sents']['0']:
            print(return_dict['test199']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"223\")@ " + str(return_dict['test199']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"223\")@ noevent  " )
            print("test199 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"OSG\", u\"223\")@ noeventexception \n " )
        print("test199 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test199']['sents']['0']:
        verbs=return_dict['test199']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test199']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test199']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test199():
    text="""The Philippines was criticized over its territorial dispute with Eriador.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	4	nsubj
3	was	_	AUX	AUX	_	4	aux
4	criticized	_	VERB	VERB	_	0	root
5	over	_	ADP	ADP	_	8	case
6	its	_	PRON	PRON	_	8	nmod:poss
7	territorial	_	ADJ	ADJ	_	8	amod
8	dispute	_	NOUN	NOUN	_	4	nmod
9	with	_	ADP	ADP	_	10	case
10	Eriador	_	PROPN	PROPN	_	8	nmod
11	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test200': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"121\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test200']['sents']['0']:
            print(return_dict['test200']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"121\")@ " + str(return_dict['test200']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"121\")@ noevent  " )
            print("test200 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"121\")@ noeventexception \n " )
        print("test200 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test200']['sents']['0']:
        verbs=return_dict['test200']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test200']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test200']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test200():
    text="""The Philippines was heavily and unjustly criticized over its territorial dispute with Eriador.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	3	nsubj
3	was	_	VERB	VERB	_	0	root
4	heavily	_	ADV	ADV	_	3	advmod
5	and	_	CONJ	CONJ	_	3	cc
6	unjustly	_	ADV	ADV	_	7	advmod
7	criticized	_	VERB	VERB	_	3	conj
8	over	_	ADP	ADP	_	11	case
9	its	_	PRON	PRON	_	11	nmod:poss
10	territorial	_	ADJ	ADJ	_	11	amod
11	dispute	_	NOUN	NOUN	_	7	nmod
12	with	_	ADP	ADP	_	13	case
13	Eriador	_	PROPN	PROPN	_	11	nmod
14	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test201': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"123\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test201']['sents']['0']:
            print(return_dict['test201']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"123\")@ " + str(return_dict['test201']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"123\")@ noevent  " )
            print("test201 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"123\")@ noeventexception \n " )
        print("test201 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test201']['sents']['0']:
        verbs=return_dict['test201']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test201']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test201']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test201():
    text="""The Philippines was heavily criticized over its territorial dispute with Eriador.
"""
    parse="""1	The	_	DET	DET	_	2	det
2	Philippines	_	PROPN	PROPN	_	5	nsubj
3	was	_	AUX	AUX	_	5	aux
4	heavily	_	ADV	ADV	_	5	advmod
5	criticized	_	VERB	VERB	_	0	root
6	over	_	ADP	ADP	_	9	case
7	its	_	PRON	PRON	_	9	nmod:poss
8	territorial	_	ADJ	ADJ	_	9	amod
9	dispute	_	NOUN	NOUN	_	5	nmod
10	with	_	ADP	ADP	_	11	case
11	Eriador	_	PROPN	PROPN	_	9	nmod
12	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test202': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"122\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test202']['sents']['0']:
            print(return_dict['test202']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"122\")@ " + str(return_dict['test202']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"122\")@ noevent  " )
            print("test202 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"PHL\", u\"ERI\", u\"122\")@ noeventexception \n " )
        print("test202 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test202']['sents']['0']:
        verbs=return_dict['test202']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test202']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test202']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test202():
    text="""Eriador was opposed by Osgiliath, the state's fiercest foe, 
in being drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nsubj
2	was	_	AUX	AUX	_	3	aux
3	opposed	_	VERB	VERB	_	0	root
4	by	_	ADP	ADP	_	5	case
5	Osgiliath	_	PROPN	PROPN	_	3	nmod
6	,	_	PUNCT	PUNCT	_	3	punct
7	the	_	DET	DET	_	8	det
8	state	_	NOUN	NOUN	_	11	nmod:poss
9	's	_	PART	PART	_	8	case
10	fiercest	_	ADJ	ADJ	_	11	amod
11	foe	_	NOUN	NOUN	_	3	nmod
12	,	_	PUNCT	PUNCT	_	3	punct
13	in	_	SCONJ	SCONJ	_	15	mark
14	being	_	AUX	AUX	_	15	aux
15	drawn	_	VERB	VERB	_	3	advcl
16	into	_	ADP	ADP	_	19	case
17	the	_	DET	DET	_	19	det
18	peace	_	NOUN	NOUN	_	19	compound
19	process	_	NOUN	NOUN	_	15	nmod
20	by	_	ADP	ADP	_	22	case
21	its	_	PRON	PRON	_	22	nmod:poss
22	resumption	_	NOUN	NOUN	_	19	nmod
23	of	_	ADP	ADP	_	25	case
24	diplomatic	_	ADJ	ADJ	_	25	amod
25	ties	_	NOUN	NOUN	_	22	nmod
26	with	_	ADP	ADP	_	27	case
27	Gondor	_	PROPN	PROPN	_	25	nmod
28	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test203': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test203']['sents']['0']:
            print(return_dict['test203']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ " + str(return_dict['test203']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noevent  " )
            print("test203 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noeventexception \n " )
        print("test203 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test203']['sents']['0']:
        verbs=return_dict['test203']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test203']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test203']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test203():
    text="""Eriador was fiercely opposed by Osgiliath, the state's fiercest foe, 
in being drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	4	nsubj
2	was	_	AUX	AUX	_	4	aux
3	fiercely	_	ADV	ADV	_	4	advmod
4	opposed	_	VERB	VERB	_	0	root
5	by	_	ADP	ADP	_	6	case
6	Osgiliath	_	PROPN	PROPN	_	4	nmod
7	,	_	PUNCT	PUNCT	_	4	punct
8	the	_	DET	DET	_	9	det
9	state	_	NOUN	NOUN	_	12	nmod:poss
10	's	_	PART	PART	_	9	case
11	fiercest	_	ADJ	ADJ	_	12	amod
12	foe	_	NOUN	NOUN	_	4	nmod
13	,	_	PUNCT	PUNCT	_	4	punct
14	in	_	SCONJ	SCONJ	_	16	mark
15	being	_	AUX	AUX	_	16	aux
16	drawn	_	VERB	VERB	_	4	advcl
17	into	_	ADP	ADP	_	20	case
18	the	_	DET	DET	_	20	det
19	peace	_	NOUN	NOUN	_	20	compound
20	process	_	NOUN	NOUN	_	16	nmod
21	by	_	ADP	ADP	_	23	case
22	its	_	PRON	PRON	_	23	nmod:poss
23	resumption	_	NOUN	NOUN	_	20	nmod
24	of	_	ADP	ADP	_	26	case
25	diplomatic	_	ADJ	ADJ	_	26	amod
26	ties	_	NOUN	NOUN	_	23	nmod
27	with	_	ADP	ADP	_	28	case
28	Gondor	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test204': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test204']['sents']['0']:
            print(return_dict['test204']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ " + str(return_dict['test204']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noevent  " )
            print("test204 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noeventexception \n " )
        print("test204 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test204']['sents']['0']:
        verbs=return_dict['test204']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test204']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test204']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test204():
    text="""Eriador has received by courier money from Osgiliath, the state's 
fiercest foe, to be drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nsubj
2	has	_	AUX	AUX	_	3	aux
3	received	_	VERB	VERB	_	0	root
4	by	_	ADP	ADP	_	6	case
5	courier	_	NOUN	NOUN	_	6	compound
6	money	_	NOUN	NOUN	_	3	nmod
7	from	_	ADP	ADP	_	8	case
8	Osgiliath	_	PROPN	PROPN	_	3	nmod
9	,	_	PUNCT	PUNCT	_	3	punct
10	the	_	DET	DET	_	11	det
11	state	_	NOUN	NOUN	_	14	nmod:poss
12	's	_	PART	PART	_	11	case
13	fiercest	_	ADJ	ADJ	_	14	amod
14	foe	_	NOUN	NOUN	_	3	nmod
15	,	_	PUNCT	PUNCT	_	3	punct
16	to	_	PART	PART	_	18	mark
17	be	_	AUX	AUX	_	18	aux
18	drawn	_	VERB	VERB	_	3	advcl
19	into	_	ADP	ADP	_	22	case
20	the	_	DET	DET	_	22	det
21	peace	_	NOUN	NOUN	_	22	compound
22	process	_	NOUN	NOUN	_	18	nmod
23	by	_	ADP	ADP	_	25	case
24	its	_	PRON	PRON	_	25	nmod:poss
25	resumption	_	NOUN	NOUN	_	22	nmod
26	of	_	ADP	ADP	_	28	case
27	diplomatic	_	ADJ	ADJ	_	28	amod
28	ties	_	NOUN	NOUN	_	25	nmod
29	with	_	ADP	ADP	_	30	case
30	Gondor	_	PROPN	PROPN	_	28	nmod
31	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test205': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"071\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test205']['sents']['0']:
            print(return_dict['test205']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"071\")@ " + str(return_dict['test205']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"071\")@ noevent  " )
            print("test205 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"071\")@ noeventexception \n " )
        print("test205 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test205']['sents']['0']:
        verbs=return_dict['test205']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test205']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test205']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test205():
    text="""Eriador was opposed earlier by Osgiliath, the state's fiercest foe, 
in being drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Eriador	_	PROPN	PROPN	_	3	nsubj
2	was	_	AUX	AUX	_	3	aux
3	opposed	_	VERB	VERB	_	0	root
4	earlier	_	ADV	ADV	_	3	advmod
5	by	_	ADP	ADP	_	6	case
6	Osgiliath	_	PROPN	PROPN	_	3	nmod
7	,	_	PUNCT	PUNCT	_	3	punct
8	the	_	DET	DET	_	9	det
9	state	_	NOUN	NOUN	_	12	nmod:poss
10	's	_	PART	PART	_	9	case
11	fiercest	_	ADJ	ADJ	_	12	amod
12	foe	_	NOUN	NOUN	_	3	nmod
13	,	_	PUNCT	PUNCT	_	3	punct
14	in	_	SCONJ	SCONJ	_	16	mark
15	being	_	AUX	AUX	_	16	aux
16	drawn	_	VERB	VERB	_	3	advcl
17	into	_	ADP	ADP	_	20	case
18	the	_	DET	DET	_	20	det
19	peace	_	NOUN	NOUN	_	20	compound
20	process	_	NOUN	NOUN	_	16	nmod
21	by	_	ADP	ADP	_	23	case
22	its	_	PRON	PRON	_	23	nmod:poss
23	resumption	_	NOUN	NOUN	_	20	nmod
24	of	_	ADP	ADP	_	26	case
25	diplomatic	_	ADJ	ADJ	_	26	amod
26	ties	_	NOUN	NOUN	_	23	nmod
27	with	_	ADP	ADP	_	28	case
28	Gondor	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test206': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test206']['sents']['0']:
            print(return_dict['test206']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ " + str(return_dict['test206']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noevent  " )
            print("test206 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"OSG\", u\"ERI\", u\"112\")@ noeventexception \n " )
        print("test206 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test206']['sents']['0']:
        verbs=return_dict['test206']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test206']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test206']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test206():
    text="""Rebuked by Eriador, the state's fiercest foe, 
Osgiliath is being drawn into the peace process by its resumption 
of diplomatic ties with Gondor. 
"""
    parse="""1	Rebuked	_	VERB	VERB	_	14	advcl
2	by	_	ADP	ADP	_	3	case
3	Eriador	_	PROPN	PROPN	_	1	nmod
4	,	_	PUNCT	PUNCT	_	3	punct
5	the	_	DET	DET	_	6	det
6	state	_	NOUN	NOUN	_	9	nmod:poss
7	's	_	PART	PART	_	6	case
8	fiercest	_	ADJ	ADJ	_	9	amod
9	foe	_	NOUN	NOUN	_	3	appos
10	,	_	PUNCT	PUNCT	_	14	punct
11	Osgiliath	_	PROPN	PROPN	_	14	nsubj
12	is	_	AUX	AUX	_	14	aux
13	being	_	AUX	AUX	_	14	aux
14	drawn	_	VERB	VERB	_	0	root
15	into	_	ADP	ADP	_	18	case
16	the	_	DET	DET	_	18	det
17	peace	_	NOUN	NOUN	_	18	compound
18	process	_	NOUN	NOUN	_	14	nmod
19	by	_	ADP	ADP	_	21	case
20	its	_	PRON	PRON	_	21	nmod:poss
21	resumption	_	NOUN	NOUN	_	14	nmod
22	of	_	ADP	ADP	_	24	case
23	diplomatic	_	ADJ	ADJ	_	24	amod
24	ties	_	NOUN	NOUN	_	21	nmod
25	with	_	ADP	ADP	_	26	case
26	Gondor	_	PROPN	PROPN	_	24	nmod
27	.	_	PUNCT	PUNCT	_	14	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test207': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test207']['sents']['0']:
            print(return_dict['test207']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test207']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test207 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test207 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test207']['sents']['0']:
        verbs=return_dict['test207']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test207']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test207']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test207():
    text="""Arnor is about to restore full diplomatic ties with Gondor, 
five years after crowds burned down its embassy,  a very senior 
Bree official said on Saturday night. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	26	nsubj
2	is	_	VERB	VERB	_	26	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	8	nmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	13	nmod
16	burned	_	VERB	VERB	_	15	acl
17	down	_	ADP	ADP	_	19	case
18	its	_	PRON	PRON	_	19	nmod:poss
19	embassy	_	NOUN	NOUN	_	16	nmod
20	,	_	PUNCT	PUNCT	_	26	punct
21	a	_	DET	DET	_	25	det
22	very	_	ADV	ADV	_	23	advmod
23	senior	_	ADJ	ADJ	_	25	amod
24	Bree	_	PROPN	PROPN	_	25	compound
25	official	_	NOUN	NOUN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	29	case
28	Saturday	_	PROPN	PROPN	_	29	compound
29	night	_	NOUN	NOUN	_	26	nmod
30	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test208': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test208']['sents']['0']:
            print(return_dict['test208']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test208']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test208 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test208 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test208']['sents']['0']:
        verbs=return_dict['test208']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test208']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test208']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test208():
    text="""Arnor is about to restore full diplomatic ties with Gondor almost 
five years after Calenardhon crowds burned down its embassy,  a senior 
Bree official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	26	nsubj
2	is	_	VERB	VERB	_	26	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	5	nmod
14	after	_	ADP	ADP	_	16	case
15	Calenardhon	_	PROPN	PROPN	_	16	compound
16	crowds	_	NOUN	NOUN	_	8	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	20	case
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	,	_	PUNCT	PUNCT	_	26	punct
22	a	_	DET	DET	_	25	det
23	senior	_	ADJ	ADJ	_	25	amod
24	Bree	_	PROPN	PROPN	_	25	compound
25	official	_	NOUN	NOUN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	28	case
28	Saturday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test209': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test209']['sents']['0']:
            print(return_dict['test209']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test209']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test209 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test209 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test209']['sents']['0']:
        verbs=return_dict['test209']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test209']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test209']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test209():
    text="""Arnor is about to restore full diplomatic ties with Gondor, 
five years after crowds burned down its embassy,  a senior 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	24	nsubj
2	is	_	VERB	VERB	_	24	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	8	nmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	13	nmod
16	burned	_	VERB	VERB	_	15	acl
17	down	_	ADP	ADP	_	19	case
18	its	_	PRON	PRON	_	19	nmod:poss
19	embassy	_	NOUN	NOUN	_	16	nmod
20	,	_	PUNCT	PUNCT	_	24	punct
21	a	_	DET	DET	_	23	det
22	senior	_	ADJ	ADJ	_	23	amod
23	official	_	NOUN	NOUN	_	24	nsubj
24	said	_	VERB	VERB	_	0	root
25	on	_	ADP	ADP	_	26	case
26	Saturday	_	PROPN	PROPN	_	24	nmod
27	.	_	PUNCT	PUNCT	_	24	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test210': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test210']['sents']['0']:
            print(return_dict['test210']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test210']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test210 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test210 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test210']['sents']['0']:
        verbs=return_dict['test210']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test210']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test210']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test210():
    text="""Arnor is about to restore complete, full diplomatic ties with Gondor almost 
five years after Cxlenardhon crowds burned down its embassy,  a senior 
Bree official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	28	nsubj
2	is	_	VERB	VERB	_	28	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	complete	_	ADJ	ADJ	_	10	amod
7	,	_	PUNCT	PUNCT	_	10	punct
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	5	dobj
11	with	_	ADP	ADP	_	12	case
12	Gondor	_	PROPN	PROPN	_	10	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	five	_	NUM	NUM	_	15	nummod
15	years	_	NOUN	NOUN	_	18	nmod:npmod
16	after	_	ADP	ADP	_	18	case
17	Cxlenardhon	_	PROPN	PROPN	_	18	compound
18	crowds	_	NOUN	NOUN	_	10	nmod
19	burned	_	VERB	VERB	_	18	acl
20	down	_	ADP	ADP	_	22	case
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	19	nmod
23	,	_	PUNCT	PUNCT	_	28	punct
24	a	_	DET	DET	_	27	det
25	senior	_	ADJ	ADJ	_	27	amod
26	Bree	_	PROPN	PROPN	_	27	compound
27	official	_	NOUN	NOUN	_	28	nsubj
28	said	_	VERB	VERB	_	0	root
29	on	_	ADP	ADP	_	30	case
30	Saturday	_	PROPN	PROPN	_	28	nmod
31	.	_	PUNCT	PUNCT	_	28	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test211': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test211']['sents']['0']:
            print(return_dict['test211']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test211']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test211 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test211 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test211']['sents']['0']:
        verbs=return_dict['test211']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test211']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test211']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test211():
    text="""Arnor is about to restore full diplomatic ties with Gxndor, almost 
five years after Calenardhon crowds burned down its embassy,  a senior 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	26	nsubj
2	is	_	VERB	VERB	_	26	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gxndor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	5	nmod
15	after	_	ADP	ADP	_	17	case
16	Calenardhon	_	PROPN	PROPN	_	17	compound
17	crowds	_	NOUN	NOUN	_	8	nmod
18	burned	_	VERB	VERB	_	17	acl
19	down	_	ADP	ADP	_	21	case
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	18	nmod
22	,	_	PUNCT	PUNCT	_	26	punct
23	a	_	DET	DET	_	25	det
24	senior	_	ADJ	ADJ	_	25	amod
25	official	_	NOUN	NOUN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	28	case
28	Saturday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test212': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test212']['sents']['0']:
            print(return_dict['test212']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"064\")@ " + str(return_dict['test212']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"064\")@ noevent  " )
            print("test212 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"CAL\", u\"064\")@ noeventexception \n " )
        print("test212 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test212']['sents']['0']:
        verbs=return_dict['test212']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test212']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test212']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test212():
    text="""Arnor is about to restore full diplomatic ties with Gondor almost five years after 
Calenardhon crowds burned down its embassy,  a clearly inebriated Bree official said today. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	27	nsubj
2	is	_	VERB	VERB	_	27	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	5	nmod
14	after	_	ADP	ADP	_	16	case
15	Calenardhon	_	PROPN	PROPN	_	16	compound
16	crowds	_	NOUN	NOUN	_	8	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	20	case
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	,	_	PUNCT	PUNCT	_	27	punct
22	a	_	DET	DET	_	26	det
23	clearly	_	ADV	ADV	_	24	advmod
24	inebriated	_	ADJ	ADJ	_	26	amod
25	Bree	_	PROPN	PROPN	_	26	compound
26	official	_	NOUN	NOUN	_	27	nsubj
27	said	_	VERB	VERB	_	0	root
28	today	_	NOUN	NOUN	_	27	nmod:tmod
29	.	_	PUNCT	PUNCT	_	27	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test213': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test213']['sents']['0']:
            print(return_dict['test213']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ " + str(return_dict['test213']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noevent  " )
            print("test213 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\")@ noeventexception \n " )
        print("test213 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test213']['sents']['0']:
        verbs=return_dict['test213']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test213']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test213']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test213():
    text="""Arnor is about to restore, it seems, complete, full diplomatic ties with Gondor almost 
five years after Calenardhon crowds burned down its embassy,  a senior 
Bree official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	32	nsubj
2	is	_	VERB	VERB	_	32	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	,	_	PUNCT	PUNCT	_	2	punct
7	it	_	PRON	PRON	_	8	nsubj
8	seems	_	VERB	VERB	_	2	parataxis
9	,	_	PUNCT	PUNCT	_	8	punct
10	complete	_	ADJ	ADJ	_	14	amod
11	,	_	PUNCT	PUNCT	_	14	punct
12	full	_	ADJ	ADJ	_	14	amod
13	diplomatic	_	ADJ	ADJ	_	14	amod
14	ties	_	NOUN	NOUN	_	8	dobj
15	with	_	ADP	ADP	_	16	case
16	Gondor	_	PROPN	PROPN	_	14	nmod
17	almost	_	ADV	ADV	_	18	advmod
18	five	_	NUM	NUM	_	19	nummod
19	years	_	NOUN	NOUN	_	22	nmod:npmod
20	after	_	ADP	ADP	_	22	case
21	Calenardhon	_	PROPN	PROPN	_	22	compound
22	crowds	_	NOUN	NOUN	_	14	nmod
23	burned	_	VERB	VERB	_	22	acl
24	down	_	ADP	ADP	_	26	case
25	its	_	PRON	PRON	_	26	nmod:poss
26	embassy	_	NOUN	NOUN	_	23	nmod
27	,	_	PUNCT	PUNCT	_	32	punct
28	a	_	DET	DET	_	31	det
29	senior	_	ADJ	ADJ	_	31	amod
30	Bree	_	PROPN	PROPN	_	31	compound
31	official	_	NOUN	NOUN	_	32	nsubj
32	said	_	VERB	VERB	_	0	root
33	on	_	ADP	ADP	_	34	case
34	Saturday	_	PROPN	PROPN	_	32	nmod
35	.	_	PUNCT	PUNCT	_	32	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test214': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test214']['sents']['0']:
            print(return_dict['test214']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")@ " + str(return_dict['test214']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")@ noevent  " )
            print("test214 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test214 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test214']['sents']['0']:
        verbs=return_dict['test214']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test214']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test214']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test214():
    text="""Arnor is about to restore complete, full diplomatic ties with Gondor almost 
five years after Calenardhon crowds burned down its embassy,  a senior 
Bree official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	28	nsubj
2	is	_	VERB	VERB	_	28	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	complete	_	ADJ	ADJ	_	10	amod
7	,	_	PUNCT	PUNCT	_	10	punct
8	full	_	ADJ	ADJ	_	10	amod
9	diplomatic	_	ADJ	ADJ	_	10	amod
10	ties	_	NOUN	NOUN	_	5	dobj
11	with	_	ADP	ADP	_	12	case
12	Gondor	_	PROPN	PROPN	_	10	nmod
13	almost	_	ADV	ADV	_	14	advmod
14	five	_	NUM	NUM	_	15	nummod
15	years	_	NOUN	NOUN	_	18	nmod:npmod
16	after	_	ADP	ADP	_	18	case
17	Calenardhon	_	PROPN	PROPN	_	18	compound
18	crowds	_	NOUN	NOUN	_	10	nmod
19	burned	_	VERB	VERB	_	18	acl
20	down	_	ADP	ADP	_	22	case
21	its	_	PRON	PRON	_	22	nmod:poss
22	embassy	_	NOUN	NOUN	_	19	nmod
23	,	_	PUNCT	PUNCT	_	28	punct
24	a	_	DET	DET	_	27	det
25	senior	_	ADJ	ADJ	_	27	amod
26	Bree	_	PROPN	PROPN	_	27	compound
27	official	_	NOUN	NOUN	_	28	nsubj
28	said	_	VERB	VERB	_	0	root
29	on	_	ADP	ADP	_	30	case
30	Saturday	_	PROPN	PROPN	_	28	nmod
31	.	_	PUNCT	PUNCT	_	28	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test215': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test215']['sents']['0']:
            print(return_dict['test215']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")@ " + str(return_dict['test215']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")@ noevent  " )
            print("test215 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test215 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test215']['sents']['0']:
        verbs=return_dict['test215']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test215']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test215']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test215():
    text="""Arnor is said to be about to restore, it seems, complete, full diplomatic ties with
Gondor almost five years after Calenardhon crowds burned down its embassy, a senior Bree 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	is	_	AUX	AUX	_	3	aux
3	said	_	VERB	VERB	_	35	ccomp
4	to	_	PART	PART	_	5	mark
5	be	_	VERB	VERB	_	3	xcomp
6	about	_	ADV	ADV	_	8	advmod
7	to	_	PART	PART	_	8	mark
8	restore	_	VERB	VERB	_	5	advcl
9	,	_	PUNCT	PUNCT	_	8	punct
10	it	_	PRON	PRON	_	11	nsubj
11	seems	_	VERB	VERB	_	8	xcomp
12	,	_	PUNCT	PUNCT	_	11	punct
13	complete	_	ADJ	ADJ	_	17	amod
14	,	_	PUNCT	PUNCT	_	17	punct
15	full	_	ADJ	ADJ	_	17	amod
16	diplomatic	_	ADJ	ADJ	_	17	amod
17	ties	_	NOUN	NOUN	_	11	dobj
18	with	_	ADP	ADP	_	19	case
19	Gondor	_	PROPN	PROPN	_	17	nmod
20	almost	_	ADV	ADV	_	21	advmod
21	five	_	NUM	NUM	_	22	nummod
22	years	_	NOUN	NOUN	_	25	nmod:npmod
23	after	_	ADP	ADP	_	25	case
24	Calenardhon	_	PROPN	PROPN	_	25	compound
25	crowds	_	NOUN	NOUN	_	17	nmod
26	burned	_	VERB	VERB	_	25	acl
27	down	_	ADP	ADP	_	29	case
28	its	_	PRON	PRON	_	29	nmod:poss
29	embassy	_	NOUN	NOUN	_	26	nmod
30	,	_	PUNCT	PUNCT	_	35	punct
31	a	_	DET	DET	_	34	det
32	senior	_	ADJ	ADJ	_	34	amod
33	Bree	_	PROPN	PROPN	_	34	compound
34	official	_	NOUN	NOUN	_	35	nsubj
35	said	_	VERB	VERB	_	0	root
36	on	_	ADP	ADP	_	37	case
37	Saturday	_	PROPN	PROPN	_	35	nmod
38	.	_	PUNCT	PUNCT	_	35	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test216': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test216']['sents']['0']:
            print(return_dict['test216']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")@ " + str(return_dict['test216']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")@ noevent  " )
            print("test216 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test216 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test216']['sents']['0']:
        verbs=return_dict['test216']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test216']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test216']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test216():
    text="""Arnor is about to restore full diplomatic ties with Gondor, almost 
five years after Calenardhon crowds burned down its embassy,  a senior 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	26	nsubj
2	is	_	VERB	VERB	_	26	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	5	nmod
15	after	_	ADP	ADP	_	17	case
16	Calenardhon	_	PROPN	PROPN	_	17	compound
17	crowds	_	NOUN	NOUN	_	8	nmod
18	burned	_	VERB	VERB	_	17	acl
19	down	_	ADP	ADP	_	21	case
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	18	nmod
22	,	_	PUNCT	PUNCT	_	26	punct
23	a	_	DET	DET	_	25	det
24	senior	_	ADJ	ADJ	_	25	amod
25	official	_	NOUN	NOUN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	28	case
28	Saturday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test217': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test217']['sents']['0']:
            print(return_dict['test217']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test217']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test217 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test217 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test217']['sents']['0']:
        verbs=return_dict['test217']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test217']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test217']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test217():
    text="""Arnor is about to improve full diplomatic ties with Gondor, almost 
five years after Calenardhon crowds burned down its embassy,  a 
clearly inebriated Bree official said today.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	28	nsubj
2	is	_	VERB	VERB	_	28	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	improve	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	5	nmod
15	after	_	ADP	ADP	_	17	case
16	Calenardhon	_	PROPN	PROPN	_	17	compound
17	crowds	_	NOUN	NOUN	_	8	nmod
18	burned	_	VERB	VERB	_	17	acl
19	down	_	ADP	ADP	_	21	case
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	18	nmod
22	,	_	PUNCT	PUNCT	_	28	punct
23	a	_	DET	DET	_	27	det
24	clearly	_	ADV	ADV	_	25	advmod
25	inebriated	_	ADJ	ADJ	_	27	amod
26	Bree	_	PROPN	PROPN	_	27	compound
27	official	_	NOUN	NOUN	_	28	nsubj
28	said	_	VERB	VERB	_	0	root
29	today	_	NOUN	NOUN	_	28	nmod:tmod
30	.	_	PUNCT	PUNCT	_	28	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test218': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test218']['sents']['0']:
            print(return_dict['test218']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")@ " + str(return_dict['test218']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")@ noevent  " )
            print("test218 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")@ noeventexception \n " )
        print("test218 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test218']['sents']['0']:
        verbs=return_dict['test218']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test218']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test218']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test218():
    text="""Arnor is about to improve full diplomatic ties with Gondor, almost 
five years after Calenardhon crowds burned down its embassy,  a 
senior Bree official said today. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	27	nsubj
2	is	_	VERB	VERB	_	27	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	improve	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	almost	_	ADV	ADV	_	13	advmod
13	five	_	NUM	NUM	_	14	nummod
14	years	_	NOUN	NOUN	_	5	nmod
15	after	_	ADP	ADP	_	17	case
16	Calenardhon	_	PROPN	PROPN	_	17	compound
17	crowds	_	NOUN	NOUN	_	8	nmod
18	burned	_	VERB	VERB	_	17	acl
19	down	_	ADP	ADP	_	21	case
20	its	_	PRON	PRON	_	21	nmod:poss
21	embassy	_	NOUN	NOUN	_	18	nmod
22	,	_	PUNCT	PUNCT	_	27	punct
23	a	_	DET	DET	_	26	det
24	senior	_	ADJ	ADJ	_	26	amod
25	Bree	_	PROPN	PROPN	_	26	compound
26	official	_	NOUN	NOUN	_	27	nsubj
27	said	_	VERB	VERB	_	0	root
28	today	_	NOUN	NOUN	_	27	nmod:tmod
29	.	_	PUNCT	PUNCT	_	27	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test219': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test219']['sents']['0']:
            print(return_dict['test219']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\")@ " + str(return_dict['test219']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\")@ noevent  " )
            print("test219 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"---\", u\"222\")@ noeventexception \n " )
        print("test219 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test219']['sents']['0']:
        verbs=return_dict['test219']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test219']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test219']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test219():
    text="""Arnor on Thursday signed an 800 million ducat trade protocol
for 1990 with Dagolath, its biggest trading partner, officials said. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	nsubj
2	on	_	ADP	ADP	_	3	case
3	Thursday	_	PROPN	PROPN	_	1	nmod
4	signed	_	VERB	VERB	_	22	advcl
5	an	_	DET	DET	_	10	det
6	800	_	NUM	NUM	_	7	compound
7	million	_	NUM	NUM	_	8	nummod
8	ducat	_	NOUN	NOUN	_	10	compound
9	trade	_	NOUN	NOUN	_	10	compound
10	protocol	_	NOUN	NOUN	_	4	dobj
11	for	_	ADP	ADP	_	12	case
12	1990	_	NUM	NUM	_	10	nmod
13	with	_	ADP	ADP	_	14	case
14	Dagolath	_	PROPN	PROPN	_	10	nmod
15	,	_	PUNCT	PUNCT	_	14	punct
16	its	_	PRON	PRON	_	19	nmod:poss
17	biggest	_	ADJ	ADJ	_	19	amod
18	trading	_	NOUN	NOUN	_	19	compound
19	partner	_	NOUN	NOUN	_	14	conj
20	,	_	PUNCT	PUNCT	_	22	punct
21	officials	_	NOUN	NOUN	_	22	nsubj
22	said	_	VERB	VERB	_	0	root
23	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test220': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test220']['sents']['0']:
            print(return_dict['test220']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ " + str(return_dict['test220']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ noevent  " )
            print("test220 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"DAG\", u\"085\")@ noeventexception \n " )
        print("test220 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test220']['sents']['0']:
        verbs=return_dict['test220']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test220']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test220']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test220():
    text="""Arnor is about to restore full diplomatic ties with Gxndor, several 
years after Calenardhon crowds burned down its embassy,  a senior 
official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	25	nsubj
2	is	_	VERB	VERB	_	25	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gxndor	_	PROPN	PROPN	_	8	nmod
11	,	_	PUNCT	PUNCT	_	8	punct
12	several	_	ADJ	ADJ	_	13	amod
13	years	_	NOUN	NOUN	_	8	nmod
14	after	_	ADP	ADP	_	16	case
15	Calenardhon	_	PROPN	PROPN	_	16	compound
16	crowds	_	NOUN	NOUN	_	8	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	17	compound:prt
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	,	_	PUNCT	PUNCT	_	25	punct
22	a	_	DET	DET	_	24	det
23	senior	_	ADJ	ADJ	_	24	amod
24	official	_	NOUN	NOUN	_	25	nsubj
25	said	_	VERB	VERB	_	0	root
26	on	_	ADP	ADP	_	27	case
27	Saturday	_	PROPN	PROPN	_	25	nmod
28	.	_	PUNCT	PUNCT	_	25	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test221': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test221']['sents']['0']:
            print(return_dict['test221']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test221']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test221 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test221 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test221']['sents']['0']:
        verbs=return_dict['test221']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test221']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test221']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test221():
    text="""Arnor is about to restore full diplomatic ties with Gxndor almost 
five years after Cxlenardhon crowds burned down its embassy,  a senior 
Bree official said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	26	nsubj
2	is	_	VERB	VERB	_	26	ccomp
3	about	_	ADV	ADV	_	5	advmod
4	to	_	PART	PART	_	5	mark
5	restore	_	VERB	VERB	_	2	advcl
6	full	_	ADJ	ADJ	_	8	amod
7	diplomatic	_	ADJ	ADJ	_	8	amod
8	ties	_	NOUN	NOUN	_	5	dobj
9	with	_	ADP	ADP	_	10	case
10	Gxndor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	5	nmod
14	after	_	ADP	ADP	_	16	case
15	Cxlenardhon	_	PROPN	PROPN	_	16	compound
16	crowds	_	NOUN	NOUN	_	8	nmod
17	burned	_	VERB	VERB	_	16	acl
18	down	_	ADP	ADP	_	20	case
19	its	_	PRON	PRON	_	20	nmod:poss
20	embassy	_	NOUN	NOUN	_	17	nmod
21	,	_	PUNCT	PUNCT	_	26	punct
22	a	_	DET	DET	_	25	det
23	senior	_	ADJ	ADJ	_	25	amod
24	Bree	_	PROPN	PROPN	_	25	compound
25	official	_	NOUN	NOUN	_	26	nsubj
26	said	_	VERB	VERB	_	0	root
27	on	_	ADP	ADP	_	28	case
28	Saturday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	26	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test222': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test222']['sents']['0']:
            print(return_dict['test222']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ " + str(return_dict['test222']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noevent  " )
            print("test222 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ No Event@ noeventexception \n " )
        print("test222 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test222']['sents']['0']:
        verbs=return_dict['test222']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test222']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test222']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test222():
    text="""Arnor will abandon full diplomatic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	diplomatic	_	ADJ	ADJ	_	6	amod
6	ties	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test223': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"901\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test223']['sents']['0']:
            print(return_dict['test223']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"901\")@ " + str(return_dict['test223']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"901\")@ noevent  " )
            print("test223 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"901\")@ noeventexception \n " )
        print("test223 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test223']['sents']['0']:
        verbs=return_dict['test223']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test223']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test223']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test223():
    text="""Arnor will abandon full &amp;TIETYPE ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday.
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	7	amod
5	&amp;	_	CONJ	CONJ	_	4	cc
6	TIETYPE	_	ADJ	ADJ	_	4	conj
7	ties	_	NOUN	NOUN	_	3	dobj
8	with	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	7	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	7	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test224': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test224']['sents']['0']:
            print(return_dict['test224']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ " + str(return_dict['test224']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noevent  " )
            print("test224 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test224 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test224']['sents']['0']:
        verbs=return_dict['test224']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test224']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test224']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test224():
    text="""Arnor will abandon full economic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	economic	_	ADJ	ADJ	_	6	amod
6	ties	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test225': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test225']['sents']['0']:
            print(return_dict['test225']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ " + str(return_dict['test225']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noevent  " )
            print("test225 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noeventexception \n " )
        print("test225 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test225']['sents']['0']:
        verbs=return_dict['test225']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test225']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test225']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test225():
    text="""Arnor will abandon full cultural ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	cultural	_	ADJ	ADJ	_	6	amod
6	ties	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test226': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test226']['sents']['0']:
            print(return_dict['test226']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ " + str(return_dict['test226']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noevent  " )
            print("test226 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noeventexception \n " )
        print("test226 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test226']['sents']['0']:
        verbs=return_dict['test226']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test226']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test226']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test226():
    text="""Arnor will abandon full military ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	military	_	ADJ	ADJ	_	6	amod
6	ties	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	6	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test227': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test227']['sents']['0']:
            print(return_dict['test227']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ " + str(return_dict['test227']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noevent  " )
            print("test227 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"902\")@ noeventexception \n " )
        print("test227 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test227']['sents']['0']:
        verbs=return_dict['test227']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test227']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test227']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test227():
    text="""Arnor will abandon full military txes with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	military	_	ADJ	ADJ	_	6	amod
6	txes	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test228': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test228']['sents']['0']:
            print(return_dict['test228']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ " + str(return_dict['test228']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noevent  " )
            print("test228 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test228 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test228']['sents']['0']:
        verbs=return_dict['test228']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test228']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test228']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test228():
    text="""Arnor will abandon full symbolic ties with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	full	_	ADJ	ADJ	_	6	amod
5	symbolic	_	ADJ	ADJ	_	6	amod
6	ties	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test229': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test229']['sents']['0']:
            print(return_dict['test229']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ " + str(return_dict['test229']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noevent  " )
            print("test229 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test229 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test229']['sents']['0']:
        verbs=return_dict['test229']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test229']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test229']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test229():
    text="""Arnor will contribute a million rupees to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	million	_	NUM	NUM	_	6	nummod
6	rupees	_	NOUN	NOUN	_	3	dobj
7	to	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test230': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"071\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test230']['sents']['0']:
            print(return_dict['test230']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"071\")@ " + str(return_dict['test230']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"071\")@ noevent  " )
            print("test230 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"071\")@ noeventexception \n " )
        print("test230 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test230']['sents']['0']:
        verbs=return_dict['test230']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test230']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test230']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test230():
    text="""Arnor will contribute a million dollars to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	million	_	NUM	NUM	_	6	nummod
6	dollars	_	NOUN	NOUN	_	3	dobj
7	to	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test231': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test231']['sents']['0']:
            print(return_dict['test231']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test231']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test231 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test231 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test231']['sents']['0']:
        verbs=return_dict['test231']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test231']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test231']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test231():
    text="""Arnor will contribute a million euros to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	million	_	NUM	NUM	_	6	nummod
6	euros	_	NOUN	NOUN	_	3	dobj
7	to	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test232': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test232']['sents']['0']:
            print(return_dict['test232']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test232']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test232 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test232 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test232']['sents']['0']:
        verbs=return_dict['test232']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test232']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test232']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test232():
    text="""Arnor will contribute a million kroner to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	million	_	NUM	NUM	_	6	nummod
6	kroner	_	NOUN	NOUN	_	3	dobj
7	to	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test233': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test233']['sents']['0']:
            print(return_dict['test233']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test233']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test233 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test233 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test233']['sents']['0']:
        verbs=return_dict['test233']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test233']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test233']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test233():
    text="""Arnor will contribute a million swiss francs to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	7	det
5	million	_	NUM	NUM	_	6	nummod
6	swiss	_	NOUN	NOUN	_	7	compound
7	francs	_	NOUN	NOUN	_	3	dobj
8	to	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	3	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	3	nmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	12	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test234': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test234']['sents']['0']:
            print(return_dict['test234']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test234']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test234 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test234 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test234']['sents']['0']:
        verbs=return_dict['test234']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test234']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test234']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test234():
    text="""Arnor will contribute a million golden goblin galleons to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	8	det
5	million	_	NUM	NUM	_	8	nummod
6	golden	_	ADJ	ADJ	_	8	amod
7	goblin	_	NOUN	NOUN	_	8	compound
8	galleons	_	NOUN	NOUN	_	3	dobj
9	to	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	3	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	3	nmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	13	nmod
16	trashed	_	VERB	VERB	_	3	advcl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	18	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	18	appos
23	said	_	VERB	VERB	_	22	acl
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test235': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test235']['sents']['0']:
            print(return_dict['test235']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test235']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test235 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test235 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test235']['sents']['0']:
        verbs=return_dict['test235']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test235']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test235']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test235():
    text="""Arnor will contribute a million goblin galleons to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	7	det
5	million	_	NUM	NUM	_	6	nummod
6	goblin	_	NOUN	NOUN	_	7	compound
7	galleons	_	NOUN	NOUN	_	3	dobj
8	to	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	3	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	3	nmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	12	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test236': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test236']['sents']['0']:
            print(return_dict['test236']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ " + str(return_dict['test236']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ noevent  " )
            print("test236 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ noeventexception \n " )
        print("test236 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test236']['sents']['0']:
        verbs=return_dict['test236']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test236']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test236']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test236():
    text="""Arnor will contribute a million golden galleons to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	7	det
5	million	_	NUM	NUM	_	7	nummod
6	golden	_	ADJ	ADJ	_	7	amod
7	galleons	_	NOUN	NOUN	_	3	dobj
8	to	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	3	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	3	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test237': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test237']['sents']['0']:
            print(return_dict['test237']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ " + str(return_dict['test237']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ noevent  " )
            print("test237 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"070\")@ noeventexception \n " )
        print("test237 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test237']['sents']['0']:
        verbs=return_dict['test237']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test237']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test237']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test237():
    text="""Bree Prime Minister Romendacil clashed over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	5	nsubj
5	clashed	_	VERB	VERB	_	0	root
6	over	_	ADP	ADP	_	8	case
7	the	_	DET	DET	_	8	det
8	efforts	_	NOUN	NOUN	_	5	nmod
9	of	_	ADP	ADP	_	10	case
10	Eriadori	_	PROPN	PROPN	_	8	nmod
11	to	_	PART	PART	_	12	mark
12	deal	_	VERB	VERB	_	5	advcl
13	with	_	ADP	ADP	_	16	case
14	an	_	DET	DET	_	16	det
15	orc	_	ADJ	ADJ	_	16	amod
16	infestation	_	NOUN	NOUN	_	12	nmod
17	during	_	ADP	ADP	_	21	case
18	a	_	DET	DET	_	21	det
19	brief	_	ADJ	ADJ	_	21	amod
20	private	_	ADJ	ADJ	_	21	amod
21	visit	_	NOUN	NOUN	_	12	nmod
22	to	_	ADP	ADP	_	23	case
23	Eriador	_	PROPN	PROPN	_	21	nmod
24	starting	_	VERB	VERB	_	21	acl
25	on	_	ADP	ADP	_	26	case
26	Sunday	_	PROPN	PROPN	_	24	nmod
27	.	_	PUNCT	PUNCT	_	5	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test238': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"121\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test238']['sents']['0']:
            print(return_dict['test238']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"121\")@ " + str(return_dict['test238']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"121\")@ noevent  " )
            print("test238 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"121\")@ noeventexception \n " )
        print("test238 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test238']['sents']['0']:
        verbs=return_dict['test238']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test238']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test238']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test238():
    text="""Bree Prime Minister Romendacil didn't clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	7	nsubj
5	did	_	AUX	AUX	_	7	aux
6	n't	_	PART	PART	_	7	neg
7	clash	_	VERB	VERB	_	0	root
8	over	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	efforts	_	NOUN	NOUN	_	7	nmod
11	of	_	ADP	ADP	_	12	case
12	Eriadori	_	PROPN	PROPN	_	10	nmod
13	to	_	PART	PART	_	14	mark
14	deal	_	VERB	VERB	_	7	advcl
15	with	_	ADP	ADP	_	18	case
16	an	_	DET	DET	_	18	det
17	orc	_	ADJ	ADJ	_	18	amod
18	infestation	_	NOUN	NOUN	_	14	nmod
19	during	_	ADP	ADP	_	23	case
20	a	_	DET	DET	_	23	det
21	brief	_	ADJ	ADJ	_	23	amod
22	private	_	ADJ	ADJ	_	23	amod
23	visit	_	NOUN	NOUN	_	14	nmod
24	to	_	ADP	ADP	_	25	case
25	Eriador	_	PROPN	PROPN	_	23	nmod
26	starting	_	VERB	VERB	_	23	acl
27	on	_	ADP	ADP	_	28	case
28	Sunday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	7	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test239': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test239']['sents']['0']:
            print(return_dict['test239']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ " + str(return_dict['test239']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noevent  " )
            print("test239 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noeventexception \n " )
        print("test239 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test239']['sents']['0']:
        verbs=return_dict['test239']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test239']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test239']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test239():
    text="""Bree Prime Minister Romendacil will not clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	7	nsubj
5	will	_	AUX	AUX	_	7	aux
6	not	_	PART	PART	_	7	neg
7	clash	_	VERB	VERB	_	0	root
8	over	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	efforts	_	NOUN	NOUN	_	7	nmod
11	of	_	ADP	ADP	_	12	case
12	Eriadori	_	PROPN	PROPN	_	10	nmod
13	to	_	PART	PART	_	14	mark
14	deal	_	VERB	VERB	_	7	advcl
15	with	_	ADP	ADP	_	18	case
16	an	_	DET	DET	_	18	det
17	orc	_	ADJ	ADJ	_	18	amod
18	infestation	_	NOUN	NOUN	_	14	nmod
19	during	_	ADP	ADP	_	23	case
20	a	_	DET	DET	_	23	det
21	brief	_	ADJ	ADJ	_	23	amod
22	private	_	ADJ	ADJ	_	23	amod
23	visit	_	NOUN	NOUN	_	14	nmod
24	to	_	ADP	ADP	_	25	case
25	Eriador	_	PROPN	PROPN	_	23	nmod
26	starting	_	VERB	VERB	_	23	acl
27	on	_	ADP	ADP	_	28	case
28	Sunday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	7	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test240': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test240']['sents']['0']:
            print(return_dict['test240']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ " + str(return_dict['test240']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noevent  " )
            print("test240 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noeventexception \n " )
        print("test240 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test240']['sents']['0']:
        verbs=return_dict['test240']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test240']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test240']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test240():
    text="""Bree Prime Minister Romendacil will not ever clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	8	nsubj
5	will	_	AUX	AUX	_	8	aux
6	not	_	PART	PART	_	8	neg
7	ever	_	ADV	ADV	_	8	advmod
8	clash	_	VERB	VERB	_	0	root
9	over	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	efforts	_	NOUN	NOUN	_	8	nmod
12	of	_	ADP	ADP	_	13	case
13	Eriadori	_	PROPN	PROPN	_	11	nmod
14	to	_	PART	PART	_	15	mark
15	deal	_	VERB	VERB	_	8	advcl
16	with	_	ADP	ADP	_	19	case
17	an	_	DET	DET	_	19	det
18	orc	_	ADJ	ADJ	_	19	amod
19	infestation	_	NOUN	NOUN	_	15	nmod
20	during	_	ADP	ADP	_	24	case
21	a	_	DET	DET	_	24	det
22	brief	_	ADJ	ADJ	_	24	amod
23	private	_	ADJ	ADJ	_	24	amod
24	visit	_	NOUN	NOUN	_	15	nmod
25	to	_	ADP	ADP	_	26	case
26	Eriador	_	PROPN	PROPN	_	24	nmod
27	starting	_	VERB	VERB	_	24	acl
28	on	_	ADP	ADP	_	29	case
29	Sunday	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test241': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test241']['sents']['0']:
            print(return_dict['test241']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ " + str(return_dict['test241']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noevent  " )
            print("test241 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noeventexception \n " )
        print("test241 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test241']['sents']['0']:
        verbs=return_dict['test241']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test241']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test241']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test241():
    text="""Bree Prime Minister Romendacil can't ever clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	8	nsubj
5	ca	_	AUX	AUX	_	8	aux
6	n't	_	PART	PART	_	8	neg
7	ever	_	ADV	ADV	_	8	advmod
8	clash	_	VERB	VERB	_	0	root
9	over	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	efforts	_	NOUN	NOUN	_	8	nmod
12	of	_	ADP	ADP	_	13	case
13	Eriadori	_	PROPN	PROPN	_	11	nmod
14	to	_	PART	PART	_	15	mark
15	deal	_	VERB	VERB	_	8	advcl
16	with	_	ADP	ADP	_	19	case
17	an	_	DET	DET	_	19	det
18	orc	_	ADJ	ADJ	_	19	amod
19	infestation	_	NOUN	NOUN	_	15	nmod
20	during	_	ADP	ADP	_	24	case
21	a	_	DET	DET	_	24	det
22	brief	_	ADJ	ADJ	_	24	amod
23	private	_	ADJ	ADJ	_	24	amod
24	visit	_	NOUN	NOUN	_	15	nmod
25	to	_	ADP	ADP	_	26	case
26	Eriador	_	PROPN	PROPN	_	24	nmod
27	starting	_	VERB	VERB	_	24	acl
28	on	_	ADP	ADP	_	29	case
29	Sunday	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test242': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test242']['sents']['0']:
            print(return_dict['test242']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ " + str(return_dict['test242']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noevent  " )
            print("test242 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noeventexception \n " )
        print("test242 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test242']['sents']['0']:
        verbs=return_dict['test242']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test242']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test242']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test242():
    text="""Bree Prime Minister Romendacil unexpectedly won't clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	8	nsubj
5	unexpectedly	_	ADV	ADV	_	8	advmod
6	wo	_	AUX	AUX	_	8	aux
7	n't	_	PART	PART	_	8	neg
8	clash	_	VERB	VERB	_	0	root
9	over	_	ADP	ADP	_	11	case
10	the	_	DET	DET	_	11	det
11	efforts	_	NOUN	NOUN	_	8	nmod
12	of	_	ADP	ADP	_	13	case
13	Eriadori	_	PROPN	PROPN	_	11	nmod
14	to	_	PART	PART	_	15	mark
15	deal	_	VERB	VERB	_	8	advcl
16	with	_	ADP	ADP	_	19	case
17	an	_	DET	DET	_	19	det
18	orc	_	ADJ	ADJ	_	19	amod
19	infestation	_	NOUN	NOUN	_	15	nmod
20	during	_	ADP	ADP	_	24	case
21	a	_	DET	DET	_	24	det
22	brief	_	ADJ	ADJ	_	24	amod
23	private	_	ADJ	ADJ	_	24	amod
24	visit	_	NOUN	NOUN	_	15	nmod
25	to	_	ADP	ADP	_	26	case
26	Eriador	_	PROPN	PROPN	_	24	nmod
27	starting	_	VERB	VERB	_	24	acl
28	on	_	ADP	ADP	_	29	case
29	Sunday	_	PROPN	PROPN	_	27	nmod
30	.	_	PUNCT	PUNCT	_	8	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test243': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test243']['sents']['0']:
            print(return_dict['test243']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ " + str(return_dict['test243']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ noevent  " )
            print("test243 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ noeventexception \n " )
        print("test243 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test243']['sents']['0']:
        verbs=return_dict['test243']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test243']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test243']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test243():
    text="""Bree Prime Minister Romendacil most certainly really did not clash over the efforts of Eriadori  
to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	10	nsubj
5	most	_	ADV	ADV	_	6	advmod
6	certainly	_	ADV	ADV	_	10	advmod
7	really	_	ADV	ADV	_	10	advmod
8	did	_	AUX	AUX	_	10	aux
9	not	_	PART	PART	_	10	neg
10	clash	_	VERB	VERB	_	0	root
11	over	_	ADP	ADP	_	13	case
12	the	_	DET	DET	_	13	det
13	efforts	_	NOUN	NOUN	_	10	nmod
14	of	_	ADP	ADP	_	15	case
15	Eriadori	_	PROPN	PROPN	_	13	nmod
16	to	_	PART	PART	_	17	mark
17	deal	_	VERB	VERB	_	10	advcl
18	with	_	ADP	ADP	_	21	case
19	an	_	DET	DET	_	21	det
20	orc	_	ADJ	ADJ	_	21	amod
21	infestation	_	NOUN	NOUN	_	17	nmod
22	during	_	ADP	ADP	_	26	case
23	a	_	DET	DET	_	26	det
24	brief	_	ADJ	ADJ	_	26	amod
25	private	_	ADJ	ADJ	_	26	amod
26	visit	_	NOUN	NOUN	_	17	nmod
27	to	_	ADP	ADP	_	28	case
28	Eriador	_	PROPN	PROPN	_	26	nmod
29	starting	_	VERB	VERB	_	26	acl
30	on	_	ADP	ADP	_	31	case
31	Sunday	_	PROPN	PROPN	_	29	nmod
32	.	_	PUNCT	PUNCT	_	10	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test244': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test244']['sents']['0']:
            print(return_dict['test244']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ " + str(return_dict['test244']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noevent  " )
            print("test244 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noeventexception \n " )
        print("test244 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test244']['sents']['0']:
        verbs=return_dict['test244']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test244']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test244']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test244():
    text="""Bree Prime Minister Romendacil didn't clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	7	nsubj
5	did	_	AUX	AUX	_	7	aux
6	n't	_	PART	PART	_	7	neg
7	clash	_	VERB	VERB	_	0	root
8	over	_	ADP	ADP	_	10	case
9	the	_	DET	DET	_	10	det
10	efforts	_	NOUN	NOUN	_	7	nmod
11	of	_	ADP	ADP	_	12	case
12	Eriadori	_	PROPN	PROPN	_	10	nmod
13	to	_	PART	PART	_	14	mark
14	deal	_	VERB	VERB	_	7	advcl
15	with	_	ADP	ADP	_	18	case
16	an	_	DET	DET	_	18	det
17	orc	_	ADJ	ADJ	_	18	amod
18	infestation	_	NOUN	NOUN	_	14	nmod
19	during	_	ADP	ADP	_	23	case
20	a	_	DET	DET	_	23	det
21	brief	_	ADJ	ADJ	_	23	amod
22	private	_	ADJ	ADJ	_	23	amod
23	visit	_	NOUN	NOUN	_	14	nmod
24	to	_	ADP	ADP	_	25	case
25	Eriador	_	PROPN	PROPN	_	23	nmod
26	starting	_	VERB	VERB	_	23	acl
27	on	_	ADP	ADP	_	28	case
28	Sunday	_	PROPN	PROPN	_	26	nmod
29	.	_	PUNCT	PUNCT	_	7	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test245': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test245']['sents']['0']:
            print(return_dict['test245']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ " + str(return_dict['test245']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noevent  " )
            print("test245 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"904\")@ noeventexception \n " )
        print("test245 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test245']['sents']['0']:
        verbs=return_dict['test245']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test245']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test245']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test245():
    text="""Arnor will contribute a million yum yennyen to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	million	_	NUM	NUM	_	6	nummod
6	yum	_	NOUN	NOUN	_	3	dobj
7	yennyen	_	ADV	ADV	_	9	advmod
8	to	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	3	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	3	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test246': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test246']['sents']['0']:
            print(return_dict['test246']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test246']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test246 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test246 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test246']['sents']['0']:
        verbs=return_dict['test246']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test246']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test246']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test246():
    text="""Arnor will contribute a million austrian florin to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	7	det
5	million	_	NUM	NUM	_	7	nummod
6	austrian	_	ADJ	ADJ	_	7	amod
7	florin	_	NOUN	NOUN	_	3	dobj
8	to	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	3	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	3	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test247': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test247']['sents']['0']:
            print(return_dict['test247']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test247']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test247 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test247 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test247']['sents']['0']:
        verbs=return_dict['test247']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test247']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test247']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test247():
    text="""Arnor will contribute a million austrian gold florin to Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	contribute	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	7	det
5	million	_	NUM	NUM	_	7	nummod
6	austrian	_	ADJ	ADJ	_	7	amod
7	gold	_	NOUN	NOUN	_	3	dobj
8	florin	_	VERB	VERB	_	7	acl
9	to	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	15	nmod:npmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	8	nmod
16	trashed	_	VERB	VERB	_	15	acl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	18	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	18	appos
23	said	_	VERB	VERB	_	22	acl
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test248': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test248']['sents']['0']:
            print(return_dict['test248']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ " + str(return_dict['test248']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noevent  " )
            print("test248 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noeventexception \n " )
        print("test248 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test248']['sents']['0']:
        verbs=return_dict['test248']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test248']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test248']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test248():
    text="""Arnor will adopt a resolution with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	adopt	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	5	det
5	resolution	_	NOUN	NOUN	_	3	dobj
6	with	_	ADP	ADP	_	7	case
7	Gondor	_	PROPN	PROPN	_	3	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	12	nmod:npmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	3	nmod
13	trashed	_	VERB	VERB	_	12	acl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	,	_	PUNCT	PUNCT	_	15	punct
17	a	_	DET	DET	_	19	det
18	senior	_	ADJ	ADJ	_	19	amod
19	official	_	NOUN	NOUN	_	15	appos
20	said	_	VERB	VERB	_	19	acl
21	on	_	ADP	ADP	_	22	case
22	Saturday	_	PROPN	PROPN	_	20	nmod
23	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test249': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"102\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test249']['sents']['0']:
            print(return_dict['test249']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"102\")@ " + str(return_dict['test249']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"102\")@ noevent  " )
            print("test249 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"102\")@ noeventexception \n " )
        print("test249 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test249']['sents']['0']:
        verbs=return_dict['test249']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test249']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test249']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test249():
    text="""Arnor will adopt a set of resolutions with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	adopt	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	5	det
5	set	_	NOUN	NOUN	_	3	dobj
6	of	_	ADP	ADP	_	7	case
7	resolutions	_	NOUN	NOUN	_	5	nmod
8	with	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	7	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	3	nmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	12	nmod
15	trashed	_	VERB	VERB	_	3	advcl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test250': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test250']['sents']['0']:
            print(return_dict['test250']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ " + str(return_dict['test250']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ noevent  " )
            print("test250 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"081\")@ noeventexception \n " )
        print("test250 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test250']['sents']['0']:
        verbs=return_dict['test250']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test250']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test250']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test250():
    text="""Arnor will adopt a revolution with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	adopt	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	5	det
5	revolution	_	NOUN	NOUN	_	3	dobj
6	with	_	ADP	ADP	_	7	case
7	Gondor	_	PROPN	PROPN	_	3	nmod
8	almost	_	ADV	ADV	_	9	advmod
9	five	_	NUM	NUM	_	10	nummod
10	years	_	NOUN	NOUN	_	12	nmod:npmod
11	after	_	ADP	ADP	_	12	case
12	crowds	_	NOUN	NOUN	_	3	nmod
13	trashed	_	VERB	VERB	_	12	acl
14	its	_	PRON	PRON	_	15	nmod:poss
15	embassy	_	NOUN	NOUN	_	13	dobj
16	,	_	PUNCT	PUNCT	_	15	punct
17	a	_	DET	DET	_	19	det
18	senior	_	ADJ	ADJ	_	19	amod
19	official	_	NOUN	NOUN	_	15	appos
20	said	_	VERB	VERB	_	19	acl
21	on	_	ADP	ADP	_	22	case
22	Saturday	_	PROPN	PROPN	_	20	nmod
23	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test251': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test251']['sents']['0']:
            print(return_dict['test251']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ " + str(return_dict['test251']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ noevent  " )
            print("test251 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ noeventexception \n " )
        print("test251 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test251']['sents']['0']:
        verbs=return_dict['test251']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test251']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test251']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test251():
    text="""Arnor will adopt a revolutionary manifesto with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	adopt	_	VERB	VERB	_	0	root
4	a	_	DET	DET	_	6	det
5	revolutionary	_	ADJ	ADJ	_	6	amod
6	manifesto	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	3	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	3	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test252': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test252']['sents']['0']:
            print(return_dict['test252']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ " + str(return_dict['test252']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ noevent  " )
            print("test252 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"802\")@ noeventexception \n " )
        print("test252 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test252']['sents']['0']:
        verbs=return_dict['test252']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test252']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test252']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test252():
    text="""Arnor will abandon new economic relations with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	new	_	ADJ	ADJ	_	6	amod
5	economic	_	ADJ	ADJ	_	6	amod
6	relations	_	NOUN	NOUN	_	3	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	6	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	3	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test253': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test253']['sents']['0']:
            print(return_dict['test253']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ " + str(return_dict['test253']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noevent  " )
            print("test253 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"903\")@ noeventexception \n " )
        print("test253 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test253']['sents']['0']:
        verbs=return_dict['test253']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test253']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test253']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test253():
    text="""Arnor will abandon new global economic relations with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	22	advcl
4	new	_	ADJ	ADJ	_	7	amod
5	global	_	ADJ	ADJ	_	7	amod
6	economic	_	ADJ	ADJ	_	7	amod
7	relations	_	NOUN	NOUN	_	3	dobj
8	with	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	7	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	7	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	22	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	22	nsubj
22	said	_	VERB	VERB	_	0	root
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	22	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test254': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test254']['sents']['0']:
            print(return_dict['test254']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ " + str(return_dict['test254']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noevent  " )
            print("test254 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test254 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test254']['sents']['0']:
        verbs=return_dict['test254']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test254']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test254']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test254():
    text="""Arnor will abandon new global economic trade relations with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	will	_	AUX	AUX	_	3	aux
3	abandon	_	VERB	VERB	_	0	root
4	new	_	ADJ	ADJ	_	8	amod
5	global	_	ADJ	ADJ	_	8	amod
6	economic	_	ADJ	ADJ	_	8	amod
7	trade	_	NOUN	NOUN	_	8	compound
8	relations	_	NOUN	NOUN	_	3	dobj
9	with	_	ADP	ADP	_	10	case
10	Gondor	_	PROPN	PROPN	_	8	nmod
11	almost	_	ADV	ADV	_	12	advmod
12	five	_	NUM	NUM	_	13	nummod
13	years	_	NOUN	NOUN	_	3	nmod
14	after	_	ADP	ADP	_	15	case
15	crowds	_	NOUN	NOUN	_	13	nmod
16	trashed	_	VERB	VERB	_	3	advcl
17	its	_	PRON	PRON	_	18	nmod:poss
18	embassy	_	NOUN	NOUN	_	16	dobj
19	,	_	PUNCT	PUNCT	_	18	punct
20	a	_	DET	DET	_	22	det
21	senior	_	ADJ	ADJ	_	22	amod
22	official	_	NOUN	NOUN	_	18	appos
23	said	_	VERB	VERB	_	22	acl
24	on	_	ADP	ADP	_	25	case
25	Saturday	_	PROPN	PROPN	_	23	nmod
26	.	_	PUNCT	PUNCT	_	3	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test255': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test255']['sents']['0']:
            print(return_dict['test255']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ " + str(return_dict['test255']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noevent  " )
            print("test255 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"345\")@ noeventexception \n " )
        print("test255 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test255']['sents']['0']:
        verbs=return_dict['test255']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test255']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test255']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test255():
    text="""Arnor will abandon improved economic relations with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	nsubj
2	will	_	AUX	AUX	_	4	aux
3	abandon	_	ADV	ADV	_	4	advmod
4	improved	_	VERB	VERB	_	0	root
5	economic	_	ADJ	ADJ	_	6	amod
6	relations	_	NOUN	NOUN	_	4	dobj
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	4	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	13	nmod:npmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	4	nmod
14	trashed	_	VERB	VERB	_	4	advcl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	16	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	16	appos
21	said	_	VERB	VERB	_	20	acl
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test256': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test256']['sents']['0']:
            print(return_dict['test256']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ " + str(return_dict['test256']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noevent  " )
            print("test256 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noeventexception \n " )
        print("test256 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test256']['sents']['0']:
        verbs=return_dict['test256']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test256']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test256']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test256():
    text="""Arnor will abandon improved global economic relations with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	4	nsubj
2	will	_	AUX	AUX	_	4	aux
3	abandon	_	ADV	ADV	_	4	advmod
4	improved	_	VERB	VERB	_	0	root
5	global	_	ADJ	ADJ	_	7	amod
6	economic	_	ADJ	ADJ	_	7	amod
7	relations	_	NOUN	NOUN	_	4	dobj
8	with	_	ADP	ADP	_	9	case
9	Gondor	_	PROPN	PROPN	_	7	nmod
10	almost	_	ADV	ADV	_	11	advmod
11	five	_	NUM	NUM	_	12	nummod
12	years	_	NOUN	NOUN	_	14	nmod:npmod
13	after	_	ADP	ADP	_	14	case
14	crowds	_	NOUN	NOUN	_	4	nmod
15	trashed	_	VERB	VERB	_	14	acl
16	its	_	PRON	PRON	_	17	nmod:poss
17	embassy	_	NOUN	NOUN	_	15	dobj
18	,	_	PUNCT	PUNCT	_	17	punct
19	a	_	DET	DET	_	21	det
20	senior	_	ADJ	ADJ	_	21	amod
21	official	_	NOUN	NOUN	_	17	appos
22	said	_	VERB	VERB	_	21	acl
23	on	_	ADP	ADP	_	24	case
24	Saturday	_	PROPN	PROPN	_	22	nmod
25	.	_	PUNCT	PUNCT	_	4	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test257': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test257']['sents']['0']:
            print(return_dict['test257']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ " + str(return_dict['test257']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noevent  " )
            print("test257 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"904\")@ noeventexception \n " )
        print("test257 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test257']['sents']['0']:
        verbs=return_dict['test257']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test257']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test257']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test257():
    text="""Bree Prime Minister Romendacil unexpectedly now won't try to clash over the efforts of Eriadori to deal 
with an orc infestation during a brief private trip to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	9	nsubj
5	unexpectedly	_	ADV	ADV	_	6	advmod
6	now	_	ADV	ADV	_	9	advmod
7	wo	_	AUX	AUX	_	9	aux
8	n't	_	PART	PART	_	9	neg
9	try	_	VERB	VERB	_	0	root
10	to	_	PART	PART	_	11	mark
11	clash	_	VERB	VERB	_	9	xcomp
12	over	_	ADP	ADP	_	14	case
13	the	_	DET	DET	_	14	det
14	efforts	_	NOUN	NOUN	_	11	nmod
15	of	_	ADP	ADP	_	16	case
16	Eriadori	_	PROPN	PROPN	_	14	nmod
17	to	_	PART	PART	_	18	mark
18	deal	_	VERB	VERB	_	11	advcl
19	with	_	ADP	ADP	_	22	case
20	an	_	DET	DET	_	22	det
21	orc	_	ADJ	ADJ	_	22	amod
22	infestation	_	NOUN	NOUN	_	18	nmod
23	during	_	ADP	ADP	_	27	case
24	a	_	DET	DET	_	27	det
25	brief	_	ADJ	ADJ	_	27	amod
26	private	_	ADJ	ADJ	_	27	amod
27	trip	_	NOUN	NOUN	_	18	nmod
28	to	_	ADP	ADP	_	29	case
29	Eriador	_	PROPN	PROPN	_	27	nmod
30	starting	_	VERB	VERB	_	27	acl
31	on	_	ADP	ADP	_	32	case
32	Sunday	_	PROPN	PROPN	_	30	nmod
33	.	_	PUNCT	PUNCT	_	9	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test258': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test258']['sents']['0']:
            print(return_dict['test258']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ " + str(return_dict['test258']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ noevent  " )
            print("test258 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"906\")@ noeventexception \n " )
        print("test258 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test258']['sents']['0']:
        verbs=return_dict['test258']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test258']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test258']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test258():
    text="""Bree Prime Minister Romendacil most certainly won't ever clash over the efforts of Eriadori  
to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	10	nsubj
5	most	_	ADV	ADV	_	6	advmod
6	certainly	_	ADV	ADV	_	10	advmod
7	wo	_	AUX	AUX	_	10	aux
8	n't	_	PART	PART	_	10	neg
9	ever	_	ADV	ADV	_	10	advmod
10	clash	_	VERB	VERB	_	0	root
11	over	_	ADP	ADP	_	13	case
12	the	_	DET	DET	_	13	det
13	efforts	_	NOUN	NOUN	_	10	nmod
14	of	_	ADP	ADP	_	15	case
15	Eriadori	_	PROPN	PROPN	_	13	nmod
16	to	_	PART	PART	_	17	mark
17	deal	_	VERB	VERB	_	10	advcl
18	with	_	ADP	ADP	_	21	case
19	an	_	DET	DET	_	21	det
20	orc	_	ADJ	ADJ	_	21	amod
21	infestation	_	NOUN	NOUN	_	17	nmod
22	during	_	ADP	ADP	_	26	case
23	a	_	DET	DET	_	26	det
24	brief	_	ADJ	ADJ	_	26	amod
25	private	_	ADJ	ADJ	_	26	amod
26	visit	_	NOUN	NOUN	_	17	nmod
27	to	_	ADP	ADP	_	28	case
28	Eriador	_	PROPN	PROPN	_	26	nmod
29	starting	_	VERB	VERB	_	26	acl
30	on	_	ADP	ADP	_	31	case
31	Sunday	_	PROPN	PROPN	_	29	nmod
32	.	_	PUNCT	PUNCT	_	10	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test259': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test259']['sents']['0']:
            print(return_dict['test259']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ " + str(return_dict['test259']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ noevent  " )
            print("test259 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ noeventexception \n " )
        print("test259 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test259']['sents']['0']:
        verbs=return_dict['test259']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test259']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test259']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test259():
    text="""Bree Prime Minister Romendacil most certainly really did not ever clash over the efforts of Eriadori  
to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	11	nsubj
5	most	_	ADV	ADV	_	6	advmod
6	certainly	_	ADV	ADV	_	11	advmod
7	really	_	ADV	ADV	_	11	advmod
8	did	_	AUX	AUX	_	11	aux
9	not	_	PART	PART	_	11	neg
10	ever	_	ADV	ADV	_	11	advmod
11	clash	_	VERB	VERB	_	0	root
12	over	_	ADP	ADP	_	14	case
13	the	_	DET	DET	_	14	det
14	efforts	_	NOUN	NOUN	_	11	nmod
15	of	_	ADP	ADP	_	16	case
16	Eriadori	_	PROPN	PROPN	_	14	nmod
17	to	_	PART	PART	_	18	mark
18	deal	_	VERB	VERB	_	11	advcl
19	with	_	ADP	ADP	_	22	case
20	an	_	DET	DET	_	22	det
21	orc	_	ADJ	ADJ	_	22	amod
22	infestation	_	NOUN	NOUN	_	18	nmod
23	during	_	ADP	ADP	_	27	case
24	a	_	DET	DET	_	27	det
25	brief	_	ADJ	ADJ	_	27	amod
26	private	_	ADJ	ADJ	_	27	amod
27	visit	_	NOUN	NOUN	_	18	nmod
28	to	_	ADP	ADP	_	29	case
29	Eriador	_	PROPN	PROPN	_	27	nmod
30	starting	_	VERB	VERB	_	27	acl
31	on	_	ADP	ADP	_	32	case
32	Sunday	_	PROPN	PROPN	_	30	nmod
33	.	_	PUNCT	PUNCT	_	11	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test260': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test260']['sents']['0']:
            print(return_dict['test260']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ " + str(return_dict['test260']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ noevent  " )
            print("test260 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"907\")@ noeventexception \n " )
        print("test260 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test260']['sents']['0']:
        verbs=return_dict['test260']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test260']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test260']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test260():
    text="""Bree Prime Minister Romendacil most certainly really did not even ever clash over the efforts 
of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	12	nsubj
5	most	_	ADV	ADV	_	6	advmod
6	certainly	_	ADV	ADV	_	12	advmod
7	really	_	ADV	ADV	_	12	advmod
8	did	_	AUX	AUX	_	12	aux
9	not	_	PART	PART	_	12	neg
10	even	_	ADV	ADV	_	11	advmod
11	ever	_	ADV	ADV	_	12	advmod
12	clash	_	VERB	VERB	_	0	root
13	over	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	efforts	_	NOUN	NOUN	_	12	nmod
16	of	_	ADP	ADP	_	17	case
17	Eriadori	_	PROPN	PROPN	_	15	nmod
18	to	_	PART	PART	_	19	mark
19	deal	_	VERB	VERB	_	12	advcl
20	with	_	ADP	ADP	_	23	case
21	an	_	DET	DET	_	23	det
22	orc	_	ADJ	ADJ	_	23	amod
23	infestation	_	NOUN	NOUN	_	19	nmod
24	during	_	ADP	ADP	_	28	case
25	a	_	DET	DET	_	28	det
26	brief	_	ADJ	ADJ	_	28	amod
27	private	_	ADJ	ADJ	_	28	amod
28	visit	_	NOUN	NOUN	_	19	nmod
29	to	_	ADP	ADP	_	30	case
30	Eriador	_	PROPN	PROPN	_	28	nmod
31	starting	_	VERB	VERB	_	28	acl
32	on	_	ADP	ADP	_	33	case
33	Sunday	_	PROPN	PROPN	_	31	nmod
34	.	_	PUNCT	PUNCT	_	12	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test261': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test261']['sents']['0']:
            print(return_dict['test261']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ " + str(return_dict['test261']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noevent  " )
            print("test261 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noeventexception \n " )
        print("test261 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test261']['sents']['0']:
        verbs=return_dict['test261']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test261']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test261']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test261():
    text="""Bree Prime Minister Romendacil most certainly really won't even ever clash over the efforts 
of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. 
"""
    parse="""1	Bree	_	PROPN	PROPN	_	3	compound
2	Prime	_	PROPN	PROPN	_	3	compound
3	Minister	_	PROPN	PROPN	_	4	compound
4	Romendacil	_	PROPN	PROPN	_	12	nsubj
5	most	_	ADV	ADV	_	6	advmod
6	certainly	_	ADV	ADV	_	12	advmod
7	really	_	ADV	ADV	_	12	advmod
8	wo	_	AUX	AUX	_	12	aux
9	n't	_	PART	PART	_	12	neg
10	even	_	ADV	ADV	_	11	advmod
11	ever	_	ADV	ADV	_	12	advmod
12	clash	_	VERB	VERB	_	0	root
13	over	_	ADP	ADP	_	15	case
14	the	_	DET	DET	_	15	det
15	efforts	_	NOUN	NOUN	_	12	nmod
16	of	_	ADP	ADP	_	17	case
17	Eriadori	_	PROPN	PROPN	_	15	nmod
18	to	_	PART	PART	_	19	mark
19	deal	_	VERB	VERB	_	12	advcl
20	with	_	ADP	ADP	_	23	case
21	an	_	DET	DET	_	23	det
22	orc	_	ADJ	ADJ	_	23	amod
23	infestation	_	NOUN	NOUN	_	19	nmod
24	during	_	ADP	ADP	_	28	case
25	a	_	DET	DET	_	28	det
26	brief	_	ADJ	ADJ	_	28	amod
27	private	_	ADJ	ADJ	_	28	amod
28	visit	_	NOUN	NOUN	_	19	nmod
29	to	_	ADP	ADP	_	30	case
30	Eriador	_	PROPN	PROPN	_	28	nmod
31	starting	_	VERB	VERB	_	28	acl
32	on	_	ADP	ADP	_	33	case
33	Sunday	_	PROPN	PROPN	_	31	nmod
34	.	_	PUNCT	PUNCT	_	12	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test262': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test262']['sents']['0']:
            print(return_dict['test262']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ " + str(return_dict['test262']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noevent  " )
            print("test262 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"BREGOV\", u\"ERI\", u\"905\")@ noeventexception \n " )
        print("test262 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test262']['sents']['0']:
        verbs=return_dict['test262']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test262']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test262']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test262():
    text="""Calenardhon welcomed memos from Bree on its role for in forthcoming peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	memos	_	NOUN	NOUN	_	2	dobj
4	from	_	ADP	ADP	_	5	case
5	Bree	_	PROPN	PROPN	_	2	nmod
6	on	_	ADP	ADP	_	8	case
7	its	_	PRON	PRON	_	8	nmod:poss
8	role	_	NOUN	NOUN	_	2	nmod
9	for	_	ADP	ADP	_	13	case
10	in	_	ADP	ADP	_	13	case
11	forthcoming	_	ADJ	ADJ	_	13	amod
12	peace	_	NOUN	NOUN	_	13	compound
13	talks	_	NOUN	NOUN	_	2	nmod
14	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test263': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test263']['sents']['0']:
            print(return_dict['test263']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ " + str(return_dict['test263']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noevent  " )
            print("test263 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noeventexception \n " )
        print("test263 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test263']['sents']['0']:
        verbs=return_dict['test263']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test263']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test263']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test263():
    text="""Calenardhon welcomed economic memos from Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	economic	_	ADJ	ADJ	_	4	amod
4	memos	_	NOUN	NOUN	_	2	dobj
5	from	_	ADP	ADP	_	6	case
6	Bree	_	PROPN	PROPN	_	2	nmod
7	on	_	ADP	ADP	_	9	case
8	its	_	PRON	PRON	_	9	nmod:poss
9	role	_	NOUN	NOUN	_	2	nmod
10	for	_	ADP	ADP	_	14	case
11	in	_	ADP	ADP	_	14	case
12	forthcoming	_	ADJ	ADJ	_	14	amod
13	peace	_	NOUN	NOUN	_	14	compound
14	talks	_	NOUN	NOUN	_	2	nmod
15	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test264': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test264']['sents']['0']:
            print(return_dict['test264']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ " + str(return_dict['test264']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ noevent  " )
            print("test264 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ noeventexception \n " )
        print("test264 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test264']['sents']['0']:
        verbs=return_dict['test264']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test264']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test264']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test264():
    text="""Calenardhon welcomed economic rumors about Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	economic	_	ADJ	ADJ	_	4	amod
4	rumors	_	NOUN	NOUN	_	2	dobj
5	about	_	ADP	ADP	_	6	case
6	Bree	_	PROPN	PROPN	_	2	nmod
7	on	_	ADP	ADP	_	9	case
8	its	_	PRON	PRON	_	9	nmod:poss
9	role	_	NOUN	NOUN	_	2	nmod
10	for	_	ADP	ADP	_	14	case
11	in	_	ADP	ADP	_	14	case
12	forthcoming	_	ADJ	ADJ	_	14	amod
13	peace	_	NOUN	NOUN	_	14	compound
14	talks	_	NOUN	NOUN	_	2	nmod
15	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test265': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test265']['sents']['0']:
            print(return_dict['test265']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ " + str(return_dict['test265']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ noevent  " )
            print("test265 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ noeventexception \n " )
        print("test265 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test265']['sents']['0']:
        verbs=return_dict['test265']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test265']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test265']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test265():
    text="""Calenardhon welcomed economic memos not about Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	economic	_	ADJ	ADJ	_	4	amod
4	memos	_	NOUN	NOUN	_	2	dobj
5	not	_	PART	PART	_	4	case
6	about	_	ADP	ADP	_	7	case
7	Bree	_	PROPN	PROPN	_	2	nmod
8	on	_	ADP	ADP	_	10	case
9	its	_	PRON	PRON	_	10	nmod:poss
10	role	_	NOUN	NOUN	_	2	nmod
11	for	_	ADP	ADP	_	15	case
12	in	_	ADP	ADP	_	15	case
13	forthcoming	_	ADJ	ADJ	_	15	amod
14	peace	_	NOUN	NOUN	_	15	compound
15	talks	_	NOUN	NOUN	_	2	nmod
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test266': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test266']['sents']['0']:
            print(return_dict['test266']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ " + str(return_dict['test266']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ noevent  " )
            print("test266 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"915\")@ noeventexception \n " )
        print("test266 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test266']['sents']['0']:
        verbs=return_dict['test266']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test266']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test266']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test266():
    text="""Calenardhon welcomed cultural memos sent by Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	cultural	_	ADJ	ADJ	_	4	amod
4	memos	_	NOUN	NOUN	_	2	dobj
5	sent	_	VERB	VERB	_	4	acl
6	by	_	ADP	ADP	_	7	case
7	Bree	_	PROPN	PROPN	_	5	nmod
8	on	_	ADP	ADP	_	10	case
9	its	_	PRON	PRON	_	10	nmod:poss
10	role	_	NOUN	NOUN	_	5	nmod
11	for	_	ADP	ADP	_	15	case
12	in	_	ADP	ADP	_	15	case
13	forthcoming	_	ADJ	ADJ	_	15	amod
14	peace	_	NOUN	NOUN	_	15	compound
15	talks	_	NOUN	NOUN	_	5	nmod
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test267': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"912\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test267']['sents']['0']:
            print(return_dict['test267']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"912\")@ " + str(return_dict['test267']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"912\")@ noevent  " )
            print("test267 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"912\")@ noeventexception \n " )
        print("test267 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test267']['sents']['0']:
        verbs=return_dict['test267']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test267']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test267']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test267():
    text="""Calenardhon welcomed cultural secret memos sent by Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	cultural	_	ADJ	ADJ	_	5	amod
4	secret	_	ADJ	ADJ	_	5	amod
5	memos	_	NOUN	NOUN	_	2	dobj
6	sent	_	VERB	VERB	_	5	acl
7	by	_	ADP	ADP	_	8	case
8	Bree	_	PROPN	PROPN	_	6	nmod
9	on	_	ADP	ADP	_	11	case
10	its	_	PRON	PRON	_	11	nmod:poss
11	role	_	NOUN	NOUN	_	6	nmod
12	for	_	ADP	ADP	_	16	case
13	in	_	ADP	ADP	_	16	case
14	forthcoming	_	ADJ	ADJ	_	16	amod
15	peace	_	NOUN	NOUN	_	16	compound
16	talks	_	NOUN	NOUN	_	6	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test268': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test268']['sents']['0']:
            print(return_dict['test268']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ " + str(return_dict['test268']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noevent  " )
            print("test268 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noeventexception \n " )
        print("test268 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test268']['sents']['0']:
        verbs=return_dict['test268']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test268']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test268']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test268():
    text="""Calenardhon welcomed memos on economic issue from Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	memos	_	NOUN	NOUN	_	2	dobj
4	on	_	ADP	ADP	_	6	case
5	economic	_	ADJ	ADJ	_	6	amod
6	issue	_	NOUN	NOUN	_	2	nmod
7	from	_	ADP	ADP	_	8	case
8	Bree	_	PROPN	PROPN	_	2	nmod
9	on	_	ADP	ADP	_	11	case
10	its	_	PRON	PRON	_	11	nmod:poss
11	role	_	NOUN	NOUN	_	2	nmod
12	for	_	ADP	ADP	_	16	case
13	in	_	ADP	ADP	_	16	case
14	forthcoming	_	ADJ	ADJ	_	16	amod
15	peace	_	NOUN	NOUN	_	16	compound
16	talks	_	NOUN	NOUN	_	2	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test269': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test269']['sents']['0']:
            print(return_dict['test269']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ " + str(return_dict['test269']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ noevent  " )
            print("test269 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"911\")@ noeventexception \n " )
        print("test269 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test269']['sents']['0']:
        verbs=return_dict['test269']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test269']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test269']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test269():
    text="""Calenardhon welcomed cultural internal memos from Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	cultural	_	ADJ	ADJ	_	5	amod
4	internal	_	ADJ	ADJ	_	5	amod
5	memos	_	NOUN	NOUN	_	2	dobj
6	from	_	ADP	ADP	_	7	case
7	Bree	_	PROPN	PROPN	_	2	nmod
8	on	_	ADP	ADP	_	10	case
9	its	_	PRON	PRON	_	10	nmod:poss
10	role	_	NOUN	NOUN	_	2	nmod
11	for	_	ADP	ADP	_	15	case
12	in	_	ADP	ADP	_	15	case
13	forthcoming	_	ADJ	ADJ	_	15	amod
14	peace	_	NOUN	NOUN	_	15	compound
15	talks	_	NOUN	NOUN	_	2	nmod
16	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test270': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test270']['sents']['0']:
            print(return_dict['test270']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ " + str(return_dict['test270']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noevent  " )
            print("test270 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"041\")@ noeventexception \n " )
        print("test270 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test270']['sents']['0']:
        verbs=return_dict['test270']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test270']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test270']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test270():
    text="""Calenardhon welcomed cultural internal assurances sent by Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	cultural	_	ADJ	ADJ	_	5	amod
4	internal	_	ADJ	ADJ	_	5	amod
5	assurances	_	NOUN	NOUN	_	2	dobj
6	sent	_	VERB	VERB	_	5	acl
7	by	_	ADP	ADP	_	8	case
8	Bree	_	PROPN	PROPN	_	6	nmod
9	on	_	ADP	ADP	_	11	case
10	its	_	PRON	PRON	_	11	nmod:poss
11	role	_	NOUN	NOUN	_	6	nmod
12	for	_	ADP	ADP	_	16	case
13	in	_	ADP	ADP	_	16	case
14	forthcoming	_	ADJ	ADJ	_	16	amod
15	peace	_	NOUN	NOUN	_	16	compound
16	talks	_	NOUN	NOUN	_	6	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test271': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"914\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test271']['sents']['0']:
            print(return_dict['test271']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"914\")@ " + str(return_dict['test271']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"914\")@ noevent  " )
            print("test271 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"914\")@ noeventexception \n " )
        print("test271 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test271']['sents']['0']:
        verbs=return_dict['test271']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test271']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test271']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test271():
    text="""Calenardhon welcomed assurances on cultural issues from Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	assurances	_	NOUN	NOUN	_	2	dobj
4	on	_	ADP	ADP	_	6	case
5	cultural	_	ADJ	ADJ	_	6	amod
6	issues	_	NOUN	NOUN	_	2	nmod
7	from	_	ADP	ADP	_	8	case
8	Bree	_	PROPN	PROPN	_	2	nmod
9	on	_	ADP	ADP	_	11	case
10	its	_	PRON	PRON	_	11	nmod:poss
11	role	_	NOUN	NOUN	_	2	nmod
12	for	_	ADP	ADP	_	16	case
13	in	_	ADP	ADP	_	16	case
14	forthcoming	_	ADJ	ADJ	_	16	amod
15	peace	_	NOUN	NOUN	_	16	compound
16	talks	_	NOUN	NOUN	_	2	nmod
17	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test272': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test272']['sents']['0']:
            print(return_dict['test272']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ " + str(return_dict['test272']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ noevent  " )
            print("test272 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ noeventexception \n " )
        print("test272 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test272']['sents']['0']:
        verbs=return_dict['test272']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test272']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test272']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test272():
    text="""Calenardhon welcomed assurances on cultural issues sent from Bree on its role for in forthcoming 
peace talks. 
"""
    parse="""1	Calenardhon	_	PROPN	PROPN	_	2	nsubj
2	welcomed	_	VERB	VERB	_	0	root
3	assurances	_	NOUN	NOUN	_	2	dobj
4	on	_	ADP	ADP	_	6	case
5	cultural	_	ADJ	ADJ	_	6	amod
6	issues	_	NOUN	NOUN	_	3	nmod
7	sent	_	VERB	VERB	_	6	acl
8	from	_	ADP	ADP	_	9	case
9	Bree	_	PROPN	PROPN	_	7	nmod
10	on	_	ADP	ADP	_	12	case
11	its	_	PRON	PRON	_	12	nmod:poss
12	role	_	NOUN	NOUN	_	7	nmod
13	for	_	ADP	ADP	_	17	case
14	in	_	ADP	ADP	_	17	case
15	forthcoming	_	ADJ	ADJ	_	17	amod
16	peace	_	NOUN	NOUN	_	17	compound
17	talks	_	NOUN	NOUN	_	7	nmod
18	.	_	PUNCT	PUNCT	_	2	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test273': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test273']['sents']['0']:
            print(return_dict['test273']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ " + str(return_dict['test273']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ noevent  " )
            print("test273 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"CAL\", u\"BRE\", u\"913\")@ noeventexception \n " )
        print("test273 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test273']['sents']['0']:
        verbs=return_dict['test273']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test273']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test273']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
def test273():
    text="""Arnor is inching nearer to accord with Gondor almost 
five years after crowds trashed its embassy, a senior official 
said on Saturday. 
"""
    parse="""1	Arnor	_	PROPN	PROPN	_	3	nsubj
2	is	_	AUX	AUX	_	3	aux
3	inching	_	VERB	VERB	_	21	advcl
4	nearer	_	NOUN	NOUN	_	3	dobj
5	to	_	ADP	ADP	_	6	case
6	accord	_	NOUN	NOUN	_	4	nmod
7	with	_	ADP	ADP	_	8	case
8	Gondor	_	PROPN	PROPN	_	6	nmod
9	almost	_	ADV	ADV	_	10	advmod
10	five	_	NUM	NUM	_	11	nummod
11	years	_	NOUN	NOUN	_	3	nmod
12	after	_	ADP	ADP	_	13	case
13	crowds	_	NOUN	NOUN	_	11	nmod
14	trashed	_	VERB	VERB	_	13	acl
15	its	_	PRON	PRON	_	16	nmod:poss
16	embassy	_	NOUN	NOUN	_	14	dobj
17	,	_	PUNCT	PUNCT	_	21	punct
18	a	_	DET	DET	_	20	det
19	senior	_	ADJ	ADJ	_	20	amod
20	official	_	NOUN	NOUN	_	21	nsubj
21	said	_	VERB	VERB	_	0	root
22	on	_	ADP	ADP	_	23	case
23	Saturday	_	PROPN	PROPN	_	21	nmod
24	.	_	PUNCT	PUNCT	_	21	punct
"""
    phrase_dict = parse_parser(parse)
    parsed = utilities._format_ud_parsed_str(parse)
    dict = {u'test274': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch_ud.do_coding(dict)
    except Exception as e: 
        fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"083\")@ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test274']['sents']['0']:
            print(return_dict['test274']['sents']['0']['events'])
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"083\")@ " + str(return_dict['test274']['sents']['0']['events']) )
        else:
            fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"083\")@ noevent  " )
            print("test274 Failed")
    except:
        #fout_report.write(text.replace("\n"," ") +"@"+ parsed.replace("\n"," ") +"@ (u\"ARN\", u\"GON\", u\"083\")@ noeventexception \n " )
        print("test274 Failed")
    #Print the verbs
    if 'verbs' in return_dict['test274']['sents']['0']:
        verbs=return_dict['test274']['sents']['0']['verbs']
        parse_verb_noun(verbs,phrase_dict)
    if 'nouns' in return_dict['test274']['sents']['0']:
        #Print the nouns
        nouns=return_dict['test274']['sents']['0']['nouns']
        parse_verb_noun(nouns,phrase_dict)
    fout_report.write("\n")
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()
test24()
test25()
test26()
test27()
test28()
test29()
test30()
test31()
test32()
test33()
test34()
test35()
test36()
test37()
test38()
test39()
test40()
test41()
test42()
test43()
test44()
test45()
test46()
test47()
test48()
test49()
test50()
test51()
test52()
test53()
test54()
test55()
test56()
test57()
test58()
test59()
test60()
test61()
test62()
test63()
test64()
test65()
test66()
test67()
test68()
test69()
test70()
test71()
test72()
test73()
test74()
test75()
test76()
test77()
test78()
test79()
test80()
test81()
test82()
test83()
test84()
test85()
test86()
test87()
test88()
test89()
test90()
test91()
test92()
test93()
test94()
test95()
test96()
test97()
test98()
test99()
test100()
test101()
test102()
test103()
test104()
test105()
test106()
test107()
test108()
test109()
test110()
test111()
test112()
test113()
test114()
test115()
test116()
test117()
test118()
test119()
test120()
test121()
test122()
test123()
test124()
test125()
test126()
test127()
test128()
test129()
test130()
test131()
test132()
test133()
test134()
test135()
test136()
test137()
test138()
test139()
test140()
test141()
test142()
test143()
test144()
test145()
test146()
test147()
test148()
test149()
test150()
test151()
test152()
test153()
test154()
test155()
test156()
test157()
test158()
test159()
test160()
test161()
test162()
test163()
test164()
test165()
test166()
test167()
test168()
test169()
test170()
test171()
test172()
test173()
test174()
test175()
test176()
test177()
test178()
test179()
test180()
test181()
test182()
test183()
test184()
test185()
test186()
test187()
test188()
test189()
test190()
test191()
test192()
test193()
test194()
test195()
test196()
test197()
test198()
test199()
test200()
test201()
test202()
test203()
test204()
test205()
test206()
test207()
test208()
test209()
test210()
test211()
test212()
test213()
test214()
test215()
test216()
test217()
test218()
test219()
test220()
test221()
test222()
test223()
test224()
test225()
test226()
test227()
test228()
test229()
test230()
test231()
test232()
test233()
test234()
test235()
test236()
test237()
test238()
test239()
test240()
test241()
test242()
test243()
test244()
test245()
test246()
test247()
test248()
test249()
test250()
test251()
test252()
test253()
test254()
test255()
test256()
test257()
test258()
test259()
test260()
test261()
test262()
test263()
test264()
test265()
test266()
test267()
test268()
test269()
test270()
test271()
test272()
test273()

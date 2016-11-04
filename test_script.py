#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import petrarch2, PETRglobals, PETRreader, utilities, codecs

config = utilities._get_data('data/config/', 'PETR_config.ini')
print("reading config")
PETRreader.parse_Config(config)
print("reading dicts")
petrarch2.read_dictionaries()
fout_report = codecs.open("test_report.txt","w",encoding='utf8') #opens test report file for writing
fout_report.write("Text~ Parse Tree~ Expected Encoding as per Petrarch~ Result from Petrarch2\n")
def test1():
    text="Arnor is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test2': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test2']['sents']['0']:
            print(return_dict['test2']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test2']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test2 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test2 Failed")
def test2():
    text="Arnor is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday."
    parse="(ROOT (S    (S      (NP (NNP Arnor) )    (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test3': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test3']['sents']['0']:
            print(return_dict['test3']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test3']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test3 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test3 Failed")
def test3():
    text="Dagolath's first Deputy Prime Minister Telemar left for Minas Tirith on Wednesday for meetings of the joint transport committee with Arnor, the Dagolathi news agency reported. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Dagolath) (POS 's)      )  (ADJP         (JJ first)      )  (NNP Deputy) (NNP Prime) (NNP Minister) (NNP Telemar)    )      (VP       (VBD left)        (PP (IN for)  (NP            (NP (NNP Minas) (NNP Tirith)          )            (PP (IN on)  (NP (NNP Wednesday)        ) ) )      )        (PP (IN for)  (NP            (NP (NNS meetings)          )            (PP (IN of)  (NP                (NP (DT the) (JJ joint) (NN transport) (NN committee)              )                (PP (IN with)  (NP (NNP Arnor)            ) ) )        ) )      )    )  )  (, ,)  (NP (DT the) (NNP Dagolathi) (NN news) (NN agency)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test4': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test4']['sents']['0']:
            print(return_dict['test4']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")~ " + str(return_dict['test4']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")~ noevent \n " )
            print("test4 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"DAGGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"DAGGOV\", u\"033\")~ noeventexception \n " )
        print("test4 Failed")
def test4():
    text="Caras Galadhon's new mayor left yesterday for Minas Tirith for meetings of the joint transport committee with Arnor. "
    parse="(ROOT (S    (NP      (NP (NNP Caras) (NNP Galadhon) (POS 's)    ) (JJ new) (NN mayor)  )    (VP     (VBD left)  (NP-TMP       (NN yesterday)    )      (PP (IN for) (NP (NNP Minas) (NNP Tirith)      )    )      (PP (IN for) (NP         (NP (NNS meetings)        )          (PP (IN of) (NP (DT the) (JJ joint) (NN transport) (NN committee)      ) ) )    )      (PP (IN with) (NP (NN Arnor)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test5': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test5']['sents']['0']:
            print(return_dict['test5']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")~ " + str(return_dict['test5']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")~ noevent \n " )
            print("test5 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"032\"),(u\"GON\", u\"ELF\", u\"033\")~ noeventexception \n " )
        print("test5 Failed")
def test5():
    text="Arnor is about to restore fxll diplomatic ties with Gondor almost five years after volleyball crowds burned down its embassy,  a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ fxll) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NN volleyball) (NNS crowds)                  )                    (VP                     (VBD burned)  (PRT                       (RP down)                    )  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test6': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test6']['sents']['0']:
            print(return_dict['test6']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test6']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test6 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test6 Failed")
def test6():
    text="An Eriadorian was shot dead in Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP (DT An) (NN Eriadorian)  )    (VP     (VBD was)      (VP       (VBN shot)  (ADJP         (JJ dead)      )        (PP (IN in)  (NP            (NP (NNP Osgiliath)          )  (, ,)  (NP              (NP (DT the) (NN state) (POS 's)            )  (JJS fiercest) (NN foe)      ) ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test7': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"224\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test7']['sents']['0']:
            print(return_dict['test7']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"224\")~ " + str(return_dict['test7']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"224\")~ noevent \n " )
            print("test7 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"224\")~ noeventexception \n " )
        print("test7 Failed")
def test7():
    text="The Calenardhon government condemned an attack by Osgiliath soldiers in south Ithilen on Thursday and promised aid to the affected Ithilen villages. "
    parse="(ROOT (S    (NP (DT The) (JJ Calenardhon) (NN government)  )    (VP      (VP       (VBD condemned)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)      ) )    )  (CC and)      (VP       (VBD promised)  (NP (NN aid)      )        (PP         (TO to)  (NP (DT the) (VBN affected) (NN Ithilen) (NNS villages)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test8': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test8']['sents']['0']:
            print(return_dict['test8']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ " + str(return_dict['test8']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ noevent \n " )
            print("test8 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ noeventexception \n " )
        print("test8 Failed")
def test8():
    text="Arnor believes Dagolath and Osgiliath can cope with a decrease in vital water from the mighty Entwash river when a major dam is filled next month. "
    parse="(ROOT (S   (NP (NNP Arnor)  )   (VP     (VBZ believes)     (SBAR       (S         (NP (NNP Dagolath) (CC and) (NNP Osgiliath)        )         (VP           (MD can)           (VP             (VB cope)             (PP (IN with) (NP                 (NP (DT a) (NN decrease)                )                 (PP (IN in) (NP                     (JJ vital) (NN water)              ) ) )            )             (PP (IN from) (NP                 (NP (DT the) (JJ mighty) (JJ Entwash) (NN river)                )                 (SBAR                   (WHADVP                     (WRB when)                  ) (S                     (NP (DT a) (JJ major) (NN dam)                    )                     (VP                       (VBZ is)                       (VP                         (VBN filled) (NP-TMP                           (JJ next) (NN month)                    ) ) )                ) )                ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test9': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950107'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test9']['sents']['0']:
            print(return_dict['test9']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")~ " + str(return_dict['test9']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")~ noevent \n " )
            print("test9 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"023\"),(u\"ARN\", u\"OSG\", u\"023\")~ noeventexception \n " )
        print("test9 Failed")
def test9():
    text="The ambassadors of Arnor, Osgiliath and Gondor presented credentials to Ithilen's president on Wednesday in a further show of support to his government by their countries. "
    parse="(ROOT (S    (NP      (NP (DT The) (NNS ambassadors)    )      (PP (IN of)  (NP (NNP Arnor) (, ,) (NNP Osgiliath)  (CC and)  (NNP Gondor)    ) )  )    (VP     (VBD presented)  (NP (NNS credentials)    )      (PP       (TO to)  (NP          (NP            (NP (NNP Ithilen) (POS 's)          )  (NN president)        )          (PP (IN on)  (NP              (NP (NNP Wednesday)            )              (PP (IN in)  (NP                  (NP (DT a) (JJ further) (NN show)                )                  (PP (IN of)  (NP (NN support)              ) ) )          ) )        )      )    )      (PP       (TO to)  (NP         (PRP$ his) (NN government)      )    )      (PP (IN by)  (NP         (PRP$ their) (NNS countries)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test10': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950108'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test10']['sents']['0']:
            print(return_dict['test10']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ " + str(return_dict['test10']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ noevent \n " )
            print("test10 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ noeventexception \n " )
        print("test10 Failed")
def test10():
    text="Gondor's Prime Minister Falastur noted that Cirith Ungol regretted Eriador's refusal to talk to Calenardhon leader Calimehtar. "
    parse="(ROOT (S    (NP      (NP (NNP Gondor) (POS 's)    )  (NNP Prime) (NNP Minister) (NNP Falastur)  )    (VP     (VBD noted)      (SBAR       (IN that)  (S          (NP (NNP Cirith) (NNP Ungol)        )          (VP           (VBD regretted)  (NP              (NP (NNP Eriador) (POS 's)            )  (NN refusal)  (S                (VP                 (TO to)                  (VP                   (VB talk)                    (PP                     (TO to)  (NP (NNP Calenardhon) (NN leader) (NNP Calimehtar)                ) ) )            ) )            ) ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test11': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950110'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GONGOV\", u\"MORMIL\", u\"115\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test11']['sents']['0']:
            print(return_dict['test11']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GONGOV\", u\"MORMIL\", u\"115\")~ " + str(return_dict['test11']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GONGOV\", u\"MORMIL\", u\"115\")~ noevent \n " )
            print("test11 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GONGOV\", u\"MORMIL\", u\"115\")~ noeventexception \n " )
        print("test11 Failed")
def test11():
    text="Bree Prime Minister Romendacil will meet Eriadori and Calenardhon leaders during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S    (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (MD will)      (VP       (VB meet)  (NP          (NP (NNP Eriadori)  (CC and)  (NNP Calenardhon)        )  (NNS leaders)      )        (PP (IN during)  (NP            (NP (DT a) (JJ brief) (JJ private) (NN visit)          )            (PP             (TO to)  (NP (NNP Eriador)        ) ) )      )        (PP         (VBG starting)          (PP (IN on)  (NP (NNP Sunday)      ) ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test12': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test12']['sents']['0']:
            print(return_dict['test12']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")~ " + str(return_dict['test12']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")~ noevent \n " )
            print("test12 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"031\"),(u\"ERI\", u\"BREGOV\", u\"031\"),(u\"BREGOV\", u\"CAL\", u\"031\"),(u\"CAL\", u\"BREGOV\", u\"031\")~ noeventexception \n " )
        print("test12 Failed")
def test12():
    text="Eriador expressed hopes on Thursday that Osgiliath, the state's fiercest foe, could be drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT (S    (NP (NNP Eriador)  )    (VP     (VBD expressed)  (NP (NNS hopes)    )      (PP (IN on)  (NP (NNP Thursday)      )    )      (SBAR        (WHNP         (WDT that)      )  (S          (NP            (NP (NNP Osgiliath)          )  (, ,)  (NP              (NP (DT the) (NN state) (POS 's)            )  (JJS fiercest) (NN foe)          )  (, ,)        )          (VP           (MD could)            (VP             (VB be)              (VP               (VBN drawn)                (PP (IN into)  (NP (DT the) (NN peace) (NN process)                )              )                (PP (IN by)  (NP                    (NP                     (PRP$ its) (NN resumption)                  )                    (PP (IN of)  (NP                       (JJ diplomatic) (NNS ties)                ) ) )              )                (PP (IN with)  (NP (NNP Gondor)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test13': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"024\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test13']['sents']['0']:
            print(return_dict['test13']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"024\")~ " + str(return_dict['test13']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"024\")~ noevent \n " )
            print("test13 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"024\")~ noeventexception \n " )
        print("test13 Failed")
def test13():
    text="Arnor on Thursday signed an 800 million ducat trade protocolfor 1990 with Dagolath, its biggest trading partner, officials said. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Arnor)      )        (PP (IN on)  (NP (NNP Thursday)      ) )    )      (VP       (VBD signed)  (NP (DT an)  (ADJP            (QP             (CD 800) (CD million)          )        )  (NN ducat) (NN trade) (NN protocol)      )        (PP (IN for)  (NP           (CD 1990)        )      )        (PP (IN with)  (NP (NN Dagolath)        )      )  (, ,)  (S          (NP           (PRP$ its) (JJS biggest) (NN trading) (NN partner)    ) ) )  )  (, ,)  (NP (NNS officials)  )    (VP     (VBD said)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test14': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test14']['sents']['0']:
            print(return_dict['test14']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ " + str(return_dict['test14']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ noevent \n " )
            print("test14 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ noeventexception \n " )
        print("test14 Failed")
def test14():
    text="Ithilen's militia vowed on Thursday to wage war on the Rohans until that group yielded ground seized in six days of fighting."
    parse="(ROOT (S    (NP      (NP (NNP Ithilen) (POS 's)    )  (NN militia)  )    (VP     (VBD vowed)      (PP (IN on)  (NP (NNP Thursday)      )    )  (S        (VP         (TO to)          (VP           (VB wage)  (NP (NN war)          )            (PP (IN on)  (NP (DT the) (NNPS Rohans)            )          )            (SBAR             (IN until)  (S                (NP (DT that) (NN group)              )                (VP                 (VBD yielded)                  (SBAR                    (S                      (NP (NN ground)                    )                      (VP                       (VBD seized)                        (PP (IN in)  (NP                            (NP                             (CD six) (NNS days)                          )                            (PP (IN of)  (NP (NN fighting)                        ) ) )                    ) )                    ) ) )          ) )    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test15': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950114'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"ROH\", u\"173\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test15']['sents']['0']:
            print(return_dict['test15']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"ROH\", u\"173\")~ " + str(return_dict['test15']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"ROH\", u\"173\")~ noevent \n " )
            print("test15 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"ROH\", u\"173\")~ noeventexception \n " )
        print("test15 Failed")
def test15():
    text="Arnor signed an accord on Thursday to supply Gondor with some 50,000 tonnes of wheat, worth 11.8 million ducats, an Arnorian embassy spokesman said."
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBD signed)  (NP (DT an) (NN accord)      )        (PP (IN on)  (NP (NNP Thursday)        )      )  (S          (VP           (TO to)            (VP             (VB supply)  (NP (NNP Gondor)            )              (PP (IN with)  (NP                  (NP (DT some) (CD 50,000) (NNS tonnes)                )                  (PP (IN of)  (NP (NN wheat)              ) ) )            )  (, ,)  (ADJP               (JJ worth)  (NP                  (QP                   (CD 11.8) (CD million)                )  (NNS ducats)          ) ) )      ) )    )  )  (, ,)  (NP (DT an) (JJ Arnorian) (NN embassy) (NN spokesman)  )    (VP     (VBD said)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test16': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950115'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test16']['sents']['0']:
            print(return_dict['test16']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ " + str(return_dict['test16']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ noevent \n " )
            print("test16 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ noeventexception \n " )
        print("test16 Failed")
def test16():
    text="Fornost President Umbardacil has again appealed for peace in Ithilen in a message to the spiritial leader of the war-torn nation's influential Douzu community."
    parse="(ROOT (S    (NP (NNP Fornost) (NNP President) (NNP Umbardacil)  )    (VP     (VBZ has)  (ADVP       (RB again)    )      (VP       (VBN appealed)        (PP (IN for)  (NP            (NP (NN peace)          )            (PP (IN in)  (NP (NNP Ithilen)        ) ) )      )        (PP (IN in)  (NP (DT a) (NN message)        )      )        (PP         (TO to)  (NP            (NP (DT the) (JJ spiritial) (NN leader)          )            (PP (IN of)  (NP                (NP (DT the) (JJ war-torn) (NN nation) (POS 's)              )  (JJ influential) (NNP Douzu) (NN community)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test17': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950116'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITH\", u\"095\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test17']['sents']['0']:
            print(return_dict['test17']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITH\", u\"095\")~ " + str(return_dict['test17']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITH\", u\"095\")~ noevent \n " )
            print("test17 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITH\", u\"095\")~ noeventexception \n " )
        print("test17 Failed")
def test17():
    text="Bree President Romendacil arrived in Gondor on Monday on his first official foreign visit since pro-restoration demonstrators in Eymn Muil were crushed last June."
    parse="(ROOT (S    (NP (NNP Bree) (NNP President) (NNP Romendacil)  )    (VP     (VBD arrived)      (PP (IN in)  (NP (NNP Gondor)      )    )      (PP (IN on)  (NP          (NP (NNP Monday)        )          (PP (IN on)  (NP             (PRP$ his) (JJ first) (JJ official) (JJ foreign) (NN visit)      ) ) )    )      (SBAR       (IN since)  (S          (NP            (NP (NN pro-restoration) (NNS demonstrators)          )            (PP (IN in)  (NP (NNP Eymn) (NNP Muil)          ) )        )          (VP           (VBD were)            (VP             (VBN crushed)  (NP-TMP               (JJ last) (NNP June)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test18': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950117'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test18']['sents']['0']:
            print(return_dict['test18']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")~ " + str(return_dict['test18']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")~ noevent \n " )
            print("test18 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"GON\", u\"032\"),(u\"GON\", u\"BREGOV\", u\"033\")~ noeventexception \n " )
        print("test18 Failed")
def test18():
    text="Calenardhon urged Bree on Monday to help win a greater role for it in forthcoming peace talks."
    parse="(ROOT (S    (NP (NN Calenardhon)  )    (VP     (VBD urged)  (NP (NNP Bree)    )      (PP (IN on)  (NP (NNP Monday)      )    )  (S        (VP         (TO to)          (VP           (VB help)            (VP             (VB win)  (NP                (NP (DT a) (JJR greater) (NN role)              )                (PP (IN for)  (NP                   (PRP it)              ) )            )              (PP (IN in)  (NP                 (JJ forthcoming) (NN peace) (NNS talks)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test19': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test19']['sents']['0']:
            print(return_dict['test19']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"102\")~ " + str(return_dict['test19']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"102\")~ noevent \n " )
            print("test19 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"102\")~ noeventexception \n " )
        print("test19 Failed")
def test19():
    text="Arnor's foreign minister, in remarks published on Monday, urged Eriador to respond to Gondor's proposals on elections."
    parse="(ROOT (S    (NP      (NP        (NP (NNP Arnor) (POS 's)      )  (JJ foreign) (NN minister)    )  (, ,)      (PP (IN in)  (NP          (NP (NNS remarks)        )          (VP           (VBN published)            (PP (IN on)  (NP (NNP Monday)        ) ) )      )    )  (, ,)  )    (VP     (VBD urged)  (S        (NP (NNP Eriador)      )        (VP         (TO to)          (VP           (VB respond)            (PP             (TO to)  (NP                (NP (NNP Gondor) (POS 's)              )  (NNS proposals)            )          )            (PP (IN on)  (NP (NNS elections)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test20': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950119'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test20']['sents']['0']:
            print(return_dict['test20']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")~ " + str(return_dict['test20']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")~ noevent \n " )
            print("test20 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOVFRM\", u\"ERI\", u\"102\")~ noeventexception \n " )
        print("test20 Failed")
def test20():
    text="Eriador's death toll has risen in the dispute with  Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP      (NP (NNP Eriador) (POS 's)    )  (NN death) (NN toll)  )    (VP     (VBZ has)      (VP       (VBN risen)        (PP (IN in)  (NP            (NP (DT the) (NN dispute)          )            (PP (IN with)  (NP                (NP (NN Osgiliath)              )  (, ,)  (NP                  (NP (DT the) (NN state) (POS 's)                )  (JJS fiercest) (NN foe)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test21': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test21']['sents']['0']:
            print(return_dict['test21']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ " + str(return_dict['test21']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ noevent \n " )
            print("test21 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ noeventexception \n " )
        print("test21 Failed")
def test21():
    text="Eriador's death and injury toll has risen in the dispute with Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP      (NP        (NP (NNP Eriador) (POS 's)      )  (NN death)    ) (CC and) (NP (NN injury) (NN toll)    )  )    (VP     (VBZ has)     (VP       (VBN risen)        (PP (IN in)  (NP           (NP (DT the) (NN dispute)          )            (PP (IN with)  (NP               (NP (NN Osgiliath)              )  (, ,) (NP                  (NP (DT the) (NN state) (POS 's)                ) (JJS fiercest) (NN foe)            ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test22': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test22']['sents']['0']:
            print(return_dict['test22']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ " + str(return_dict['test22']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ noevent \n " )
            print("test22 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\")~ noeventexception \n " )
        print("test22 Failed")
def test22():
    text="Eriador's death and injury toll has risen in the dispute with Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP      (NP        (NP (NNP Eriador) (POS 's)      )  (NN death)    ) (CC and) (NP (NN injury) (NN toll)    )  )    (VP     (VBZ has)     (VP       (VBN risen)        (PP (IN in)  (NP           (NP (DT the) (NN dispute)          )            (PP (IN with)  (NP               (NP (NN Osgiliath)              )  (, ,) (NP                  (NP (DT the) (NN state) (POS 's)                ) (JJS fiercest) (NN foe)            ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test23': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\"),(u\"\", u\"OSG\", u\"223\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test23']['sents']['0']:
            print(return_dict['test23']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\"),(u\"\", u\"OSG\", u\"223\")~ " + str(return_dict['test23']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\"),(u\"\", u\"OSG\", u\"223\")~ noevent \n " )
            print("test23 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"223\"),(u\"\", u\"OSG\", u\"223\")~ noeventexception \n " )
        print("test23 Failed")
def test23():
    text="Eriador's death total has risen in the dispute with  Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP      (NP (NNP Eriador) (POS 's)    )  (NN death) (NN total)  )    (VP     (VBZ has)      (VP       (VBN risen)        (PP (IN in)  (NP            (NP (DT the) (NN dispute)          )            (PP (IN with)  (NP                (NP (NN Osgiliath)              )  (, ,)  (NP                  (NP (DT the) (NN state) (POS 's)                )  (JJS fiercest) (NN foe)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test24': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"224\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test24']['sents']['0']:
            print(return_dict['test24']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"224\")~ " + str(return_dict['test24']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"224\")~ noevent \n " )
            print("test24 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"224\")~ noeventexception \n " )
        print("test24 Failed")
def test24():
    text="Eriador's death and injury total has risen in the dispute with Osgiliath, the state's fiercest foe. "
    parse="(ROOT (S    (NP      (NP        (NP (NNP Eriador) (POS 's)      )  (NN death)    ) (CC and) (NP (NN injury) (NN total)    )  )    (VP     (VBZ has)     (VP       (VBN risen)        (PP (IN in)  (NP           (NP (DT the) (NN dispute)          )            (PP (IN with)  (NP               (NP (NN Osgiliath)              )  (, ,) (NP                  (NP (DT the) (NN state) (POS 's)                ) (JJS fiercest) (NN foe)            ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test25': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test25']['sents']['0']:
            print(return_dict['test25']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test25']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test25 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test25 Failed")
def test25():
    text="Gondor and Osgiliath have postponed their meeting after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT (S (NP (NNP Gondor) (CC and) (NNP Osgiliath)) (VP (VBP have) (VP (VBN postponed) (NP (PRP$ their) (NN meeting)) (SBAR (IN after) (S (NP (DT a) (NN hafling)) (VP (VBD was) (VP (VBN reported) (PP (IN on) (NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test26': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test26']['sents']['0']:
            print(return_dict['test26']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")~ " + str(return_dict['test26']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")~ noevent \n " )
            print("test26 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORMIL\", u\"191\"),(u\"OSG\", u\"MORMIL\", u\"191\")~ noeventexception \n " )
        print("test26 Failed")
def test26():
    text="Gondor and Osgiliath have delayed their meeting after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT (S 	(NP (NNP Gondor) (CC and) (NNP Osgiliath)) 	(VP (VBP have) (VP (VBN delayed) 	(NP (PRP$ their) (NN meeting)) (SBAR (IN after) 	(S (NP (DT a) (NN hafling)) (VP (VBD was) 	(VP (VBN reported) (PP (IN on) 	(NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test27': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test27']['sents']['0']:
            print(return_dict['test27']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ " + str(return_dict['test27']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noevent \n " )
            print("test27 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noeventexception \n " )
        print("test27 Failed")
def test27():
    text="Gondor and Osgiliath have downplayed their meeting after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT (S 	(NP (NNP Gondor) (CC and) (NNP Osgiliath)) 	(VP (VBP have) (VP (VBN downplayed) 	(NP (PRP$ their) (NN meeting)) (SBAR (IN after) 	(S (NP (DT a) (NN hafling)) (VP (VBD was) 	(VP (VBN reported) (PP (IN on) 	(NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test28': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test28']['sents']['0']:
            print(return_dict['test28']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ " + str(return_dict['test28']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noevent \n " )
            print("test28 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noeventexception \n " )
        print("test28 Failed")
def test28():
    text="It has been noted that Gondor and Osgiliath have delayed their meeting after a hafling was reported on the pass"
    parse="(ROOT (S 	(NP (PRP It)) 	(VP (VBZ has) (VP (VBN been) (VP (VBN noted) 	(SBAR (IN that) 	(S (NP (NNP Gondor) (CC and) (NNP Osgiliath)) 	(VP (VBP have) (VP (VBN delayed) 	(NP (PRP$ their) (NN meeting)) (SBAR (IN after) 	(S (NP (DT a) (NN hafling)) 	(VP (VBD was) (VP (VBN reported) (PP (IN on) 	(NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol)))))))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test29': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test29']['sents']['0']:
            print(return_dict['test29']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ " + str(return_dict['test29']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noevent \n " )
            print("test29 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"191\"),(u\"OSG\", u\"GON\", u\"191\")~ noeventexception \n " )
        print("test29 Failed")
def test29():
    text="Soldiers from Gondor have cordoned off the roads leading into Mordor along the pass of Cirith Ungol."
    parse="(ROOT (S (NP (NP (NNS Soldiers)) (PP (IN from) (NP (NNP Gondor)))) (VP (VBP have) (VP (VBN cordoned) (PRT (RP off)) (NP (DT the) (NNS roads)) (S (VP (VBG leading) (PP (IN into) (NP (NNP Mordor))) (PP (IN along) (NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test30': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1721\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test30']['sents']['0']:
            print(return_dict['test30']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1721\")~ " + str(return_dict['test30']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1721\")~ noevent \n " )
            print("test30 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1721\")~ noeventexception \n " )
        print("test30 Failed")
def test30():
    text="Soldiers from Gondor wire tapped all communication links leading into Mordor along the pass of Cirith Ungol."
    parse="(ROOT (S (NP (NP (NNS Soldiers)) (PP (IN from) (NP (NNP Gondor) (NN wire)))) (VP (VBD tapped) (NP (NP (DT all) (NN communication) (NNS links)) (VP (VBG leading) (PP (IN into) (NP (NNP Mordor))) (PP (IN along) (NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol)))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test31': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1711\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test31']['sents']['0']:
            print(return_dict['test31']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1711\")~ " + str(return_dict['test31']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1711\")~ noevent \n " )
            print("test31 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"1711\")~ noeventexception \n " )
        print("test31 Failed")
def test31():
    text="Soldiers from Gondor will not wire tap the communication links leading into Mordor along  the pass of Cirith Ungol."
    parse="(ROOT (S (NP (NP (NNS Soldiers)) (PP (IN from) (NP (NNP Gondor)))) (VP (MD will) (RB not) (VP (VB wire) (VP (VB tap) (NP (NP (DT the) (NN communication) (NNS links)) (VP (VBG leading) (PP (IN into) (NP (NNP Mordor))) (PP (IN along) (NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol)))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test32': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"081\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test32']['sents']['0']:
            print(return_dict['test32']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"081\")~ " + str(return_dict['test32']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"081\")~ noevent \n " )
            print("test32 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"081\")~ noeventexception \n " )
        print("test32 Failed")
def test32():
    text="Soldiers from Gondor have cordoned off for construction the roads leading into Mordor along the pass of Cirith Ungol."
    parse="(ROOT (S (NP (NP (NNS Soldiers)) (PP (IN from) (NP (NNP Gondor)))) (VP (VBP have) (VP (VBN cordoned) (PRT (RP off)) (PP (IN for) (NP (NN construction))) (NP (NP (DT the) (NNS roads)) (VP (VBG leading) (PP (IN into) (NP (NNP Mordor))))) (PP (IN along) (NP (NP (DT the) (NN pass)) (PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test33': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"071\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test33']['sents']['0']:
            print(return_dict['test33']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"071\")~ " + str(return_dict['test33']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"071\")~ noevent \n " )
            print("test33 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GONMIL\", u\"MOR\", u\"071\")~ noeventexception \n " )
        print("test33 Failed")
def test33():
    text="Arnor cleric is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP      (NNP Arnor) (JJ cleric)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  ))  (. .) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test34': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNREL\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test34']['sents']['0']:
            print(return_dict['test34']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNREL\", u\"GON\", u\"064\")~ " + str(return_dict['test34']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNREL\", u\"GON\", u\"064\")~ noevent \n " )
            print("test34 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNREL\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test34 Failed")
def test34():
    text="MSF Arnor is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP MSF) (NNP Arnor)  )    (VP     (VBZ is)      (VP       (IN about)  (S         (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              ) (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test35': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"NGOARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test35']['sents']['0']:
            print(return_dict['test35']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"NGOARN\", u\"GON\", u\"064\")~ " + str(return_dict['test35']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"NGOARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test35 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"NGOARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test35 Failed")
def test35():
    text="An MSF Arnor diplomat is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (DT An) (NNP MSF) (NNP Arnor)(NN diplomat)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  ))  (. .) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test36': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"NGOARNGOV\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test36']['sents']['0']:
            print(return_dict['test36']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"NGOARNGOV\", u\"GON\", u\"064\")~ " + str(return_dict['test36']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"NGOARNGOV\", u\"GON\", u\"064\")~ noevent \n " )
            print("test36 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"NGOARNGOV\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test36 Failed")
def test36():
    text="Arnor is about to restore full diplomatic ties with the Gondor main opposition group almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (DT the) (NNP Gondor) (JJ main) (NN opposition) (NN group)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              ) (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test37': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test37']['sents']['0']:
            print(return_dict['test37']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ " + str(return_dict['test37']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noevent \n " )
            print("test37 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noeventexception \n " )
        print("test37 Failed")
def test37():
    text="Arnor is about to restore full diplomatic ties with Gondor's government almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                  (NP (NNP Gondor) (POS 's)                ) (NN government)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              ) (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test38': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGOV\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test38']['sents']['0']:
            print(return_dict['test38']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGOV\", u\"064\")~ " + str(return_dict['test38']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGOV\", u\"064\")~ noevent \n " )
            print("test38 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGOV\", u\"064\")~ noeventexception \n " )
        print("test38 Failed")
def test38():
    text="Arnor is about to restore full diplomatic ties with Gondor's main opposition group almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                  (NP (NNP Gondor) (POS 's)                ) (JJ main) (NN opposition) (NN group)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              ) (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test39': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test39']['sents']['0']:
            print(return_dict['test39']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ " + str(return_dict['test39']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noevent \n " )
            print("test39 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noeventexception \n " )
        print("test39 Failed")
def test39():
    text="Human rights activists in Arnor are about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP     (NP       (JJ Human) (NNS rights) (NNS activists)    )     (PP (IN in) (NP (NNP Arnor)    ) )  )    (VP     (VBP are)      (VP       (IN about) (S         (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )             (PP (IN with) (NP (NNP Gondor)              )            )              (SBAR               (NP                 (RB almost) (CD five) (NNS years)              ) (IN after) (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test40': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNOPP\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test40']['sents']['0']:
            print(return_dict['test40']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNOPP\", u\"GON\", u\"064\")~ " + str(return_dict['test40']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNOPP\", u\"GON\", u\"064\")~ noevent \n " )
            print("test40 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNOPP\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test40 Failed")
def test40():
    text="Arnor is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday."
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test41': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test41']['sents']['0']:
            print(return_dict['test41']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")~ " + str(return_dict['test41']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")~ noevent \n " )
            print("test41 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"XYZGOV\", u\"XYZ\", u\"023\")~ noeventexception \n " )
        print("test41 Failed")
def test41():
    text="The Calenardhon government condemned an attack by Osgiliath soldiers in south Ithilen on Thursday "
    parse="(ROOT (S    (NP (DT The) (JJ Calenardhon) (NN government)  )    (VP      (VP       (VBD condemned)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test42': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test42']['sents']['0']:
            print(return_dict['test42']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ " + str(return_dict['test42']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noevent \n " )
            print("test42 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noeventexception \n " )
        print("test42 Failed")
def test42():
    text="Arnor security officials are about to restore full diplomatic ties with Gondor police. "
    parse="(ROOT (S    (NP (NNP Arnor) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor) (NNS police)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test43': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"GONCOP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test43']['sents']['0']:
            print(return_dict['test43']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"GONCOP\", u\"064\")~ " + str(return_dict['test43']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"GONCOP\", u\"064\")~ noevent \n " )
            print("test43 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"GONCOP\", u\"064\")~ noeventexception \n " )
        print("test43 Failed")
def test43():
    text="White House security officials are about to restore full diplomatic ties with Minas Tirith border police. "
    parse="(ROOT (S    (NP (NNP White) (NNP House) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Minas) (NNP Tirith) (NN border) (NN police)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test44': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GONCOP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test44']['sents']['0']:
            print(return_dict['test44']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GONCOP\", u\"064\")~ " + str(return_dict['test44']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GONCOP\", u\"064\")~ noevent \n " )
            print("test44 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GONCOP\", u\"064\")~ noeventexception \n " )
        print("test44 Failed")
def test44():
    text="The Calenardhon government condemned an attack by Osgiliath soldiers in south Ithilen on Thursday "
    parse="(ROOT (S    (NP (DT The) (JJ Calenardhon) (NN Congresses)  )    (VP      (VP       (VBD condemned)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test45': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test45']['sents']['0']:
            print(return_dict['test45']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ " + str(return_dict['test45']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ noevent \n " )
            print("test45 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ noeventexception \n " )
        print("test45 Failed")
def test45():
    text="The Calenardhon government condemned an attack by Osgiliath soldiers in south Ithilen on Thursday "
    parse="(ROOT (S    (NP (DT The) (JJ Calenardhon) (NN Congressmen)  )    (VP      (VP       (VBD condemned)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test46': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test46']['sents']['0']:
            print(return_dict['test46']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ " + str(return_dict['test46']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ noevent \n " )
            print("test46 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALLEG\", u\"OSGMIL\", u\"122\")~ noeventexception \n " )
        print("test46 Failed")
def test46():
    text="The Calenardhon Ministry of Silly Walks condemned an attack by Osgiliath soldiers in south Ithilen on Thursday "
    parse="(ROOT (S    (NP     (NP (DT The) (NNP Calenardhon) (NNP Ministry)    )     (PP (IN of) (NP         (JJ Silly) (NNS Walks)    ) )  )    (VP     (VBD condemned)  (NP (DT an) (NN attack)    )      (PP (IN by)  (NP          (NP (NNP Osgiliath) (NNS soldiers)        )          (PP (IN in)  (NP             (JJ south) (NNP Ithilen)      ) ) )    )      (PP (IN on)  (NP (NNP Thursday)  ) ) )) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test47': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test47']['sents']['0']:
            print(return_dict['test47']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ " + str(return_dict['test47']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noevent \n " )
            print("test47 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noeventexception \n " )
        print("test47 Failed")
def test47():
    text="The Calenardhon Minister of Silly Walks condemned an attack by Osgiliath soldiers in south Ithilen on Thursday "
    parse="(ROOT (S    (NP     (NP (DT The) (NNP Calenardhon) (NNP Minister)    )     (PP (IN of) (NP         (JJ Silly) (NNS Walks)    ) )  )    (VP     (VBD condemned)  (NP (DT an) (NN attack)    )      (PP (IN by)  (NP          (NP (NNP Osgiliath) (NNS soldiers)        )          (PP (IN in)  (NP             (JJ south) (NNP Ithilen)      ) ) )    )      (PP (IN on)  (NP (NNP Thursday)  ) ) )) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test48': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test48']['sents']['0']:
            print(return_dict['test48']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ " + str(return_dict['test48']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noevent \n " )
            print("test48 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\")~ noeventexception \n " )
        print("test48 Failed")
def test48():
    text="The human rights activists of Amnesty International are about to restore full diplomatic ties with Gondor. "
    parse="(ROOT (S    (NP     (NP (DT The) (JJ human) (NNS rights) (NNS activists)    )      (PP (IN of)  (NP (NNP Amnesty) (NNP International)    ) )  )    (VP     (VBP are)     (VP       (IN about)  (S          (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)          ) ) )        )      )      )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test49': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"NGMOPP\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test49']['sents']['0']:
            print(return_dict['test49']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"NGMOPP\", u\"GON\", u\"064\")~ " + str(return_dict['test49']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"NGMOPP\", u\"GON\", u\"064\")~ noevent \n " )
            print("test49 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"NGMOPP\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test49 Failed")
def test49():
    text="Washington security officials are about to restore full diplomatic ties with Gondor. "
    parse="(ROOT (S    (NP (NNP Washington) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test50': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test50']['sents']['0']:
            print(return_dict['test50']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ " + str(return_dict['test50']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ noevent \n " )
            print("test50 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test50 Failed")
def test50():
    text="White House security officials are about to restore full diplomatic ties with Gondor. "
    parse="(ROOT (S    (NP (NNP White) (NNP House) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test51': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test51']['sents']['0']:
            print(return_dict['test51']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ " + str(return_dict['test51']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ noevent \n " )
            print("test51 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test51 Failed")
def test51():
    text="The Quibbler government newspaper is about to restore full diplomatic ties with Gondor now. "
    parse="(ROOT (S    (NP (DT The) (NNP Quibbler) (NN government) (NN newspaper)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)              )            )  (ADVP               (RB now)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test52': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HGWGOVMED\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test52']['sents']['0']:
            print(return_dict['test52']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HGWGOVMED\", u\"GON\", u\"064\")~ " + str(return_dict['test52']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HGWGOVMED\", u\"GON\", u\"064\")~ noevent \n " )
            print("test52 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HGWGOVMED\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test52 Failed")
def test52():
    text="Arnor is about to restore full diplomatic ties with Gondor's main opposition groups almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)     (VP       (IN about)  (S         (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (NP (NNP Gondor) (POS 's)                ) (JJ main) (NN opposition) (NNS groups)              )            )              (SBAR               (NP                 (RB almost) (CD five) (NNS years)              ) (IN after)  (S                 (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test53': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test53']['sents']['0']:
            print(return_dict['test53']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ " + str(return_dict['test53']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noevent \n " )
            print("test53 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONMOP\", u\"064\")~ noeventexception \n " )
        print("test53 Failed")
def test53():
    text="Arnor is about to restore full diplomatic ties with Gondor's golden geese almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)     (VP       (IN about)  (S         (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (NP (NNP Gondor) (POS 's)                ) (JJ golden) (NNS geese)              )            )              (SBAR               (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                 (NP (NNS crowds)                )                 (VP                   (VBD trashed) (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test54': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGGS\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test54']['sents']['0']:
            print(return_dict['test54']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGGS\", u\"064\")~ " + str(return_dict['test54']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGGS\", u\"064\")~ noevent \n " )
            print("test54 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GONGGS\", u\"064\")~ noeventexception \n " )
        print("test54 Failed")
def test54():
    text="Arnor is about to restore full diplomatic ties with Gondor's polices almost five years after crowds trashed its embassy."
    parse="(ROOT (S    (NP (NNP Arnor)  )    (VP     (VBZ is)     (VP       (IN about)  (S         (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (NP (NNP Gondor) (POS 's)                ) (NNS polices)              )            )              (SBAR               (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                 (NP (NNS crowds)                )                 (VP                   (VBD trashed) (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test55': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test55']['sents']['0']:
            print(return_dict['test55']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test55']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test55 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test55 Failed")
def test55():
    text="West German world government activists are about to restore full diplomatic ties with human rights activists of Gonzo GMO. "
    parse="(ROOT (S    (NP     (JJ West) (JJ German) (NN world) (NN government) (NNS activists)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                  (NP                   (JJ human) (NNS rights) (NNS activists)                )                  (PP (IN of)  (NP (NNP Gonzo) (NNP GMO)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test56': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test56']['sents']['0']:
            print(return_dict['test56']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")~ " + str(return_dict['test56']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")~ noevent \n " )
            print("test56 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GMWGOVWGO\", u\"GONGMOOPP\", u\"064\")~ noeventexception \n " )
        print("test56 Failed")
def test56():
    text="White House security officials are about to restore full diplomatic ties with Gondor and Arnor. "
    parse="(ROOT (S    (NP (NNP White) (NNP House) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)  (CC and)  (NNP Arnor)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test57': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test57']['sents']['0']:
            print(return_dict['test57']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ " + str(return_dict['test57']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ noevent \n " )
            print("test57 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ noeventexception \n " )
        print("test57 Failed")
def test57():
    text="Arnor former security officials are about to restore full diplomatic ties with former Gondor prosecutors. "
    parse="(ROOT (S    (NP (NNP Arnor) (JJ former) (NN security) (NNS officials)  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (JJ former) (NNP Gondor) (NNS prosecutors)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test58': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNELI\", u\"GONELI\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test58']['sents']['0']:
            print(return_dict['test58']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNELI\", u\"GONELI\", u\"064\")~ " + str(return_dict['test58']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNELI\", u\"GONELI\", u\"064\")~ noevent \n " )
            print("test58 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNELI\", u\"GONELI\", u\"064\")~ noeventexception \n " )
        print("test58 Failed")
def test58():
    text="Former security officials in White House are about to restore full diplomatic ties with former Minas Tirith border police. "
    parse="(ROOT (S    (NP      (NP       (JJ Former) (NN security) (NNS officials)    )      (PP (IN in)  (NP (NNP White) (NNP House)    ) )  )    (VP     (VBP are)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (JJ former) (NNP Minas) (NNP Tirith) (NN border) (NN police)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test59': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOVELI\", u\"GONELI\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test59']['sents']['0']:
            print(return_dict['test59']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOVELI\", u\"GONELI\", u\"064\")~ " + str(return_dict['test59']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOVELI\", u\"GONELI\", u\"064\")~ noevent \n " )
            print("test59 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOVELI\", u\"GONELI\", u\"064\")~ noeventexception \n " )
        print("test59 Failed")
def test59():
    text="Old foes Gondor and Osgiliath have renewed diplomatic ties after a 12-year break in a step that holds advantages for both major powers. "
    parse="(ROOT (S   (NP     (NP       (JJ Old) (NNS foes)    ) (NP (NNP Gondor) (CC and) (NNP Osgiliath)    )  )   (VP     (VBP have)     (VP       (VBN renewed) (NP         (JJ diplomatic) (NNS ties)      )       (PP (IN after) (NP           (NP (DT a) (JJ 12-year) (NN break)          )           (PP (IN in) (NP               (NP (DT a) (NN step)              )               (SBAR                 (WHNP                   (WDT that)                ) (S                   (VP                     (VBZ holds) (NP                       (NP (NNS advantages)                      )                       (PP (IN for) (NP (DT both) (JJ major) (NNS powers)                    ) ) )                ) )                ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test60': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test60']['sents']['0']:
            print(return_dict['test60']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")~ " + str(return_dict['test60']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")~ noevent \n " )
            print("test60 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"064\"),(u\"OSG\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test60 Failed")
def test60():
    text="Mordor, Rohan, Fornost and Bree welcomed their resumption of formal diplomatic ties with Osgiliath after a 12-year rift. "
    parse="(ROOT (S   (NP (NNP Mordor) (, ,) (NNP Rohan) (, ,) (NNP Fornost) (CC and) (NNP Bree)  )   (VP     (VBD welcomed) (NP       (NP         (PRP$ their) (NN resumption)      )       (PP (IN of) (NP           (JJ formal) (JJ diplomatic) (NNS ties)      ) )    )     (PP (IN with) (NP (NN Osgiliath)      )    )     (PP (IN after) (NP (DT a) (JJ 12-year) (NN rift)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test61': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test61']['sents']['0']:
            print(return_dict['test61']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ " + str(return_dict['test61']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test61 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test61 Failed")
def test61():
    text="Fornost and Gondor welcome a resumption of formal diplomatic ties with  Osgiliath after a 12-year rift, the primary official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP (NNP Fornost)  (CC and)  (NNP Gondor)    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ primary) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test62': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test62']['sents']['0']:
            print(return_dict['test62']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test62']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test62 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test62 Failed")
def test62():
    text="Fornost welcomed a resumption of formal diplomatic ties between Gondor and Osgiliath after a 12-year rift, the primary official news agency WFNA said on Thursday. "
    parse="(ROOT (S   (S      (NP       (JJ Fornost)    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP              (NP               (JJ formal) (JJ diplomatic) (NNS ties)            )              (PP (IN between)  (NP (NNP Gondor)  (CC and)  (NNP Osgiliath)          ) ) )        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ primary) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test63': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test63']['sents']['0']:
            print(return_dict['test63']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test63']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test63 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test63 Failed")
def test63():
    text="Osgiliath welcomed the resumption of formal  diplomatic ties with Mordor, Rohan, Fornost and Bree after a 12-year rift. "
    parse="(ROOT (S    (NP (NN Osgiliath)  )    (VP     (VBD welcomed)  (NP       (NP (DT the) (NN resumption)      )        (PP (IN of)  (NP           (JJ formal) (JJ diplomatic) (NNS ties)      ) )    )      (PP (IN with)  (NP (NNP Mordor) (, ,) (NNP Rohan) (, ,) (NNP Fornost) (CC and) (NNP Bree)      )    )      (PP (IN after) (NP (DT a) (JJ 12-year) (NN rift)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test64': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test64']['sents']['0']:
            print(return_dict['test64']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")~ " + str(return_dict['test64']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")~ noevent \n " )
            print("test64 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"MOR\", u\"041\"),(u\"OSG\", u\"ROH\", u\"041\"),(u\"OSG\", u\"FOR\", u\"041\"),(u\"OSG\", u\"BRE\", u\"041\")~ noeventexception \n " )
        print("test64 Failed")
def test64():
    text="Fornost and Gondor welcomed a resumption of formal diplomatic tiesbetween Eriador and Osgiliath after a 12-year rift, the official newsagency WFNA said on Thursday . "
    parse="(ROOT (S    (S      (NP (NNP Fornost)  (CC and)  (NNP Gondor)    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP              (NP               (JJ formal) (JJ diplomatic) (NNS ties)            )              (PP (IN between)  (NP (NNP Eriador)  (CC and)  (NNP Osgiliath)          ) ) )        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test65': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test65']['sents']['0']:
            print(return_dict['test65']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ " + str(return_dict['test65']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test65 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"ERI\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"ERI\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test65 Failed")
def test65():
    text="Mordor, Rohan, Fornost and Bree welcomed a resumption of formal diplomatic ties between Gondor and Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday . "
    parse="(ROOT (S    (S      (NP (NNP Mordor) (, ,) (NNP Rohan) (, ,) (NNP Fornost)  (CC and)  (NNP Bree)    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP              (NP               (JJ formal) (JJ diplomatic) (NNS ties)            )              (PP (IN between)  (NP (NNP Gondor)  (CC and)  (NNP Osgiliath)          ) ) )        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test66': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test66']['sents']['0']:
            print(return_dict['test66']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ " + str(return_dict['test66']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test66 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"ROH\", u\"GON\", u\"041\"),(u\"ROH\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test66 Failed")
def test66():
    text="Mordor, the Shire, Fornost and Bree welcomed a resumption of formal diplomatic ties between Minas Tirith and Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Mordor)      )  (, ,)  (NP (DT the) (NNP Shire)      )  (, ,)  (NP (NNP Fornost)      )  (CC and)  (NP (NNP Bree)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP              (NP               (JJ formal) (JJ diplomatic) (NNS ties)            )              (PP (IN between)  (NP                 (NP (NNP Minas) (NNP Tirith)                )  (CC and)  (NNP Osgiliath)          ) ) )        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test67': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test67']['sents']['0']:
            print(return_dict['test67']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ " + str(return_dict['test67']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test67 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"GON\", u\"041\"),(u\"MOR\", u\"OSG\", u\"041\"),(u\"FRO\", u\"GON\", u\"041\"),(u\"BIL\", u\"GON\", u\"041\"),(u\"SAM\", u\"GON\", u\"041\"),(u\"FRO\", u\"OSG\", u\"041\"),(u\"BIL\", u\"OSG\", u\"041\"),(u\"SAM\", u\"OSG\", u\"041\"),(u\"FOR\", u\"GON\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"BRE\", u\"GON\", u\"041\"),(u\"BRE\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test67 Failed")
def test67():
    text="Lawmakers in Fornost and Gondor welcomed a resumption of formal diplomatic tieswith Eriador. "
    parse="(ROOT (S    (NP     (NP (NNS Lawmakers)    )     (PP (IN in)  (NP (NNP Fornost) (CC and) (NNP Gondor)    ) )  )    (VP     (VBD welcomed)  (NP       (NP (DT a) (NN resumption)      )       (PP (IN of) (NP           (JJ formal) (JJ diplomatic) (NNS ties)      ) )    )      (PP (IN with) (NP (NN Eriador)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test68': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test68']['sents']['0']:
            print(return_dict['test68']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")~ " + str(return_dict['test68']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")~ noevent \n " )
            print("test68 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\")~ noeventexception \n " )
        print("test68 Failed")
def test68():
    text="Lawmakers and officials in Fornost and Gondor welcomed a resumption of formal diplomatic tieswith Eriador. "
    parse="(ROOT (S    (NP     (NP (NNS Lawmakers) (CC and) (NNS official)    )     (PP (IN in)  (NP (NNP Fornost) (CC and) (NNP Gondor)    ) )  )    (VP     (VBD welcomed)  (NP       (NP (DT a) (NN resumption)      )       (PP (IN of) (NP           (JJ formal) (JJ diplomatic) (NNS ties)      ) )    )      (PP (IN with) (NP (NN Eriador)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test69': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test69']['sents']['0']:
            print(return_dict['test69']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")~ " + str(return_dict['test69']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")~ noevent \n " )
            print("test69 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FORLEG\", u\"ERI\", u\"041\"),(u\"GONLEG\", u\"ERI\", u\"041\"),(u\"FORGOV\", u\"ERI\", u\"041\"),(u\"GONGOV\", u\"ERI\", u\"041\")~ noeventexception \n " )
        print("test69 Failed")
def test69():
    text="The Shire is about to restore full diplomatic ties with Lorien almost five years after crowds burned down its embassy. "
    parse="(ROOT (S    (NP (DT The) (NNP Shire)  )    (VP     (VBZ is)      (VP       (IN about)  (S          (VP           (TO to)            (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP (NNP Lorien)              )            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBN burned)  (PRT                     (RP down)                  )  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test70': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test70']['sents']['0']:
            print(return_dict['test70']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")~ " + str(return_dict['test70']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")~ noevent \n " )
            print("test70 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FRO\", u\"ELR\", u\"064\"),(u\"FRO\", u\"GAL\", u\"064\"),(u\"BIL\", u\"ELR\", u\"064\"),(u\"BIL\", u\"GAL\", u\"064\"),(u\"SAM\", u\"ELR\", u\"064\"),(u\"SAM\", u\"GAL\", u\"064\")~ noeventexception \n " )
        print("test70 Failed")
def test70():
    text="Fornost and the evil awful Gondor welcomed a resumption of formal diplomatic  ties with Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Fornost)      )  (CC and)  (NP (DT the) (JJ evil) (JJ awful) (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test71': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test71']['sents']['0']:
            print(return_dict['test71']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ " + str(return_dict['test71']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test71 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test71 Failed")
def test71():
    text="Evil Mordor, the awful Fornost, and good Gondor welcomed a resumption of formal   diplomatic ties with Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Evil) (NNP Mordor)      )  (, ,)  (NP (DT the) (JJ awful) (NNP Fornost)      )  (, ,)  (CC and)  (NP         (JJ good) (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test72': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test72']['sents']['0']:
            print(return_dict['test72']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ " + str(return_dict['test72']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test72 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"OSG\", u\"041\"),(u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test72 Failed")
def test72():
    text="Arnor, Calenardhon and the evil awful Gondor welcomed a resumption of formal diplomatic  ties with Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Arnor)      )  (, ,)  (NP (NNP Calenardhon)      )  (CC and)  (NP (DT the) (JJ evil) (JJ awful) (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test73': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test73']['sents']['0']:
            print(return_dict['test73']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ " + str(return_dict['test73']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test73 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"OSG\", u\"041\"),(u\"CAL\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test73 Failed")
def test73():
    text="Calenardhon and the evil Arnor awful Gondor welcomed a resumption of formal diplomatic  ties with Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NN Calenardhon)      )  (CC and)  (NP (DT the) (JJ evil) (NN Arnor) (JJ awful) (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test74': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test74']['sents']['0']:
            print(return_dict['test74']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")~ " + str(return_dict['test74']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test74 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"OSG\", u\"041\"),(u\"ARN\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test74 Failed")
def test74():
    text="The lions and the evil awful Gondor welcomed a resumption of formal diplomatic  ties with Osgiliath after a 12-year rift, the primary official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (DT The) (NNS lions)      )  (CC and)  (NP (DT the) (JJ evil) (JJ awful) (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the)  (JJ primary) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test75': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test75']['sents']['0']:
            print(return_dict['test75']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test75']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test75 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test75 Failed")
def test75():
    text="Lions, tigers, and Gondor welcomed a resumption of formal diplomatic ties  with Osgiliath after a 12-year rift, the primary official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP        (NP (NNS Lions)      )  (, ,)  (NP (NNS tigers)      )  (, ,)  (CC and)  (NP (NNP Gondor)      )    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the)  (JJ primary) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test76': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test76']['sents']['0']:
            print(return_dict['test76']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test76']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test76 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"041\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test76 Failed")
def test76():
    text="Ithilen's awful and evil minister Calimehtar warned of the Prince of Dol Amroth. "
    parse="(ROOT (S    (NP      (NP (NNP Ithilen) (POS 's)    )  (ADJP       (JJ awful)  (CC and)  (JJ evil)    )  (NN minister) (NN Calimehtar)  )    (VP     (VBD warned)      (PP (IN of)  (NP          (NP (DT the) (NNP Prince)        )          (PP (IN of)  (NP (NNP Dol) (NNP Amroth)      ) ) )  ) ))  (. .) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test77': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test77']['sents']['0']:
            print(return_dict['test77']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ " + str(return_dict['test77']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ noevent \n " )
            print("test77 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ noeventexception \n " )
        print("test77 Failed")
def test77():
    text="Fornost and Gondor welcomed a resumption of formal diplomatic ties with  Osgiliath after a 12-year rift, the official news agency WFNA said on Thursday. "
    parse="(ROOT (S    (S      (NP (NNP Fornost)  (CC and)  (NNP Gondor)    )      (VP       (VBD welcomed)  (NP          (NP (DT a) (NN resumption)        )          (PP (IN of)  (NP             (JJ formal) (JJ diplomatic) (NNS ties)        ) )      )        (PP (IN with)  (NP (NN Osgiliath)        )      )        (PP (IN after)  (NP (DT a) (JJ 12-year) (NN rift)    ) ) )  )  (, ,)  (NP (DT the) (JJ official) (NN news) (NN agency) (NNP WFNA)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Thursday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test78': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test78']['sents']['0']:
            print(return_dict['test78']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ " + str(return_dict['test78']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noevent \n " )
            print("test78 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FOR\", u\"OSG\", u\"041\"),(u\"GON\", u\"OSG\", u\"041\")~ noeventexception \n " )
        print("test78 Failed")
def test78():
    text="Ithilen's awful and cool minister Calimehtar warned of the Prince of Dol Amroth. "
    parse="(ROOT  (S    (NP      (NP (NNP Ithilen) (POS 's))      (ADJP (JJ awful)        (CC and)        (JJ cool))      (NN minister) (NN Calimehtar))    (VP (VBD warned)      (PP (IN of)        (NP          (NP (DT the) (NNP Prince))          (PP (IN of)            (NP (NNP Dol) (NNP Amroth))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test79': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test79']['sents']['0']:
            print(return_dict['test79']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ " + str(return_dict['test79']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ noevent \n " )
            print("test79 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITHGOV\", u\"DOL\", u\"160\")~ noeventexception \n " )
        print("test79 Failed")
def test79():
    text="Ithilen's sheep and goats of Gondor warned of the Prince of Dol_Amroth. "
    parse="(ROOT  (S    (NP      (NP        (NP (NNP Ithilen) (POS 's))        (NN sheep))      (CC and)      (NP        (NP (NNS goats))        (PP (IN of)          (NP (NNP Gondor)))))    (VP (VBD warned)      (PP (IN of)        (NP          (NP (DT the) (NNP Prince))          (PP (IN of)            (NP (NNP Dol) (NNP Amroth))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test80': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test80']['sents']['0']:
            print(return_dict['test80']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")~ " + str(return_dict['test80']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")~ noevent \n " )
            print("test80 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"160\"),(u\"GON\", u\"DOL\", u\"160\")~ noeventexception \n " )
        print("test80 Failed")
def test80():
    text="Ithilen and the government of Gondor warned their populations about the Prince of Dol_Amroth. "
    parse="(ROOT (S 	(NP (NP (NNP Ithilen)) 	(CC and) 	(NP (NP (DT the) (NN government)) (PP (IN of) (NP (NNP Gondor))))) 	(VP (VBD warned) 	(NP (PRP$ their) (NNS populations)) 	(PP (IN about) 	(NP (NP (DT the) (NNP Prince)) (PP (IN of) (NP (NNP Dol) (NNP Amroth))	)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test81': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test81']['sents']['0']:
            print(return_dict['test81']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ " + str(return_dict['test81']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ noevent \n " )
            print("test81 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ noeventexception \n " )
        print("test81 Failed")
def test81():
    text="Ithilen and the government of Gondor warned their Ent populations about the Prince of Dol_Amroth. "
    parse="(ROOT (S 	(NP (NP (NNP Ithilen)) 	(CC and) 	(NP (NP (DT the) (NN government)) 	(PP (IN of) 	(NP (NNP Gondor))))) 	(VP (VBD warned) 	(NP (PRP$ their) (NN Ent) (NNS populations)) 	(PP (IN about) 	(NP (NP (DT the) (NNP Prince)) (PP (IN of) (NP (NNP Dol) (NNP Amroth)))	))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test82': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test82']['sents']['0']:
            print(return_dict['test82']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ " + str(return_dict['test82']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ noevent \n " )
            print("test82 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ITH\", u\"DOL\", u\"162\"),(u\"GONGOV\", u\"DOL\", u\"162\")~ noeventexception \n " )
        print("test82 Failed")
def test82():
    text="Neither Galadriel nor Gollum boycotted the parade supporting Gondor on Saturday. "
    parse="(ROOT (S 	(NP (NP (DT Neither)) 	(NP (NNP Galadriel) 	(CC nor) 	(NNP Gollum))) 	(VP (VBD boycotted) 	(NP (NP (DT the) (NN parade)) 	(VP (VBG supporting) 	(NP (NP (NNP Gondor)) 	(PP (IN on) 	(NP (NNP Saturday))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test83': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test83']['sents']['0']:
            print(return_dict['test83']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")~ " + str(return_dict['test83']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")~ noevent \n " )
            print("test83 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ELF\", u\"GON\", u\"081\"),(u\"HOB\", u\"GON\", u\"081\")~ noeventexception \n " )
        print("test83 Failed")
def test83():
    text="The Calenardhon government condemned an attack by Osgiliath soldiers in south Ithilen on Thursday and promised aid to the affected Ithilen villages. "
    parse="(ROOT  (S    (NP (DT The) (JJ Calenardhon) (NN government))    (VP      (VP (VBD condemned)        (NP (DT an) (NN attack))        (PP (IN by)          (NP            (NP (NNP Osgiliath) (NNS soldiers))            (PP (IN in)              (NP (JJ south) (NNP Ithilen)))))        (PP (IN on)          (NP (NNP Thursday))))      (CC and)      (VP (VBD promised)        (NP (NN aid))        (PP (TO to)          (NP (DT the) (VBN affected) (NN Ithilen) (NNS villages)))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test84': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test84']['sents']['0']:
            print(return_dict['test84']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ " + str(return_dict['test84']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ noevent \n " )
            print("test84 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"122\"),(u\"CALGOV\", u\"ITH\", u\"050\")~ noeventexception \n " )
        print("test84 Failed")
def test84():
    text="Danish media and government warned at the Gondor of the Prince of Dol Amroth. "
    parse="(ROOT  (S    (NP (JJ Danish) (NNS media)      (CC and)      (NNS government))    (VP (VBD warned)      (PP (IN at)        (NP          (NP (DT the) (NNP Gondor))          (PP (IN of)            (NP              (NP (DT the) (NNP Prince))              (PP (IN of)                (NP (NNP Dol) (NNP Amroth))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test85': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test85']['sents']['0']:
            print(return_dict['test85']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")~ " + str(return_dict['test85']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")~ noevent \n " )
            print("test85 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"DOL\", u\"162\"),(u\"DNKGOV\", u\"DOL\", u\"162\")~ noeventexception \n " )
        print("test85 Failed")
def test85():
    text=""
    parse="(ROOT (S   (NP     (NP       (DT The) (JJ Danish) (NNS media)    ) (CC and) (NP (NN government)    )  )   (VP     (VBD warned) (NP       (NP (DT the) (NN population)      )       (PP (IN of) (NP           (NP (NNP Gondor)          )           (PP (IN of) (NP               (NP (DT the) (NNP Prince)              )               (PP (IN of) (NP (NNP Dol) (NNP Amroth)            ) ) )        ) )      )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test86': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test86']['sents']['0']:
            print(return_dict['test86']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")~ " + str(return_dict['test86']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")~ noevent \n " )
            print("test86 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"DNKMED\", u\"GON\", u\"160\"),(u\"---GOV\", u\"GON\", u\"160\")~ noeventexception \n " )
        print("test86 Failed")
def test86():
    text="The Danish Islamist media and government warned at the Gondor of the Prince of Dol Amroth. "
    parse="(ROOT (S   (NP      (DT The) (JJ Danish) (JJ Islamist) (NNS media)    (CC and) (NN government)      )   (VP     (VBD warned) (NP       (NP (DT the) (NN population)      )       (PP (IN of) (NP           (NP (NNP Gondor)          )           (PP (IN of) (NP               (NP (DT the) (NNP Prince)              )               (PP (IN of) (NP (NNP Dol) (NNP Amroth)            ) ) )        ) )      )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test87': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990809'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test87']['sents']['0']:
            print(return_dict['test87']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")~ " + str(return_dict['test87']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")~ noevent \n " )
            print("test87 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"DNKMUSMED\", u\"GON\", u\"160\"),(u\"DNKMUSGOV\", u\"GON\", u\"160\")~ noeventexception \n " )
        print("test87 Failed")
def test87():
    text="Frodo said he has deep satisfaction toward Gondor and Arnor's Elrond, and Gondor's dramatic cooperation and its eye-catching development are of great significance to the region and even the entire world, he noted. "
    parse="(ROOT  (S    (S      (NP (NNP Frodo)    )      (VP       (VBD said)        (SBAR          (S            (S              (NP               (PRP he)            )              (VP               (VBZ has)  (NP                  (NP                    (NP                     (JJ deep) (NN satisfaction)                  )                    (PP (IN toward)  (NP (NNP Gondor)                  ) )                )  (CC and)  (NP                    (NP                      (NP (NNP Arnor) (POS 's)                    )  (NNP Elrond)                  )  (, ,)  (CC and)  (NP                      (NP (NNP Gondor) (POS 's)                    )  (JJ dramatic) (NN cooperation)              ) ) )            )          )  (CC and)  (S              (NP               (PRP$ its) (JJ eye-catching) (NN development)            )              (VP               (VBP are)                (PP (IN of)  (NP                   (JJ great) (NN significance)                )              )                (PP                 (TO to)  (NP                    (NP (DT the) (NN region)                  )  (CC and)  (NP                     (RB even) (DT the) (JJ entire) (NN world)              ) ) )          ) )          ) ) )  )  (, ,)  (NP     (PRP he)  )    (VP     (VBD noted)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test88': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20000423'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test88']['sents']['0']:
            print(return_dict['test88']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")~ " + str(return_dict['test88']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")~ noevent \n " )
            print("test88 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"023\"),(u\"HOB\", u\"ARN\", u\"023\")~ noeventexception \n " )
        print("test88 Failed")
def test88():
    text="The Calenardhon government issue condemned an attack by Osgiliath soldiers in south Ithilen on Thursday and promised raids to the affected Ithilen villages. "
    parse="(ROOT  (S    (NP (DT The) (JJ Calenardhon) (NN government) (NN issue)  )    (VP      (VP       (VBD condemned)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)      ) )    )  (CC and)      (VP       (VBD promised)  (NP (NNS raids)      )        (PP         (TO to)  (NP (DT the) (VBN affected) (NN Ithilen) (NNS villages)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test89': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test89']['sents']['0']:
            print(return_dict['test89']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")~ " + str(return_dict['test89']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")~ noevent \n " )
            print("test89 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"132\"),(u\"CALGOV\", u\"ITH\", u\"173\")~ noeventexception \n " )
        print("test89 Failed")
def test89():
    text="The Calenardhon government chided an attack by Osgiliath soldiers in south Ithilen on Thursday and ousted the affected Ithilen villages. "
    parse="(ROOT  (S    (NP (DT The) (JJ Calenardhon) (NN government)  )    (VP      (VP       (VBD chided)  (NP (DT an) (NN attack)      )        (PP (IN by)  (NP            (NP (NNP Osgiliath) (NNS soldiers)          )            (PP (IN in)  (NP               (JJ south) (NNP Ithilen)        ) ) )      )        (PP (IN on)  (NP (NNP Thursday)      ) )    )  (CC and)      (VP       (VBN ousted)  (NP (DT the) (VBN affected) (NN Ithilen) (NNS villages)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test90': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test90']['sents']['0']:
            print(return_dict['test90']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")~ " + str(return_dict['test90']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")~ noevent \n " )
            print("test90 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CALGOV\", u\"OSGMIL\", u\"131\"),(u\"CALGOV\", u\"ITH\", u\"201\")~ noeventexception \n " )
        print("test90 Failed")
def test90():
    text="And Eriador has called for a boycott against Osgiliath, the state's fiercest foe. "
    parse="(ROOT  (S (CC And)    (NP (NNP Eriador))    (VP (VBZ has)      (VP (VBN called)        (PP (IN for)          (NP            (NP (DT a) (NN boycott))            (PP (IN against)              (NP                (NP (NNP Osgiliath))                (, ,)                (NP                  (NP (DT the) (NN state) (POS 's))                  (JJS fiercest) (NN foe))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test91': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"096\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test91']['sents']['0']:
            print(return_dict['test91']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"096\")~ " + str(return_dict['test91']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"096\")~ noevent \n " )
            print("test91 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"OSG\", u\"096\")~ noeventexception \n " )
        print("test91 Failed")
def test91():
    text="Resumption of ties between Arnor and Gondor may spur reconciliation between Calenardhon and Gondor, and Gondor and Dagolath, the Osgiliathnewspaper al-Raya said on Friday. "
    parse="(ROOT  (S    (S      (NP        (NP (NN Resumption)      )        (PP (IN of)  (NP            (NP (NNS ties)          )            (PP (IN between)  (NP (NNP Arnor)  (CC and)  (NNP Gondor)        ) ) )      )    )      (VP       (MD may)        (VP         (VB spur)  (NP            (NP (NN reconciliation)          )            (PP (IN between)  (NP (NNP Calenardhon)  (CC and)  (NNP Gondor)        ) ) )    ) )  )  (, ,)  (CC and)  (S      (NP        (NP (NNP Gondor)  (CC and)  (NNP Dagolath)      )  (, ,)  (NP          (NP (DT the) (NNP Osgiliath) (NN newspaper)        )  (NP (NNP al-Raya)      ) )    )      (VP       (VBD said)        (PP (IN on)  (NP (NNP Friday)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test92': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20000423'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test92']['sents']['0']:
            print(return_dict['test92']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")~ " + str(return_dict['test92']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")~ noevent \n " )
            print("test92 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"081\"),(u\"ARN\", u\"GON\", u\"081\"),(u\"GON\", u\"CAL\", u\"081\")~ noeventexception \n " )
        print("test92 Failed")
def test92():
    text="Clerics and lawmakers believe Dagolath and Osgiliath can cope with a decrease in vital water from the mighty Entwash river when a major dam is filled next month. "
    parse="(ROOT  (S    (NP (NNS Clerics)      (CC and)      (NNS lawmakers))    (VP (VBP believe)      (SBAR        (S          (NP (NN Dagolath)            (CC and)            (NN Osgiliath))          (VP (MD can)            (VP (VB cope)              (PP (IN with)                (NP                  (NP (DT a) (NN decrease))                  (PP (IN in)                    (NP (JJ vital) (NN water)))))              (PP (IN from)                (NP                  (NP (DT the) (JJ mighty) (JJ Entwash) (NN river))                  (SBAR                    (WHADVP (WRB when))                    (S                      (NP (DT a) (JJ major) (NN dam))                      (VP (VBZ is)                        (VP (VBN filled)                          (NP-TMP (JJ next) (NN month)))))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test93': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950107'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test93']['sents']['0']:
            print(return_dict['test93']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")~ " + str(return_dict['test93']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")~ noevent \n " )
            print("test93 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"---REL\", u\"DAG\", u\"023\"),(u\"---REL\", u\"OSG\", u\"023\"),(u\"---LEG\", u\"DAG\", u\"023\"),(u\"---LEG\", u\"OSG\", u\"023\")~ noeventexception \n " )
        print("test93 Failed")
def test93():
    text="The Nasgul said on Friday that an arms embargo against Mordor would not work and warned that a blockade of the Bay of Belfalas would harm all  countries of the region. "
    parse="(ROOT  (S    (NP (DT The) (NNP Nasgul))    (VP (VBD said)      (PP (IN on)        (NP (NNP Friday)))      (SBAR (IN that)        (S          (NP            (NP (DT an) (NNS arms) (NN embargo))            (PP (IN against)              (NP (NNP Mordor))))          (VP            (VP (MD would) (RB not)              (VP (VB work)))            (CC and)            (VP (VBD warned)              (SBAR (IN that)                (S                  (NP                    (NP (DT a) (NN blockade))                    (PP (IN of)                      (NP                        (NP (DT the) (NNP Bay))                        (PP (IN of)                          (NP (NNP Belfalas))))))                  (VP (MD would)                    (VP (VB harm)                      (NP                        (NP (DT all) (NNS countries))                        (PP (IN of)                          (NP (DT the) (NN region)))))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test94': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950105'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"###\", u\"MOR\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test94']['sents']['0']:
            print(return_dict['test94']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"###\", u\"MOR\", u\"023\")~ " + str(return_dict['test94']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"###\", u\"MOR\", u\"023\")~ noevent \n " )
            print("test94 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"###\", u\"MOR\", u\"023\")~ noeventexception \n " )
        print("test94 Failed")
def test94():
    text="The information ministry of Gondor and the Nasgul said on Friday that an arms embargo against the Mordor police would not work and warned that a blockade of the Bay of Belfalas would harm all countries of the region. "
    parse="(ROOT  (S    (NP      (NP (DT The) (NN information) (NN ministry))      (PP (IN of)        (NP (NNP Gondor)          (CC and)          (NP (DT the)(NNP Nasgul)))))    (VP (VBD said)      (PP (IN on)        (NP (NNP Friday)))      (SBAR (IN that)        (S          (NP            (NP (DT an) (NNS arms) (NN embargo))            (PP (IN against)              (NP (DT the)  (NNP Mordor)  (NN police))))          (VP            (VP (MD would) (RB not)              (VP (VB work)))            (CC and)            (VP (VBD warned)              (SBAR (IN that)                (S                  (NP                    (NP (DT a) (NN blockade))                    (PP (IN of)                      (NP                        (NP (DT the) (NNP Bay))                        (PP (IN of)                          (NP (NNP Belfalas))))))                  (VP (MD would)                    (VP (VB harm)                      (NP                        (NP (DT all) (NNS countries))                        (PP (IN of)                          (NP (DT the) (NN region)))))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test95': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950105'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test95']['sents']['0']:
            print(return_dict['test95']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")~ " + str(return_dict['test95']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")~ noevent \n " )
            print("test95 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"MORCOP\", u\"023\"),(u\"###\", u\"MORCOP\", u\"023\")~ noeventexception \n " )
        print("test95 Failed")
def test95():
    text="White House security officials are about to restore full diplomatic ties with Gondor and Arnor. "
    parse="(ROOT  (S    (NP (NNP White) (NNP House) (NN security) (NNS officials))    (VP (VBP are)      (VP (IN about)        (S          (VP (TO to)            (VP (VB restore)              (NP (JJ full) (JJ diplomatic) (NNS ties))              (PP (IN with)                (NP (NNP Gondor)                  (CC and)                  (NNP Arnor))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test96': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test96']['sents']['0']:
            print(return_dict['test96']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ " + str(return_dict['test96']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ noevent \n " )
            print("test96 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAGOV\", u\"GON\", u\"064\"),(u\"USAGOV\", u\"ARN\", u\"064\")~ noeventexception \n " )
        print("test96 Failed")
def test96():
    text="The ambassadors of Arnor, Osgiliath and Gondor presented their credentials to Ithilen's president on Wednesday in a further show of support to his government by their countries. "
    parse="(ROOT  (S    (NP      (NP (DT The) (NNS ambassadors))      (PP (IN of)        (NP (NNP Arnor) (, ,) (NNP Osgiliath)          (CC and)          (NNP Gondor))))    (VP (VBD presented)      (NP (PRP$ their) (NNS credentials))      (PP (TO to)        (NP          (NP            (NP (NNP Ithilen) (POS 's))            (NN president))          (PP (IN on)            (NP              (NP (NNP Wednesday))              (PP (IN in)                (NP                  (NP (DT a) (JJ further) (NN show))                  (PP (IN of)                    (NP (NN support)))))))))      (PP (TO to)        (NP (PRP$ his) (NN government)))      (PP (IN by)        (NP (PRP$ their) (NNS countries))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test97': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950108'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test97']['sents']['0']:
            print(return_dict['test97']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ " + str(return_dict['test97']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ noevent \n " )
            print("test97 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARNGOV\", u\"ITHGOV\", u\"032\"),(u\"OSGGOV\", u\"ITHGOV\", u\"032\"),(u\"GONGOV\", u\"ITHGOV\", u\"032\")~ noeventexception \n " )
        print("test97 Failed")
def test97():
    text="The Philippines and the European Union (EU) agree that territorial disputes in the South China Sea should be resolved through international arbitration."
    parse="(ROOT (S (NP (NP (NP (DT The) (NNPS Philippines)) (CC and) (NP (DT the) (NNP European) (NNP Union))) (PRN (-LRB- -LRB-) (NP (NNP EU)) (-RRB- -RRB-))) (VP (VBP agree) (SBAR (IN that) (S (NP (NP (JJ territorial) (NNS disputes)) (PP (IN in) (NP (DT the) (NNP South) (NNP China) (NNP Sea)))) (VP (MD should) (VP (VB be) (VP (VBN resolved) (PP (IN through) (NP (JJ international) (NN arbitration))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test98': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test98']['sents']['0']:
            print(return_dict['test98']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")~ " + str(return_dict['test98']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")~ noevent \n " )
            print("test98 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"IGOEEU\", u\"030\"),(u\"IGOEEU\", u\"PHL\", u\"030\")~ noeventexception \n " )
        print("test98 Failed")
def test98():
    text="The Philippines and France agree that territorial disputes should be resolved through international arbitration."
    parse="(ROOT (S (NP     (NP (DT The) (NNPS Philippines))     (CC and)     (NP (NNP France))) (VP (VBP agree) (SBAR (IN that) (S     (NP (JJ territorial) (NNS disputes))     (VP (MD should) (VP (VB be) (VP (VBN resolved) (PP (IN through)     (NP (JJ international) (NN arbitration))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test99': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test99']['sents']['0']:
            print(return_dict['test99']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ " + str(return_dict['test99']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ noevent \n " )
            print("test99 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ noeventexception \n " )
        print("test99 Failed")
def test99():
    text="The Philippines and the Central African Republic agree that territorial disputes should be resolved through international arbitration."
    parse="(ROOT (S (NP (NP (DT The) (NNPS Philippines)) (CC and) (NP (DT the)(NNP Central) (NNP African) (NNP Republic))) (VP (VBP agree) (SBAR (IN that) (S (NP (JJ territorial) (NNS disputes)) (VP (MD should) (VP (VB be) (VP (VBN resolved) (PP (IN through) (NP (JJ international) (NN arbitration))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test100': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test100']['sents']['0']:
            print(return_dict['test100']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")~ " + str(return_dict['test100']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")~ noevent \n " )
            print("test100 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"CAF\", u\"030\"),(u\"CAF\", u\"PHL\", u\"030\")~ noeventexception \n " )
        print("test100 Failed")
def test100():
    text="The Philippines and France agree that territorial disputes in the South China Sea should be resolved through international arbitration."
    parse="(ROOT (S (NP (NP (DT The) (NNPS Philippines)) (CC and) (NP (NNP France))) (VP (VBP agree) (SBAR (IN that) (S (NP (NP (JJ territorial) (NNS disputes)) (PP (IN in) (NP (DT the) (NNP South) (NNP China) (NNP Sea)))) (VP (MD should) (VP (VB be) (VP (VBN resolved) (PP (IN through) (NP (JJ international) (NN arbitration))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test101': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test101']['sents']['0']:
            print(return_dict['test101']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ " + str(return_dict['test101']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ noevent \n " )
            print("test101 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"FRA\", u\"030\"),(u\"FRA\", u\"PHL\", u\"030\")~ noeventexception \n " )
        print("test101 Failed")
def test101():
    text="Eriador agrees with the Philippines and France that territorial disputes should be resolved through international arbitration."
    parse="(ROOT (S (NP (NNP Eriador)) (VP (VBZ agrees) (PP (IN with) (NP (NP (DT the) (NNPS Philippines)) (CC and) (NP (NNP France)))) (SBAR (IN that) (S (NP (JJ territorial) (NNS disputes)) (VP (MD should) (VP (VB be) (VP (VBN resolved) (PP (IN through) (NP (JJ international) (NN arbitration))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test102': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test102']['sents']['0']:
            print(return_dict['test102']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")~ " + str(return_dict['test102']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")~ noevent \n " )
            print("test102 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"FRA\", u\"031\"),(u\"ERI\", u\"PHL\", u\"031\")~ noeventexception \n " )
        print("test102 Failed")
def test102():
    text="Sam Gamgee will be renewing his gardener's license in Michel Delving."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (MD will)     (VP       (VB be)       (VP         (VBG renewing)  (NP           (NP             (NP               (PRP$ his) (NN gardener) (POS 's)            ) (NN license)          )            (PP (IN in) (NP (NNP Michel) (NNP Delving)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test103': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test103']['sents']['0']:
            print(return_dict['test103']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ " + str(return_dict['test103']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ noevent \n " )
            print("test103 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ noeventexception \n " )
        print("test103 Failed")
def test103():
    text="Sam Gamgee will be renewing his gardener's license in Michel Delving."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (MD will)     (VP       (VB be)       (VP         (VBG renewing)  (NP           (NP             (NP               (PRP$ his) (NN gardener) (POS 's)            ) (NN license)          )            (PP (IN in) (NP (NNP Michel) (NNP Delving)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test104': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20080119'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test104']['sents']['0']:
            print(return_dict['test104']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ " + str(return_dict['test104']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ noevent \n " )
            print("test104 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBCIV\", u\"SHRGOV\", u\"031\")~ noeventexception \n " )
        print("test104 Failed")
def test104():
    text="Hamfast Gamgee has rescheduled his annual mushroom hunting trip in the White Downs."
    parse="(ROOT (S    (NP (NNP Hamfast) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN rescheduled)  (NP         (PRP$ his) (JJ annual)  (NN mushroom) (NN hunting) (NN trip)      )        (PP (IN in) (NP (DT the) (NNP White) (NNP Downs)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test105': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test105']['sents']['0']:
            print(return_dict['test105']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ " + str(return_dict['test105']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ noevent \n " )
            print("test105 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ noeventexception \n " )
        print("test105 Failed")
def test105():
    text="Hamfast Gamgee has criticized the recent closure of guest houses in Bree."
    parse="(ROOT (S    (NP (NNP Hamfast) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN criticized)  (NP         (NP (DT the) (JJ recent) (NN closure)        )          (PP (IN of) (NP (NN guest) (NNS houses)        ) )      )        (PP (IN in) (NP (NNP Bree)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test106': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"121\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test106']['sents']['0']:
            print(return_dict['test106']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"121\")~ " + str(return_dict['test106']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"121\")~ noevent \n " )
            print("test106 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"121\")~ noeventexception \n " )
        print("test106 Failed")
def test106():
    text="Hamfast Gamgee has criticized the recent closure of guest houses in Michel Delving."
    parse="(ROOT (S   (NP      (NNP Hamfast) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN criticized)  (NP         (NP (DT the) (JJ recent) (NN closure)        )          (PP (IN of) (NP (NN guest) (NNS houses)        ) )      )        (PP (IN in) (NP (NNP Michel) (NNP Delving)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test107': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121225'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test107']['sents']['0']:
            print(return_dict['test107']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")~ " + str(return_dict['test107']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")~ noevent \n " )
            print("test107 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"121\")~ noeventexception \n " )
        print("test107 Failed")
def test107():
    text="Hamfast Gamgee has arranged for the reopening of guest houses in Bree."
    parse="(ROOT (S    (NP (NNP Hamfast) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN arranged)        (PP (IN for)  (NP           (NP (DT the) (VBG reopening)          )            (PP (IN of) (NP               (NP (NN guest) (NNS houses)              )               (PP (IN in) (NP (NNP Bree)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test108': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"031\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test108']['sents']['0']:
            print(return_dict['test108']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"031\")~ " + str(return_dict['test108']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"031\")~ noevent \n " )
            print("test108 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"BRE\", u\"031\")~ noeventexception \n " )
        print("test108 Failed")
def test108():
    text="Hamfast Gamgee has rescheduled his annual mushroom hunting trip in the White Downs."
    parse="(ROOT (S    (NP (NNP Hamfast) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN rescheduled)  (NP         (PRP$ his) (JJ annual) (NN mushroom) (NN hunting) (NN trip)      )        (PP (IN in) (NP (DT the) (NNP White) (NNP Downs)    ) ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test109': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20140104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test109']['sents']['0']:
            print(return_dict['test109']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ " + str(return_dict['test109']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ noevent \n " )
            print("test109 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"SHR\", u\"082\")~ noeventexception \n " )
        print("test109 Failed")
def test109():
    text="Sam Gamgee has marched very close to the border with Mordor."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN marched)  (ADVP         (RB very) (RB close)      )        (PP         (TO to)  (NP           (NP (DT the) (NN border)          )            (PP (IN with)  (NP (NNP Mordor)          ) )        )      ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test110': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100106'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MOR\", u\"181\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test110']['sents']['0']:
            print(return_dict['test110']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MOR\", u\"181\")~ " + str(return_dict['test110']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MOR\", u\"181\")~ noevent \n " )
            print("test110 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MOR\", u\"181\")~ noeventexception \n " )
        print("test110 Failed")
def test110():
    text="Sam Gamgee met a bunch of Morgul Orcs."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (VBD met)  (NP       (NP (DT a) (NN bunch)      )        (PP (IN of)  (NP (NNP Morgul) (NNP Orcs)        )      ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test111': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100109'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test111']['sents']['0']:
            print(return_dict['test111']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")~ " + str(return_dict['test111']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")~ noevent \n " )
            print("test111 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"031\"),(u\"MRGORC\", u\"ORCHOB\", u\"032\")~ noeventexception \n " )
        print("test111 Failed")
def test111():
    text="Sam Gamgee has overcome the animosity of the Morgul Orcs, which is no small feat."
    parse="(ROOT (S   (NP (NNP Sam) (NNP Gamgee)  )   (VP     (VBZ has)     (VP       (VBN overcome) (NP         (NP (DT the) (NN animosity)        )         (PP (IN of) (NP             (NP (DT the) (NNP Morgul) (NNP Orcs)            ) (, ,)             (SBAR               (WHNP                 (WDT which)              ) (S                 (VP                   (VBZ is) (NP (DT no) (JJ small) (NN feat)              ) ) )          ) )          ) ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test112': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100110'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"036\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test112']['sents']['0']:
            print(return_dict['test112']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"036\")~ " + str(return_dict['test112']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"036\")~ noevent \n " )
            print("test112 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"036\")~ noeventexception \n " )
        print("test112 Failed")
def test112():
    text="Sam Gamgee has begun to question whether he really has much of a future with theMorgul Orcs."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN begun)  (S         (VP           (TO to)           (VP             (VB question)              (SBAR               (IN whether) (S                 (NP                   (PRP he)                ) (ADVP                   (RB really)                )                  (VP                   (VBZ has) (NP                     (NP                       (RB much)                    )                     (PP (IN of)  (NP                         (NP (DT a) (NN future)                        )                          (PP (IN with) (NP (DT the) (NNP Morgul) (NNP Orcs)                      ) ) )                  ) )                  ) ) )        ) )      )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test113': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"212\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test113']['sents']['0']:
            print(return_dict['test113']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"212\")~ " + str(return_dict['test113']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"212\")~ noevent \n " )
            print("test113 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ORCHOB\", u\"MRGORC\", u\"212\")~ noeventexception \n " )
        print("test113 Failed")
def test113():
    text="Sam Gamgee halted his march towards further adventures in the vicinity of Cirith Ungol."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (VBD halted) (NP       (PRP$ his) (NN march)    )      (PP (IN towards)  (NP         (JJ further) (NNS adventures)      )    )      (PP (IN in)  (NP         (NP (DT the) (NN vicinity)        )          (PP (IN of)  (NP (NNP Cirith) (NNP Ungol)        ) )      )      )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test114': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20100113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MORMIL\", u\"192\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test114']['sents']['0']:
            print(return_dict['test114']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MORMIL\", u\"192\")~ " + str(return_dict['test114']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MORMIL\", u\"192\")~ noevent \n " )
            print("test114 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBMIL\", u\"MORMIL\", u\"192\")~ noeventexception \n " )
        print("test114 Failed")
def test114():
    text="Sam Gamgee has reasserted friendship with the gardening license raj of Michel Delving."
    parse="(ROOT (S    (NP (NNP Sam) (NNP Gamgee)  )    (VP     (VBZ has)     (VP       (VBN reasserted)  (NP (NN friendship)      )       (PP (IN with)  (NP           (NP (DT the) (NN gardening) (NN license) (NN raj)          )            (PP (IN of)  (NP (NNP Michel) (NNP Delving)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test115': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20121231'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test115']['sents']['0']:
            print(return_dict['test115']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")~ " + str(return_dict['test115']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")~ noevent \n " )
            print("test115 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"SHRGOV\", u\"042\")~ noeventexception \n " )
        print("test115 Failed")
def test115():
    text="Smeagol is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Smeagol)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test116': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19951101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test116']['sents']['0']:
            print(return_dict['test116']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ " + str(return_dict['test116']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ noevent \n " )
            print("test116 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test116 Failed")
def test116():
    text="Arnor  is about to restore full diplomatic ties with Slinker almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Slinker)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test117': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19951101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test117']['sents']['0']:
            print(return_dict['test117']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ " + str(return_dict['test117']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ noevent \n " )
            print("test117 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ noeventexception \n " )
        print("test117 Failed")
def test117():
    text="Stinker is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Stinker)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test118': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test118']['sents']['0']:
            print(return_dict['test118']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test118']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test118 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test118 Failed")
def test118():
    text="Arnor  is about to restore full diplomatic ties with Slinker almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Slinker)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test119': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19980101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test119']['sents']['0']:
            print(return_dict['test119']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ " + str(return_dict['test119']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ noevent \n " )
            print("test119 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBGOV\", u\"064\")~ noeventexception \n " )
        print("test119 Failed")
def test119():
    text="Smeagol is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Smeagol)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test120': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test120']['sents']['0']:
            print(return_dict['test120']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ " + str(return_dict['test120']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ noevent \n " )
            print("test120 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOBGOV\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test120 Failed")
def test120():
    text="Arnor is about to restore full diplomatic ties with Slinker almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Slinker)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test121': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20010101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBREB\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test121']['sents']['0']:
            print(return_dict['test121']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBREB\", u\"064\")~ " + str(return_dict['test121']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBREB\", u\"064\")~ noevent \n " )
            print("test121 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"HOBREB\", u\"064\")~ noeventexception \n " )
        print("test121 Failed")
def test121():
    text="Zimbabwe is about to restore full diplomatic ties with Slinker almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Zimbabwe)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Slinker)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test122': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19781223'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"RHO\", u\"HOB\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test122']['sents']['0']:
            print(return_dict['test122']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"RHO\", u\"HOB\", u\"064\")~ " + str(return_dict['test122']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"RHO\", u\"HOB\", u\"064\")~ noevent \n " )
            print("test122 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"RHO\", u\"HOB\", u\"064\")~ noeventexception \n " )
        print("test122 Failed")
def test122():
    text="Arnor is about to restore full diplomatic ties with Zimbabwe almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Zimbabwe)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test123': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'20010101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"ZBW\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test123']['sents']['0']:
            print(return_dict['test123']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"ZBW\", u\"064\")~ " + str(return_dict['test123']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"ZBW\", u\"064\")~ noevent \n " )
            print("test123 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"ZBW\", u\"064\")~ noeventexception \n " )
        print("test123 Failed")
def test123():
    text="An investigation determined that the amount of radioactivity that seeped from a valve was less than half a microcurie, or less than what one would find in a 50-pound bag of lawn fertilizer, a senior illiterate university professor said. "
    parse="(ROOT (S   (S     (NP (DT An) (NN investigation)    )     (VP       (VBD determined)       (SBAR         (IN that) (S           (NP             (NP (DT the) (NN amount)            )             (PP (IN of) (NP                 (NP (NN radioactivity)                )                 (SBAR                   (WHNP                     (WDT that)                  ) (S                     (VP                       (VBD seeped)                       (PP (IN from) (NP (DT a) (NN valve)                    ) ) )                ) )              )            )          )           (VP             (VBD was) (NP               (NP                 (NP                   (QP                     (JJR less) (IN than) (PDT half)                  )                ) (NP (DT a) (NN microcurie)                )              ) (, ,) (NP                 (NP                   (QP                     (CC or) (JJR less)                  )                )                 (PP (IN than)                   (SBAR                     (WHNP                       (WP what)                    ) (S                       (NP                         (PRP one)                      )                       (VP                         (MD would)                         (VP                           (VB find)                           (PP (IN in) (NP                               (NP (DT a) (JJ 50-pound) (NN bag)                              )                               (PP (IN of) (NP (NN lawn) (NN fertilizer)                            ) ) )                        ) )                        ) ) )              ) )        ) ) )    ) )  ) (, ,) (NP (DT a) (JJ senior) (JJ illiterate) (NN university) (NN professor)  )   (VP     (VBD said)  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test124': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test124']['sents']['0']:
            print(return_dict['test124']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test124']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test124 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test124 Failed")
def test124():
    text="A Pakistani woman believed linked to Al-Qaeda who shot at US military officers while in detention in Afghanistan was extradited Monday to the United States where she faces trial for her actions, a US attorney said. "
    parse="(ROOT (S   (S     (NP       (NP (DT A) (JJ Pakistani) (NN woman)      )       (VP         (VBN believed) (S           (ADJP             (VBN linked)             (PP               (TO to) (NP                 (NP (NN Al-Qaeda)                )                 (SBAR                   (WHNP                     (WP who)                  ) (S                     (VP                       (VBD shot)                       (PP (IN at) (NP (NNP US) (JJ military) (NNS officers)                        )                      )                       (PP (IN while)                         (PP (IN in) (NP (NN detention)                      ) ) )                  ) )                  ) ) )          )        )         (PP (IN in) (NP (NNP Afghanistan)      ) ) )    )     (VP       (AUXD was)       (VP         (VBN extradited) (NP (NNP Monday)        )         (PP           (TO to) (NP (DT the) (NNP United) (NNPS States)          )        )         (SBAR           (WHADVP             (WRB where)          ) (S             (NP               (PRP she)            )             (VP               (VBZ faces) (NP                 (NP (NN trial)                )                 (PP (IN for) (NP                     (PRP$ her) (NNS actions)              ) ) )          ) )          ) ) )  ) (, ,) (NP (DT a) (NNP US) (NN attorney)  )   (VP     (VBD said)  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test125': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test125']['sents']['0']:
            print(return_dict['test125']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")~ " + str(return_dict['test125']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")~ noevent \n " )
            print("test125 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\"),(u\"PAK\", u\"AFG\", u\"174\")~ noeventexception \n " )
        print("test125 Failed")
def test125():
    text="A Pakistani woman believed linked to Al-Qaeda who shot at US military officers while in detention in Afghanistan was extradited Monday to the United States where she faces trial for her actions, a US attorney said. "
    parse="(ROOT (S   (NP (DT A) (JJ Pakistani) (NN woman)  )   (VP     (VBD believed)     (VP       (VBN linked)       (PP         (TO to) (NP           (NP (NNP Al-Qaeda)          )           (SBAR             (WHNP               (WP who)            ) (S               (VP                 (VBD shot)                 (PP (IN at) (NP (NNP US) (JJ military) (NNS officers)                  )                )                 (SBAR                   (IN while) (S                     (SBAR                       (IN in) (S                         (NP                           (NP (NN detention)                          )                           (PP (IN in) (NP (NNP Afghanistan)                          ) )                        )                         (VP                           (VBD was)                           (VP                             (VBN extradited) (NP-TMP                               (NNP Monday)                            )                             (PP                               (TO to) (NP (DT the) (NNP United) (NNPS States)                              )                            )                             (SBAR                               (WHADVP                                 (WRB where)                              ) (S                                 (NP                                   (PRP she)                                )                                 (VP                                   (VBZ faces) (NP                                     (NP (NN trial)                                    )                                     (PP (IN for) (NP                                         (PRP$ her) (NNS actions)                                  ) ) )                              ) )                              ) ) )                      )                    ) (, ,) (NP (DT a) (NNP US) (NN attorney)                    )                     (VP                       (VBD said)                ) ) )            ) )            ) ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test126': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test126']['sents']['0']:
            print(return_dict['test126']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")~ " + str(return_dict['test126']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")~ noevent \n " )
            print("test126 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PAK\", u\"IMGMOSALQ\", u\"111\")~ noeventexception \n " )
        print("test126 Failed")
def test126():
    text="On improvement of primary health and Gondor's health centres, he saidgovernment proposed to take up the issue with the World Bank in a phased mannerwith priority being assigned to states with low health indices. "
    parse="(ROOT  (S    (PP (IN On)  (NP        (NP          (NP (NN improvement)        )          (PP (IN of)  (NP             (JJ primary) (NN health)        ) )      )  (CC and)  (NP          (NP (NNP Gondor) (POS 's)        )  (NN health) (NNS centres)    ) )  )  (, ,)  (NP     (PRP he)  )    (VP     (VBD said)      (SBAR        (S          (NP (NN government)        )          (VP           (VBD proposed)  (S              (VP               (TO to)                (VP                 (VB take)  (PRT                   (RP up)                )  (NP (DT the) (NN issue)                )                  (PP (IN with)  (NP                      (NP (DT the) (NNP World) (NNP Bank)                    )                      (PP (IN in)  (NP                          (NP (DT a) (JJ phased) (NN manner)                        )                          (PP (IN with)  (NP                              (NP (NN priority)                            )                              (VP                               (VBG being)                                (VP                                 (VBN assigned)                                  (PP                                   (TO to)  (NP                                      (NP (NNS states)                                    )                                      (PP (IN with)  (NP                                         (JJ low) (NN health) (NNS indices)                                  ) ) )                              ) )                              ) ) )                    ) )              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test127': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19990101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test127']['sents']['0']:
            print(return_dict['test127']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test127']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test127 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test127 Failed")
def test127():
    text="South Korea's women have grabbed gold in the team's section since then, while their male counterparts are on the verge of completing a hat-trick, having triumphed in 2000 and 2004. "
    parse="(ROOT (S (NP (NP (NNP South) (NNP Korea) (POS 's)) (NNS women)) (VP (AUXP have) (VP (VBN grabbed) (NP (NN gold)) (PP (IN in) (NP (NP (DT the) (NN team) (POS 's)) (NN section))) (PP (IN since) (NP (RB then))) (, ,) (SBAR (IN while) (S (NP (PRP$ their) (NN male) (NNS counterparts)) (VP (VBP are) (PP (IN on) (NP (NP (DT the) (NN verge)) (PP (IN of) (S (VP (VBG completing) (NP (DT a) (NN hat-trick))))))) (, ,) (S (VP (AUXG having) (VP (VBD triumphed) (PP (IN in) (NP (CD 2000) (CC and) (CD 2004))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test128': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test128']['sents']['0']:
            print(return_dict['test128']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test128']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test128 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test128 Failed")
def test128():
    text="An explosion sent a wall of flame through the school dormitory just as the girls, aged from eight to 16, were getting up for morning prayers, one of the girls said. "
    parse="(ROOT (S (S (NP (DT An) (NN explosion)) (VP (VBD sent) (NP (NP (DT a) (NN wall)) (PP (IN of) (NP (NN flame)))) (PP (IN through) (NP (DT the) (NN school) (NN dormitory))) (SBAR (RB just) (IN as) (S (NP (NP (DT the) (NNS girls)) (, ,) (VP (VBN aged) (PP (IN from) (NP (QP (CD eight) (TO to) (CD 16))))) (, ,)) (VP (AUXD were) (VP (VBG getting) (PRT (RP up)) (PP (IN for) (NP (NN morning) (NNS prayers))))))))) (, ,) (NP (NP (CD one)) (PP (IN of) (NP (DT the) (NNS girls)))) (VP (VBD said)) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test129': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test129']['sents']['0']:
            print(return_dict['test129']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test129']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test129 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test129 Failed")
def test129():
    text="Grahame Russell, who lost his son Philip when one of the four suicide bombers detonated a device on a bus in central London, said:`` A lot of families' ideas were included in the design; it's very different. "
    parse="( (S (NP (NP (NNP Grahame) (NNP Russell)) (, ,) (SBAR (WHNP (WP who)) (S (VP (VBD lost) (NP (PRP$ his) (NN son)) (NP (NNP Philip)) (SBAR (WHADVP (WRB when)) (S (NP (NP (CD one)) (PP (IN of) (NP (DT the) (CD four) (NN suicide) (NNS bombers)))) (VP (VBD detonated) (NP (DT a) (NN device)) (PP (IN on) (NP (DT a) (NN bus))) (PP (IN in) (NP (JJ central) (NNP London))))))))) (, ,)) (VP (VBD said) (: :) (`` ``) (S (S (NP (NP (DT A) (NN lot)) (PP (IN of) (NP (NP (NNS families) (POS ')) (NNS ideas)))) (VP (AUXD were) (VP (VBN included) (PP (IN in) (NP (DT the) (NN design)))))) (: ;) (S (NP (PRP it)) (VP (VBZ 's) (ADJP (RB very) (JJ different)))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test130': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test130']['sents']['0']:
            print(return_dict['test130']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test130']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test130 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test130 Failed")
def test130():
    text="The park is to be jointly managed by the government and local communities, with assistance from Birdlife International and the Australian state of New South Wales. "
    parse="( (S (NP (DT The) (NN park)) (VP (VBZ is) (S (VP (TO to) (VP (AUXB be) (VP (ADVP (RB jointly)) (VBN managed) (PP (IN by) (NP (NP (DT the) (NN government)) (CC and) (NP (JJ local) (NNS communities)))) (, ,) (PP (IN with) (NP (NP (NN assistance)) (PP (IN from) (NP (NP (NNP Birdlife) (NNP International)) (CC and) (NP (NP (DT the) (JJ Australian) (NN state)) (PP (IN of) (NP (NNP New) (NNP South) (NNP Wales))))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test131': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test131']['sents']['0']:
            print(return_dict['test131']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test131']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test131 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test131 Failed")
def test131():
    text="China's coal mines are among the most dangerous in the world, with safety standards often ignored in the quest for profits and the drive to meet demand for coal-- the source of about 70 percent of China's energy. "
    parse="( (S (NP (NP (NNP China) (POS 's)) (NN coal) (NNS mines)) (VP (VBP are) (PP (IN among) (NP (NP (DT the) (ADJP (RBS most) (JJ dangerous))) (PP (IN in) (NP (DT the) (NN world))))) (, ,) (PP (IN with) (NP (NP (NN safety) (NNS standards)) (VP (ADVP (RB often)) (VBN ignored) (PP (IN in) (NP (NP (NP (DT the) (NN quest)) (PP (IN for) (NP (NNS profits)))) (CC and) (NP (NP (DT the) (NN drive) (S (VP (TO to) (VP (VB meet) (NP (NP (NN demand)) (PP (IN for) (NP (NN coal)))))))) (: --) (NP (NP (DT the) (NN source)) (PP (IN of) (NP (NP (QP (IN about) (CD 70)) (NN percent)) (PP (IN of) (NP (NP (NNP China) (POS 's)) (NN energy))))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test132': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test132']['sents']['0']:
            print(return_dict['test132']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test132']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test132 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test132 Failed")
def test132():
    text="They issued a joint statement calling for a continued expansion of the International Monetary Fund's reserves and a shake-up of countries' representation and voting rights on that and other Bretton Woods institutions. "
    parse="( (S (NP (PRP They)) (VP (VBD issued) (NP (NP (DT a) (JJ joint) (NN statement)) (VP (VBG calling) (PP (IN for) (NP (NP (NP (DT a) (VBN continued) (NN expansion)) (PP (IN of) (NP (NP (DT the) (NNP International) (NNP Monetary) (NNP Fund) (POS 's)) (NNS reserves)))) (CC and) (NP (NP (NP (DT a) (NN shake-up)) (PP (IN of) (NP (NP (NNS countries) (POS ')) (NN representation)))) (CC and) (NP (NP (VBG voting) (NNS rights)) (PP (IN on) (NP (NP (DT that)) (CC and) (NP (JJ other) (NNP Bretton) (NNP Woods) (NNS institutions))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test133': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test133']['sents']['0']:
            print(return_dict['test133']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test133']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test133 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test133 Failed")
def test133():
    text="President Ilham Aliyev and President of the European Commission Jose Manuel Barroso held a one-on-one meeting on June 14."
    parse="(ROOT (S (NP (NP (NNP President) (NNP Ilham) (NNP Aliyev) (CC and) (NNP President)) (PP (IN of) (NP (DT the) (JJ European) (NNP Commission) (NNP Jose) (NNP Manuel) (NNP Barroso)))) (VP (VBD held) (NP (DT a) (JJ one-on-one) (NN meeting)) (PP (IN on) (NP (NNP June) (CD 14)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test134': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test134']['sents']['0']:
            print(return_dict['test134']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test134']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test134 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test134 Failed")
def test134():
    text="Abubakar also directed Zuokumor to ensure that there is adequate police presence in all the polling units and collation centres in the state."
    parse="(ROOT (S (NP (NNP Abubakar)) (ADVP (RB also)) (VP (VBD directed) (S (NP (NNP Zuokumor)) (VP (TO to) (VP (VB ensure) (SBAR (IN that) (S (NP (EX there)) (VP (VBZ is) (NP (NP (JJ adequate) (NN police) (NN presence)) (PP (IN in) (NP (NP (NP (PDT all) (DT the) (NN polling) (NNS units)) (CC and) (NP (NN collation) (NNS centres))) (PP (IN in) (NP (DT the) (NN state))))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test135': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'ence date = '}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test135']['sents']['0']:
            print(return_dict['test135']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test135']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test135 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test135 Failed")
def test135():
    text="Gryffindor's head Minerva McGonagall left for the Ministry of Magic on Wednesday for meetings of the joint OWL standards committee with Albus Dumbledore, Luna Lovegood's news agency reported. "
    parse="(ROOT (S    (S      (NP       (NP (NNP Gryffindor) (POS 's)      ) (NN head) (NN Minerva) (NN McGonagall)    )      (VP       (VBD left)        (PP (IN for)  (NP           (NP (DT the) (NNP Ministry)          )           (PP (IN of) (NP (NNP Magic)        ) ) )      )        (PP (IN on)  (NP           (NP (NNP Wednesday)          )            (PP (IN for) (NP               (NP (NNS meetings)              )                (PP (IN of)  (NP (DT the) (JJ joint) (NN OWL) (NNS standards) (NN committee)            ) ) )        ) )      )        (PP (IN with) (NP (NNP Albus) (NNP Dumbledore)    ) ) )  )  (, ,)  (NP     (NP (NNP Luna) (NNP Lovegood) (POS 's)    ) (NN news) (NN agency)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test136': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"\", u\"032\"),(u\"\", u\"\", u\"033\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test136']['sents']['0']:
            print(return_dict['test136']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"\", u\"032\"),(u\"\", u\"\", u\"033\")~ " + str(return_dict['test136']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"\", u\"032\"),(u\"\", u\"\", u\"033\")~ noevent \n " )
            print("test136 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"\", u\"032\"),(u\"\", u\"\", u\"033\")~ noeventexception \n " )
        print("test136 Failed")
def test136():
    text="Gryffindor's head Minerva McGonagall left for Minas Tirith on Wednesday for meetings of the joint OWL standards committee with Albus Dumbledore, Luna Lovegood's news agency reported. "
    parse="(ROOT (S    (S      (NP       (NP (NNP Gryffindor) (POS 's)      ) (NN head) (NN Minerva) (NN McGonagall)    )      (VP       (VBD left)        (PP (IN for)  (NP (NNP Minas) (NNP Tirith)        )      )        (PP (IN on)  (NP           (NP (NNP Wednesday)          )            (PP (IN for) (NP               (NP (NNS meetings)              )                (PP (IN of)  (NP (DT the) (JJ joint) (NN OWL) (NNS standards) (NN committee)            ) ) )        ) )      )        (PP (IN with) (NP (NNP Albus) (NNP Dumbledore)    ) ) )  )  (, ,)  (NP     (NP (NNP Luna) (NNP Lovegood) (POS 's)    ) (NN news) (NN agency)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test137': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"GON\", u\"032\"),(u\"GON\", u\"\", u\"033\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test137']['sents']['0']:
            print(return_dict['test137']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"GON\", u\"032\"),(u\"GON\", u\"\", u\"033\")~ " + str(return_dict['test137']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"GON\", u\"032\"),(u\"GON\", u\"\", u\"033\")~ noevent \n " )
            print("test137 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"\", u\"GON\", u\"032\"),(u\"GON\", u\"\", u\"033\")~ noeventexception \n " )
        print("test137 Failed")
def test137():
    text="Gryffindor's head Minerva McGonagall left for the Ministry of Magic on Wednesday for meetings of the joint OWL standards committee with Albus Dumbledore, Luna Lovegood's news agency reported. "
    parse="(ROOT (S    (S      (NP       (NP (NNP Gryffindor) (POS 's)      ) (NN head) (NN Minerva) (NN McGonagall)    )      (VP       (VBD left)        (PP (IN for)  (NP           (NP (DT the) (NNP Ministry)          )           (PP (IN of) (NP (NNP Magic)        ) ) )      )        (PP (IN on)  (NP           (NP (NNP Wednesday)          )            (PP (IN for) (NP               (NP (NNS meetings)              )                (PP (IN of)  (NP (DT the) (JJ joint) (NN OWL) (NNS standards) (NN committee)            ) ) )        ) )      )        (PP (IN with) (NP (NNP Albus) (NNP Dumbledore)    ) ) )  )  (, ,)  (NP     (NP (NNP Luna) (NNP Lovegood) (POS 's)    ) (NN news) (NN agency)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test138': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test138']['sents']['0']:
            print(return_dict['test138']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test138']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test138 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test138 Failed")
def test138():
    text="Gryffindor's head Minerva McGonagall left for the Ministry of Magic on Wednesday for meetings of the joint OWL standards committee with Albus Dumbledore, Luna Lovegood's news agency reported. "
    parse="(ROOT (S    (S      (NP       (NP (NNP Gryffindor) (POS 's)      ) (NN head) (NN Minerva) (NN McGonagall)    )      (VP       (VBD left)        (PP (IN for)  (NP           (NP (DT the) (NNP Ministry)          )           (PP (IN of) (NP (NNP Magic)        ) ) )      )        (PP (IN on)  (NP           (NP (NNP Wednesday)          )            (PP (IN for) (NP               (NP (NNS meetings)              )                (PP (IN of)  (NP (DT the) (JJ joint) (NN OWL) (NNS standards) (NN committee)            ) ) )        ) )      )        (PP (IN with) (NP (NNP Albus) (NNP Dumbledore)    ) ) )  )  (, ,)  (NP     (NP (NNP Luna) (NNP Lovegood) (POS 's)    ) (NN news) (NN agency)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test139': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test139']['sents']['0']:
            print(return_dict['test139']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test139']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test139 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test139 Failed")
def test139():
    text="The Kuwait government is about to restore full diplomatic ties with Libya almost crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (DT The) (JJ Kuwait) (NN government)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP                    (NP (NNP Libya) (RB almost) (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test140': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"KUWGOV\", u\"LBY\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test140']['sents']['0']:
            print(return_dict['test140']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"KUWGOV\", u\"LBY\", u\"064\")~ " + str(return_dict['test140']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"KUWGOV\", u\"LBY\", u\"064\")~ noevent \n " )
            print("test140 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"KUWGOV\", u\"LBY\", u\"064\")~ noeventexception \n " )
        print("test140 Failed")
def test140():
    text="The KU basketball team is about to restore full diplomatic ties with Libya almost crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (DT The) (NNP KU) (NN basketball) (NN team)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP                    (NP (NNP Libya) (RB almost) (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test141': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test141']['sents']['0']:
            print(return_dict['test141']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ " + str(return_dict['test141']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ noevent \n " )
            print("test141 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ noeventexception \n " )
        print("test141 Failed")
def test141():
    text="The K.U. basketball team is about to restore full diplomatic ties with Libya almost crowds trashed its embassy. "
    parse="(ROOT (S    (NP (DT The) (NNP K.U.) (NN basketball) (NN team)  )    (VP     (VBZ is)     (VP       (IN about)  (S         (VP           (TO to)           (VP             (VB restore)  (NP               (JJ full) (JJ diplomatic) (NNS ties)            )              (PP (IN with)  (NP                 (NP (NNP Libya) (RB almost) (NNS crowds)                )                  (VP                   (VBD trashed) (NP                     (PRP$ its) (NN embassy)                  )                )            ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test142': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test142']['sents']['0']:
            print(return_dict['test142']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ " + str(return_dict['test142']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ noevent \n " )
            print("test142 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USAEDU\", u\"LBY\", u\"064\")~ noeventexception \n " )
        print("test142 Failed")
def test142():
    text="The Australian government is about to restore full diplomatic ties with Libya almost crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (DT The) (JJ Australian) (NN government)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP                    (NP (NNP Libya) (RB almost) (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test143': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"AUSGOV\", u\"LBY\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test143']['sents']['0']:
            print(return_dict['test143']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"AUSGOV\", u\"LBY\", u\"064\")~ " + str(return_dict['test143']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"AUSGOV\", u\"LBY\", u\"064\")~ noevent \n " )
            print("test143 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"AUSGOV\", u\"LBY\", u\"064\")~ noeventexception \n " )
        print("test143 Failed")
def test143():
    text="The AU is about to restore full diplomatic ties with Libya almost crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (DT The) (NN AU)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP                    (NP (NNP Libya) (RB almost) (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test144': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"IGOAFR\", u\"LBY\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test144']['sents']['0']:
            print(return_dict['test144']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"IGOAFR\", u\"LBY\", u\"064\")~ " + str(return_dict['test144']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"IGOAFR\", u\"LBY\", u\"064\")~ noevent \n " )
            print("test144 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"IGOAFR\", u\"LBY\", u\"064\")~ noeventexception \n " )
        print("test144 Failed")
def test144():
    text="The Hermit Kingdom fired two artillery shells at New Zealand on Thursday."
    parse="(ROOT (S (NP (DT The) (NNP Hermit) (NNP Kingdom)) (VP (VBD fired) (NP (CD two) (NN artillery) (NNS shells)) (PP (IN at) (NP (JJ New) (NNP Zealand))) (PP (IN on) (NP (NNP Thursday)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test145': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"NZE\", u\"194\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test145']['sents']['0']:
            print(return_dict['test145']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"NZE\", u\"194\")~ " + str(return_dict['test145']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"NZE\", u\"194\")~ noevent \n " )
            print("test145 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"NZE\", u\"194\")~ noeventexception \n " )
        print("test145 Failed")
def test145():
    text="The Hermit Kingdom fired two artillery shells at Zealand on Thursday."
    parse="(ROOT (S (NP (DT The) (NNP Hermit) (NNP Kingdom)) (VP (VBD fired) (NP (CD two) (NN artillery) (NNS shells)) (PP (IN at) (NP (NNP Zealand))) (PP (IN on) (NP (NNP Thursday)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test146': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"DNK\", u\"194\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test146']['sents']['0']:
            print(return_dict['test146']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"DNK\", u\"194\")~ " + str(return_dict['test146']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"DNK\", u\"194\")~ noevent \n " )
            print("test146 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"DNK\", u\"194\")~ noeventexception \n " )
        print("test146 Failed")
def test146():
    text="The United States on Thursday fired two artillery shells at Seoul."
    parse="(ROOT (S (NP (NP (DT The) (NNP United) (NNPS States)) (PP (IN on) (NP (NNP Thursday)))) (VP (VBD fired) (NP (CD two) (NN artillery) (NNS shells)) (PP (IN at) (NP (NNP Seoul)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test147': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"USA\", u\"KOR\", u\"194\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test147']['sents']['0']:
            print(return_dict['test147']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"USA\", u\"KOR\", u\"194\")~ " + str(return_dict['test147']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"USA\", u\"KOR\", u\"194\")~ noevent \n " )
            print("test147 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"USA\", u\"KOR\", u\"194\")~ noeventexception \n " )
        print("test147 Failed")
def test147():
    text="Pyongyang on Thursday fired two artillery shells at Seoul."
    parse="(ROOT (S (NP (NP (NNP Pyongyang)) (PP (IN on) (NP (NNP Thursday)))) (VP (VBD fired) (NP (CD two) (NN artillery) (NNS shells)) (PP (IN at) (NP (NNP Seoul)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test148': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test148']['sents']['0']:
            print(return_dict['test148']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ " + str(return_dict['test148']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ noevent \n " )
            print("test148 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ noeventexception \n " )
        print("test148 Failed")
def test148():
    text="The Hermit Kingdom fired two artillery shells at Seoul on Thursday."
    parse="(ROOT (S (NP (DT The) (NNP Hermit) (NNP Kingdom)) (VP (VBD fired) (NP (CD two) (NN artillery) (NNS shells)) (PP (IN at) (NP (NNP Seoul))) (PP (IN on) (NP (NNP Thursday)))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test149': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test149']['sents']['0']:
            print(return_dict['test149']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ " + str(return_dict['test149']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ noevent \n " )
            print("test149 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PRK\", u\"KOR\", u\"194\")~ noeventexception \n " )
        print("test149 Failed")
def test149():
    text="Ethiopia has broken relations with Libya almost five years after crowds trashed its embassy. "
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (VBZ has)     (VP       (VBN broken)  (NP         (NP (NNS relations)        )          (PP (IN with) (NP (NNP Libya)        ) )      )        (SBAR         (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S           (NP (NNS crowds)          )            (VP             (VBD trashed) (NP               (PRP$ its) (NN embassy)            )          )      ) ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test150': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test150']['sents']['0']:
            print(return_dict['test150']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ " + str(return_dict['test150']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noevent \n " )
            print("test150 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noeventexception \n " )
        print("test150 Failed")
def test150():
    text="Ethiopia has broken down relations with Libya almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Ethiopia)    )     (VP       (VBZ has)       (VP         (VBN broken)  (PRT           (RP down)        ) (NP           (NP (NNS relations)          )            (PP (IN with) (NP (NNP Libya)          ) )        )          (SBAR           (NP             (RB almost) (CD five) (NNS years)          ) (IN after) (S             (NP (NNS crowds)            )              (VP               (VBD trashed) (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,) (NP (DT a) (JJ senior) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test151': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test151']['sents']['0']:
            print(return_dict['test151']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ " + str(return_dict['test151']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noevent \n " )
            print("test151 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noeventexception \n " )
        print("test151 Failed")
def test151():
    text="Ethiopia will break relations with Libya almost five years after crowds trashed its embassy."
    parse="(ROOT (S   (NP (NNP Ethiopia)  )   (VP     (MD will)     (VP       (VB break) (NP (NNS relations)      )       (PP (IN with) (NP (NNP Libya)        )      )       (SBAR         (NP           (RB almost) (CD five) (NNS years)        ) (IN after) (S           (NP (NNS crowds)          )           (VP             (VBD trashed) (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test152': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test152']['sents']['0']:
            print(return_dict['test152']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ " + str(return_dict['test152']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noevent \n " )
            print("test152 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noeventexception \n " )
        print("test152 Failed")
def test152():
    text="Ethiopia broken down a treaty with Libya's  almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBN broken)  (PRT         (RP down)      )  (NP (DT a) (NN treaty)      )        (PP (IN with)  (NP (NNP Libya) (POS 's)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test153': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test153']['sents']['0']:
            print(return_dict['test153']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ " + str(return_dict['test153']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ noevent \n " )
            print("test153 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ noeventexception \n " )
        print("test153 Failed")
def test153():
    text="Ethiopia broken down a treaty with Libya's  almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBN broken)  (PRT         (RP down)      )  (NP (DT a) (NN treaty)      )        (PP (IN with)  (NP (NNP Libya) (POS 's)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test154': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test154']['sents']['0']:
            print(return_dict['test154']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ " + str(return_dict['test154']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ noevent \n " )
            print("test154 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"161\")~ noeventexception \n " )
        print("test154 Failed")
def test154():
    text="Ethiopia is acting strangely with Libya almost five years after  crowds trashed its embassy. "
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (VBZ is)     (VP       (VBG acting) (ADVP         (RB strangely)      )        (PP (IN with) (NP (NNP Libya)        )      )        (SBAR         (NP           (RB almost) (CD five) (NNS years)        ) (IN after)  (S           (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test155': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test155']['sents']['0']:
            print(return_dict['test155']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ " + str(return_dict['test155']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ noevent \n " )
            print("test155 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ noeventexception \n " )
        print("test155 Failed")
def test155():
    text="Ethiopia has acted oddly with respect to Libya almost five years after  crowds trashed its embassy"
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (VBZ has)     (VP       (VBN acted)  (ADVP         (RB oddly)      )       (PP (IN with)  (NP           (NP (NN respect)          )            (PP             (TO to)  (NP (NNP Libya)        ) ) )      )        (SBAR         (NP           (RB almost) (CD five) (NNS years)        ) (IN after)  (S           (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test156': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test156']['sents']['0']:
            print(return_dict['test156']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ " + str(return_dict['test156']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ noevent \n " )
            print("test156 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"100\")~ noeventexception \n " )
        print("test156 Failed")
def test156():
    text="Ethiopia indicated it would act now with Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBD indicated)        (SBAR          (S            (NP             (PRP it)          )            (VP             (MD would)              (VP               (VB act)  (ADVP                 (RB now)              )                (PP (IN with)  (NP (NNP Libya)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test157': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test157']['sents']['0']:
            print(return_dict['test157']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ " + str(return_dict['test157']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ noevent \n " )
            print("test157 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ noeventexception \n " )
        print("test157 Failed")
def test157():
    text="Ethiopia indicated it would acting now  with Libya's  almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBD indicated)        (SBAR          (S            (NP             (PRP it)          )            (VP             (MD would)  (S                (VP                 (VBG acting)  (ADVP                   (RB now)                )                  (PP (IN with)  (NP (NNP Libya) (POS 's)                  )                )                  (SBAR                    (NP                     (RB almost) (CD five) (NNS years)                  )  (IN after)  (S                      (NP (NNS crowds)                    )                      (VP                       (VBD trashed)  (NP                         (PRP$ its) (NN embassy)                  ) ) )              ) )              ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test158': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test158']['sents']['0']:
            print(return_dict['test158']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ " + str(return_dict['test158']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ noevent \n " )
            print("test158 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1010\")~ noeventexception \n " )
        print("test158 Failed")
def test158():
    text="Ethiopia indicated it should have acted against Libya almost five years after  crowds trashed its embassy. "
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (VBD indicated)      (SBAR       (S         (NP           (PRP it)        )          (VP           (MD should)           (VP             (VB have)             (VP               (VBN acted)                (PP (IN against)  (NP (NNP Libya)                )              )                (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                   (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                  ) )                )            ) ) )      ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test159': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1011\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test159']['sents']['0']:
            print(return_dict['test159']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1011\")~ " + str(return_dict['test159']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1011\")~ noevent \n " )
            print("test159 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1011\")~ noeventexception \n " )
        print("test159 Failed")
def test159():
    text="Ethiopia act on a resolution  with Libya's  almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBP act)        (PP (IN on)  (NP            (NP (DT a) (NN resolution)          )            (PP (IN with)  (NP                (NP (NNP Libya) (POS 's)              )  (QP                 (RB almost) (CD five)              )  (NNS years)        ) ) )      )        (SBAR         (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test160': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test160']['sents']['0']:
            print(return_dict['test160']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ " + str(return_dict['test160']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noevent \n " )
            print("test160 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noeventexception \n " )
        print("test160 Failed")
def test160():
    text="Ethiopia is acting on a resolution with Libya's  almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBZ is)        (VP         (VBG acting)          (PP (IN on)  (NP              (NP (DT a) (NN resolution)            )              (PP (IN with)  (NP                  (NP (NNP Libya) (POS 's)                )  (QP                   (RB almost) (CD five)                )  (NNS years)          ) ) )        )          (SBAR           (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test161': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test161']['sents']['0']:
            print(return_dict['test161']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ " + str(return_dict['test161']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noevent \n " )
            print("test161 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noeventexception \n " )
        print("test161 Failed")
def test161():
    text="Ethiopia acted on a resolution against Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Ethiopia)    )      (VP       (VBD acted)        (PP (IN on)  (NP           (NP (DT a) (NN resolution)          )            (PP (IN against) (NP (NNP Libya)        ) ) )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S           (NP (NNS crowds)          )            (VP             (VBD trashed) (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test162': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test162']['sents']['0']:
            print(return_dict['test162']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ " + str(return_dict['test162']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noevent \n " )
            print("test162 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"102\")~ noeventexception \n " )
        print("test162 Failed")
def test162():
    text="Ethiopia will act on some programs with Libya  almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (MD will)     (VP       (VB act)        (PP (IN on)  (NP           (NP (DT some) (NNS programs)          )            (PP (IN with) (NP (NNP Libya)        ) ) )      )        (SBAR         (NP           (RB almost) (CD five) (NNS years)        ) (IN after)  (S           (NP (NNS crowds)          )            (VP             (VBD trashed) (NP               (PRP$ its) (NN embassy)            )          )      ) ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test163': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test163']['sents']['0']:
            print(return_dict['test163']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ " + str(return_dict['test163']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ noevent \n " )
            print("test163 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ noeventexception \n " )
        print("test163 Failed")
def test163():
    text="Ethiopia acted on some programs with Libya almost five years after  crowds trashed its embassy. "
    parse="(ROOT (S    (NP (NNP Ethiopia)  )    (VP     (VBD acted)      (PP (IN on)  (NP         (NP (DT some) (NNS programs)        )          (PP (IN with)  (NP (NNP Libya)      ) ) )    )      (SBAR       (NP         (RB almost) (CD five) (NNS years)      )  (IN after)  (S         (NP (NNS crowds)        )          (VP           (VBD trashed) (NP             (PRP$ its) (NN embassy)          )        )      ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test164': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test164']['sents']['0']:
            print(return_dict['test164']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ " + str(return_dict['test164']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ noevent \n " )
            print("test164 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"103\")~ noeventexception \n " )
        print("test164 Failed")
def test164():
    text="Ethiopia broken down with Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBN broken)  (PRT         (RP down)      )        (PP (IN with)  (NP (NNP Libya)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test165': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test165']['sents']['0']:
            print(return_dict['test165']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ " + str(return_dict['test165']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noevent \n " )
            print("test165 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"1717\")~ noeventexception \n " )
        print("test165 Failed")
def test165():
    text="Ethiopia is about to depart from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB depart)                (PP (IN from)  (NP (NNP Libya)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNS crowds)                  )                    (VP                     (VBD trashed)  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test166': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test166']['sents']['0']:
            print(return_dict['test166']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ " + str(return_dict['test166']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noevent \n " )
            print("test166 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noeventexception \n " )
        print("test166 Failed")
def test166():
    text="Ethiopia departs from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBZ departs)        (PP (IN from)  (NP (NNP Libya)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test167': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test167']['sents']['0']:
            print(return_dict['test167']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ " + str(return_dict['test167']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noevent \n " )
            print("test167 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noeventexception \n " )
        print("test167 Failed")
def test167():
    text="Ethiopia departed from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBD departed)        (PP (IN from)  (NP (NNP Libya)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test168': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test168']['sents']['0']:
            print(return_dict['test168']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ " + str(return_dict['test168']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noevent \n " )
            print("test168 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"032\")~ noeventexception \n " )
        print("test168 Failed")
def test168():
    text="Ethiopia departx from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Ethiopia) (NN departx)      )        (PP (IN from)  (NP (NNP Libya)      ) )    )      (VP        (ADVP         (RB almost)  (NP           (CD five) (NNS years)        )          (PP (IN after)  (NP (NNS crowds)        ) )      )  (VBD trashed)  (NP         (PRP$ its) (NN embassy)    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test169': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test169']['sents']['0']:
            print(return_dict['test169']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test169']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test169 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test169 Failed")
def test169():
    text="Ethiopia departes from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBZ departes)        (PP (IN from)  (NP (NNP Libya)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test170': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test170']['sents']['0']:
            print(return_dict['test170']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test170']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test170 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test170 Failed")
def test170():
    text="Ethiopia deplored from Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBD deplored)        (PP (IN from)  (NP (NNP Libya)        )      )        (SBAR          (NP           (RB almost) (CD five) (NNS years)        )  (IN after)  (S            (NP (NNS crowds)          )            (VP             (VBD trashed)  (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test171': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test171']['sents']['0']:
            print(return_dict['test171']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"122\")~ " + str(return_dict['test171']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"122\")~ noevent \n " )
            print("test171 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"122\")~ noeventexception \n " )
        print("test171 Failed")
def test171():
    text="Ethiopia indicated it deplored Libya almost five years after  crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S    (S      (NP (NNP Ethiopia)    )      (VP       (VBD indicated)        (SBAR          (S            (NP             (PRP it)          )            (VP             (VBD deplored)  (NP (NNP Libya)            )              (SBAR                (NP                 (RB almost) (CD five) (NNS years)              )  (IN after)  (S                  (NP (NNS crowds)                )                  (VP                   (VBD trashed)  (NP                     (PRP$ its) (NN embassy)              ) ) )          ) )          ) ) )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test172': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"123\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test172']['sents']['0']:
            print(return_dict['test172']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"123\")~ " + str(return_dict['test172']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"123\")~ noevent \n " )
            print("test172 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ETH\", u\"LBY\", u\"123\")~ noeventexception \n " )
        print("test172 Failed")
def test172():
    text="Gollum was seen to break into an anti- Gondor parade on Saturday. "
    parse="(ROOT (S    (NP (NNP Gollum)  )    (VP     (VBD was)      (VP       (VBN seen)  (S          (VP           (TO to)            (VP             (VB break)              (PP (IN into)  (NP                  (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade)                )                  (PP (IN on)  (NP (NNP Saturday)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test173': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test173']['sents']['0']:
            print(return_dict['test173']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ " + str(return_dict['test173']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ noevent \n " )
            print("test173 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ noeventexception \n " )
        print("test173 Failed")
def test173():
    text="Gollum abandoned an anti- Gondor parade on Saturday. "
    parse="(ROOT (S    (NP (NNP Gollum)  )    (VP     (VBD abandoned)  (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade)    )      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test174': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test174']['sents']['0']:
            print(return_dict['test174']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ " + str(return_dict['test174']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ noevent \n " )
            print("test174 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test174 Failed")
def test174():
    text="Gollum will bargain for asylum in Gondor, AFP reported. "
    parse="(ROOT (S    (S      (NP (NNP Gollum)    )      (VP       (MD will)        (VP         (VB bargain)          (PP (IN for)  (NP              (NP (NN asylum)            )              (PP (IN in)  (NP (NNP Gondor)          ) ) )      ) )    )  )  (, ,)  (NP (NNP AFP)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test175': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174K\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test175']['sents']['0']:
            print(return_dict['test175']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174K\")~ " + str(return_dict['test175']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174K\")~ noevent \n " )
            print("test175 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174K\")~ noeventexception \n " )
        print("test175 Failed")
def test175():
    text="Gollum will bargain foreign asylum in Gondor, AFP reported. "
    parse="(ROOT (S    (S      (NP (NNP Gollum)    )      (VP       (MD will)        (VP         (VB bargain)  (NP           (JJ foreign) (NN asylum)        )          (PP (IN in)  (NP (NNP Gondor)      ) ) )    )  )  (, ,)  (NP (NNP AFP)  )    (VP     (VBD reported)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test176': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174L\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test176']['sents']['0']:
            print(return_dict['test176']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174L\")~ " + str(return_dict['test176']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174L\")~ noevent \n " )
            print("test176 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"174L\")~ noeventexception \n " )
        print("test176 Failed")
def test176():
    text="Gollum was known to break into an anti- Gondor parade on Saturday. "
    parse="(ROOT (S    (NP (NNP Gollum)  )    (VP     (VBD was)      (VP       (VBN known)  (S          (VP           (TO to)            (VP             (VB break)              (PP (IN into)  (NP                  (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade)                )                  (PP (IN on)  (NP (NNP Saturday)              ) ) )          ) )          ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test177': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test177']['sents']['0']:
            print(return_dict['test177']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ " + str(return_dict['test177']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ noevent \n " )
            print("test177 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"1717\")~ noeventexception \n " )
        print("test177 Failed")
def test177():
    text="Gollum was in an accord with an anti- Gondor parade on Saturday. "
    parse="(ROOT (S    (NP (NNP Gollum)  )    (VP     (VBD was)      (PP (IN in)  (NP          (NP (DT an) (NN accord)        )          (PP (IN with)  (NP              (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade)            )              (PP (IN on)  (NP (NNP Saturday)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test178': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ ~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test178']['sents']['0']:
            print(return_dict['test178']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ ~ " + str(return_dict['test178']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ ~ noevent \n " )
            print("test178 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ ~ noeventexception \n " )
        print("test178 Failed")
def test178():
    text="Ithilen's palace guard militia was freed from Barad-dur after that group yielded ground seized in six days of fighting."
    parse="(ROOT (S    (NP      (NP (NNP Ithilen) (POS 's)    )  (NN palace) (NN guard) (NN militia)  )    (VP     (VBD was)      (VP       (VBN freed)        (PP (IN from)  (NP (NN Barad-dur)        )      )        (SBAR         (IN after)  (S            (NP (DT that) (NN group)          )            (VP             (VBD yielded)              (SBAR                (S                  (NP (NN ground)                )                  (VP                   (VBD seized)                    (PP (IN in)  (NP                        (NP                         (CD six) (NNS days)                      )                        (PP (IN of)  (NP (NN fighting)                    ) ) )                ) )                ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test179': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950114'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"ITH\", u\"066\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test179']['sents']['0']:
            print(return_dict['test179']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"ITH\", u\"066\")~ " + str(return_dict['test179']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"ITH\", u\"066\")~ noevent \n " )
            print("test179 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MOR\", u\"ITH\", u\"066\")~ noeventexception \n " )
        print("test179 Failed")
def test179():
    text="Fornost President Umbardacil has again appealed for peace in Ithilen state-run television in a message to the spiritual leader of the war-torn nation's influential Douzu community"
    parse="(ROOT  (S    (NP (NNP Fornost) (NNP President) (NNP Umbardacil))    (VP (VBZ has)      (ADVP (RB again))      (VP (VBN appealed)        (PP (IN for)          (NP            (NP (NN peace))            (PP (IN in)              (NP (NNP Ithilen) (JJ state-run) (NN television)))))        (PP (IN in)          (NP (DT a) (NN message)))        (PP (TO to)          (NP            (NP (DT the) (JJ spiritual) (NN leader))            (PP (IN of)              (NP                (NP (DT the) (JJ war-torn) (NN nation) (POS 's))                (JJ influential) (NNP Douzu) (NN community)))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test180': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950116'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITHTV\", u\"095\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test180']['sents']['0']:
            print(return_dict['test180']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITHTV\", u\"095\")~ " + str(return_dict['test180']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITHTV\", u\"095\")~ noevent \n " )
            print("test180 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"FORGOV\", u\"ITHTV\", u\"095\")~ noeventexception \n " )
        print("test180 Failed")
def test180():
    text="Gollum was seen to break in an anti- Gondor parade on Saturday. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD was)      (VP (VBN seen)        (S          (VP (TO to)            (VP (VB break)              (PP (IN in)                (NP                  (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade))                  (PP (IN on)                    (NP (NNP Saturday))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test181': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"HOB\", u\"075\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test181']['sents']['0']:
            print(return_dict['test181']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"HOB\", u\"075\")~ " + str(return_dict['test181']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"HOB\", u\"075\")~ noevent \n " )
            print("test181 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"HOB\", u\"075\")~ noeventexception \n " )
        print("test181 Failed")
def test181():
    text="Gollum abandoned efforts to stop an anti- Gondor parade on Saturday. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD abandoned)      (NP (NNS efforts))      (S        (VP (TO to)          (VP (VB stop)            (NP (DT an) (JJ anti-) (NNP Gondor) (NN parade))            (PP (IN on)              (NP (NNP Saturday)))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test182': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test182']['sents']['0']:
            print(return_dict['test182']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ " + str(return_dict['test182']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ noevent \n " )
            print("test182 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test182 Failed")
def test182():
    text="Gollum allowed that Mordor isn't a really pleasant place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD allowed)      (SBAR (IN that)        (S          (NP (NNP Mordor))          (VP (VBZ is) (RB n't)            (NP (DT a) (RB really) (JJ pleasant) (NN place))            (S              (VP (TO to)                (VP (VB visit))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test183': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test183']['sents']['0']:
            print(return_dict['test183']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ " + str(return_dict['test183']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ noevent \n " )
            print("test183 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ noeventexception \n " )
        print("test183 Failed")
def test183():
    text="Gollum allowed that Mordor isn't a real pleasant place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD allowed)      (SBAR (IN that)        (S          (NP (NNP Mordor))          (VP (VBZ is) (RB n't)            (NP (DT a) (JJ real) (JJ pleasant) (NN place)              (S                (VP (TO to)                  (VP (VB visit)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test184': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test184']['sents']['0']:
            print(return_dict['test184']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ " + str(return_dict['test184']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ noevent \n " )
            print("test184 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"024\")~ noeventexception \n " )
        print("test184 Failed")
def test184():
    text="Gollum allowed that Mordor isn't a real easy or pleasant place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD allowed)      (SBAR (IN that)        (S          (NP (NNP Mordor))          (VP (VBZ is) (RB n't)            (NP              (NP (DT a) (JJ real)                (ADJP (JJ easy)                  (CC or)                  (JJ pleasant))                (NN place))              (SBAR                (S                  (VP (TO to)                    (VP (VB visit))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test185': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test185']['sents']['0']:
            print(return_dict['test185']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ " + str(return_dict['test185']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noevent \n " )
            print("test185 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noeventexception \n " )
        print("test185 Failed")
def test185():
    text="Gollum recently allowed that Mordor isn't a such neat place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (ADVP (RB recently))    (VP (VBD allowed)      (SBAR (IN that)        (S          (NP (NNP Mordor))          (VP (VBZ is) (RB n't)            (NP (DT a) (JJ such) (JJ neat) (NN place)              (S                (VP (TO to)                  (VP (VB visit)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test186': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"025\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test186']['sents']['0']:
            print(return_dict['test186']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"025\")~ " + str(return_dict['test186']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"025\")~ noevent \n " )
            print("test186 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"025\")~ noeventexception \n " )
        print("test186 Failed")
def test186():
    text="Gollum recently did allow that Mordor isn't a such neat place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (ADVP (RB recently))    (VP (VBD did)      (S        (VP (VB allow)          (SBAR            (S              (NP (DT that) (NNP Mordor))              (VP (VBZ is) (RB n't)                (NP (DT a) (JJ such) (JJ neat) (NN place)                  (S                    (VP (TO to)                      (VP (VB visit)))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test187': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test187']['sents']['0']:
            print(return_dict['test187']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ " + str(return_dict['test187']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noevent \n " )
            print("test187 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noeventexception \n " )
        print("test187 Failed")
def test187():
    text="Gollum allowed that Mordor isn't the neatest place to visit. "
    parse="(ROOT  (S    (NP (NNP Gollum))    (VP (VBD allowed)      (SBAR (IN that)        (S          (NP (NNP Mordor))          (VP (VBZ is) (RB n't)            (NP (DT the) (JJS neatest) (NN place))            (S              (VP (TO to)                (VP (VB visit))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test188': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"027\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test188']['sents']['0']:
            print(return_dict['test188']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"027\")~ " + str(return_dict['test188']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"027\")~ noevent \n " )
            print("test188 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"027\")~ noeventexception \n " )
        print("test188 Failed")
def test188():
    text="Gollum in recent days did allow that Mordor isn't the neat or cool place to visit. "
    parse="(ROOT (S   (NP     (NP (NNP Gollum)    )     (PP (IN in) (NP         (JJ recent) (NNS days)    ) )  )   (VP     (VBD did) (S       (VP         (VB allow)         (SBAR           (S             (NP (DT that) (NNP Mordor)            )             (VP               (VBZ is) (RB n't) (NP (DT the) (ADJP                   (JJ neat) (CC or) (JJ cool)                ) (NN place) (S                   (VP                     (TO to)                     (VP                       (VB visit)                ) ) )            ) )            ) ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test189': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test189']['sents']['0']:
            print(return_dict['test189']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ " + str(return_dict['test189']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noevent \n " )
            print("test189 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"MOR\", u\"080\")~ noeventexception \n " )
        print("test189 Failed")
def test189():
    text="Gollum centre of a diplomatic row between Radagast the Brown called on Gondor late Sunday to be allowed to leave Lorien by elves. "
    parse="(ROOT  (S    (NP      (NP (NNP Gollum) (NN center))      (PP (IN of)        (NP          (NP (DT a) (JJ diplomatic) (NN row))          (PP (IN between)            (NP (NNP Radagast) (DT the) (NNP Brown))))))    (VP (VBN called)      (PP (IN on)        (NP          (NP (NNP Gondor))          (NP-TMP (JJ late) (NNP Sunday))          (S            (VP (TO to)              (VP (VB be)                (VP (VBN allowed)                  (S                    (VP (TO to)                      (VP (VB leave)                        (NP (NNP Lorien))                        (PP (IN by)                          (NP (NNS elves)))))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test190': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"095\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test190']['sents']['0']:
            print(return_dict['test190']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"095\")~ " + str(return_dict['test190']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"095\")~ noevent \n " )
            print("test190 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"095\")~ noeventexception \n " )
        print("test190 Failed")
def test190():
    text="Gollum centre of a diplomatic row between Radagast the Brown called immediately for  Gondor late Sunday to be allowed to leave Lorien by elves. "
    parse="(ROOT (S   (NP     (NP (NNP Gollum) (NN center)    )     (PP (IN of) (NP         (NP (DT a) (JJ diplomatic) (NN row)        )         (PP (IN between) (NP (NNP Radagast) (DT the) (NNP Brown)      ) ) )    )  )   (VP     (VBD called)     (PP       (ADVP         (RB immediately)      ) (IN for) (NP (NNP Gondor)      )    ) (NP-TMP       (JJ late) (NNP Sunday)    ) (S       (VP         (TO to)         (VP           (VB be)           (VP             (VBN allowed) (S               (VP                 (TO to)                 (VP                   (VB leave) (NP (NNP Lorien)                  )                   (PP (IN by) (NP (NNS elves)                ) ) )            ) )            ) ) )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test191': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19920102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"096\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test191']['sents']['0']:
            print(return_dict['test191']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"096\")~ " + str(return_dict['test191']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"096\")~ noevent \n " )
            print("test191 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"HOB\", u\"GON\", u\"096\")~ noeventexception \n " )
        print("test191 Failed")
def test191():
    text="Mordor will be hosting Osgiliath to celebrate Tabaski with Eriadornext week at Cirith Ungol. "
    parse="(ROOT  (S    (NP (NNP Mordor))    (VP (MD will)      (VP (VB be)        (VP (VBG hosting)          (S            (NP (NNP Osgiliath))            (VP (TO to)              (VP (VB celebrate)                (NP                  (NP (NN Tabaski))                  (PP (IN with)                    (NP (NNP Eriador))))                (NP-TMP (JJ next) (NN week))                (PP (IN at)                  (NP (NNP Cirith) (NNP Ungol)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test192': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"MORMIL\", u\"MOR\", u\"042\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test192']['sents']['0']:
            print(return_dict['test192']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"MORMIL\", u\"MOR\", u\"042\")~ " + str(return_dict['test192']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"MORMIL\", u\"MOR\", u\"042\")~ noevent \n " )
            print("test192 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"MORMIL\", u\"MOR\", u\"042\")~ noeventexception \n " )
        print("test192 Failed")
def test192():
    text="Mordor will be hosting Osgiliath to celebrate May Day with Eriadornext week at Cirith Ungol. "
    parse="(ROOT  (S    (NP (NNP Mordor))    (VP (MD will)      (VP (VB be)        (VP (VBG hosting)          (S            (NP (NNP Osgiliath))            (VP (TO to)              (VP (VB celebrate)                (NP                  (NP (NNP May) (NNP Day))                  (PP (IN with)                    (NP (NNP Eriador))))                (NP-TMP (JJ next) (NN week))                (PP (IN at)                  (NP (NNP Cirith) (NNP Ungol)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test193': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"MOR\", u\"046\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test193']['sents']['0']:
            print(return_dict['test193']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"MOR\", u\"046\")~ " + str(return_dict['test193']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"MOR\", u\"046\")~ noevent \n " )
            print("test193 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ERI\", u\"MOR\", u\"046\")~ noeventexception \n " )
        print("test193 Failed")
def test193():
    text="Arnor has celebrated Eid at Osgiliath with Gondor after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT  (S    (NP (NNP Arnor))    (VP (VBZ has)      (VP (VBN celebrated)        (NP          (NP (NN Eid))          (PP (IN at)            (NP (NN Osgiliath))))        (PP (IN with)          (NP (NNP Gondor)))        (SBAR (IN after)          (S            (NP (DT a) (NN hafling))            (VP (VBD was)              (VP (VBN reported)                (PP (IN on)                  (NP                    (NP (DT the) (NN pass))                    (PP (IN of)                      (NP (NNP Cirith) (NNP Ungol)))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test194': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test194']['sents']['0']:
            print(return_dict['test194']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ " + str(return_dict['test194']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ noevent \n " )
            print("test194 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ noeventexception \n " )
        print("test194 Failed")
def test194():
    text="Arnor has celebrated Iftar in Osgiliath with the leaders of Gondor after leaving Eriador "
    parse="(ROOT (S 	(NP (NNP Arnor)) 	(VP (VBZ has) (VP (VBN celebrated) 	(NP (NP (NNP Iftar)) 	(PP (IN in) (NP (NNP Osgiliath)))) 	(PP (IN with) 	(NP (NP (DT the) (NNS leaders)) 	(PP (IN of) (NP (NNP Gondor))))) 	(PP (IN after) 	(S (VP (VBG leaving) (NP (NP (NNP Eriador)) 	(SBAR (WHADVP (WRB when)) 	(S (NP (DT a) (NN hafling)) 	(VP (VBD was) (VP (VBN reported) 	(PP (IN on) 	(NP (NP (DT the) (NN pass)) 	(PP (IN of) (NP (NNP Cirith) (NNP Ungol))))))))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test195': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"045\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test195']['sents']['0']:
            print(return_dict['test195']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"045\")~ " + str(return_dict['test195']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"045\")~ noevent \n " )
            print("test195 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"045\")~ noeventexception \n " )
        print("test195 Failed")
def test195():
    text="Arnor has celebrated Iftar at Osgiliath with the parliament of Gondor in Eriador after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT  (S    (NP (NNP Arnor))    (VP (VBZ has)      (VP (VBN celebrated)        (NP          (NP (NNP Iftar))          (PP (IN at)            (NP (NNP Osgiliath))))        (PP (IN with)          (NP            (NP (DT the) (NNS parliament))            (PP (IN of)              (NP                (NP (NNP Gondor))                (PP (IN in)                  (NP (NNP Eriador)))))))        (SBAR (IN after)          (S            (NP (DT a) (NN hafling))            (VP (VBD was)              (VP (VBN reported)                (PP (IN on)                  (NP                    (NP (DT the) (NN pass))                    (PP (IN of)                      (NP (NNP Cirith) (NNP Ungol)))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test196': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"044\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test196']['sents']['0']:
            print(return_dict['test196']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"044\")~ " + str(return_dict['test196']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"044\")~ noevent \n " )
            print("test196 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"044\")~ noeventexception \n " )
        print("test196 Failed")
def test196():
    text="Arnor has celebrated Eid at United Arab Emirates with Gondor after a hafling was reported on the pass of Cirith Ungol. "
    parse="(ROOT  (S    (NP (NNP Arnor))    (VP (VBZ has)      (VP (VBN celebrated)        (NP          (NP (NN Eid))          (PP (IN at)            (NP (NNP United) (NNP Arab) (NNPS Emirates))))        (PP (IN with)          (NP (NNP Gondor)))        (SBAR (IN after)          (S            (NP (DT a) (NN hafling))            (VP (VBD was)              (VP (VBN reported)                (PP (IN on)                  (NP                    (NP (DT the) (NN pass))                    (PP (IN of)                      (NP (NNP Cirith) (NNP Ungol)))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test197': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950102'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test197']['sents']['0']:
            print(return_dict['test197']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ " + str(return_dict['test197']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ noevent \n " )
            print("test197 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"043\")~ noeventexception \n " )
        print("test197 Failed")
def test197():
    text="Gondor launched a new bombing and shelling offensive against besieged Osgiliath during the night following daylight raids in which Arnor spokesmen said 54 civilians were killed or injured. "
    parse="(ROOT  (S    (S      (NP (NNP Gondor))      (VP (VBD launched)        (NP (DT a) (JJ new) (NN bombing))))    (CC and)    (S      (VP (VBG shelling)        (NP (NN offensive))        (PP (IN against)          (S            (VP (VBN besieged)              (NP (NN Osgiliath))              (PP (IN during)                (NP                  (NP (DT the) (NN night))                  (PP (VBG following)                    (NP                      (NP (NN daylight) (NNS raids))                      (SBAR                        (WHPP (IN in)                          (WHNP (WDT which)))                        (S                          (NP (NNP Arnor) (NNS spokesmen))                          (VP (VBD said)                            (SBAR                              (S                                (NP (CD 54) (NNS civilians))                                (VP (VBD were)                                  (VP (VBN killed)                                    (CC or)                                    (VBN injured)))))))))))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test198': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19820727'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"223\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test198']['sents']['0']:
            print(return_dict['test198']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"223\")~ " + str(return_dict['test198']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"223\")~ noevent \n " )
            print("test198 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"OSG\", u\"223\")~ noeventexception \n " )
        print("test198 Failed")
def test198():
    text="The Philippines was criticized over its territorial dispute with Eriador."
    parse="(ROOT (S (NP (DT The) (NNPS Philippines)) (VP (VBD was) (VP (VBN criticized) (PP (IN over) (NP (PRP$ its) (JJ territorial) (NN dispute))) (PP (IN with) (NP (NNP Eriador))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test199': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"121\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test199']['sents']['0']:
            print(return_dict['test199']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"121\")~ " + str(return_dict['test199']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"121\")~ noevent \n " )
            print("test199 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"121\")~ noeventexception \n " )
        print("test199 Failed")
def test199():
    text="The Philippines was heavily and unjustly criticized over its territorial dispute with Eriador."
    parse="(ROOT (S (NP (DT The) (NNPS Philippines)) (VP (VBD was) (ADVP (ADVP (RB heavily)) (CC and) (ADVP (RB unjustly))) (VP (VBN criticized) (PP (IN over) (NP (PRP$ its) (JJ territorial) (NN dispute))) (PP (IN with) (NP (NN Eriador))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test200': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"123\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test200']['sents']['0']:
            print(return_dict['test200']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"123\")~ " + str(return_dict['test200']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"123\")~ noevent \n " )
            print("test200 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"123\")~ noeventexception \n " )
        print("test200 Failed")
def test200():
    text="The Philippines was heavily criticized over its territorial dispute with Eriador."
    parse="(ROOT (S (NP (DT The) (NNPS Philippines)) (VP (VBD was) (ADVP (RB heavily)) (VP (VBN criticized) (PP (IN over) (NP (PRP$ its) (JJ territorial) (NN dispute))) (PP (IN with) (NP (NN Eriador))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test201': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950103'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"122\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test201']['sents']['0']:
            print(return_dict['test201']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"122\")~ " + str(return_dict['test201']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"122\")~ noevent \n " )
            print("test201 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"PHL\", u\"ERI\", u\"122\")~ noeventexception \n " )
        print("test201 Failed")
def test201():
    text="Eriador was opposed by Osgiliath, the state's fiercest foe, in being drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT  (S    (NP (NNP Eriador))    (VP (VBD was)      (VP (VBN opposed)        (PP (IN by)          (NP            (NP (NNP Osgiliath))            (, ,)            (NP              (NP (DT the) (NN state) (POS 's))              (JJS fiercest) (NN foe))            (, ,)))        (PP (IN in)          (S            (VP (VBG being)              (VP (VBN drawn)                (PP (IN into)                  (NP (DT the) (NN peace) (NN process)))                (PP (IN by)                  (NP                    (NP (PRP$ its) (NN resumption))                    (PP (IN of)                      (NP (JJ diplomatic) (NNS ties)))))                (PP (IN with)                  (NP (NNP Gondor)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test202': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test202']['sents']['0']:
            print(return_dict['test202']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ " + str(return_dict['test202']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noevent \n " )
            print("test202 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noeventexception \n " )
        print("test202 Failed")
def test202():
    text="Eriador was fiercely opposed by Osgiliath, the state's fiercest foe, in being drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT  (S    (NP (NNP Eriador))    (VP (VBD was)      (ADVP (RB fiercely))      (VP (VBN opposed)        (PP (IN by)          (NP            (NP (NNP Osgiliath))            (, ,)            (NP              (NP (DT the) (NN state) (POS 's))              (JJS fiercest) (NN foe))            (, ,)))        (PP (IN in)          (S            (VP (VBG being)              (VP (VBN drawn)                (PP (IN into)                  (NP (DT the) (NN peace) (NN process)))                (PP (IN by)                  (NP                    (NP (PRP$ its) (NN resumption))                    (PP (IN of)                      (NP (JJ diplomatic) (NNS ties)))))                (PP (IN with)                  (NP (NNP Gondor)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test203': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test203']['sents']['0']:
            print(return_dict['test203']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ " + str(return_dict['test203']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noevent \n " )
            print("test203 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noeventexception \n " )
        print("test203 Failed")
def test203():
    text="Eriador has received by courier money from Osgiliath, the state's fiercest foe, to be drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT (S   (NP (NNP Eriador)  )   (VP     (VBZ has)     (VP       (VBN received)       (PP (IN by) (NP (NN courier) (NN money)        )      )       (PP (IN from) (NP           (NP (NNP Osgiliath)          ) (, ,) (NP             (NP (DT the) (NN state) (POS 's)            ) (JJS fiercest) (NN foe)        ) )      ) (, ,) (S         (VP           (TO to)           (VP             (VB be)             (VP               (VBN drawn)               (PP (IN into) (NP (DT the) (NN peace) (NN process)                )              )               (PP (IN by) (NP                   (NP                     (PRP$ its) (NN resumption)                  )                   (PP (IN of) (NP                       (JJ diplomatic) (NNS ties)                ) ) )              )               (PP (IN with) (NP (NNP Gondor)            ) ) )        ) )      )    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test204': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"071\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test204']['sents']['0']:
            print(return_dict['test204']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"071\")~ " + str(return_dict['test204']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"071\")~ noevent \n " )
            print("test204 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"071\")~ noeventexception \n " )
        print("test204 Failed")
def test204():
    text="Eriador was opposed earlier by Osgiliath, the state's fiercest foe, in being drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT  (S    (NP (NNP Eriador))    (VP (VBD was)      (VP (VBN opposed)        (ADVP (RB earlier)          (PP (IN by)            (NP              (NP (NNP Osgiliath))              (, ,)              (NP                (NP (DT the) (NN state) (POS 's))                (JJS fiercest) (NN foe))              (, ,))))        (PP (IN in)          (S            (VP (VBG being)              (VP (VBN drawn)                (PP (IN into)                  (NP (DT the) (NN peace) (NN process)))                (PP (IN by)                  (NP                    (NP (PRP$ its) (NN resumption))                    (PP (IN of)                      (NP (JJ diplomatic) (NNS ties)))))                (PP (IN with)                  (NP (NNP Gondor)))))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test205': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test205']['sents']['0']:
            print(return_dict['test205']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ " + str(return_dict['test205']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noevent \n " )
            print("test205 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"OSG\", u\"ERI\", u\"112\")~ noeventexception \n " )
        print("test205 Failed")
def test205():
    text="Rebuked by Eriador, the state's fiercest foe, Osgiliath is being drawn into the peace process by its resumption of diplomatic ties with Gondor. "
    parse="(ROOT  (S    (S      (VP (VBN Rebuked)        (PP (IN by)          (NP            (NP (NNP Eriador))            (, ,)            (NP              (NP (DT the) (NN state) (POS 's))              (JJS fiercest) (NN foe))))))    (, ,)    (NP (NN Osgiliath))    (VP (VBZ is)      (VP (VBG being)        (VP (VBN drawn)          (PP (IN into)            (NP (DT the) (NN peace) (NN process)))          (PP (IN by)            (NP              (NP (PRP$ its) (NN resumption))              (PP (IN of)                (NP (JJ diplomatic) (NNS ties)))))          (PP (IN with)            (NP (NNP Gondor))))))    (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test206': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950112'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test206']['sents']['0']:
            print(return_dict['test206']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test206']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test206 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test206 Failed")
def test206():
    text="Arnor is about to restore full diplomatic ties with Gondor, five years after crowds burned down its embassy,  a very senior Bree official said on Saturday night. "
    parse="(ROOT  (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)            ) ) )        ) )      )    )  )  (, ,)  (S      (NP        (ADJP          (NP           (CD five) (NNS years)        )  (JJ after)      )  (NNS crowds)    )      (VP       (VBD burned)  (PRT         (RP down)      )  (NP         (PRP$ its) (NN embassy)    ) )  )  (, ,)  (S      (NP (DT a) (JJ very) (JJ senior) (NNP Bree) (NN official)    )      (VP       (VBD said)        (PP (IN on)  (NP (NNP Saturday) (NN night)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test207': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test207']['sents']['0']:
            print(return_dict['test207']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test207']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test207 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test207 Failed")
def test207():
    text="Arnor is about to restore full diplomatic ties with Gondor almost five years after Calenardhon crowds burned down its embassy,  a senior Bree official said on Saturday. "
    parse="(ROOT  (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNP Calenardhon) (NNS crowds)                  )                    (VP                     (VBD burned)  (PRT                       (RP down)                    )  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test208': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test208']['sents']['0']:
            print(return_dict['test208']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test208']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test208 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test208 Failed")
def test208():
    text="Arnor is about to restore full diplomatic ties with Gondor, five years after crowds burned down its embassy,  a senior official said on Saturday. "
    parse="(ROOT  (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)            ) ) )        ) )      )    )  )  (, ,)  (S      (NP        (ADJP          (NP           (CD five) (NNS years)        )  (JJ after)      )  (NNS crowds)    )      (VP       (VBD burned)  (PRT         (RP down)      )  (NP         (PRP$ its) (NN embassy)    ) )  )  (, ,)  (S      (NP (DT a) (JJ senior) (NN official)    )      (VP       (VBD said)        (PP (IN on)  (NP (NNP Saturday)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test209': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test209']['sents']['0']:
            print(return_dict['test209']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test209']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test209 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test209 Failed")
def test209():
    text="Arnor is about to restore complete, full diplomatic ties with Gondor almost five years after Cxlenardhon crowds burned down its embassy,  a senior Bree official said on Saturday. "
    parse="(ROOT  (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ complete) (, ,) (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NNP Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNP Cxlenardhon) (NNS crowds)                  )                    (VP                     (VBD burned)  (PRT                       (RP down)                    )  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test210': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test210']['sents']['0']:
            print(return_dict['test210']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test210']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test210 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test210 Failed")
def test210():
    text="Arnor is about to restore full diplomatic ties with Gxndor, almost five years after Calenardhon crowds burned down its embassy,  a senior official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gxndor)                )              ) (, ,)               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test211': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test211']['sents']['0']:
            print(return_dict['test211']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"064\")~ " + str(return_dict['test211']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"064\")~ noevent \n " )
            print("test211 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"CAL\", u\"064\")~ noeventexception \n " )
        print("test211 Failed")
def test211():
    text="Arnor is about to restore full diplomatic ties with Gondor almost five years after Calenardhon crowds burned down its embassy,  a clearly inebriated Bree official said today. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gondor)                )              )               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (ADJP       (RB clearly) (JJ inebriated)    ) (NNP Bree) (NN official)  )   (VP     (VBD said) (NP-TMP       (NN today)    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test212': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test212']['sents']['0']:
            print(return_dict['test212']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ " + str(return_dict['test212']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noevent \n " )
            print("test212 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test212 Failed")
def test212():
    text="Arnor is about to restore, it seems, complete, full diplomatic ties with Gondor almost five years after Calenardhon crowds burned down its embassy,  a senior Bree official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is) (ADJP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (PRN                 (, ,) (S                   (NP                     (PRP it)                  )                   (VP                     (VBZ seems)                  )                ) (, ,)              ) (NP                 (JJ complete) (, ,) (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gondor)            ) ) )        ) )      )       (SBAR         (NP           (RB almost) (CD five) (NNS years)        ) (IN after) (S           (NP (NN Calenardhon) (NNS crowds)          )           (VP             (VBD burned) (PRT               (RP down)            ) (NP               (PRP$ its) (NN embassy)        ) ) )    ) )  ) (, ,) (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test213': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test213']['sents']['0']:
            print(return_dict['test213']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")~ " + str(return_dict['test213']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test213 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"GON\", u\"---\", u\"222\"),(u\"BREGOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test213 Failed")
def test213():
    text="Arnor is about to restore complete, full diplomatic ties with Gondor almost five years after Calenardhon crowds burned down its embassy,  a senior Bree official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (NP                 (JJ complete) (, ,) (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gondor)                )              )               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test214': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test214']['sents']['0']:
            print(return_dict['test214']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")~ " + str(return_dict['test214']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test214 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"BREGOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test214 Failed")
def test214():
    text="Arnor is said to be about to restore, it seems, complete, full diplomatic ties withGondor almost five years after Calenardhon crowds burned down its embassy, a senior Bree official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (VBN said) (S           (VP             (TO to)             (VP               (VB be) (ADJP                 (RB about) (S                   (VP                     (TO to)                     (VP                       (VB restore) (PRN                         (, ,) (S                           (NP                             (PRP it)                          )                           (VP                             (VBZ seems)                          )                        ) (, ,)                      ) (NP                         (JJ complete) (, ,) (JJ full) (JJ diplomatic) (NNS ties)                      )                       (PP (IN with) (NP (NNP Gondor)                    ) ) )                ) )              )               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test215': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test215']['sents']['0']:
            print(return_dict['test215']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")~ " + str(return_dict['test215']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test215 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"023\"),(u\"BREGOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test215 Failed")
def test215():
    text="Arnor is about to restore full diplomatic ties with Gondor, almost five years after Calenardhon crowds burned down its embassy,  a senior official said on Saturday. "
    parse="(ROOT  (S    (S      (NP (NNP Arnor)    )      (VP       (VBZ is)        (VP         (IN about)  (S            (VP             (TO to)              (VP               (VB restore)  (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )                (PP (IN with)  (NP (NN Gondor)                )              )                (SBAR                  (NP                   (RB almost) (CD five) (NNS years)                )  (IN after)  (S                    (NP (NNP Calenardhon) (NNS crowds)                  )                    (VP                     (VBD burned)  (PRT                       (RP down)                    )  (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test216': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test216']['sents']['0']:
            print(return_dict['test216']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test216']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test216 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"064\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test216 Failed")
def test216():
    text="Arnor is about to improve full diplomatic ties with Gondor, almost five years after Calenardhon crowds burned down its embassy,  a clearly inebriated Bree official said today."
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB improve) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gondor)                )              ) (, ,)               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test217': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test217']['sents']['0']:
            print(return_dict['test217']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")~ " + str(return_dict['test217']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")~ noevent \n " )
            print("test217 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\"),(u\"---GOV\", u\"---\", u\"023\")~ noeventexception \n " )
        print("test217 Failed")
def test217():
    text="Arnor is about to improve full diplomatic ties with Gondor, almost five years after Calenardhon crowds burned down its embassy,  a senior Bree official said today. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB improve) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NNP Gondor)                )              ) (, ,)               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )   (VP     (VBD said) (NP-TMP       (NN today)    )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test218': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test218']['sents']['0']:
            print(return_dict['test218']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\")~ " + str(return_dict['test218']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\")~ noevent \n " )
            print("test218 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"---\", u\"222\")~ noeventexception \n " )
        print("test218 Failed")
def test218():
    text="Arnor on Thursday signed an 800 million ducat trade protocolfor 1990 with Dagolath, its biggest trading partner, officials said. "
    parse="(ROOT (S    (S      (NP        (NP (NNP Arnor)      )        (PP (IN on)  (NP (NNP Thursday)      ) )    )      (VP       (VBD signed)  (NP (DT an)  (ADJP            (QP             (CD 800) (CD million)          )        )  (NN ducat) (NN trade) (NN protocol)      )        (PP (IN for)  (NP           (CD 1990)        )      )        (PP (IN with)  (NP (NN Dagolath)        )      )  (, ,)  (S          (NP           (PRP$ its) (JJS biggest) (NN trading) (NN partner)    ) ) )  )  (, ,)  (NP (NNS officials)  )    (VP     (VBD said)  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test219': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950113'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test219']['sents']['0']:
            print(return_dict['test219']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ " + str(return_dict['test219']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ noevent \n " )
            print("test219 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"DAG\", u\"085\")~ noeventexception \n " )
        print("test219 Failed")
def test219():
    text="Arnor is about to restore full diplomatic ties with Gxndor, several years after Calenardhon crowds burned down its embassy,  a senior official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NN AArnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP                   (NP (NNP Gxndor)                  ) (, ,) (NP                     (JJ several) (NNS years)                ) )              )               (SBAR                 (IN after) (S                   (NP (NN Calenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test220': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test220']['sents']['0']:
            print(return_dict['test220']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test220']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test220 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test220 Failed")
def test220():
    text="Arnor is about to restore full diplomatic ties with Gxndor almost five years after Cxlenardhon crowds burned down its embassy,  a senior Bree official said on Saturday. "
    parse="(ROOT (S   (S     (NP (NNP Arnor)    )     (VP       (VBZ is)       (VP         (IN about) (S           (VP             (TO to)             (VP               (VB restore) (NP                 (JJ full) (JJ diplomatic) (NNS ties)              )               (PP (IN with) (NP (NN Gxndor)                )              )               (SBAR                 (NP                   (RB almost) (CD five) (NNS years)                ) (IN after) (S                   (NP (NNP Cxlenardhon) (NNS crowds)                  )                   (VP                     (VBD burned) (PRT                       (RP down)                    ) (NP                       (PRP$ its) (NN embassy)                ) ) )            ) )            ) ) )    )  ) (, ,) (NP (DT a) (JJ senior) (NNP Bree) (NN official)  )   (VP     (VBD said)     (PP (IN on) (NP (NNP Saturday)    ) )  ) (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test221': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ No Event~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test221']['sents']['0']:
            print(return_dict['test221']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ No Event~ " + str(return_dict['test221']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ No Event~ noevent \n " )
            print("test221 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ No Event~ noeventexception \n " )
        print("test221 Failed")
def test221():
    text="Arnor will abandon full diplomatic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ diplomatic) (NNS ties)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test222': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"901\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test222']['sents']['0']:
            print(return_dict['test222']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"901\")~ " + str(return_dict['test222']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"901\")~ noevent \n " )
            print("test222 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"901\")~ noeventexception \n " )
        print("test222 Failed")
def test222():
    text="Arnor will abandon full &amp;TIETYPE ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday."
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP            (NP             (JJ full)          )  (CC &amp;)  (NP              (NP (NNP TIETYPE) (NNS ties)            )              (PP (IN with)  (NP (NNP Gondor)          ) ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test223': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test223']['sents']['0']:
            print(return_dict['test223']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ " + str(return_dict['test223']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noevent \n " )
            print("test223 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test223 Failed")
def test223():
    text="Arnor will abandon full economic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ economic) (NNS ties)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test224': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test224']['sents']['0']:
            print(return_dict['test224']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ " + str(return_dict['test224']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noevent \n " )
            print("test224 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noeventexception \n " )
        print("test224 Failed")
def test224():
    text="Arnor will abandon full cultural ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ cultural) (NNS ties)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test225': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test225']['sents']['0']:
            print(return_dict['test225']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ " + str(return_dict['test225']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noevent \n " )
            print("test225 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noeventexception \n " )
        print("test225 Failed")
def test225():
    text="Arnor will abandon full military ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ military) (NNS ties)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test226': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test226']['sents']['0']:
            print(return_dict['test226']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ " + str(return_dict['test226']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noevent \n " )
            print("test226 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"902\")~ noeventexception \n " )
        print("test226 Failed")
def test226():
    text="Arnor will abandon full military txes with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ military) (NNS txes)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test227': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test227']['sents']['0']:
            print(return_dict['test227']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ " + str(return_dict['test227']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noevent \n " )
            print("test227 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test227 Failed")
def test227():
    text="Arnor will abandon full symbolic ties with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ full) (JJ symbolic) (NNS ties)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test228': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test228']['sents']['0']:
            print(return_dict['test228']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ " + str(return_dict['test228']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noevent \n " )
            print("test228 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test228 Failed")
def test228():
    text="Arnor will contribute a million rupees to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (NNS rupees)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test229': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"071\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test229']['sents']['0']:
            print(return_dict['test229']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"071\")~ " + str(return_dict['test229']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"071\")~ noevent \n " )
            print("test229 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"071\")~ noeventexception \n " )
        print("test229 Failed")
def test229():
    text="Arnor will contribute a million dollars to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (NNS dollars)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test230': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test230']['sents']['0']:
            print(return_dict['test230']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test230']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test230 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test230 Failed")
def test230():
    text="Arnor will contribute a million euros to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (NNS euros)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test231': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test231']['sents']['0']:
            print(return_dict['test231']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test231']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test231 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test231 Failed")
def test231():
    text="Arnor will contribute a million kroner to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP (DT a) (CD million) (NN kroner)        )          (PP           (TO to)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test232': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test232']['sents']['0']:
            print(return_dict['test232']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test232']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test232 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test232 Failed")
def test232():
    text="Arnor will contribute a million swiss francs to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (JJ swiss) (NNS francs)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test233': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test233']['sents']['0']:
            print(return_dict['test233']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test233']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test233 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test233 Failed")
def test233():
    text="Arnor will contribute a million golden goblin galleons to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP (DT a) (CD million) (JJ golden) (NN goblin) (NNS galleons)        )          (PP           (TO to)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test234': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test234']['sents']['0']:
            print(return_dict['test234']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test234']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test234 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test234 Failed")
def test234():
    text="Arnor will contribute a million goblin galleons to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP (DT a) (CD million) (NN goblin) (NNS galleons)        )          (PP           (TO to)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test235': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test235']['sents']['0']:
            print(return_dict['test235']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ " + str(return_dict['test235']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ noevent \n " )
            print("test235 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ noeventexception \n " )
        print("test235 Failed")
def test235():
    text="Arnor will contribute a million golden galleons to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (JJ golden) (NNS galleons)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test236': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test236']['sents']['0']:
            print(return_dict['test236']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ " + str(return_dict['test236']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ noevent \n " )
            print("test236 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"070\")~ noeventexception \n " )
        print("test236 Failed")
def test236():
    text="Bree Prime Minister Romendacil clashed over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (VBD clashed)      (PP (IN over)  (NP          (NP (DT the) (NNS efforts)        )          (PP (IN of)  (NP (NNP Eriadori)      ) ) )    )  (S        (VP         (TO to)          (VP           (VB deal)            (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)            )          )            (PP (IN during)  (NP                (NP (DT a) (JJ brief) (JJ private) (NN visit)              )                (PP                 (TO to)  (NP (NNP Eriador)            ) ) )          )            (PP             (VBG starting)              (PP (IN on)  (NP (NNP Sunday)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test237': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"121\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test237']['sents']['0']:
            print(return_dict['test237']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"121\")~ " + str(return_dict['test237']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"121\")~ noevent \n " )
            print("test237 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"121\")~ noeventexception \n " )
        print("test237 Failed")
def test237():
    text="Bree Prime Minister Romendacil didn't clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (VBD did) (RB n't)      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test238': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test238']['sents']['0']:
            print(return_dict['test238']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ " + str(return_dict['test238']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noevent \n " )
            print("test238 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noeventexception \n " )
        print("test238 Failed")
def test238():
    text="Bree Prime Minister Romendacil will not clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (MD will) (RB not)      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test239': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test239']['sents']['0']:
            print(return_dict['test239']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ " + str(return_dict['test239']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noevent \n " )
            print("test239 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noeventexception \n " )
        print("test239 Failed")
def test239():
    text="Bree Prime Minister Romendacil will not ever clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (MD will) (RB not)  (ADVP       (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test240': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test240']['sents']['0']:
            print(return_dict['test240']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ " + str(return_dict['test240']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noevent \n " )
            print("test240 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noeventexception \n " )
        print("test240 Failed")
def test240():
    text="Bree Prime Minister Romendacil can't ever clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (MD ca) (RB n't)  (ADVP       (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test241': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test241']['sents']['0']:
            print(return_dict['test241']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ " + str(return_dict['test241']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noevent \n " )
            print("test241 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noeventexception \n " )
        print("test241 Failed")
def test241():
    text="Bree Prime Minister Romendacil unexpectedly won't clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RB unexpectedly)  )    (VP     (MD wo) (RB n't)      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test242': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test242']['sents']['0']:
            print(return_dict['test242']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ " + str(return_dict['test242']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ noevent \n " )
            print("test242 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ noeventexception \n " )
        print("test242 Failed")
def test242():
    text="Bree Prime Minister Romendacil most certainly really did not clash over the efforts of Eriadori  to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RBS most) (RB certainly)  )  (ADVP     (RB really)  )    (VP     (VBD did) (RB not)      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test243': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test243']['sents']['0']:
            print(return_dict['test243']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ " + str(return_dict['test243']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noevent \n " )
            print("test243 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noeventexception \n " )
        print("test243 Failed")
def test243():
    text="Bree Prime Minister Romendacil didn't clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )    (VP     (VBD did) (RB n't)      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test244': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test244']['sents']['0']:
            print(return_dict['test244']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ " + str(return_dict['test244']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noevent \n " )
            print("test244 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"904\")~ noeventexception \n " )
        print("test244 Failed")
def test244():
    text="Arnor will contribute a million yum yennyen to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP (DT a) (CD million) (NN yum) (NN yennyen)        )          (PP           (TO to)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test245': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test245']['sents']['0']:
            print(return_dict['test245']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test245']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test245 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test245 Failed")
def test245():
    text="Arnor will contribute a million austrian florin to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP (DT a)  (ADJP               (CD million) (JJ austrian)            )  (NN florin)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test246': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test246']['sents']['0']:
            print(return_dict['test246']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test246']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test246 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test246 Failed")
def test246():
    text="Arnor will contribute a million austrian gold florin to Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB contribute)  (NP            (NP              (QP               (DT a) (CD million)            )  (JJ austrian) (NN gold) (NN florin)          )            (PP             (TO to)  (NP (NNP Gondor)          ) )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test247': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test247']['sents']['0']:
            print(return_dict['test247']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ " + str(return_dict['test247']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noevent \n " )
            print("test247 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noeventexception \n " )
        print("test247 Failed")
def test247():
    text="Arnor will adopt a resolution with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB adopt)  (NP (DT a) (NN resolution)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test248': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"102\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test248']['sents']['0']:
            print(return_dict['test248']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"102\")~ " + str(return_dict['test248']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"102\")~ noevent \n " )
            print("test248 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"102\")~ noeventexception \n " )
        print("test248 Failed")
def test248():
    text="Arnor will adopt a set of resolutions with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB adopt)  (NP            (NP (DT a) (NN set)          )            (PP (IN of)  (NP (NNS resolutions)          ) )        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test249': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test249']['sents']['0']:
            print(return_dict['test249']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ " + str(return_dict['test249']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ noevent \n " )
            print("test249 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"081\")~ noeventexception \n " )
        print("test249 Failed")
def test249():
    text="Arnor will adopt a revolution with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB adopt)  (NP (DT a) (NN revolution)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test250': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test250']['sents']['0']:
            print(return_dict['test250']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ " + str(return_dict['test250']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ noevent \n " )
            print("test250 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ noeventexception \n " )
        print("test250 Failed")
def test250():
    text="Arnor will adopt a revolutionary manifesto with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB adopt)  (NP (DT a) (JJ revolutionary) (NN manifesto)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test251': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test251']['sents']['0']:
            print(return_dict['test251']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ " + str(return_dict['test251']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ noevent \n " )
            print("test251 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"802\")~ noeventexception \n " )
        print("test251 Failed")
def test251():
    text="Arnor will abandon new economic relations with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ new) (JJ economic) (NNS relations)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test252': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test252']['sents']['0']:
            print(return_dict['test252']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ " + str(return_dict['test252']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noevent \n " )
            print("test252 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"903\")~ noeventexception \n " )
        print("test252 Failed")
def test252():
    text="Arnor will abandon new global economic relations with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ new) (JJ global) (JJ economic) (NNS relations)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test253': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test253']['sents']['0']:
            print(return_dict['test253']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ " + str(return_dict['test253']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noevent \n " )
            print("test253 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test253 Failed")
def test253():
    text="Arnor will abandon new global economic trade relations with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ new) (JJ global) (JJ economic) (NN trade) (NNS relations)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test254': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test254']['sents']['0']:
            print(return_dict['test254']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ " + str(return_dict['test254']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noevent \n " )
            print("test254 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"345\")~ noeventexception \n " )
        print("test254 Failed")
def test254():
    text="Arnor will abandon improved economic relations with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ improved) (JJ economic) (NNS relations)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test255': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test255']['sents']['0']:
            print(return_dict['test255']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ " + str(return_dict['test255']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noevent \n " )
            print("test255 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noeventexception \n " )
        print("test255 Failed")
def test255():
    text="Arnor will abandon improved global economic relations with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (S      (NP (NNP Arnor)    )      (VP       (MD will)        (VP         (VB abandon)  (NP           (JJ improved) (JJ global) (JJ economic) (NNS relations)        )          (PP (IN with)  (NP (NNP Gondor)          )        )          (SBAR            (NP             (RB almost) (CD five) (NNS years)          )  (IN after)  (S              (NP (NNS crowds)            )              (VP               (VBD trashed)  (NP                 (PRP$ its) (NN embassy)          ) ) )      ) )    )  )  (, ,)  (NP (DT a) (JJ senior) (NN official)  )    (VP     (VBD said)      (PP (IN on)  (NP (NNP Saturday)    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test256': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test256']['sents']['0']:
            print(return_dict['test256']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ " + str(return_dict['test256']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noevent \n " )
            print("test256 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"904\")~ noeventexception \n " )
        print("test256 Failed")
def test256():
    text="Bree Prime Minister Romendacil unexpectedly now won't try to clash over the efforts of Eriadori to deal with an orc infestation during a brief private trip to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RB unexpectedly)  )  (ADVP     (RB now)  )    (VP     (MD wo) (RB n't)      (VP       (VB try)  (S          (VP           (TO to)            (VP             (VB clash)              (PP (IN over)  (NP                  (NP (DT the) (NNS efforts)                )                  (PP (IN of)  (NP (NNP Eriadori)              ) ) )            )  (S                (VP                 (TO to)                  (VP                   (VB deal)                    (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)                    )                  )                    (PP (IN during)  (NP                        (NP (DT a) (JJ brief) (JJ private) (NN trip)                      )                        (PP                         (TO to)  (NP (NNP Eriador)                    ) ) )                ) )                ) ) )        )      )        (PP         (VBG starting)          (PP (IN on)  (NP (NNP Sunday)      ) ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test257': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test257']['sents']['0']:
            print(return_dict['test257']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ " + str(return_dict['test257']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ noevent \n " )
            print("test257 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"906\")~ noeventexception \n " )
        print("test257 Failed")
def test257():
    text="Bree Prime Minister Romendacil most certainly won't ever clash over the efforts of Eriadori  to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RBS most) (RB certainly)  )    (VP     (MD wo) (RB n't)  (ADVP       (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test258': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test258']['sents']['0']:
            print(return_dict['test258']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ " + str(return_dict['test258']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ noevent \n " )
            print("test258 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ noeventexception \n " )
        print("test258 Failed")
def test258():
    text="Bree Prime Minister Romendacil most certainly really did not ever clash over the efforts of Eriadori  to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RBS most) (RB certainly)  )  (ADVP     (RB really)  )    (VP     (VBD did) (RB not)  (ADVP       (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test259': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test259']['sents']['0']:
            print(return_dict['test259']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ " + str(return_dict['test259']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ noevent \n " )
            print("test259 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"907\")~ noeventexception \n " )
        print("test259 Failed")
def test259():
    text="Bree Prime Minister Romendacil most certainly really did not even ever clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RBS most) (RB certainly)  )  (ADVP     (RB really)  )    (VP     (VBD did) (RB not)  (ADVP       (RB even) (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test260': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test260']['sents']['0']:
            print(return_dict['test260']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ " + str(return_dict['test260']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noevent \n " )
            print("test260 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noeventexception \n " )
        print("test260 Failed")
def test260():
    text="Bree Prime Minister Romendacil most certainly really won't even ever clash over the efforts of Eriadori to deal with an orc infestation during a brief private visit to Eriador starting on Sunday. "
    parse="(ROOT (S   (NP (NNP Bree) (NNP Prime) (NNP Minister) (NNP Romendacil)  )  (ADVP     (RBS most) (RB certainly)  )  (ADVP     (RB really)  )    (VP     (MD wo) (RB n't)  (ADVP       (RB even) (RB ever)    )      (VP       (VB clash)        (PP (IN over)  (NP            (NP (DT the) (NNS efforts)          )            (PP (IN of)  (NP (NNP Eriadori)        ) ) )      )  (S          (VP           (TO to)            (VP             (VB deal)              (PP (IN with)  (NP (DT an) (NN orc) (NN infestation)              )            )              (PP (IN during)  (NP                  (NP (DT a) (JJ brief) (JJ private) (NN visit)                )                  (PP                   (TO to)  (NP (NNP Eriador)              ) ) )            )              (PP               (VBG starting)                (PP (IN on)  (NP (NNP Sunday)            ) ) )        ) )      )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test261': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950111'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test261']['sents']['0']:
            print(return_dict['test261']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ " + str(return_dict['test261']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noevent \n " )
            print("test261 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"BREGOV\", u\"ERI\", u\"905\")~ noeventexception \n " )
        print("test261 Failed")
def test261():
    text="Calenardhon welcomed memos from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP (NNS memos)    )      (PP (IN from)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test262': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test262']['sents']['0']:
            print(return_dict['test262']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ " + str(return_dict['test262']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noevent \n " )
            print("test262 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noeventexception \n " )
        print("test262 Failed")
def test262():
    text="Calenardhon welcomed economic memos from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP       (JJ economic) (NNS memos)    )      (PP (IN from)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test263': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test263']['sents']['0']:
            print(return_dict['test263']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ " + str(return_dict['test263']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ noevent \n " )
            print("test263 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ noeventexception \n " )
        print("test263 Failed")
def test263():
    text="Calenardhon welcomed economic rumors about Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP       (JJ economic) (NNS rumors)    )      (PP (IN about)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test264': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test264']['sents']['0']:
            print(return_dict['test264']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ " + str(return_dict['test264']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ noevent \n " )
            print("test264 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ noeventexception \n " )
        print("test264 Failed")
def test264():
    text="Calenardhon welcomed economic memos not about Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP       (JJ economic) (NNS memos)    )      (PP       (RB not) (IN about)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test265': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test265']['sents']['0']:
            print(return_dict['test265']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ " + str(return_dict['test265']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ noevent \n " )
            print("test265 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"915\")~ noeventexception \n " )
        print("test265 Failed")
def test265():
    text="Calenardhon welcomed cultural memos sent by Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP        (NP         (JJ cultural) (NNS memos)      )        (VP         (VBN sent)          (PP (IN by)  (NP (NNP Bree)          )        )          (PP (IN on)  (NP             (PRP$ its) (NN role)          )        )          (PP (IN for)            (PP (IN in)  (NP               (JJ forthcoming) (NN peace) (NNS talks)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test266': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"912\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test266']['sents']['0']:
            print(return_dict['test266']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"912\")~ " + str(return_dict['test266']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"912\")~ noevent \n " )
            print("test266 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"912\")~ noeventexception \n " )
        print("test266 Failed")
def test266():
    text="Calenardhon welcomed cultural secret memos sent by Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP        (NP         (JJ cultural) (JJ secret) (NNS memos)      )        (VP         (VBN sent)          (PP (IN by)  (NP (NNP Bree)          )        )          (PP (IN on)  (NP             (PRP$ its) (NN role)          )        )          (PP (IN for)            (PP (IN in)  (NP               (JJ forthcoming) (NN peace) (NNS talks)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test267': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test267']['sents']['0']:
            print(return_dict['test267']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ " + str(return_dict['test267']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noevent \n " )
            print("test267 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noeventexception \n " )
        print("test267 Failed")
def test267():
    text="Calenardhon welcomed memos on economic issue from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP (NNS memos)    )      (PP (IN on)  (NP         (JJ economic) (NN issue)      )    )      (PP (IN from)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test268': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test268']['sents']['0']:
            print(return_dict['test268']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ " + str(return_dict['test268']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ noevent \n " )
            print("test268 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"911\")~ noeventexception \n " )
        print("test268 Failed")
def test268():
    text="Calenardhon welcomed cultural internal memos from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP       (JJ cultural) (JJ internal) (NNS memos)    )      (PP (IN from)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test269': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test269']['sents']['0']:
            print(return_dict['test269']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ " + str(return_dict['test269']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noevent \n " )
            print("test269 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"041\")~ noeventexception \n " )
        print("test269 Failed")
def test269():
    text="Calenardhon welcomed cultural internal assurances sent by Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP        (NP         (JJ cultural) (JJ internal) (NNS assurances)      )        (VP         (VBN sent)          (PP (IN by)  (NP (NNP Bree)          )        )          (PP (IN on)  (NP             (PRP$ its) (NN role)          )        )          (PP (IN for)            (PP (IN in)  (NP               (JJ forthcoming) (NN peace) (NNS talks)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test270': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"914\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test270']['sents']['0']:
            print(return_dict['test270']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"914\")~ " + str(return_dict['test270']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"914\")~ noevent \n " )
            print("test270 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"914\")~ noeventexception \n " )
        print("test270 Failed")
def test270():
    text="Calenardhon welcomed assurances on cultural issues from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S   (NP (NN Calenardhon)  )    (VP     (VBD welcomed)  (NP (NNS assurances)    )      (PP (IN on)  (NP         (JJ cultural) (NNS issues)      )    )      (PP (IN from)  (NP          (NP (NNP Bree)        )          (PP (IN on)  (NP             (PRP$ its) (NN role)      ) ) )    )      (PP (IN for)        (PP (IN in)  (NP           (JJ forthcoming) (NN peace) (NNS talks)    ) ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test271': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test271']['sents']['0']:
            print(return_dict['test271']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ " + str(return_dict['test271']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ noevent \n " )
            print("test271 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ noeventexception \n " )
        print("test271 Failed")
def test271():
    text="Calenardhon welcomed assurances on cultural issues sent from Bree on its role for in forthcoming peace talks. "
    parse="(ROOT (S (NP (NN Calenardhon))  (VP (VBD welcomed)  (NP (NNS assurances)    )      (PP (IN on)  (NP          (NP           (JJ cultural) (NNS issues)        )          (VP           (VBN sent)            (PP (IN from)  (NP (NNP Bree)            )          )            (PP (IN on)  (NP               (PRP$ its) (NN role)            )          )            (PP (IN for)              (PP (IN in)  (NP                 (JJ forthcoming) (NN peace) (NNS talks)          ) ) )      ) )    )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test272': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950118'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test272']['sents']['0']:
            print(return_dict['test272']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ " + str(return_dict['test272']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ noevent \n " )
            print("test272 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"CAL\", u\"BRE\", u\"913\")~ noeventexception \n " )
        print("test272 Failed")
def test272():
    text="Arnor is inching nearer to accord with Gondor almost five years after crowds trashed its embassy, a senior official said on Saturday. "
    parse="(ROOT (S   (NP (NNP Arnor)  )    (VP     (VBZ is)      (VP       (VBG inching)  (S          (SBAR           (IN nearer)  (S              (VP               (TO to)                (VP                 (VB accord)                  (PP (IN with)  (NP (NNP Gondor)                  )                )                  (SBAR                    (NP                     (RB almost) (CD five) (NNS years)                  )  (IN after)  (S                      (NP (NNS crowds)                    )                      (VP                       (VBD trashed)  (NP                         (PRP$ its) (NN embassy)                  ) ) )              ) )            )          )        )  (, ,)  (NP (DT a) (JJ senior) (NN official)        )          (VP           (VBD said)            (PP (IN on)  (NP (NNP Saturday)        ) ) )    ) )  )  (. .)) )"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test273': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950101'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"083\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test273']['sents']['0']:
            print(return_dict['test273']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"083\")~ " + str(return_dict['test273']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"083\")~ noevent \n " )
            print("test273 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"ARN\", u\"GON\", u\"083\")~ noeventexception \n " )
        print("test273 Failed")
def test273():
    text="Russian police arrested Russian students in Moscow today."
    parse="(ROOT (S (NP (JJ Russian) (NN police)) (VP (VBD arrested) (NP (JJ Russian) (NNS students)) (PP (IN in) (NP (NNP Moscow))) (NP-TMP (NN today))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test274': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"RUSEDU\", u\"212\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test274']['sents']['0']:
            print(return_dict['test274']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"RUSEDU\", u\"212\")~ " + str(return_dict['test274']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"RUSEDU\", u\"212\")~ noevent \n " )
            print("test274 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"RUSEDU\", u\"212\")~ noeventexception \n " )
        print("test274 Failed")
def test274():
    text="Russian police arrested students in Moscow today."
    parse="(ROOT (S (NP (JJ Russian) (NN police)) (VP (VBD arrested) (NP (NNS students)) (PP (IN in) (NP (NNP Moscow))) (NP-TMP (NN today))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test275': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"---EDU\", u\"212\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test275']['sents']['0']:
            print(return_dict['test275']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"---EDU\", u\"212\")~ " + str(return_dict['test275']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"---EDU\", u\"212\")~ noevent \n " )
            print("test275 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"RUSCOP\", u\"---EDU\", u\"212\")~ noeventexception \n " )
        print("test275 Failed")
def test275():
    text="The International Criminal Court is about to restore full diplomatic ties with Gondor almost five years after crowds trashed its embassy."
    parse="(ROOT (S (NP (DT The) (NNP International) (NNP Criminal) (NNP Police) (NNP Organization)) (VP (VBZ is) (VP (IN about) (S (VP (TO to) (VP (VB restore) (NP (JJ full) (JJ diplomatic) (NNS ties)) (PP (IN with) (NP (NNP Gondor))) (SBAR (NP (RB almost) (CD five) (NNS years)) (IN after) (S (NP (NNS crowds)) (VP (VBD trashed) (NP (PRP$ its) (NN embassy)))))))))) (. .)))"
    parsed = utilities._format_parsed_str(parse)
    dict = {u'test276': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},
   		u'meta': {u'date': u'19950104'}}}
    return_dict = "" 
    try: 
        return_dict = petrarch2.do_coding(dict)
    except Exception as e: 
        fout_report.write(text +"~"+ parsed +"~ (u\"IGOCOPITP\", u\"GON\", u\"064\")~ Petrarch Runtime Error "+ str(e) +"\n " )
    try:
        if 'events' in return_dict['test276']['sents']['0']:
            print(return_dict['test276']['sents']['0']['events'])
            fout_report.write(text +"~"+ parsed +"~ (u\"IGOCOPITP\", u\"GON\", u\"064\")~ " + str(return_dict['test276']['sents']['0']['events']) + "\n")
        else:
            fout_report.write(text +"~"+ parsed +"~ (u\"IGOCOPITP\", u\"GON\", u\"064\")~ noevent \n " )
            print("test276 Failed")
    except:
        #fout_report.write(text +"~"+ parsed +"~ (u\"IGOCOPITP\", u\"GON\", u\"064\")~ noeventexception \n " )
        print("test276 Failed")
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
test274()
test275()

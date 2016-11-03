import sys

#Test Suite builder

fout = open("test_script.py","w") #opens file with name of "test_script.py"

tfuncnum = 1
date=""
id = "" 
category = ""
sentence = ""
eventcode = ""
textflag = 0
parseflag = 0
text = ""
parse=""

def check_line(line):
	global tfuncnum, date,id,category,sentence,eventcode,textflag,parseflag,text,parse
	sentence_tag = line.find("<Sentence ")
	eventcode_tag = line.find("<EventCoding ")
	text_tag_start = line.find("<Text>")
	text_tag_end = line.find("</Text>")
	parse_tag_start = line.find("<Parse>")
	parse_tag_end = line.find("</Parse>")
	
	line = line.replace("\n","")
	line = line.replace("\r","")
	
	
	if parse_tag_end != -1:
		parseflag = 0
		eventcode = eventcode.replace("'","\\\"")
		fout.write("\"\n")
		# Write other lines
		fout.write("    parsed = utilities._format_parsed_str(parse)\n")
		#	print("#######\n")
		#fout.write("#    print(parse)\n")
		#fout.write("#    print(parsed)\n")
		#	print("#######")
		fout.write("    dict = {u'test"+str(tfuncnum)+"': {u'sents': {u'0': {u'content': text, u'parsed': parsed}},\n")
		fout.write("   		u'meta': {u'date': u'"+date+"'}}}\n")

		fout.write("    return_dict = \"\" \n")
		fout.write("    try: \n")
		fout.write("        return_dict = petrarch2.do_coding(dict)\n")
		fout.write("    except Exception as e: \n")
		fout.write("        fout_report.write(text +\"~\"+ parsed +\"~ "+ eventcode + "~ Petrarch Runtime Error \"+ str(e) +\"\\n \" )\n")
		#fout.write("#    print(return_dict)\n")

		functionname = "test"+str(tfuncnum)
		fout.write("    try:\n")
		fout.write("        if 'events' in return_dict['test"+str(tfuncnum)+"']['sents']['0']:\n")
		fout.write("            print(return_dict['test"+str(tfuncnum)+"']['sents']['0']['events'])\n")
		#write report to file
		fout.write("            fout_report.write(text +\"~\"+ parsed +\"~ "+ eventcode + "~ \" + str(return_dict['"+functionname+"']['sents']['0']['events']) + \"\\n\")\n")
		#fout.write("#           assert return_dict['test"+str(tfuncnum)+"']['sents']['0']['events'] == ["+eventcode+"]\n")
		fout.write("        else:\n")
		fout.write("            fout_report.write(text +\"~\"+ parsed +\"~ "+ eventcode + "~ noevent \\n \" )\n")
		fout.write("            print(\"test"+str(tfuncnum)+" Failed\")\n")
		fout.write("    except:\n")
		fout.write("        fout_report.write(text +\"~\"+ parsed +\"~ "+ eventcode + "~ noeventexception \\n \" )\n")
		fout.write("        print(\"test"+str(tfuncnum)+" Failed\")\n")
		eventcode = ""
		text=""
		parse=""
	#print("result")
	#print(return_dict['test123']['sents']['0']['events'])
	#assert return_dict['test123']['sents']['0']['events'] == [(u'DEU', u'FRA', u'173')]
	
	
	
	if text_tag_end != -1:
		textflag = 0
		fout.write("\"\n")
		
	if textflag == 1:
		text = text + line
		fout.write("" + line)
	elif parseflag == 1:
		parse = parse + line
		fout.write("" + line)
	elif sentence_tag != -1:
		print("Sentence tag found")
		fout.write("def test"+ str(tfuncnum) +"():\n")
		tfuncnum = tfuncnum + 1
		
		#Find Date
		date_tag = line.find("date=\"")
		line = line[date_tag+6:]
		pos = line.find("\"")
		date = line[:pos]
		line = line[pos+1:]
		print("Date="+date)
		#print(line)
		#Find id
		id_tag = line.find("id=\"")
		line = line[id_tag+4:]
		pos = line.find("\"")
		id = line[:pos]
		line = line[pos+1:]
		print("ID="+id)
		#print(line)
		#Find category
		category_tag = line.find("category=\"")
		line = line[category_tag+10:]
		pos = line.find("\"")
		category = line[:pos]
		line = line[pos+1:]
		print("Category="+category)
		#print(line)
		#Find sentence
		sentence_tag = line.find("sentence=\"")
		line = line[sentence_tag+10:]
		pos = line.find("\"")
		sentence = line[:pos]
		line = line[pos+1:]
		print("Sentence="+sentence)
		#print(line)
		
	elif eventcode_tag != -1:
		print("Event Code Found")
		#Check if noevent sentence
		noevent_tag = line.find("noevents = ")
		if noevent_tag != -1:
		    eventcode = "No Event"
		else:
		    #Find sourcecode
		    sourcecode_tag = line.find("sourcecode=")
		    line = line[sourcecode_tag+12:]
		    pos = line.find("\"")
		    sourcecode = line[:pos]
		    line = line[pos+1:]
		    print("sourcecode="+sourcecode)
		    #print(line)
		    #Find targetcode
		    targetcode_tag = line.find("targetcode=")
		    line = line[targetcode_tag+12:]
		    pos = line.find("\"")
		    targetcode = line[:pos]
		    line = line[pos+1:]
		    print("targetcode="+targetcode)
		    #print(line)
		    #Find eventcode
		    eventcode_tag = line.find("eventcode=")
		    line = line[eventcode_tag+11:]
		    pos = line.find("\"")
		    ecode = line[:pos]
		    line = line[pos+1:]
		    print("eventcode="+ecode)
		    #print(line)
		    if eventcode == "":
			    eventcode = "(u'"+sourcecode+"', u'"+targetcode+"', u'"+ecode+"')"
		    else:
			    eventcode = eventcode + ",(u'"+sourcecode+"', u'"+targetcode+"', u'"+ecode+"')"
		    print(eventcode)
	
	if parse_tag_start != -1:
		parseflag = 1
		fout.write("    parse=\"")	
	
	if text_tag_start != -1:
		textflag = 1
		fout.write("    text=\"")
		
def write_header():
    fout.write("#! /usr/bin/env python \n")
    fout.write("# -*- coding: utf-8 -*- \n")
    fout.write("import petrarch2, PETRglobals, PETRreader, utilities, codecs\n\n")
    fout.write("config = utilities._get_data('data/config/', 'PETR_config.ini')\n")
    fout.write("print(\"reading config\")\n")
    fout.write("PETRreader.parse_Config(config)\n")
    fout.write("print(\"reading dicts\")\n")
    fout.write("petrarch2.read_dictionaries()\n")
    fout.write("fout_report = codecs.open(\"test_report.txt\",\"w\",encoding='utf8') #opens test report file for writing\n");
    fout.write("fout_report.write(\"Text~ Parse Tree~ Expected Encoding as per Petrarch~ Result from Petrarch2\\n\")\n")
	
# ========================== PRIMARY CODING FUNCTIONS ====================== #
# Write the header code to file
write_header()

# Get the Input XML
input_xml = sys.argv[1]

# Read through each line of XML
# Things to parse from the XML File ->
# date, ID, category, sentence, Event Coding, Text and Parse Tree
for line in open('test.xml','r').readlines():
    #Check the line and decode text
	check_line(line)

	
for x in range(1, tfuncnum):
    fout.write("test"+str(x)+"()\n")

fout.close()	
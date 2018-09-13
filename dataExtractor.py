import re;
import sys;

f = open("usb256.001", "r");
o = open("dataExtracted.txt", "w");
rawData = f.read();

list_email = re.findall(r"\b[a-z/A-Z/0-9/_/.]+@[a-z/A-Z/-/0-9]+\.[a-z/A-Z/-/0-9]+\.?[a-z/A-Z/-/0-9]+?\.?[a-z/A-Z/-/0-9]+?\b",rawData);
list_phoneNum1 = re.findall(r"\([\d][\d][\d]\)[-/./\s][\d][\d][\d][-/./\s][\d][\d][\d][\d]", rawData);
list_phoneNum2 = re.findall(r"\b[\d][\d][\d][-/./\s][\d][\d][\d][-/./\s][\d][\d][\d][\d]\b", rawData);
list_phoneNum = list_phoneNum1 + list_phoneNum2;

x = len(list_email); 
y = len(list_phoneNum);

def only_emails():
	o.write("total emails: ");
	o.write(str(x));
	o.write("\n");

	for i in list_email:
		o.write(i);
		o.write("\n");


def only_phne():
	o.write("total phone numbers:");
	o.write(str(y));
	o.write("\n");

	for i in list_phoneNum:
		o.write(i);
		o.write("\n");


if sys.argv[1] == "-emails":
	only_emails();
	

elif sys.argv[1] == "-phonenumbers":
	only_phne();

	
elif sys.argv[1] == "-emails" and sys.argv[2]== "-phonenumbers":
	only_emails();
	only_phne();


elif sys.argv[1] == "-phonenumbers" and sys.argv[2]== "-emails":
	only_emails();
	only_phne();


#only_emails();
#only_phne();
f.close();
o.close();






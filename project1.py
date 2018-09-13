import re;
fp = open("usb256.001",'r');
op = open("output.txt", 'w');
f = fp.read();
def email_number(email_pattern1, f1):
	re.compile(email_pattern1, f1);

def phone_number(reg1, f1):
	re.compile(reg1, f1);
email_pattern = "[\w0-9\._]+@[\w]+\.[\w]+\.[\w]+";
reg = "[\d]{3}[-.\s][\d]{3}[-.\s][\d]{4}";
a = email_number(email_pattern,f);
b = phone_number(reg, f);


def print_email():
	for x in a:
		op.write(x);
		op.write("\n");


def print_phonenumbers():
	for x in b:
		op.write(x);
		op.write("\n");


fp.close();
op.close();
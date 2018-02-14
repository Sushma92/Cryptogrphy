#include<conio.h>
#include <string>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	int count = 0;
	ifstream infile;
	ofstream outfile;
	string alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string key = "deceptive";

	//int ct[1000];
	int i, j, k;

	string text = "";

	infile.open("a.txt");
	string justText = "";
	if (infile.is_open())
	{
		while (getline(infile, text))
		{
			for (int i = 0; i < text.length(); i++)
			{
				text[i] = toupper(text[i]);
				if (text[i] >= 'A' && text[i] <= 'Z')
					justText += text[i];
			}
		}
	}
	infile.close();

	int t = justText.size();
	int y = key.length();
		
	string subkey;
	
	subkey = key;
	int s = subkey.length();
	cout << "s: " << s <<"t: " << t<< '\n';
	int x = 0;
	while ( s < t)
	{
		subkey += justText[x];
		x++;
		s = subkey.length();
	}
	
	cout << subkey << '\n';
	
	
	
	string cipherText = "";

	for (i = 0; i < t; i++)
	{
		subkey[i] = toupper(subkey[i]);
		int textIndex = alphabets.find(justText.at(i));
		int keyIndex = alphabets.find(subkey.at(i));
		int total = (textIndex + keyIndex) % 26;
		cipherText += alphabets.at(total);
	}

	cout << "cipher text: " << cipherText << '\n';
	
	outfile.open("b.txt");
	outfile << cipherText;	
	outfile.close();

	return 0;
}

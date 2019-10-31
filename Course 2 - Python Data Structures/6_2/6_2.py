text = "X-DSPAM-Confidence:    0.8475";

spacepos = text.find('0')
endpos = text.find('5',spacepos)

num = text[spacepos:endpos+1]
print(float(num))

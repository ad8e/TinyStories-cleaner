import random
import json
import glob
import pickle

# this freezes my computer. let's load 1 at a time instead
# data = list()
# for file in glob.glob("TinyStories_all_data/*"):
# 	with open(file) as o:
# 		# print(type(json.load(o)))
# 		data.extend(json.load(o))

thrown_out = 0
def process_paragraph(par):
	global thrown_out
	par = par.strip()
	par = par.replace('\\', '')
	par = par.replace('  ', ' ')
	par = par.replace('–', '-')
	par = par.replace(' — ', ' - ')
	par = par.replace('—', ' - ')
	par = par.replace('…', '...')
	par = par.replace('“', '"')
	par = par.replace('”', '"')
	par = par.replace('’', '\'') # curly quotes. don't replace the opposite side: we want to cull them
	# in the future, we might try replacing 160 and 180. nah, it doesn't matter. we're only throwing out 1282 paragraphs
	# there's some grammar mistakes, like missing commas, and ?". which is double punctuation
	# "\ ", a space after a \
	for c in par:
		if ord(c) != 10 and (ord(c) > 127 or ord(c) < 32):
			thrown_out += 1
			# print("offending char:", ord(c), c)
			return ""
	return par

total_data = []
def clean(d):
	global total_data
	# print("generators:", set([i['source'] for i in d])) # it's only GPT-3.5 and GPT-4. no mistakes here
	d = [process_paragraph(i['story']) for i in d if i['source'] == 'GPT-4']
	d = [i for i in d if i != ''] # remove empty lines
	total_data += d

# for file in ["TinyStories_all_data/data00.json"]:
for file in glob.glob("TinyStories_all_data/*"):
	with open(file) as o:
		# print(type(json.load(o)))
		data = json.load(o)
		clean(data)

print("thrown out:", thrown_out)
print("total size:", len(total_data))
print(random.choice(total_data))
with open("cleaned_data.pkl", "wb") as file:
	pickle.dump(total_data, file)

import random
import json
import glob
import pickle
from collections import Counter

# this freezes my computer. let's load 1 at a time instead
# data = list()
# for file in glob.glob("TinyStories_all_data/*"):
# 	with open(file) as o:
# 		# print(type(json.load(o)))
# 		data.extend(json.load(o))

thrown_out = 0
def process_story(par):
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

	for c in par:
		if c == '|' or c == '<' or c == '/' or c == '`' or c == '*' or c == '=' or c == '_' or c == '&' or c == '@' or c == '~' or c == '#' or c == '%' or c == '[' or c == ']' or c == '+' or c == '(' or c == ')':
			# ` is usually as strange punctuation, or `` ''
			# / is for Tom/Lily stories, "he/she"
			# * is usually in *emphasis*, but often incorrect, or in *** separating parts of a story
			# $ is usually correct
			# & is as an abbrev, or &rsquo;s
			# ')': 199, '(': 194,
			# ~ is rare and not used well
			# # is wrong, hashtags and rarely as numbers
			# there's one mistake for % and the rest are ok. I decided to clean it anyway
			# [ is used wrong
			# _ is used poorly
			# = is sometimes used for addition but more often for mistakes
			# + is for addition, abbreviation, and A+. but has some mistakes
			# ( ) is about 80% correctly used
			thrown_out += 1
			# print("offending char:", ord(c), c, ":", par) #<i>, <End of Story>, <|im_start|>
			return ""

	if len(par) < 100:
		thrown_out += 1
		# if len(par) > 0:
		# 	print("too short:", par) # many empty stories or story fragments. some legitimate stories are deleted below 200
		return ""
	if par[-1] != '.' and par[-1] != '!' and par[-1] != '"' and par[-1] != '?':
		thrown_out += 1
		# print("offending char:", par[-1])
		# print(par)
		return ""

	return par

total_data = []
def clean(d):
	global total_data
	# print("generators:", set([i['source'] for i in d])) # it's only GPT-3.5 and GPT-4. no mistakes here
	d = [process_story(i['story']) for i in d if i['source'] == 'GPT-4']
	d = [i for i in d if i != ''] # remove empty lines
	total_data += d

# for file in ["TinyStories_all_data/data00.json"]:
for file in glob.glob("TinyStories_all_data/*"):
	with open(file) as o:
		# print(type(json.load(o)))
		data = json.load(o)
		clean(data)

print("thrown out:", thrown_out)
print("survived:", len(total_data))

# after some removals: Counter({' ': 426859449, 'e': 204912889, 'a': 150822107, 't': 139517558, 'o': 112349865, 'h': 105934005, 'n': 100530370, 'd': 95421243, 'i': 94879636, 's': 84200324, 'r': 75921863, 'l': 67910605, 'y': 51200735, 'm': 44606524, '.': 44303626, 'w': 43890889, 'u': 41336733, 'p': 33429250, 'g': 31785986, 'c': 30360697, 'b': 26834430, 'f': 24930515, ',': 23967379, 'k': 20172791, 'T': 20115680, '"': 12313202, 'v': 11770115, '\n': 9128807, 'S': 8571627, 'H': 6240920, 'I': 5084215, 'O': 4663978, "'": 4138731, 'L': 4092379, '!': 3870671, 'B': 3417017, 'x': 3397591, 'M': 3275768, 'A': 2511284, 'W': 1795287, 'j': 1644565, '?': 1400451, 'Y': 1313533, 'z': 1015289, 'J': 906218, 'F': 825037, 'D': 770337, 'C': 609437, 'q': 596899, 'N': 483349, 'E': 465002, 'K': 337323, 'P': 301036, 'G': 252938, 'R': 226506, '-': 193971, ':': 119893, 'Z': 67185, 'V': 42153, 'U': 31080, '3': 24147, ';': 11440, 'Q': 9834, 'X': 3447, '1': 3416, '0': 2392, '2': 1941, '5': 1672, '4': 770, '/': 472, '9': 433, '`': 366, '8': 356, '6': 317, '7': 273, ')': 199, '(': 194, '$': 155, '_': 102, '*': 88, '&': 44, '=': 43, '+': 27, '[': 18, ']': 18, '%': 13, '#': 9, '~': 5, '@': 2})
# c = Counter()
# for s in total_data:
# 	c += Counter(s)
# print(c)
print(random.choice(total_data))

with open("cleaned_data.pkl", "wb") as file:
	pickle.dump(total_data, file)

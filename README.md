# TinyStories-cleaner

TinyStories contains these characters: {'ó', '\xad', '\t', '❤', '¡', '(', '€', 'r', 'V', '把', 'T', '自', '\u3000', 'Z', '在', '恩', '\u2005', ';', '"', 'ā', '‘', '\u202a', 'p', 'â', '\u2009', '。', ')', '應', '了', '會', 'S', 'h', 'D', 'u', '兒', '剛', '5', 'd', '\ue000', 'İ', '/', 'ᴇ', '9', '¢', '’', '‑', 'è', '當', '\uf04a', 'É', '給', 'N', 'j', '米', '_', '\\', '…', '~', '‐', '―', '獨', '\u200e', 'ᴜ', '度', 'n', 'P', '�', 'a', 'O', 'ñ', '—', 'f', '🎓', '>', 'l', 'Y', 'ᴀ', 's', '\xa0', 'í', '\x92', 'G', '童', 'ғ', 'c', 'E', '7', '£', 'W', '兩', '\u2028', '!', '很', '興', '−', '留', 'á', 'K', 'ᴢ', 'F', '8', '們', '保', 'ʏ', '´', 'J', '但', '又', 'I', '奮', '$', '🤩', '4', '過', '她', '\u200c', '+', 'L', 'o', '3', '是', '🌴', '️', '個', '=', '0', 'b', 'ᴅ', 'q', '己', '·', '天', '#', 'ᴏ', 'A', '1', '他', '*', '莉', '─', '艾', 'R', 'ᴡ', '}', '難', 'U', 'X', '[', '和', '™', '»', ' ', '裡', 'y', 'à', ']', 'C', '?', '些', '整', '¿', '6', ':', '🍌', 'ᴄ', 'ᴛ', 'x', 'ɪ', 'm', 'g', '田', 'e', 'M', '„', ',', '\u200a', '°', '<', '\u2029', '{', '.', '”', '`', 'ö', '的', 'ß', "'", 'Q', 'ú', '%', '分', 'v', '–', 'і', 'ê', 'B', '“', '\ufeff', 'ʙ', 'i', 'z', '«', '@', '-', '一', 'ï', 't', 'w', '巴', '到', '玉', 'k', 'œ', '，', '‚', 'H', 'é', 'ʜ', '&', '§', '2', '\u200b', '這', '答', '高', '|', '時'}

This script coerces characters to the ASCII range when possible (like — and ”), and cleans up some whitespace.

It throws away stories with strange unicode characters.

It throws away stories <100 chars or ones that don't end in punctuation. These are mostly interrupted fragments, such as "Once upon a time, there", or simply empty stories.

It throws away the GPT-3.5 stories, which were described as "of lesser quality".

In total, 12039 stories are deleted, and 2733291 stories remain.

It throws away the metadata. If you need it, you'll need to change the script to preserve the metadata.

## Instructions

Download https://huggingface.co/datasets/roneneldan/TinyStories/blob/main/TinyStories_all_data.tar.gz. This is the right file; the others have problems.

Unzip it. Then run `prepare.py`. It'll produce a pickle file `cleaned_data.pkl`, containing a list of strings.

You can load the cleaned data using:

```
with open('cleaned_data.pkl', 'rb') as file:
	data_strings = pickle.load(file)
```
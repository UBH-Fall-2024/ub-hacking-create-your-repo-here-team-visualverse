import random
from nltk.corpus import wordnet as wn, words

import nltk
nltk.download('words')
nltk.download('wordnet')

# Load a general English word list for additional vocabulary
english_words = set(words.words())

# Vastly expanded seed words for arts and emotions
art_words = [
    "painting", "sculpture", "dance", "poetry", "theater", "music", "film",
    "photography", "literature", "drama", "opera", "design", "architecture",
    "drawing", "sketching", "ceramics", "fashion", "performance", "collage",
    "installation", "media", "animation", "printmaking", "exhibition", "gallery",
    "craft", "folk art", "modernism", "impressionism", "surrealism", "portrait",
    "landscape", "abstract", "graphic design", "illustration", "calligraphy",
    "mosaic", "street art", "graffiti", "carving", "digital art", "visual arts",
    "cinematography", "scriptwriting", "choreography", "composing", "orchestra",
    "pottery", "musical", "prose", "fine arts", "avant-garde", "expressionism",
    "realism", "cubism", "conceptual art", "expressionism", "baroque", "dadaism",
    "pop art", "renaissance", "romanticism", "neoclassicism", "futurism", "symbolism",
    "installation", "print", "still life", "sculpting", "impression", "etching",
    "mixed media", "urban art", "live performance", "gallery installation",
    # Adding new words related to other art fields
    "ballet", "jazz", "acrylic", "watercolor", "pottery", "folk", "animation",
    "improvisation", "ink", "scenography", "symphony", "scoring", "arrangement",
    "literary", "sonnet", "metaphor", "narrative", "allegory", "pastel",
    "fresco", "stanza", "chorus", "conductor", "orchestration", "scene"
]

emotion_words = [
    "joy", "anger", "fear", "love", "sadness", "hope", "happiness", "grief",
    "surprise", "disgust", "envy", "pride", "contentment", "anxiety",
    "compassion", "desire", "nostalgia", "frustration", "excitement",
    "affection", "tension", "tranquility", "confidence", "inspiration",
    "loneliness", "anticipation", "sorrow", "guilt", "shame", "melancholy",
    "boredom", "indifference", "euphoria", "ecstasy", "rage", "sympathy",
    "irritation", "resentment", "admiration", "awe", "gratitude", "relief",
    "tenderness", "self-esteem", "self-doubt", "motivation", "calmness",
    "apprehension", "satisfaction", "disappointment", "humiliation", "forgiveness",
    "hatred", "affection", "desperation", "insecurity", "empathy", "bitterness",
    "contentment", "vulnerability", "serenity", "compassion", "ecstasy", "remorse",
    "mourning", "relaxation", "sensitivity", "romanticism", "friendship", "affection",
    "jealousy", "arousal", "optimism", "faith", "regret", "obsession", "desperation",
    # New words related to complex emotions
    "resentment", "irritation", "joyfulness", "melancholia", "abandonment",
    "elation", "pity", "enlightenment", "foreboding", "calm", "reluctance",
    "jealousy", "appreciation", "patience", "distrust", "tolerance", "apathy",
    "compassion", "cynicism", "endearment", "repentance", "optimism"
]

# Function to get related words (synonyms, antonyms, hypernyms, hyponyms, entailments, causes, attributes, similar-to)
def get_related_words(word):
    related_words = set()
    for syn in wn.synsets(word):
        # Add synonyms and antonyms
        for lemma in syn.lemmas():
            related_words.add(lemma.name().replace('_', ' '))
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    related_words.add(ant.name().replace('_', ' '))
        # Add hypernyms, hyponyms, and additional relationships
        for related_syn in syn.hypernyms() + syn.hyponyms() + syn.entailments() + syn.causes() + syn.attributes() + syn.similar_tos():
            for lemma in related_syn.lemmas():
                related_words.add(lemma.name().replace('_', ' '))
    return related_words

# Collect words by category
art_related_words = set()
emotion_related_words = set()
other_words = set()

# Expand art-related and emotion-related words
for word in art_words:
    art_related_words.update(get_related_words(word))
for word in emotion_words:
    emotion_related_words.update(get_related_words(word))

# Add general English words and separate into categories
for word in english_words:
    if word in art_related_words:
        art_related_words.add(word)
    elif word in emotion_related_words:
        emotion_related_words.add(word)
    else:
        other_words.add(word)

# Combine all unique words and sample if necessary
all_words = art_related_words | emotion_related_words | other_words
if len(all_words) > 1000000:
    final_word_list = random.sample(all_words, 1000000)
else:
    final_word_list = list(all_words)

art_related_list = list(art_related_words)
emotion_related_list = list(emotion_related_words)
other_words_list = list(other_words)

print(art_related_list[:10])
print(emotion_related_list[:10])
print(other_words_list[:10])
descriptions = [
    "a beautiful landscape with serene vibes",
    "a joyful and lively scene",
    "a dark and mysterious setting",
        "a calm and peaceful image",
        "a dynamic and action-filled scene",
        "a warm and comforting environment",
        "an intense and dramatic composition",
        "a cheerful and bright scene",
        "a nostalgic and emotional photo",
        "a relaxing and tranquil place",
        "a flower photo",
        "joyful", "melancholic", "peaceful", "angry", "romantic", "serene", "hopeful",
        "anxious", "nostalgic", "dramatic", "surreal", "inspired", "mysterious",
        "playful", "euphoric", "dismal", "graceful", "calm", "fearful", "intense",
        "dreamy", "passionate", "somber", "mournful", "whimsical", "exhilarated",
        "Art Nouveau",
        "Fauvism",
        "Neoclassicism",
        "Symbolism",
        "Dadaism",
        "Realism",
        "Art Deco",
        "Minimalism",
        "Futurism",
        "Conceptual Art",
        "Op Art",
        "Hyperrealism",
        "Constructivism",
        "Pre-Raphaelite",
        "Expressionism",
        "Transavantgarde",
        "Street Art",
        "Photo Realism",
        "Abstract Surrealism",
        "Stuckism",
        "Tachisme",
        "Arte Povera",
        "Vorticism",
        "Symbolist Realism",
        "Magic Realism",
        "Neo-Expressionism",
        "Digital Art",
        "Biomorphic Abstraction",
        "Impressionism",
        "Renaissance",
        "Surrealism",
        "Abstract Expressionism",
        "Baroque",
        "Pop Art",
        "Cubism",
        "Romanticism",

    ]

combined_list = art_related_list + emotion_related_list + other_words_list + descriptions

with open("words.txt", "w") as file:
    file.write(f"{combined_list}\n")

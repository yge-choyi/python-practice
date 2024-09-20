import re
from collections import Counter
from typing import List, Tuple

# Step 2: Text Pre-processing
def preprocess_text(text: str) -> List[str]:
    text = re.sub(r'[^\w\s]', '', text)   # Remove punctuation
    words = text.split()
    return words

# Step 3: Word Frequency and Overlap
def word_frequency(words: List[str]) -> Counter:
    return Counter(words)

def word_overlap(freq1: Counter, freq2: Counter) -> float:
    common_words = set(freq1.keys()) & set(freq2.keys())
    overlap = len(common_words) / min(len(freq1), len(freq2))
    return overlap

# Step 4: Grapheme to Phoneme Conversion (Placeholder)
def g2p_conversion(text: str) -> List[str]:
    phonemes = list(text)  
    return phonemes

# Step 5: Statistical Analysis
def phoneme_distribution(phonemes: List[str]) -> Counter:
    return Counter(phonemes)

def phoneme_overlap(dist1: Counter, dist2: Counter) -> float:
    common_phonemes = set(dist1.keys()) & set(dist2.keys())
    overlap = len(common_phonemes) / min(len(dist1), len(dist2))
    return overlap

# Example usage
text1 = "በአዲስ አበባ እየተመዘገበ የመጣው ሁለንተናዊ ለውጥ እያደገ ካለው የገቢ አሰባሰብ ሥርዓት የሚመነጭ መሆኑን ከንቲባ አዳነች አቤቤ ገለጹ። ከከተማ እስከ ወረዳ ያለው የአዲስ አበባ ከተማ አስተዳደር አመራሮችን ያሳተፈ የ2016 አፈጻጸም ግምገማ እና የ2017 ዕቅድ ውይይት መድረክ እየተካሄደ ይገኛል። የአዲስ አበባ ከተማ ከንቲባ አዳነች አቤቤ መድረኩን ሲያስጀምሩ እንደገለጹት፥ በአዲስ አበባ ሁለንተናዊ ለውጥ እንዲመዘገብ ካስቻሉ በርካታ ጉዳዮች መካከል ገቢ ከማሳደግ አንጻር የተከናወኑ ውጤታማ ተግባራት ወሳኝ ሚና አላቸው።"
text2 = "ብመሰረት እቲ ንሱ ዝበሎ እቲ ኣብ ኣድዲስ ኣቤባ ዘሎ ዅነታት ለውጢ ካብቲ እናወሰኸ ዝኸይድ ዘሎ ኣገባብ ምእካብ ኣታዊ ዝመነጨ ኢዩ ። ባጀት 2016ን ባጀት 2017ን ኣብ ቤት ተወከልቲ ይመያየጡ ኣለዉ። ከንቲባ ኣድኣድነኽ ኣቢበ እቲ ዋዕላ ኣብ እተጀመረሉ እዋን ኣታዊ ንምርካብ ዚግበር ውጽኢታዊ ንጥፈታት ሓደ ኻብቲ ኣብ ኣድዲስ ኣቤባ ሓፈሻዊ ለውጢ ንኺግበር ዘኽኣሎ ብዙሕ ረቛሒታት ምዃኑ ገለጸ ።"

# Pre-process text
words1 = preprocess_text(text1)
words2 = preprocess_text(text2)

# Word frequency and overlap
freq1 = word_frequency(words1)
freq2 = word_frequency(words2)
word_overlap_score = word_overlap(freq1, freq2)

# Grapheme to phoneme conversion
phonemes1 = g2p_conversion(text1)
phonemes2 = g2p_conversion(text2)

# Phoneme distribution and overlap
dist1 = phoneme_distribution(phonemes1)
dist2 = phoneme_distribution(phonemes2)
phoneme_overlap_score = phoneme_overlap(dist1, dist2)

print(f"Word Overlap: {word_overlap_score}")
print(f"Phoneme Overlap: {phoneme_overlap_score}")

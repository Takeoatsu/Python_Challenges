vowels = 'AEIOU'
consts = 'BCDFGHJKLMNPQRSTVWXYZ'
consts = consts + consts.lower()
vowels = vowels + vowels.lower()

def is_vowel(letter):
    return letter in vowels 
def is_const(letter):
    return letter in consts

# get the syllables for vc/cv
def vc_cv(word):
    segment_length = 4 # because this pattern needs four letters to check
    pattern = [is_vowel, is_const, is_const, is_vowel] # functions above
    split_points = []

    # find where the pattern occurs
    for i in range(len(word) - segment_length):
        segment = word[i:i+segment_length]

        # this will check the four letter each match the vc/cv pattern based on their position
        # if this is new to you I made a small note about it below
        if all([fi(letter) for letter, fi in zip(segment, pattern)]):
            split_points.append(i+segment_length/2)

    # use the index to find the syllables - add 0 and len(word) to make it work
    split_points.insert(0, 0)
    split_points.append(len(word))
    syllables = []
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i+1]
        syllables.append(word[start:end])
    return syllables

word = 'vortex'

print(vc_cv(word))
# ['vor', 'text']
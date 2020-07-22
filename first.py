pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.upper()
  first = word[0]
  new_word = first + word + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
  print len(new_word)
else:
    print 'empty'

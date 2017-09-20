usage='Usage python find.py <Letters> <No of letter output>'
import enchant,sys
from itertools import permutations
if len(sys.argv) != 3:
   print(usage,len(sys.argv),sys.argv)
   exit(1)
else:
   letters=sys.argv[1]
   no=int(sys.argv[2])
   d=enchant.Dict('en_Us')
   sets={ ''.join(i) for i in permutations(letters,no) if d.check(''.join(i)) ==True}
   print('\n'.join(sets))
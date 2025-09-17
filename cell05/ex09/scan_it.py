import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    found_matches = re.findall(keyword, search_string, re.IGNORECASE)
    
    if found_matches:
        print(len(found_matches))
    else:
        print('none')
else:
    print('none')

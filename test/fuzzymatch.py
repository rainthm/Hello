from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio("北京澳太科技有限公司","北京澳太科技有限公司") #抽取匹配
print(a)

b = fuzz.partial_ratio("北京澳太科技有限公司","北京澳太科技有限公司..") #抽取匹配
print(b)
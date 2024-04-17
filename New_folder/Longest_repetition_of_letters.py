def longest_repeated_chars(s):
    max_count = 0
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    max_count = max(max_count, current_count)
    return max_count

# اختبار الدالة
s = 'AAAAAAAAAA'
print(longest_repeated_chars(s))  # Output: 10


def replace_article(txt):
    # تقسيم النص إلى كلمات
    words = txt.split()

    # تحديد ما إذا كانت "the" تحتاج إلى استبدالها بـ "a" أو "an"
    for i in range(len(words)):
        if words[i].lower() == "the":
            if i == len(words) - 1:  # إذا كانت "the" هي الكلمة الأخيرة في النص
                words[i] = "a"
            else:
                next_word = words[i + 1].lower()
                if next_word[0] in ['a', 'e', 'i', 'o', 'u']:  # إذا كانت الكلمة التالية تبدأ بحرف متحرك
                    words[i] = "an"
                else:
                    words[i] = "a"

    # إعادة تجميع الكلمات إلى نص جديد
    new_txt = ' '.join(words)
    return new_txt


# اختبار الدالة
print(replace_article('Here is the plan'))  # يجب أن تطبع 'Here is a plan'
from typing import List

def word_repeat(word: str, n: int) -> str:
    return ' '.join([word] * n)

# اختبار الدالة
word = 'Hi'
n = 2
print(word_repeat(word, n))  # Output: 'Hi Hi'




def count_words(text):
    # يستخدم الدالة split() لتقسيم النص إلى قائمة من الكلمات
    words_list = text.split()
    # يستخدم الدالة len() لحساب عدد الكلمات في القائمة
    num_words = len(words_list)
    return num_words

# مثال على كيفية استخدام الدالة
txt = 'Plant hope in the hearts of others'
print(count_words(txt))


def compare_lengths(words):
    # تحقق من أن المصفوفة تحتوي على أكثر من عنصر واحد
    if len(words) <= 1:
        return False

    # حساب عدد الأحرف في العناصر النصية في المصفوفة
    lengths = [len(word) for word in words]

    # التحقق مما إذا كانت جميع الأطوال متساوية
    return all(length == lengths[0] for length in lengths)


# مثال على كيفية استخدام الدالة
words = ['A', 'B']
print(compare_lengths(words))

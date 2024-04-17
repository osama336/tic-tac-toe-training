def can_form_target(source, target):
    # قم بتحويل النصوص إلى صيغة صغيرة لتجنب التعقيدات بسبب حالة الأحرف
    source = source.lower()
    target = target.lower()

    # قم بتحويل النصوص إلى قوائم لتسهيل الاستخدام في التحقق
    source_chars = list(source)
    target_chars = list(target)

    # افحص ما إذا كان بإمكان تشكيل target من الأحرف الموجودة في source
    for char in target_chars:
        if char in source_chars:
            # إذا وجد الحرف في source، قم بإزالته من source_chars لتجنب تكرار استخدامه
            source_chars.remove(char)
        else:
            return 'no'

    return 'yes'



# اختبار الدالة
source = 'Hubcoders'
target = 'coderhub'
print(can_form_target(source, target))  # الإخراج: 'yes'

def find_first_index(word, character):
    # البحث عن الحرف في الكلمة
    for i, char in enumerate(word):
        if char == character:
            return i
    # في حال عدم العثور على الحرف
    return -1

# اختبار الدالة
word = 'cloud'
character = 'u'
print(find_first_index(word, character))  # الإخراج: 3

def count_decimal_digits(num):
    # البحث عن النقطة العائمة في النص
    decimal_index = num.find('.')
    if decimal_index == -1:
        # إذا لم تكن هناك نقطة عائمة، فلا يوجد أرقام بعد الفاصلة
        return 0
    else:
        # العثور على الأرقام بعد الفاصلة وإرجاع عددها
        decimal_digits = num[decimal_index + 1:]
        return len(decimal_digits)

# اختبار الدالة
num = '3.967'
print(count_decimal_digits(num))  # الإخراج: 3

def hours_to_seconds(hours):
    # قم بضرب عدد الساعات بعدد الثواني في كل ساعة (60 دقيقة * 60 ثانية)
    return hours * 60 * 60

# اختبار الدالة
hours = 6
print(hours_to_seconds(hours))  # الإخراج: 21600

def min_sum_pair(arr):
    # قم بترتيب المصفوفة بترتيب تصاعدي
    arr.sort()
    # جمع أدنى رقمين وإرجاع النتيجة
    return arr[0] + arr[1]

# اختبار الدالة
arr = [2, 5, 6, 7, 3]
print(min_sum_pair(arr))  # الإخراج: 5

import re

file = open('data.txt', mode='r', encoding='utf-8-sig')
data = file.readlines()
professions = [
    {
        'id': 1,
        'title': 'პროგრამისტი',
    },
    {
        'id': 2,
        'title': 'მომღერალი',
    },
]
array = []


def parseData(arr):
    for line in arr:
        line = line.replace("\n", "")
        line = line.replace(" | ", ",")
        empty_array = line.split(',')

        obj = {
            'name': empty_array[0],
            'year': int(empty_array[1]),
            'professions': empty_array[2],
            'profession_id': 0,
            'experience': int(empty_array[3]),
        }

        for proff in professions:
            if obj['professions'] == proff['title']:
                obj['profession_id'] = proff['id']
        array.append(obj)


parseData(data)


def getBiggestNumber(proffesion_id, comparison):
    first_person_age = 0
    for item in array:
        if item['profession_id'] == proffesion_id:
            if first_person_age < item[comparison]:
                first_person_age = item[comparison]
    return first_person_age


def getSmallestNumber(proffesion_id, comparison):
    first_person_age = getBiggestNumber(proffesion_id, comparison)
    for item in array:
        if item['profession_id'] == proffesion_id:
            if first_person_age > item[comparison]:
                first_person_age = item[comparison]
    return first_person_age


# getDataInfo(1, 'year', 'პროგრამისტებში ყველაზე ახალგაზრდა:')
def getDataInfo(proffesion_id, comparison, print_text, is_asc=False):
    print('---------------------------')
    print(print_text)
    for item in array:
        if item['profession_id'] == proffesion_id:
            if is_asc == False:
                if getBiggestNumber(proffesion_id, comparison) == item[comparison]:
                    print(item['name'], '| year:', item['year'], '| experience:', item['experience'])
            else:
                if getSmallestNumber(proffesion_id, comparison) == item[comparison]:
                    print(item['name'], '| year:', item['year'], '| experience:', item['experience'])

    print('---------------------------')


getDataInfo(1, 'year', 'პროგრამისტებში ყველაზე ახალგაზრდა:')
getDataInfo(2, 'experience', 'მომღერლებში ყველაზე "გამოცდილი":')
getDataInfo(2, 'year', 'მომღერლებში ყველაზე ხანდაზმული:')
getDataInfo(1, 'experience', 'პროგრამისტებში ყველაზე "გამოუცდილი":', True)
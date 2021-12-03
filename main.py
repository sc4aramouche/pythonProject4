proffesions = [
    {
        'id': 1,
        'title': 'პროგრამისტი',
    },
    {
        'id': 2,
        'title': 'მომღერალი',
    },
]

array = [
    {
        'name': 'ცოტნე შარვაძე',
        'year': 1997,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'გივი სიხარულიძე',
        'year': 1997,
        'profession_id': 2,
        'experience': 72,
    },
    {
        'name': 'ცოტნე1 შარვ3აძე',
        'year': 1957,
        'profession_id': 1,
        'experience': 3,
    },
    {
        'name': 'ცოტნე2 შარვ3აძე',
        'year': 13987,
        'profession_id': 2,
        'experience': 7,
    },
    {
        'name': 'ცოტნე3 შარვ3აძე',
        'year': 1997,
        'profession_id': 2,
        'experience': 2,
    },
    {
        'name': 'ცოტნე4 შარვ3აძე',
        'year': 1957,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'ცოტნე4 შა3რვაძე',
        'year': 1990,
        'profession_id': 2,
        'experience': 6,
    },
    {
        'name': 'ცოტნე შარვ3აძე',
        'year': 1991,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'ცოტნე შარვა3ძე',
        'year': 1997,
        'profession_id': 2,
        'experience': 12,
    },
    {
        'name': 'ცოტნე55 შა3რვაძე',
        'year': 1990,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'ცოტნე555 შ3არვაძე',
        'year': 1997,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'ცოტნე შარვ3აძე',
        'year': 1997,
        'profession_id': 2,
        'experience': 2,
    },
    {
        'name': 'ცოტნე255 შარვ3აძე',
        'year': 1992,
        'profession_id': 1,
        'experience': 7,
    },
    {
        'name': 'ცოტნე2 შარვაძე',
        'year': 1997,
        'profession_id': 2,
        'experience': 1,
    },
    {
        'name': 'ცოტნე2 შარვაძე',
        'year': 1978,
        'profession_id': 1,
        'experience': 7,
    },
]


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



#1
l = list()

#2-3
l1 = [1,2,3,4,5,6]
print(l1)
print(len(l1))

#4
print(l1[0],l1[len(l1)//2],l1[-1])

#5
l2 = ["Sefa",21,1.87,"Male","Turkey"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7
print(it_companies)
#8
print(len(it_companies))

#9
print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])

#10
it_companies[1] = "Comp1"
print(it_companies)

#11
it_companies.append("Comp2")
print(it_companies)

#12
it_companies.insert(len(it_companies)//2,"Comp3")

#13
it_companies[2] = it_companies[2].upper()
print(it_companies)

#14
str_ = "#; ".join(it_companies)
print(str_)

#15
print("Apple" in it_companies)
print("X" in it_companies)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.sort(reverse=True)
print(it_companies)

#18
print(it_companies[3:])

#19
print(it_companies[:len(it_companies)-3])

#20 - 22
del it_companies[len(it_companies)//2]
print(it_companies)

#21
del it_companies[0]
print(it_companies)

#23
del it_companies[len(it_companies)-1]
print(it_companies)

#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#print(it_companies) #HATA

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

new_list = front_end + back_end
print(new_list)

full_stack = new_list.copy()
full_stack.append("Python")
full_stack.append("SQL")
full_stack.append("Redux")
print(full_stack)

#LEVEL2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort() # ages = ages.sort() diye bir şey yok ,ages none olur!!!!
print(ages)

min1 = ages[0]
min2 = min(ages)
print(min1,min2)
max1 = ages[len(ages)-1]
max2 = max(ages)
print(max1,max2)

if(len(ages) % 2 == 0):
    v1 = ages[len(ages)//2]
    v2 = ages[len(ages)//2 - 1]
    print(v1,v2)
else:
    print(ages[len(ages)//2])


print(sum(ages)/len(ages))
print(max(ages)-min(ages))

avg = sum(ages)/len(ages)
print(abs(min(ages) - avg) is abs(max(ages)- avg))

#1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

if(len(countries) % 2 == 0):
    v1 = countries(len(countries)//2)
    v2 = countries(len(countries)//2-1)
    print(v1,v2)
else:
    print(countries[len(countries)//2])

#2
part1 = countries[:len(countries)//2]
part2 = countries[len(countries)//2:]
print(part1)
print()
print(part2)

#3

country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

c1,c2,c3, *rest = country_list
print(c1,c2,c3)
print(rest)



 











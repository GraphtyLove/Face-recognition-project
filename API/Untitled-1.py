name = "Daniele"
daniele_is_hungry = True
daniele_favorite_food = 'fish'

if daniele_is_hungry == True:
    print(f'{name} need to eat some {daniele_favorite_food} because she is hungry')



number_of_fish_eated_by_daniele = 0


while(daniele_is_hungry == True):
    if number_of_fish_eated_by_daniele < 5:
        print(f'{name} need to eat some {daniele_favorite_food} because she is hungry')
        print(f'Daniele eat a fish, she eated: {number_of_fish_eated_by_daniele} fish')
        number_of_fish_eated_by_daniele += 1
    else:
        print('daniel is not hungry anymore!')
        daniele_is_hungry = False

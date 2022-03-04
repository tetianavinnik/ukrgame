import my_game

kyiv = my_game.City("Київ")
kyiv.set_open(0)
kyiv.set_points(1)

chernihiv = my_game.City("Чернігів")
chernihiv.set_open(5)
chernihiv.set_points(3)

sumi = my_game.City("Суми")
sumi.set_open(2)
sumi.set_points(2)

kharchiv = my_game.BossCity("Харків")
kharchiv.set_open(22)
kharchiv.set_points(0)

chuhuiv = my_game.City("Чугуїв")
chuhuiv.set_open(2)
chuhuiv.set_points(2)

donetsk = my_game.City("Донецьк")
donetsk.set_open(14)
donetsk.set_points(4)

mariupol = my_game.City("Маріуполь")
mariupol.set_open(10)
mariupol.set_points(4)

zhitomir = my_game.City("Житомир")
zhitomir.set_open(0)
zhitomir.set_points(1)

uman = my_game.City("Умань")
uman.set_open(0)
uman.set_points(1)

kropivnitskiy = my_game.City("Кропивницький")
kropivnitskiy.set_open(3)
kropivnitskiy.set_points(2)

odesa = my_game.City("Одеса")
odesa.set_open(6)
odesa.set_points(3)

bomb = my_game.Enemy("Бомбардування", "Увага! Увага! Проводиться бомбардування міста з повітря!")
bomb.set_weakness("привид")
kyiv.set_enemy(bomb)

gas = my_game.Enemy("Газова атака", "Увага! Увага! Рашисти проводять зачистку міста за допомогою хімічної зброї!")
gas.set_weakness("протигаз")
chernihiv.set_enemy(gas)

rashisti = my_game.Enemy("Рашисти", "Увага! Увага! Рашисти знаходяться на під'їзді до міста!")
rashisti.set_weakness("бандерівське смузі")
sumi.set_enemy(rashisti)

diverse = my_game.Enemy("Диверсанти", "Увага! Увага! Будьте обережними, у місті були помічені диверсантські групи!")
diverse.set_weakness("комендантська година")
chuhuiv.set_enemy(diverse)

freedom = my_game.Enemy("'Звільнення'", "Окупанти рятують нас від нацистської влади")
freedom.set_weakness("граната")
donetsk.set_enemy(freedom)

panic = my_game.Enemy("Паніка", "Увага! Увага! Через пропагандистсбку кампанію Путіна у місті швидко поширюється паніка!")
panic.set_weakness("медитація")
mariupol.set_enemy(panic)

spy = my_game.Enemy("Шпіон", "Увага! Увага! По місту ходять рашисти-розвідники!")
spy.set_weakness("нісенітниця")
zhitomir.set_enemy(spy)

block = my_game.Enemy("Блокпост", "Увага! Увага! На виїзді з міста розташувалися рашистські блокпости, які вимагають документи")
block.set_weakness("дуля")
uman.set_enemy(block)

sign = my_game.Enemy("Мітки", "Увага! Увага! На дахах будинків були знайдені мітки!")
sign.set_weakness("фарба")
kropivnitskiy.set_enemy(sign)

path = my_game.Enemy("Корабель", "Вніманіе! Ми - русскій ваєнний карабль...")
path.set_weakness("дорожній знак(-14.408923886851756, -71.29932736927732)")
odesa.set_enemy(path)

dulya = my_game.Knowledge("дуля")
dulya.set_description("з маком, або з хріном(коротше, на український смак)")
kyiv.set_item(dulya)

did_Petro = my_game.Friend("Дід Петро", "Прожив у місті 40 років, знає, як правильно відмовити у проханні", "Навчу те синку, як правильно терористам отказувать")
kyiv.set_friend(did_Petro)

antigas = my_game.Thing("протигаз")
antigas.set_description("а шоб ви рашисти метану обнюхались")
kropivnitskiy.set_item(antigas)

smuzi = my_game.Thing("бандерівське смузі")
smuzi.set_description("єєєй, ще один танчик!")
chuhuiv.set_item(smuzi)

hour = my_game.Knowledge("комендантська година")
hour.set_description("нічого тут шастать")
chernihiv.set_item(hour)

police = my_game.Friend("Поліцейські", "якщо лежачі, то можуть допомогти в обмеженні пересування", "Увага! Вводимо комендантську годину")
chernihiv.set_friend(police)

nonsens = my_game.Knowledge("нісенітниця")
nonsens.set_description("хоч язик і без кісток, та він у вас зламається")
sumi.set_item(nonsens)

teacher = my_game.Friend("Людмила Степанівна", "Вчителька української мови та літератури", "Роз-, без- пишеться з літерою з")
sumi.set_friend(teacher)

helicopter = my_game.Thing("привид")
helicopter.set_description("тищ, тидищ, тищ!")
uman.set_item(helicopter)

granata = my_game.Thing("граната")
granata.set_description("лови рашист гранату!")
donetsk.set_item(granata)

paint = my_game.Thing("фарба")
paint.set_description("як заблудитесь, краще в українців дорогу не питати")
mariupol.set_item(paint)

dorz = my_game.Thing("дорожній знак(-14.408923886851756, -71.29932736927732)")
dorz.set_description("баба Надя вам привіт передавала")
zhitomir.set_item(dorz)

meditation = my_game.Knowledge("медитація")
meditation.set_description("залякати нас не вдасться, ми абсолютні у своїй єдності та певності перемоги!")
odesa.set_item(meditation)

jap = my_game.Friend("Сянь Цзі", "Японський практик медитації", "Після мого уроку, будеш спокійним, наче слон")
odesa.set_friend(jap)

cities = [kyiv, chernihiv, sumi, kharchiv, chuhuiv, donetsk, mariupol, zhitomir, uman, kropivnitskiy, odesa]
current_city = kyiv
backpack = []
total = 0
dead = False

print("""
Вітаємо у грі-блукачці!

Пропонуємо побувати в гарячих точках українсько-російської війни

1) Щоб пересувати по містах, необхідно ввести назву зі списку доступних.
2) Щоб попросити про допомогу у жителя та отримати нові знання
треба ввести слово допомога.
3) Щоб вирішити наявну у місті проблему потрібно ввести слово знешкодити
і потім обрати наявний у вашому арсеналі предмет або знання.
4) Щоб взяти наявний на локації предмет потрібно ввести слово взяти.

Натисніть Enter, щоб продовжити
""")

input()

while dead == False:
    open_cities_name = [i.name for i in cities if total >= i.open and i.free == False]
    go_city = [i for i in cities if (i.friend != '' or i.item != ''or i.free == False) and total >= i.open]
    go_city_name = [i.name for i in cities if (i.friend != '' or i.item != '' or i.free == False) and total >= i.open]

    print("\n")
    current_city.get_details()
    print('Міста, які потребують звільнення:\n')
    for i in open_cities_name:
        print(i)
    print('--------------------')
    print('Доступні міста:\n')
    for i in go_city:
        print(i.name)
    print('--------------------')
    
    friend = current_city.get_friend()
    inhabitant = current_city.get_enemy()
    if friend != '':
        print('Жителі:')
        friend.describe()
        print('')
    if inhabitant != '':
        print('Проблема:')
        inhabitant.describe()
        print('')

    item = current_city.get_item()
    if item != '' and type(item).__name__ == 'Thing':
        item.describe()

    command = input("> ")
    if command == 'Харків':
        kharchiv.boss_level_one()
        kharchiv.boss_level_two()
        break
    if command in go_city_name:
        current_city = go_city[go_city_name.index(command)]
    elif command == "допомога" and type(item).__name__ != 'Thing':
        if friend != '':
            backpack.append(friend.ask_help(current_city))
            print('Тепер ти знаєш як {}'.format(item.get_name()))
            current_city.set_item('')
            current_city.set_friend('')
        else:
            print('Тут немає жодного друга')
    elif command == "знешкодити":
        if inhabitant != '':
            print("Обери, чим битимеш москалів\n")
            for i in backpack:
                print(i.name)
            print('--------------------')
            fight_with = input()
            for i in backpack:
                if i.name == fight_with:
                    fight_with = i

            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("Ти звільнив місто!")
                    total += current_city.points
                    current_city.enemy = ''
                    current_city.free = True
                else:
                    print("Цей спосіб тут не працює")
                    print("Спробуй ще раз")
            else:
                print("Я не маю " + fight_with)
        else:
            print("Тут уже немає ворога")
    elif command == "взяти" and type(item).__name__ == 'Thing':
        item = current_city.get_item()
        if item != '':
            print("У тебе тепер є " + item.get_name())
            backpack.append(item)
            current_city.set_item('')
        else:
            print("Тут немає чого брати")
    else:
        print("Я не знаю як " + command)

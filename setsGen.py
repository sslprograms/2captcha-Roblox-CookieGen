import requests, random

HATS = [4819740796, 7212268341, 8136940617, 607702162, 5917433699, 617605556, 6555565708, 3409612660]
SHIRTS = [607785314, 398633584, 6829670577, 3670737444, 7673098764, 7427983453, 398635081, 144076358, 4047884046, 4047884939, 382538059]
PANTS = [398633812, 398635338, 6829667358, 7673101417, 144076760, 382537950, 382538503, 382537569]
HAIRS = [451221329, 2956239660, 376524487, 62234425, 3814476174, 451220849, 376548738]
EXTRA = [376526673, 376527115, 7893377446, 7893377446, 4619597156, 6375710342, 4771618549]
FACES = [7074764, 616380929, 7074786, 86487766]


COMBOS =  15000

done = []

while True:

    hat_or_hair = random.choice(['hair', 'hat'])

    combo  = ''

    if hat_or_hair == 'hair':

        combo = f'{random.choice(HAIRS)}'
    
    elif hat_or_hair == 'hat':

        combo = f'{random.choice(HATS)}'

    
    combo = combo +  f':{random.choice(SHIRTS)}'
    combo = combo +  f':{random.choice(PANTS)}'

    combo = combo + f':{random.choice(FACES)}'
    combo = combo + f':{random.choice(EXTRA)}'

    if done.count(combo) < 1:

        done.append(combo)


        open('asset_sets.txt', 'a').write(f'{combo}\n')

        print(combo)

    if len(done) >= COMBOS:
        break

from random_name_generator.constants import Descent
import requests, json, subprocess, threading, time, string, random, random_name_generator 
from random_word import RandomWords
from requests.api import patch
r = RandomWords()

SKIN_TONES = [125, 217, 192, 351, 359]

CONFIG = json.loads(
    open('config.json').read()
)['config']

API_KEY = CONFIG['api_key']
ARKOSE_KEY = CONFIG['arkose_key']
THREADING_PROCESSES = CONFIG['threads']

GENDERS = [random_name_generator.Sex.MALE, random_name_generator.Sex.FEMALE]

proxies = open('proxies.txt', 'r').read().splitlines()

TOTAL = 0

def generate_username():
    while True:
        time.sleep(3)
        try:
            main_ = r.get_random_word().lower().replace(' ', '')
            user = main_ + f'{random.randint(1, 10000)}'
            username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={user}')
            print(user)
            if username.json()['message'] == "Username is valid":
                return user, main_
        except:
            pass

def getCaptchaId(proxy):

    with requests.session() as session:

        session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
        session.proxies = {
            'https':proxy,
            'http':proxy
        }

        session.headers['x-csrf-token'] = session.post(f"https://auth.roblox.com/v1/usernames/validate").headers['x-csrf-token']

        captchaId = session.post(
            'https://auth.roblox.com/v2/signup',
            json={'captchaId':'', 'username':'james', 'captchaToken':''}
        ).json()['failureDetails'][0]['fieldData'].split(',')

    
    return captchaId




def extract_token(email_data):
    token = email_data.split('class=\"email-button\" href=\"https://www.roblox.com/account/settings/verify-email?ticket=')[1].split('\" style=\"border-radius:8px;')[0]
    print(token)
    return token



def create_account(captcha_token, captchaId, proxy, key):
    global TOTAL
    with requests.session() as session:
        proxy = {
            'https':proxy,
            'http':proxy
        }
        agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30']
        session.headers['user-agent'] = random.choice(agents)
        session.headers['x-csrf-token'] = session.post(f"https://auth.roblox.com/v1/usernames/validate", proxies=proxy).headers['x-csrf-token']
        session.headers['referer'] = 'https://www.roblox.com/'
        session.headers['origin'] = 'https://www.roblox.com'
        session.proxies = proxy
        gender = random.randint(1,2)
        username, main_user = generate_username()
        password = f''.join(random.choices(string.ascii_letters, k=10))
        nwset = []

        email_session = requests.session()

            
        forum = {
            'abTestVariation':0,
            "agreementIds":[
                "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
                "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
            ],

            "birthday":"21 Sep 2006",
            "captchaProvider":"PROVIDER_ARKOSE_LABS",
            "captchaToken":captcha_token,
            "context":"MultiverseSignupForm",
            "displayAvatarV2":False,
            "displayContextV2":False,
            "gender":gender,
            "captchaId":captchaId,
            "isTosAgreementBoxChecked":True,
            "password":password,
            "username":username,
            "referralData":'null',
        }
        create = session.post('https://auth.roblox.com/v2/signup', data=forum, proxies=proxy)

        
        print(create.text)
        if create.status_code == 200 or create.status_code == 302:

            cookie = create.cookies['.ROBLOSECURITY']
            open('unverified_cookies.txt', 'a').write(f'{username}:{password}:{cookie}\n')






            # cookie = create.cookies['.ROBLOSECURITY']
            # with open('upc_cookies.txt', 'a') as gen:
            #     gen.write(f'{username}:{password}:{cookie}\n')
            

            # with open('cookies.txt', 'a') as gen:
            #     gen.write(f'{cookie}\n')

            # session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']

            # products =  []

            # productData = {
            #     'items':[

            #     ]
            # }

            # for __asset__id__ in picked_set:
            #     reqData = {
            #         'itemType':'Asset',
            #         'id':__asset__id__
            #     }
            #     productData['items'].append(reqData)

            # getProducts = session.post(
            #     'https://catalog.roblox.com/v1/catalog/items/details',
            #     json=productData,
            #     proxies=proxy
            # )

            # for __product__ in getProducts.json()['data']:
            #     products.append(__product__['productId'])

            # for _buy_product_ in products:

            #     buy = session.post(
            #         f'https://economy.roblox.com/v1/purchases/products/{_buy_product_}',
            #         data = {
            #             'expectedCurrency':1,
            #             'expectedSellerId':1,
            #             'expectedPrice':0
            #         },
            #         proxies=proxy
            #     )

            #     print(buy.text)
 
            # for _asset_id_ in picked_set:

            #     wear = session.post(
            #         f'https://avatar.roblox.com/v1/avatar/assets/{_asset_id_}/wear'
            #     )

            #     print(wear.text)
            
            # color = random.choice(SKIN_TONES)
            # change = session.post(
            #     'https://avatar.roblox.com/v1/avatar/set-body-colors',

            #     json = {
            #         'headColorId':color,
            #         'leftArmColorId':color,
            #         'leftLegColorId':color,
            #         'rightArmColorId':color,
            #         'rightLegColorId':color,
            #         'torsoColorId':color
            #     }
            # )


            # session.post(
            #     f'https://avatar.roblox.com/v1/avatar/assets/1772336109/remove'
            # )

            # online = random.randint(1,4)

            # if online == 3:

            #     session.post('https://presence.roblox.com/v1/presence/register-app-presence')

            # userId = session.get(
            #     'https://users.roblox.com/v1/users/authenticated'
            # ).json()['id']

            # patch_ = session.patch(
            #     f'https://users.roblox.com/v1/users/{userId}/display-names',
            #     json = {
            #         'newDisplayName':main_user
            #     }
            # )

            # print(patch_.text)


        if create.status_code != 200:

            report_bad = requests.post(
                f'http://2captcha.com/res.php?key={API_KEY}&action=reportbad&id={key}'
            )

            print(report_bad.text)
    
        return

def counter():
    import os

    while True:
        time.sleep(0.1)
        os.system(f'title TOTAL: {TOTAL}')

threading.Thread(target=counter,).start()

def solveCaptcha(captcha, proxy):

    captchaBlob = captcha[1]


    requestTwoCaptcha = requests.post(
        f'http://2captcha.com/in.php',
        params = {
            'key':API_KEY,
            'method':'funcaptcha',
            'publickey':ARKOSE_KEY,
            'surl':'https://roblox-api.arkoselabs.com/',
            'pageurl':'https://www.roblox.com/',
            'data[blob]':captchaBlob
        }
    )

    if requestTwoCaptcha.status_code == 200:

        print(requestTwoCaptcha.text)

        KEY = requestTwoCaptcha.text.split('|')[1]

        while True:

            time.sleep(10)


            checkKey = requests.get(
                f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={KEY}'
            )

            if checkKey.text != 'CAPCHA_NOT_READY':
                token = checkKey.text.replace('OK|', '')
                print(token + ' -|- ' + captcha[0] + ' -|- ' + captcha[1])
                try:
                    create_account(token, captcha[0], proxy, KEY)
                except:
                    report_bad = requests.post(
                        f'http://2captcha.com/res.php?key={API_KEY}&action=reportbad&id={KEY}'
                    )

                    print(report_bad.text)
    
                return
        

def main():
    while True:
        proxy = random.choice(proxies)
        captcha = getCaptchaId(proxy)
        solveCaptcha(captcha, proxy)

for x in range(int(THREADING_PROCESSES)):
    threading.Thread(target=main,).start()

input()
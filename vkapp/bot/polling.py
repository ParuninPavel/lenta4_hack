import os
import vk
import requests
import time
import json
from .handlers import handle_update

def get_polling_server():
    session = vk.Session(access_token=os.environ['GROUP_TOKEN'])
    vkapi = vk.API(session)
    r = vkapi('messages.getLongPollServer', need_pts=1)
    return r['server'], r['key'], r['ts']

class Poller:
    server, key, ts = get_polling_server()


def polling():
    #server, key, ts = get_polling_server()

    while True:
        time.sleep(0.01)
        r = requests.get('https://{}?act=a_check&key={}&ts={}&wait=25&mode=2&version=2'.format(Poller.server, Poller.key, Poller.ts))
        resp = json.loads(r.text)

        if 'failed' in resp:
            Poller.server, Poller.key, Poller.ts = get_polling_server()
            continue

        if 'updates' in resp:
            if len(resp['updates'])!=0:
                for update in resp['updates']:
                    if update[0] == 4:
                        if ((update[2] >> 1) & 1) == 0:

                            handle_update(update)
                            # serialized_update = json.dumps(update)

                            # url = 'http://127.0.0.1:8000/botupdates'
                            # headers = {'content-type': 'application/json'}
                            #
                            # response = requests.post(url, data=json.dumps(serialized_update), headers=headers)
                            # print ('SENT: ', response)

        Poller.ts = resp['ts']+1
        print (resp)
        #time.sleep(1)


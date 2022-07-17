# coding=utf-8
from memory_profiler import profile
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession
import requests_html
import time
import telebot
import logging
import datetime
import os
import ast
import pytz
import urllib3
import gc
from subprocess import check_output
import subprocess
import psutil
# import concurrent.futures as pool
# from multiprocessing import Process

import subprocess
os.system('chcp 65001')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(handlers=[logging.FileHandler('main.log', 'a', 'utf-8')], level=logging.INFO)
logging.getLogger("pyppeteer.launcher").disabled = True
def to_list(same_info):
    return ast.literal_eval(same_info)
# fp=open('memory_profiler.log','w+')
# @profile(stream=fp)
# def pars_site(session, site_ad, params, kol, number_of_attempts = 0):
#     try:
#         good = True
#         r = session.get(site_ad, headers=headers, verify=False, stream=True)
#         if params == "Umschreibung eines ausländischen Führerscheins (kein EU/EWR-Führerschein) beantragen":
#             script = """
#                 () =>{
#                     $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=1]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
#                     $('.WEB_APPOINT_FORWARDBUTTON').click();
#                 }
#                 """
#         elif params == 'Ersatz Personenbeförderungsschein wegen Verlust / Diebstahl':
#             script = """
#                 () =>{
#                     $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=1]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
#                     $('.WEB_APPOINT_FORWARDBUTTON').click();
#                 }
#                 """
#         elif params == 'Dienstführerschein umschreiben':
#             script = """
#                 () =>{
#                     $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=1]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
#                     $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
#                     $('.WEB_APPOINT_FORWARDBUTTON').click();
#                 }
#                 """
#         else:
#             print("Error params {0}".format(params))
#             logging.error("Error params {0} at {1}".format(params, datetime.datetime.now()))
#             good = False
#             r.close()
#             return ''
#         if good == True:
#             # r.html.render(script=script, sleep=5+number_of_attempts*2, keep_page=True)
#             r.html.render(script=script, sleep=5+number_of_attempts*2)
#             soup = BS(r.html.html, 'html.parser')
#             # r.html.page.close()
#             # r.html.render.quit()
#             del r
#             #gc.collect()
#             # print(soup.find("div", {"id": "locationContent"}).find_all("td", {"class": "nat_calendar"}))
#             info = soup.find("div", {"id": "locationContent"}).find_all("td", {"class": "nat_calendar"})
#             del soup
#             new_mass_for_mes = []
#             for i in info:
#                 # print(i.text)
#                 if "Keine freien Termine am" not in i.text and i.text != "":
#                     new_mass_for_mes.append(i.text)
#             #     print("------------")
#             # print(new_mass_for_mes)
#             if kol >= 59:
#                 print(datetime.datetime.now(pytz.timezone('Europe/Moscow')), end="")
#                 print(len(info), end="")
#                 print(new_mass_for_mes)
#             del info
#             gc.collect()
#             msg = ''
#             if len(new_mass_for_mes) > 0:
#                 times = get_times()
#                 if params[0:5] not in times.keys():
#                     times[params[0:5]] = []
#                 for i in new_mass_for_mes:
#                     if i.split()[-2] not in times[params[0:5]]:
#                         times[params[0:5]].append(i.split()[-2])
#                         msg += i.split()[-2]+'\n'
#                     else:
#                         pass
#                 put_times(times)
#             if msg != '':
#                 new_msg = params + '\n'
#                 if "Umsch" in params:
#                     new_msg += 'https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071898\n'
#                 elif "Ersat" in params:
#                     new_msg += "https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html\n"
#                 elif "Diens" in params:
#                     new_msg += "https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071837\n"
#                 new_msg += 'Some appointments are available for the following dates:\n'
#                 new_msg += msg
#                 # new_chat_id = [chat_id[-1]]
#                 for j in chat_id:
#                     bot.send_message(chat_id = j, text=new_msg)
#             else:
#                 logging.info(str(datetime.datetime.now(pytz.timezone('Europe/Moscow'))))
#                 logging.info(str(params))
#         logging.info("Work good")
#     except Exception as e:
#         logging.error("{0} at {1}".format(e, datetime.datetime.now()))
#         logging.error(e)
#     return ''

#Получаем chat_id из файла
def get_chat_id():
    try:
        file=open("chat_id.txt","r")
        chat_id=file.read()
        file.close()
        logging.info("Chat_id get"+str(chat_id))
        # chat_id = [id, id, id, admin_id]
        return chat_id
    except FileNotFoundError:
        logging.error("FileNotFoundError(chat_id)")
        file=open("chat_id.txt","w")
        file.close()
#Получаем токен из файла
def get_token():
    try:
        file=open("token.txt","r")
        token=file.read()
        if ":" not in token:
            logging.error("Invalid token")
            print("Invalid token")
        else:
            if token.split(":")[0].isdigit()==False:
                logging.error("Invalid token")
                print("Invalid token")
            else:
                logging.info("Token get")
                return token
        file.close()
    except FileNotFoundError:
        logging.error("FileNotFoundError(token)")
        file=open("token.txt","w")
        file.close()

def get_times():
    file=open("times.txt","r")
    times=file.read()
    file.close()
    logging.info("Times get"+str(times))
    return to_list(times)
def put_times(info):
    logging.info(str(info))
    my_file = open("times.txt", "w", encoding="utf-8")
    my_file.write(str(info))
    my_file.close()
    return ''
def get_pid(name):
    try:
        return map(int,check_output(["pidof",name]).split())
    except:
        return ''

token=get_token()
# chat_id=int(get_chat_id())
chat_id = to_list(get_chat_id())
if token!='' and chat_id!='':
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id = chat_id[-1], text = "Работает.")
    bot.stop_bot()
    logging.info("BOT start at {}\n".format(datetime.datetime.now()))
    print("Bot work")
    print(datetime.datetime.now(pytz.timezone('Europe/Moscow')))
    logging.info(str("Bot work"))
    url = "https://terminvereinbarung.muenchen.de/fs/termin/?loc=FS&ct=1071898"
    # print(chat_id[-1])
    # print(bot.get_me())
    # a=bot.send_message(chat_id=chat_id[-1],text="Старт работы")
    # bot.delete_message(chat_id=chat_id[-1],message_id=a.id)
    # print(a.id, a.date)
    k = 0
    while True:
        print("Work", end= " ")
        print(datetime.datetime.now(pytz.timezone('Europe/Moscow')))
        data = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        if data.hour < 6:
            put_times({})
            time.sleep((6*60-data.hour*60-data.minute)*60)
        elif data.hour > 21:
        # elif data.hour > 24:
            put_times({})
            time.sleep((24 - data.hour) * 60 * 60)
        else:
            ses = HTMLSession(browser_args=['--disable-setuid-sandbox','--no-sandbox'])
            # ses = requests_html.HTMLSession()
            # with pool.ThreadPoolExecutor(max_workers=1) as executor:
            #     params = "Umschreibung eines ausländischen Führerscheins (kein EU/EWR-Führerschein) beantragen"
            #     # pars_site(ses, url, params, k)
            #     future1 = executor.submit(pars_site, ses, url, params, k)
            params = "Umschreibung eines ausländischen Führerscheins (kein EU/EWR-Führerschein) beantragen"
            # pars_site(ses, url, params, k, headers)
            subprocess.run("python3 pars.py", universal_newlines=True, input=str(url) + "\n" + str(params) + "\n" + str(k) + "\n", shell=True)
            # p = Process(target=pars_site, args=(ses, url, params, k,))
            # p.start()
            # p.join()
            # params = "Ersatz Personenbeförderungsschein wegen Verlust / Diebstahl"
            # pars_site(ses, url, params, k)
            # with pool.ThreadPoolExecutor(max_workers=1) as executor:
            #     params = "Dienstführerschein umschreiben"
            #     # pars_site(ses, url, params, k)
            #     future3 = executor.submit(pars_site, ses, url, params, k)
            params = "Dienstführerschein umschreiben"
            # pars_site(ses, url, params, k, headers)
            subprocess.run("python3 pars.py", universal_newlines=True, input=str(url) + "\n" + str(params) + "\n" + str(k) + "\n", shell=True)
            # p = Process(target=pars_site, args=(ses, url, params, k,))
            # p.start()
            # p.join()
            # ses.browser.close()
            # for attr in dir(ses.browser):
            #     # if not attr.startswith('_'):  # Если не внутренний и не служебный
            #     print(getattr(ses.browser, attr))
            # ses.browser.Browser.driver.quit()
            # print(ses.browser)
            # ses.browser.close()
            ses.close()
            #ses.close()
            # subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
            # subprocess.call("TASKKILL /f  /IM  chromedriver")
            # subprocess.call("TASKKILL /f  /IM  chrome")
            # process_name = "chrome"
            # rez = get_pid(process_name)
            # print(rez)
            # if type(rez) != '':
            #     rez = list(rez)
            #     for i in rez:
            #         print(i)
            #     # Kill process.
            #     for pid in rez:
            #         p = psutil.Process(pid)
            #         p.terminate()
            #         p.kill()
            k += 1
            if k == 60*3:
                put_times({})
                k = 0
        time.sleep(1*20)


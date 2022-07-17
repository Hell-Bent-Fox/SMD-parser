from memory_profiler import profile
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession
import requests_html
import logging
import datetime
import gc
import pytz
import ast
import telebot
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def to_list(same_info):
    return ast.literal_eval(same_info)
def get_times():
    file=open("times.txt","r")
    times=file.read()
    file.close()
    logging.info("Times get"+str(times))
    return to_list(times)
def get_chat_id():
    try:
        file=open("chat_id.txt","r")
        chat_id=file.read()
        file.close()
        logging.info("Chat_id get"+str(chat_id))
        return chat_id
    except FileNotFoundError:
        logging.error("FileNotFoundError(chat_id)")
        file=open("chat_id.txt","w")
        file.close()
def put_times(info):
    logging.info(str(info))
    my_file = open("times.txt", "w", encoding="utf-8")
    my_file.write(str(info))
    my_file.close()
    return ''
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
chat_id = to_list(get_chat_id())
fp=open('memory_profiler.log','w+')
@profile(stream=fp)
def pars_site(session, site_ad, params, kol, bot, headers, number_of_attempts = 0):
    try:
        good = True
        r = session.get(site_ad, headers=headers, verify=False, stream=True)
        if params == "Umschreibung eines ausländischen Führerscheins (kein EU/EWR-Führerschein) beantragen":
            script = """
                () =>{
                    $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=1]').prop('selected', true);
                    $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
                    $('.WEB_APPOINT_FORWARDBUTTON').click();
                }
                """
        elif params == 'Ersatz Personenbeförderungsschein wegen Verlust / Diebstahl':
            script = """
                () =>{
                    $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=1]').prop('selected', true);
                    $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
                    $('.WEB_APPOINT_FORWARDBUTTON').click();
                }
                """
        elif params == 'Dienstführerschein umschreiben':
            script = """
                () =>{
                    $('select[name="CASETYPES[FS Internationaler FS beantragen]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Umschreibung Ausländischer FS]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Ersatz PBS]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Dienstführerschein umschreiben]"] option[value=1]').prop('selected', true);
                    $('select[name="CASETYPES[FS Internationaler FS bei Besitz]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung Führerschein]"] option[value=0]').prop('selected', true);
                    $('select[name="CASETYPES[FS Abholung eines Personenbeförderungsscheines]"] option[value=0]').prop('selected', true);
                    $('.WEB_APPOINT_FORWARDBUTTON').click();
                }
                """
        else:
            print("Error params {0}".format(params))
            logging.error("Error params {0} at {1}".format(params, datetime.datetime.now()))
            good = False
            r.close()
            return ''
        if good == True:
            # r.html.render(script=script, sleep=5+number_of_attempts*2, keep_page=True)
            r.html.render(script=script, sleep=5+number_of_attempts*2)
            soup = BS(r.html.html, 'html.parser')
            # r.html.page.close()
            # r.html.render.quit()
            del r
            #gc.collect()
            # print(soup.find("div", {"id": "locationContent"}).find_all("td", {"class": "nat_calendar"}))
            info = soup.find("div", {"id": "locationContent"}).find_all("td", {"class": "nat_calendar"})
            del soup
            new_mass_for_mes = []
            for i in info:
                # print(i.text)
                if "Keine freien Termine am" not in i.text and i.text != "":
                    new_mass_for_mes.append(i.text)
            #     print("------------")
            # print(new_mass_for_mes)
            if kol >= 59:
                print(datetime.datetime.now(pytz.timezone('Europe/Moscow')), end="")
                print(len(info), end="")
                print(new_mass_for_mes)
            del info
            gc.collect()
            msg = ''
            if len(new_mass_for_mes) > 0:
                times = get_times()
                if params[0:5] not in times.keys():
                    times[params[0:5]] = []
                for i in new_mass_for_mes:
                    if i.split()[-2] not in times[params[0:5]]:
                        times[params[0:5]].append(i.split()[-2])
                        msg += i.split()[-2]+'\n'
                    else:
                        pass
                put_times(times)
            if msg != '':
                new_msg = params + '\n'
                if "Umsch" in params:
                    new_msg += 'https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071898\n'
                elif "Ersat" in params:
                    new_msg += "https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html\n"
                elif "Diens" in params:
                    new_msg += "https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071837\n"
                new_msg += 'Some appointments are available for the following dates:\n'
                new_msg += msg
                # new_chat_id = [chat_id[-1]]
                for j in chat_id:
                    bot.send_message(chat_id = j, text=new_msg)
            else:
                logging.info(str(datetime.datetime.now(pytz.timezone('Europe/Moscow'))))
                logging.info(str(params))
        logging.info("Work good")
    except Exception as e:
        logging.error("{0} at {1}".format(e, datetime.datetime.now()))
        logging.error(e)
    return ''
if __name__ == "__main__":
    token = get_token()
    bot = telebot.TeleBot(token)
    ses = HTMLSession(browser_args=['--disable-setuid-sandbox', '--no-sandbox'])
    url = input()
    params = input()
    k = int(input())
    headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    pars_site(ses, url, params, k, bot, headers)
    bot.stop_bot()
    ses.close()
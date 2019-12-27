# -*- coding: utf8 -*-
import vk_api
import random
import json
import sqlite3
import time

token = "c9366828897ea7dd0e9789b21236e1bd02e794833e9da6db78b680c73cca47e98a3ce3bac222fa8739b4a"

vk = vk_api.VkApi(token=token)

vk._auth_token()

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
conn = sqlite3.connect('db.sqlite')
curs=conn.cursor()
keyboard = {
    "one_time": False,
    "buttons": [
    [get_button(label="Направления", color="primary")],
    [get_button(label="Военная кафедра", color="primary")],
    [get_button(label="Общежитие", color="primary")],
    [get_button(label="Сроки подачи документов", color="primary")],
    ]
}
def doc(nume):
	curs.execute("SELECT text FROM docs WHERE name='"+nume+"'")
	nume=str(curs.fetchone())
	nume=nume[2:-3]
	nume = nume.replace('\\n', '\n')
	return nume
	
def cou(nume):
	nume=str(nume)
	curs.execute("SELECT descr FROM courses WHERE id="+nume+"")
	nume=str(curs.fetchone())
	nume=nume[2:-3]
	nume = nume.replace('\\n', '\n')
	return nume
keyboard_direction = {
    "one_time": False,
    "buttons": [
    [get_button(label="09.03.01", color="positive"), get_button(label="09.03.03", color="positive")],
    [get_button(label="09.03.04", color="positive"), get_button(label="10.03.01", color="positive")],
    [get_button(label="11.03.01", color="positive"), get_button(label="11.03.02", color="positive")],
    [get_button(label="11.03.03", color="positive"), get_button(label="27.03.04", color="positive")],
    [get_button(label="29.03.03", color="positive"), get_button(label="20.03.01", color="positive")],
    [get_button(label="10.05.02", color="positive"), get_button(label="10.05.04", color="positive")],
    [get_button(label="11.05.01", color="positive"), get_button(label="20.05.01", color="positive")],
    [get_button(label="Назад", color="default")],
    ]
}

keyboard_dormitory = {
    "one_time": False,
    "buttons": [
    [get_button(label="Как происходит заселение?", color="positive")],
    [get_button(label="Кого заселяют в первую очередь?", color="positive")],
    [get_button(label="Заселение не льготных студентов", color="positive")],
    [get_button(label="Кому не предоставляется общежитие?", color="positive")],
    [get_button(label="Где находится общежитие?", color="positive")],
    [get_button(label="Назад", color="default")],
    ]
}

keyboard_period = {
    "one_time": False,
    "buttons": [
    [get_button(label="Начало приема документов", color="positive")],
    [get_button(label="Завершение приема документов", color="positive")],
    [get_button(label="Как происходит зачисление?", color="positive")],
    [get_button(label="Назад", color="default")],
    ]
}

keyboard_enrollment = {
    "one_time": False,
    "buttons": [
    [get_button(label="Очная форма", color="negative")],
    [get_button(label="Заочная форма", color="negative")],
    [get_button(label="Контрактная форма", color="negative")],
    [get_button(label="Обратно", color="default")],
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


keyboard_direction = json.dumps(keyboard_direction, ensure_ascii=False).encode('utf-8')
keyboard_direction = str(keyboard_direction.decode('utf-8'))

keyboard_dormitory = json.dumps(keyboard_dormitory, ensure_ascii=False).encode('utf-8')
keyboard_dormitory = str(keyboard_dormitory.decode('utf-8'))

keyboard_period = json.dumps(keyboard_period, ensure_ascii=False).encode('utf-8')
keyboard_period = str(keyboard_period.decode('utf-8'))

keyboard_enrollment = json.dumps(keyboard_enrollment, ensure_ascii=False).encode('utf-8')
keyboard_enrollment = str(keyboard_enrollment.decode('utf-8'))

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            if (body.lower() == "привет" or body.lower() =="хай" or body.lower() =="здарова"):
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "пока":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Прощай!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "клавиатура":
                vk.method("messages.send", {"peer_id": id, "message": "Выберите интересующую вас тему", "random_id": random.randint(1, 2147483647), "keyboard": keyboard})

            elif body == "Направления":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("all_d") ,
                                            "random_id": random.randint(1, 2147483647),
                                            "keyboard": keyboard_direction
                                            }
                          )

            elif body == "09.03.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message":cou(1) ,
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "09.03.03":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(2),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "09.03.04":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(3),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "10.03.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(4),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "11.03.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(5),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "11.03.02":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message":cou(6),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "11.03.03":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(7),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "27.03.04":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(8),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "29.03.03":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message":cou(9) ,
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "20.03.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(10),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "10.05.02":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(11),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "10.05.04":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": cou(12),
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "11.05.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message":cou(13) ,
                           "random_id": random.randint(1, 2147483647)
                           }
                          )
            elif body == "20.05.01":
                vk.method("messages.send",
                          {"peer_id": id,
                           "message":cou(14) ,
                           "random_id": random.randint(1, 2147483647)
                           }
                          )


            elif body == "Военная кафедра":
               
                vk.method("messages.send",
                          {
                              "peer_id": id,
                              "message": doc("mlt_dep"),
                              "random_id": random.randint(1, 2147483647)
                          }
                          )
                military_department.close()

            elif body == "Общежитие":
                vk.method("messages.send",
                          {
                           "peer_id": id,
                           "message": "Выберите интересующую вас тему",
                           "random_id": random.randint(1, 2147483647),
                           "keyboard": keyboard_dormitory
                          }
                          )

            elif body == "Как происходит заселение?":
                vk.method("messages.send", {"peer_id": id,
                                            "message": doc("l1"),
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Кого заселяют в первую очередь?":
                vk.method("messages.send", {"peer_id": id,
                                            "message": doc("l2"),
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Заселение не льготных студентов":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("l3") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Кому не предоставляется общежитие?":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("l4") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Где находится общежитие?":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("l5") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )



            elif body == "Сроки подачи документов":
                vk.method("messages.send",
                          {
                              "peer_id": id,
                              "message": "Выберите интересующую вас тему",
                              "random_id": random.randint(1, 2147483647),
                              "keyboard": keyboard_period
                          }
                          )

            elif body == "Начало приема документов":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("str_d") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Завершение приема документов":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("fin_d") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Как происходит зачисление?":
                vk.method("messages.send",
                          {
                              "peer_id": id,
                              "message": "Выберите форму обучения",
                              "random_id": random.randint(1, 2147483647),
                              "keyboard": keyboard_enrollment
                          }
                          )
            elif body == "Очная форма":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("ochno") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Заочная форма":
                vk.method("messages.send", {"peer_id": id,
                                            "message":doc("zaochno") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )

            elif body == "Контрактная форма":
                vk.method("messages.send", {"peer_id": id,
                                            "message": doc("pay") ,
                                            "random_id": random.randint(1, 2147483647),
                                            }
                          )


            elif body == "Начать":
                vk.method("messages.send", {"peer_id": id, "message": "Выберите интересующую вас тему", "random_id": random.randint(1, 2147483647), "keyboard": keyboard})
            elif body == "Обратно":
                vk.method("messages.send", {"peer_id": id, "message": "Выберите интересующую вас тему", "random_id": random.randint(1, 2147483647), "keyboard": keyboard_period})
            elif body == "Назад":
                vk.method("messages.send", {"peer_id": id, "message": "Выберите интересующую вас тему", "random_id": random.randint(1, 2147483647), "keyboard": keyboard})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(0.5)
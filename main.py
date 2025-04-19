import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '7642849177:AAH6hmG0-gNmGFivSunrxN1kOgII4xXUVKs'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'напиши /staart что бы начать')

@bot.message_handler(commands=['staart'])
def send_image_1(message):
    with open('1.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='1 вапрос /1_question')
@bot.message_handler(commands=['1_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Chap tomondagi yondosh hududdan foydalanib qayrilib olishning ko'rsatilgan qaysi usuli harakat xavfsizligini ta'minlaydi? /1_answers") 

@bot.message_handler(commands=['1_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Faqat o'ng tomondagi rasmda (a) ", callback_data= 'a'))
    markup.add(InlineKeyboardButton("Faqat chap tomondagi rasmda (b) ", callback_data="b"))
    markup.add(InlineKeyboardButton("Ikkisida ham (c) ", callback_data="c"))

    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a')
def send_photo_1_1(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /2__question ')
@bot.callback_query_handler(func=lambda call: call.data == 'b')
def send_photo_1_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /1_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c')
def send_photo_1_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /1_answers')




@bot.message_handler(commands=['2__question'])
def send_image_1(message):
    with open('2.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='2 вапрос /2_qusetion')
@bot.message_handler(commands=['2_qusetion'])        
def quation(message):
    bot.send_message(message.chat.id, "Siz chorrahada chapga burilishda qaysi transport vositasiga yo'l berishingiz lozim? /2_answers") 

@bot.message_handler(commands=['2_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Avtobusha(a) ", callback_data= 'a_2'))
    markup.add(InlineKeyboardButton("YEngil avtomobilga(b) ", callback_data="b_2"))
    markup.add(InlineKeyboardButton("Hech biriga(c) ", callback_data="c_2"))

    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_2')
def send_photo_2_1(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /2_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'b_2')
def send_photo_2_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /2_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c_2')
def send_photo_2_3(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /3__question')




@bot.message_handler(commands=['3__question'])
def send_image_1(message):
    with open('3.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='3 вапрос /3_question')
@bot.message_handler(commands=['3_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Shatakka olingan avtobusda odam tashishga ruxsat beriladimi? /3_answers") 

@bot.message_handler(commands=['3_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Taqiqlanadi(a) ", callback_data= 'a_3'))
    markup.add(InlineKeyboardButton("Faqat o'tirgan holda tashishga ruxsat beriladi (b) ", callback_data="b_3"))
    markup.add(InlineKeyboardButton("Ruxsat beriladi (c) ", callback_data="c_3"))

    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_3')
def send_photo_3_1(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /4__question')
@bot.callback_query_handler(func=lambda call: call.data == 'b_3')
def send_photo_3_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /3_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c_3')
def send_photo_3_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /3_answers')




@bot.message_handler(commands=['4__question'])
def send_image_1(message):
    with open('3.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='4 вапрос /4_question')
@bot.message_handler(commands=['4_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Yo'l-transport hodisasi bu /4_answers") 

@bot.message_handler(commands=['4_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Transport vositasining yo'lda harakatlanishi jarayonida ro'y bergan, fuqarolarning halok bo'lishiga yoki sog'lig'iga zarar yetishiga, transport vositalari, inshootlar, yuklarning shikastlanishi yoxud boshqa moddiy zarar yetishiga sabab bo'lgan hodisa (a) ", callback_data= 'a_4'))
    markup.add(InlineKeyboardButton("Yo'l harakati qatnashchilarining yo'l-transport hodisalari va ularning oqibatlaridan himoyalanganlik darajasini aks ettiruvchi yo'l harakati holati (b) ", callback_data="b_4"))

    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_4')
def send_photo_4_1(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /5__question')
@bot.callback_query_handler(func=lambda call: call.data == 'b_4')
def send_photo_4_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /4_answers')




@bot.message_handler(commands=['5__question'])
def send_image_1(message):
    with open('5.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='5 вапрос /5_question')
@bot.message_handler(commands=['5_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Qaysi transport vositasiga harakatlanish taqiqlangan?  /5_answers") 

@bot.message_handler(commands=['5_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Xech kimga taqiqlanmagan  (a) ", callback_data= 'a_5'))
    markup.add(InlineKeyboardButton("Motosiklga  (b) ", callback_data="b_5"))
    markup.add(InlineKeyboardButton("Yuk avtomobiliga (c) ", callback_data="c_5"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_5')
def send_photo_5_1(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /5_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'b_5')
def send_photo_5_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /5_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c_5')
def send_photo_5_3(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /6__question')





@bot.message_handler(commands=['6__question'])
def send_image_1(message):
    with open('6.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='6 вапрос /6_question')
@bot.message_handler(commands=['6_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Ushbu yo'l belgisi:   /6_answers") 

@bot.message_handler(commands=['6_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Oldinda boshqariladigan to'suvchi qurilma borligini bildiradi   (a) ", callback_data= 'a_6'))
    markup.add(InlineKeyboardButton("Chorraxa oldida to'suvchi qurilma borligini bildiradi   (b) ", callback_data="b_6"))
    markup.add(InlineKeyboardButton("Qatnov qismida to'suvchi qurilma borligini bildiradi (c) ", callback_data="c_6"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_6')
def send_photo_6_1(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /7__question')
@bot.callback_query_handler(func=lambda call: call.data == 'b_6')
def send_photo_6_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /6_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c_6')
def send_photo_6_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /6_answers')





@bot.message_handler(commands=['7__question'])
def send_image_1(message):
    with open('3.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='7 вапрос /7_question')
@bot.message_handler(commands=['7_question'])        
def quation(message):
    bot.send_message(message.chat.id, "108 km/s tezlikda harakatlanayotgan transport vositasi 1 sekundda qancha masofani bosib o'tadi?   /7_answers") 

@bot.message_handler(commands=['7_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("15m   (a) ", callback_data= 'a_7'))
    markup.add(InlineKeyboardButton("30m   (b) ", callback_data="b_7"))
    markup.add(InlineKeyboardButton("25m   (c) ", callback_data="c_7"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_7')
def send_photo_7_1(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /7_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'b_7')
def send_photo_7_2(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /8__question')
@bot.callback_query_handler(func=lambda call: call.data == 'c_7')
def send_photo_7_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /7_answers')





@bot.message_handler(commands=['8__question'])
def send_image_1(message):
    with open('3.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='8 вапрос /8_question')
@bot.message_handler(commands=['8_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Piyodalar to'xtab turgan avtobus va trolleybusning qaysi tomonidan yo'lni kesib o'tishlari kerak?    /8_answers") 

@bot.message_handler(commands=['8_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Oldi tomonidan  (a) ", callback_data= 'a_8'))
    markup.add(InlineKeyboardButton("Orqa tomonidan  (b) ", callback_data="b_8"))
    markup.add(InlineKeyboardButton("Istalgan tomonidan (c) ", callback_data="c_8"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_8')
def send_photo_8_1(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /8_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'b_8')
def send_photo_8_2(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /9__question')
@bot.callback_query_handler(func=lambda call: call.data == 'c_8')
def send_photo_8_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /8_answers')




@bot.message_handler(commands=['9__question'])
def send_image_1(message):
    with open('9.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='9 вапрос /9_question')
@bot.message_handler(commands=['9_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Usbu belgi... /9_answers") 

@bot.message_handler(commands=['9_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Oldinda transport vositalarining tirbandligi haqida ogohlantiradi.  (a) ", callback_data= 'a_9'))
    markup.add(InlineKeyboardButton("Oldinda transport vositalari orasida xavfsiz oraliqni ta'minlash lozimligi haqida ogohlantiradi (b) ", callback_data="b_9"))
    markup.add(InlineKeyboardButton("Oldinda harakatlanish intensivligi yuqoriligi haqida ogohlantiradi. (c) ", callback_data="c_9"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_9')
def send_photo_9_1(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /10__question')
@bot.callback_query_handler(func=lambda call: call.data == 'b_9')
def send_photo_9_2(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /9_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'c_9')
def send_photo_9_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /9_answers')




@bot.message_handler(commands=['10__question'])
def send_image_1(message):
    with open('3.jpg','rb') as img:
        bot.send_photo(message.chat.id, img, caption='10 вапрос /10_question')
@bot.message_handler(commands=['10_question'])        
def quation(message):
    bot.send_message(message.chat.id, "Yengil avtomobil burilishda ag'darilib ketishga qarshi turg'unroq:  /10_answers") 

@bot.message_handler(commands=['10_answers']) 
def welcome(message):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("Yo'lovchilari bilan yuksiz   (a) ", callback_data= 'a_10'))
    markup.add(InlineKeyboardButton("Yo'lovchisiz va yuksiz  (b) ", callback_data="b_10"))
    markup.add(InlineKeyboardButton("Yo'lovchi va yuki bilan  (c) ", callback_data="c_10"))
    markup.add(InlineKeyboardButton("Yo'lovchisiz, biroq yuqori yukxonasidagi yuki bilan  (d) ", callback_data="d_10"))
 
    bot.send_message(message.chat.id, 'выберите правильный ответ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_10')
def send_photo_10_1(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /10_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'b_10')
def send_photo_10_2(call):
    with open('ok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили правильно /Congratulation')
@bot.callback_query_handler(func=lambda call: call.data == 'c_10')
def send_photo_10_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /10_answers')
@bot.callback_query_handler(func=lambda call: call.data == 'd_10')
def send_photo_10_3(call):
    with open('dok.png','rb') as img:
        bot.send_photo(call.message.chat.id, img, caption='вы ответили не правильно /10_answers')



@bot.message_handler(commands=['Congratulation'])
def Congratulation(message):
    bot.send_message(message.chat.id, 'Поздравляем от имени нашей компании вы прошли тест  но не так уж и хорошо можно было и лутче  (￢︿̫̿￢☆)')

bot.polling()







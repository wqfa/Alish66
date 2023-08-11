import telebot
import requests
tt = ("6686522734:AAEIpbf8eGPs1DAdjiHldcC_BZecRkFKdtY") 
bot = telebot.TeleBot(tt)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    chat_id = message.chat.id    
    if 't.me' in text:
        url = "https://ava-tar.online/api/free_view?jack=" + text
        response = requests.get(url)             
        bot.reply_to(message, "تم تقديم طلب الرشق بنجاح. شكرًا على الثقة بنا!")
    else:        
        photo1 = "https://imgbox.com/SFwuu01f"
        caption = """. — — — — — — — — — — .
        اهلا بك في بوت رشق مشاهدات تيليجرام ارسل رابط المنشور وانتضر
        . — — — — — — — — — — .
        - 𝗙𝗿𝗢𝗺 𝗧𝗲𝗹𝗲: @lll7I3
        - 𝗙𝗿𝗢𝗺 𝗖𝗵 𝗧𝗲𝗹𝗲: @IIl7l2"""
        
        reply_markup = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text=" - Programeer", url="https://t.me/HisokaTeam")
        reply_markup.add(url_button)        
        bot.send_photo(chat_id, photo1, caption=caption, reply_markup=reply_markup) 
print(" - Go Start Bot. ")        
bot.polling()

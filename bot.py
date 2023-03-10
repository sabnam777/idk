import telebot

TOKEN = '<insert your bot token here>'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def send_welcome(message):

    # Greet the user and display an image

    bot.send_message(message.chat.id, "Welcome to MyBot!")

    photo = open('welcome_image.jpg', 'rb')

    bot.send_photo(message.chat.id, photo)

    # Create keyboard with options

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)

    know_more_button = telebot.types.KeyboardButton('Know More')

    report_button = telebot.types.KeyboardButton('Report')

    claim_reward_button = telebot.types.KeyboardButton('Claim Reward')

    refer_button = telebot.types.KeyboardButton('Refer a Friend')

    keyboard.add(know_more_button, report_button, claim_reward_button, refer_button)

    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)

def handle_all_messages(message):

    if message.text == 'Know More':

        # Display information about the bot's features and purpose

        bot.send_message(message.chat.id, "MyBot is a reporting bot that allows users to report inappropriate behavior "

                                          "in groups and channels. Reports earn users points, which can be redeemed "

                                          "for rewards. To report someone, simply click on the Report button and "

                                          "select the group or channel where the behavior occurred.")

    elif message.text == 'Report':

        # Display message explaining how to report a user in a group or channel to earn points

        report_keyboard = telebot.types.InlineKeyboardMarkup()

        groups_button = telebot.types.InlineKeyboardButton('Groups', callback_data='groups')

        channels_button = telebot.types.InlineKeyboardButton('Channels', callback_data='channels')

        premium_button = telebot.types.InlineKeyboardButton('Premium Reports', callback_data='premium')

        report_keyboard.row(groups_button, channels_button)

        report_keyboard.row(premium_button)

        bot.send_message(message.chat.id, "To report someone, select the group or channel where the behavior occurred:",

                         reply_markup=report_keyboard)

    elif message.text == 'Claim Reward':

        # Display message showing user their points and allowing them to redeem rewards

        bot.send_message(message.chat.id, "You have earned 50 points!")

        reward_keyboard = telebot.types.InlineKeyboardMarkup()

        premium_button = telebot.types.InlineKeyboardButton('Premium', url='https://example.com/premium')

        donate_button = telebot.types.InlineKeyboardButton('Donate', url='https://example.com/donate')

        claim_button = telebot.types.InlineKeyboardButton('Claim', callback_data='claim')

        reward_keyboard.row(premium_button, donate_button)

        reward_keyboard.row(claim_button)

        bot.send_photo(message.chat.id, open('profile_pic.jpg', 'rb'), caption="Name: John Smith\nUsername: @john_smith\n"

                                                                              "User ID: 123456\nDC: US\n\nSelect an "

                                                                              "option to redeem your points:",

                       reply_markup=reward_keyboard)

    elif message.text == 'Refer a Friend':

        # Generate referral link for user to share with friends

        referral_link = 'https://t.me/mybot?start=referral123'

        bot.send_message(message.chat.id, f"Use this referral link to invite your friends to MyBot:\n\n{referral_link}")

 @bot.callback_query_handler(func=lambda call: call.data == 'report')

def report_callback(call):

    message_text = 'To report a user and earn coins, please select an option below:\n\n'

    message_text += 'Groups:\n'

    message_text += 'Group 1 - https://t.me/group1\n'

    message_text += 'Group 2 - https://t.me/group2\n\n'

    message_text += 'Channels:\n'

    message_text += 'Channel 1 - https://t.me/channel1\n'

    message_text += 'Channel 2 - https://t.me/channel2\n\n'

    message_text += 'Premium Reports:\n'

    message_text += 'Group 3 - https://t.me/group3\n\n'

    message_text += 'Please make sure to send a screenshot of your report to the bot inbox after you report to receive your coins.'

    bot.send_message(chat_id=call.message.chat.id, text=message_text)

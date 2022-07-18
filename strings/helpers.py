#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>مرحبا اليك اوامر الادمن:</u>**

⚡️ <u>**و التكرار التخطي المحدد:**</u>
/skip او /cskip + العدد
- لتخطي اغنيه او اكثر من قائمه التشغيل
/loop + الرقم - لتكرار الاغنيه المشغله ( ارقام بين  1- 10 ) 
•─━──━──━─━──━──━─•
⚡️ <u>**اوامر رفع وتنزيل ادمن:**</u>
- يمكن لهذه الاشخاص استخدام اوامر البوت بدون رفعه مشرف في الجروب
/auth + يوزر الشخص او بالرد - لاضافته ادمن في المجموعه
/unauth + المعرف او بالرد - لازالته من قائمه الادمنيه
/authusers - لعرض قائمه الادمنيه بالمجموعه.
•─━──━──━─━──━──━─•
⚡️ **<u>اوامر قوائم الشتغيل الخاصه بالبوت</u>**
/playlist - تحقق من قائمة التشغيل المحفوظة على الخوادم.
/deleteplaylist - حذف أي موسيقى محفوظة في قائمة التشغيل الخاصة بك
/play - ابدأ تشغيل قائمة التشغيل المحفوظة من الخوادم."""


HELP_2 = """✅<u>**اوامر تشغيل البوت في القناه والجروب:**</u>

⚡️ اوامر تشغيل البوت في الجروب

- لتشغيل اغنيه :  تشغيل او شغل او /play
- لتشغيل فيديو : فيديو او /vplay
- لأنهاء الاغنيه : ايقاف او انهاء او /stop
- لايقاف الاغنيه مؤقت : وقف او /pause
- لتكملة الاغنيه  : كمل او /resume
- لتخطي الاغنيه : تخطي او /skip
- لكتم البوت في الكول : اسكت او /mute
- لألغاء كتم البوت في الكول : اتكلم او /unmute
•─━──━──━─━──━──━─•
⚡️ اوامر تشغيل البوت في القناه
1 قم بربط القناه ب اي جروب
2 قم برفع البوت مشرف بالقناه وبالجروب
3 استخدم ام /channelplay + معرف القناه للربط
• ثم استخمد الاوامر بالاسفل للتشغيل
- لتشغيل اغنيه : ق تشغيل او ق شغل او /cplay
- لتشغيل فيديو : ق فيديو او /cvplay
- لأنهاء الاغنيه  : ق ايقاف او ق انهاء او /cstop
- لايقاف الاغنيه مؤقت : ق وقف او cpause
- لتكملة الاغنيه  : ق كمل او /cresume
- لتخطي الاغنيه : تخطي او /cskip
- لكتم البوت في الكول  : ق اسكت او /cmute
- لألغاء كتم البوت في الكول  : ق اتكلم او /cunmute
•─━──━──━─━──━──━─•
/seek + الرقم - لتقديم الاغنيه للامام 
مثال : /seek 10 - يقدم الاغنيه عشر ثواني
/seekback + الرقم  - يرجع للخلف."""


HELP_3 = """✅<u>**الاوامر الخاصه بالبوت:**</u>

/stats - للحصول علي احصائيات البوت العالميه والخاصه البوت
/sudolist - لعرض قائمه المطورين بالبوت

/lyrics + اسم الاغنيه - للبحث علي كلمات الاغنيه

/song + اسم اللاغنيه او رابط الاغنيه - للتحميل من اليوتيوب بصيغه mp3 , mp4
/player -  للحصول علي لوحه تشغيل تفاعليه

/queue او /cqueue- تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - للحصول علي قائمه الاوامر
/ping - تحقق من إحصائيات ذاكرة الوصول العشوائي ووحدة المعالجة المركزية وما إلى ذلك الخاصة بالبوت.
/settings - لعرض اعدادات المجموعه الكامه باستخدم الازرار"""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/vplaymode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""

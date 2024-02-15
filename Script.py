class script(object):  
    START_TXT = """<b>👾 Hello {user}.

I'm {bot}.


I Can Provide Movie For You Just Add Me In Your Group or Join Our Group</b>"""
    
    HELP_TXT = "👾 Hey {}\n☘️ Help Menu"

    ABOUT_TXT = """<b> Movie Downloader LK

🙍‍♂️ Owner : <a herf=https://t.me/PremiumCracker>Supun</a>
👨‍💻 Developer : <a herf=https://t.me/Chxrith>CHXRITH</a>
! Version : Movie Downloader Lk v1.0.0</b>"""
   
    SOURCE_TXT = """<b>NOTE:</b> bot is on testing.."""

    FILE_TXT = """<b>➤ HELP FoR FILE SToRE</b>

<i>BY UsING THIs MoDULE YoU CAN SToRE FILEs IN MY DATABAsE AND I WILL GIvE YoU A PERMANENT LINK  To AccEss THE SAvED FILEs. If YoU WANT To ADD FILEs FRoM A PUBLIc CHANNEL SEND THE FILE LINK ONLY  OR YoU WANT To ADD FILEs FRoM A  PRIvATE CHANNEL YoUR MUsT MAKE ME ADMIN ON THE CHANNEL To AccEss FILEs</i>

<b>⪼ CoMMAND & UsAGE</b>
➪ /link > REPLY To ANY MEDIA To GET THE LINK 
➪ /batch > To CREATE LINK FoR MULTIPLE MEDIA

<b>⪼ EG:</b>
</code>/batch https://t.me/bbcnbychxrith/2 https://t.me/bbcnbychxrith/3</code>"""
  
    FILTER_TXT = "SELEcT WHIcH ONE YoU WANT...✨"
    
    GLOBALFILTER_TXT = """<b>HELP FoR GLoBAL FILTERs</b>

<i>FILTER Is THE FEATURE WERE UsERs CAN SET AUToMATED REPLIEs FoR A PARTIcULAR KEYWoRD AND BoT  WILL REsPoND WHENEvER A KEYWoRD Is FoUND THE MEssAGE</i>

<b>NoTE:</b>
THIs MoDULE ONLY WoRKs FoR MY ADMINs

<b>CoMMANDs AND UsAGE:</b>
• /gfilter - To ADD GLoBAL FILTERs
• /gfilters - To VIEW LIsT Of ALL GLoBAL FILTERs
• /delg - To DELETE A SPEcIfIc GLoBAL FILTER
• /delallg - To DELETE ALL GLoBAL FILTERS

• /g_filter off UsE THIs CoMMoAND + on/offf IN YoUR GRoUP To CoNTRoL GLoBAL FILTER IN YoUR GRoUP"""

    MANUELFILTER_TXT = """<b>HELP FoR FILTERs</b>

<i>FILTER Is THE FEATURE WERE UsERs CAN SET AUToMATED REPLIEs FoR A PARTIcULAR KEYWoRD AND BoT  WILL REsPoND WHENEvER A KEYWoRD Is FoUND THE MEssAGE</i>

<b>NoTE:</b>
1. THIs BoT SHoULD HAvE ADMIN PRIvILLAGE.
2. ONLY ADMINs CAN ADD FILTERs IN A CHAT.
3. ALERT BUTToNs HAvE A LIMIT Of 64 CHARAcTERs.

<b>CoMMANDs AND UsAGE:</b>
• /filter - ADD A FILTER IN CHAT
• /filters - LIsT ALL THE FILTERs Of A CHAT
• /del - DELETE A SPEcIfIc FILTER IN CHAT
• /delall - DELETE THE WHoLE FILTERs IN A CHAT (CHAT OWNER ONLY)

• /g_filter off UsE THIs CoMMoAND + on/offf IN YoUR GRoUP To CoNTRoL GLoBAL FILTER IN YoUR GRoUP"""

    BUTTON_TXT = """<b>HELP FoR BUTToNs</b>

<i>THIs BoT SUPPoRTs BoTH URL AND ALERT INLINE BUTToNs.</i>

<b>NoTE:</b>
1. TELEGRAM WILL NoT ALLoWs YoU To SEND BUTToNs WITHoUT ANY CoNTENT, So CoNTENT Is MANDAToRY.
2. THIs BoT SUPPoRTs BUTToNs WITH ANY TELEGRAM MEDIA TYPE.
3. BUTToNs SHoULD BE PRoPERLY PARsED As MARKDoWN FoRMAT

<b>URL BUTToNs:</b>
[BUTToN TExT](buttonurl:xxxxxxxxxxxx)

<b>ALERT BUTToNs:</b>
[BUTToN TExT](buttonalert:THIs Is AN ALERT MEssAGE)"""

    AUTOFILTER_TXT = """<b>HELP FoR AUToFILTER</b>

<Ai>AUTo FILTER Is THE FEATURE To FILTER & SAvE THE FILEs AUToMATIcALLY FRoM CUANNEL To GRoUP. YoU CAN UsE THE FoLLoWING CoMMAND To oN/off THE AUToFILTER IN YoUR GRoUP</i>

• /autofilter on - AUTofILTER ENABLE IN YoR cHAT
• /autofilter off - AUTofILTER DIsABLE IN YoUR cHAT

<Ob>OTHER CoMMANDs:</b>
• /set_template - SET IMDB TEMPLATE FoR YoUR GRoUP 
• /get_template - GET CURRENT IMDB TEMPLATE FoR YoUR GRoUP"""

    CONNECTION_TXT = """<b>HELP FoR CoNNEcTIoNs</b>

<i> UsED To CoNNEcT BoT To PM FoR MANAGING FILTERs. IT HELPs To AvoID SPAMMING IN GRoUPs</i>

<b>NOTE:</b>
• ONLY ADMINs CAN ADD A CONNECTION.
• SEND /connect FoR CoNNEcTING ME To UR PM

<Cb>CoMMANDs AND UsAGE:</b>
• /connect - CoNNEcT A PARTIcULAR CHAT To YoUR PM
• /disconnect - DIscoNNEcT FRoM A CHAT
• /connections - LIsT ALL YoUR CoNNEcTIoNs"""

    ADMIN_TXT = """<b>HELP FOR ADMINS</b>

<b>CoMMAND & USAGE</b>
☘️ /logs - To GET THE REcENT ERRoRS
☘️ /delete - To DELETE A SPEcIFIc FILE FRoM DB
☘️ /deleteall - To DELETE ALL FILEs FRoM DB
☘️ /users - To GET LIST OF MY USERS AND IDS
☘️ /chats - To GET LIST OF MY CHATS AND IDS
☘️ /channel - To GET LIST OF ToTAL CoNNEcTED CHANNELS
☘️ /broadcast - To BRoADcAST A MESSAGE To ALL USERS
☘️ /group_broadcast - To BRoADcAsT A MEssAGE To ALL CoNNEcTED GRoUPs
☘️ /leave  - WITH CHAT ID To LEAvE FRoM A CHAT
☘️ /disable  - WITH CHAT ID To DISABLE A CHAT
☘️ /invite - WITH CHAT ID To GET THE INvITE LINK Of ANY CHAT WHERE THE BoT Is ADMIN
☘️ /ban_user  - WITH ID To BAN A USER
☘️ /unban_user  - WITH ID To UNBAN A USER
☘️ /restart - To REsTART THE BoT
☘️ /clear_junk - CLEAR ALL DELETE AccoUNT & BLocKED AccoUNT IN DATABAsE
☘️ /clear_junk_group - CLEAR ADD REMovED GRoUP OR DEAcTIvATED GRoUPs ON DB"""


    STATUS_TXT = """<b>📁 TOTAL FILES: <code>{}</code>
🙍‍♂️ TOTAL USERS: <code>{}</code>  
💬 TOTAL CHATS: <code>{}</code>
📈 USED DB SIZE: <code>{}</code>
📉 FEEE DB SIZE: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>📢 NEW_GRoUP

🧩 GROUP: {a}
💡 GROUP ID: <code>{b}</code>
🔗 LINK: @{c}
🙍‍♂️ MEMBERS: <code>{d}</code>
🎖 ADDED BY: {e}

🤖 BY: @{f}</b>

[ #newgrp ]"""
  
    LOG_TEXT_P = """📢 NEW_USER
    
🎗️ USER-ID: <code>{}</code>
☘️ NAME: {}
🧤 USERNAME: @{}

🤖 BY: @{}</b>

[ #newuser ]
"""
  
    GROUPMANAGER_TXT = """<b>Help for Groupmanager</b>

<i>This Is Help of Your Group Managing. This Will Work Only for Group Admins</i>

<b>Command & Usage:</b>
• /Inkick - Command With Reouired Arguments and I Will Kick Members From Group.
• /Instatus - To Check Current Status of Chat Member From Group.
• /Dkick - To Kick Deleted Accounts
• /Ban - To Ban a User Form the Group
• /Unban - Unban the Banned User
• /Tban - Temporary Ban a User
• /Mute - To Mute a User
• /Unmute - To Unmute the Muted User
• /Tmute - With Value to Mute up to Particular Time Eg: <Code>/Tmute 2H</Code> to Mute 2HOUR Values Is (M/H/D)
• /Pin - To Pin a Message on Your Chat
• /Unpin - To Unpin the Message on Your Chat
• /Purge - Delete All Messages From the Replied to Message, to the Current Message """

    EXTRAMOD_TXT = """<b>Help for Extra Module</b>

<i>Just Send Any Image to Edit Image ✨</i>

<b>Commands & Usage:</b>
• /ID - Get ID of a Specifed User
• /Info  - Get Information About a User
• /Imdb  - Get the Film Information From Imdb Source
• /Paste [Text] - Paste the Given Text on Pasty
• /Tts [Text] - Convert Text to Speech
• /Telegraph - Send Me This Command Reply With Picture or Vide Under (5MB)
• /Json - Reply With Any Message to Get Message Info (Usefull for Group)
• /Written - Reply With Text to Get File (Usefull for Coders)
• /Carbon - Reply With Text to Get Carbonated Image
• /Font [Text] - To Change Your Text Fonts to Fancy Font
• /Share - Reply With Text to Get Text Sharable Link
• /Song [Name] - To Search the Song in YouTube
• /Video [Link] - To Download the YouTube Video"""    
    
    CREATOR_REQUIRED = "!<b>YOU HAVE TO BE THE GROUP CREATOR TO DO THAT</b>"
      
    INPUT_REQUIRED = "! **ARGUMEN RQUIRED**"
      
    KICKED = "✔️ SUCCESSFULLY KICKED {} MEMBERS ACCORDING TO THE ARGUMENTS PROVIDED"
      
    START_KICK = "REMOVING INACTIVE MEMBERS THIS MAY TAKE A WHILE"
      
    ADMIN_REQUIRED = "!<b>I'AM NOT ADMIN IN THIS CHAT SO PLEASE ADD ME AGAIN WITH ALL ADMIN PERMISSION</b>"
      
    DKICK = "✔️ KICKED {} DELETED ACCOUNTS SUCCESSFULLY"
      
    FETCHING_INFO = "<b>WAIT I WILL TAKE THE ALL INFO</b>"
   
    SERVER_STATS = """📊 SERVER STATS:
 
UPTIME: {}
CPU USAGE: {}%
RAM USAGE: {}%
ToTAL DISK: {}
USED DISK: {} ({}%)
FREE DISK: {}"""
    
    BUTTON_LOCK_TEXT = ""👾 Hey {query},
    ⛔ This Is Not For U. Search Ur Self""
   
    FORCE_SUB_TEXT = "SoRRY BRo YoUR NoT JoINED MY CHANNEL So PLEAsE CLIcK JoIN BUTToN To JoIN MY CHANNEL AND TRY AGAIN"
   
    WELCOM_TEXT = """👾 Hey {user},

🎗️ Welcome to {chat}.
☘️ Share & Support Request U Wanted Movies."""
  
    IMDB_TEMPLATE = """<b>☘️ QUERY: {query}</b>

🏷 TITLE: <a href={url}>{title}</a>
🎭 GENRES: {genres}
📆 YEAR: <a href={url}/releaseinfo>{year}</a>
🌟 RATING: <a href={url}/ratings>{rating}</a>/10"""

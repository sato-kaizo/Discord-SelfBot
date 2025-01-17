import discord
import ctypes
import json
import os
import random
import requests
import asyncio
import string
import time
import datetime
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

with open('config.json') as f:
    config = json.load(f)

__version__ = "2.1"
token = config.get('token')
prefix = config.get('prefix')

start_time = datetime.datetime.utcnow()

class MyClient(discord.Client):
    async def on_ready(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"SelfBot v{__version__} - Made By Astraa")
        os.system('cls')
        print(f"""\n\n{Fore.RESET}                            ██████╗ ████████╗██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                           ██╔═══██╗╚══██╔══╝██║██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                           ██║██╗██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ██║██║██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ╚█║████╔╝   ██║   ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚╝╚═══╝    ╚═╝   ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""".replace('█', f'{b}█{y}'))
        print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}raadev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://git\n{y}------------------------------------------------------------------------------------------------------------------------\n""")
        print(f"""{y}[{b}+{y}]{w} SelfBot Informations:\n
\t{y}[{w}#{y}]{w} Version: v{__version__}
\t{y}[{w}#{y}]{w} Logged in as: {self.user}
\t{y}[{w}#{y}]{w} User ID: {self.user.id}\n\n
{y}[{b}+{y}]{w} Settings View:\n
\t{y}[{w}#{y}]{w} SelfBot Prefix: {prefix}
\t{y}[{w}#{y}]{w} Cached Users: {len(self.users)}
\t{y}[{w}#{y}]{w} Guilds Scraped: {len(self.guilds)}\n\n\n
{y}[{Fore.GREEN}!{y}]{w} SelftBot Online!""")

    async def on_message(self, message):
        if message.author != self.user:
            return
        
            
        if message.content == f"{prefix}help":
            await message.delete()
            embed = f"""**Astraa SelfBot | Prefix: `{prefix}`**\n
        > :pushpin: `GENERAL`\n*Shows all general commands* (like prefix, shutdown, ...)
        > :notepad_spiral: `USEFUL`\n*Shows all useful commands* (like tts, hastebin, nitro, ...)
        > :tools: `ATIO`\n*Shows all ATIO Tool commands* (like tokeninfo, serverinfo, ...)
        > :space_invader: `EXPLOIT`\n*Shows all exploit commands* (like hide, edit, bypassblock, ...)
        > :woozy_face: `FUN`\n*Shows all fun commands* (like magik, hack, minesweeper, ...)
        > :pager: `SERVER`\n*Shows all server commands* (like copy, massban, massdm, ...)
        > :incoming_envelope: `MESSAGE`\n*Shows all message commands* (like lenny, bold, empty, ...)"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help general":
            await message.delete()
            embed = f"""**GENERAL COMMANDS | Prefix: `{prefix}`**\n
        > :handshake: `{prefix}help <category>`\n*Returns all commands of that category*
        > :electric_plug: `{prefix}ping`\n*Returns the bot's latency*
        > :hourglass: `{prefix}uptime`\n*Return how long the selfbot has been running*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help useful":
            await message.delete()
            embed = f"""**USEFUL COMMANDS | Prefix: `{prefix}`**\n
        > :cold_face: `{prefix}astraa`\n*Show my social networks* 
        > :gear: `{prefix}geoip <ip>`\n*Looks up the ip's location*
        > :globe_with_meridians: `{prefix}pingweb <website-url>`\n*Pings a website to see if it's up*
        > :cyclone: `{prefix}gentoken <user>`\n*Returns the user's token* 
        > :no_entry: `{prefix}quickdelete <message>`\n*Quickly delete your message after sending it*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help atio":
            await message.delete()
            embed = f"""**ATIO COMMANDS | Prefix: `{prefix}`**\n
        > :page_facing_up: `{prefix}tokeninfo <token>`\n*Scrape info with a token*
        > :broom: `{prefix}cleardm <amount>`\n*Delete all dm with a user*
        > :house: `{prefix}hypesquad <house>`\n*Change your hypesquad badge*
        > :page_facing_up: `{prefix}serverinfo`\n*Get all infos about a discord server*
        > :crystal_ball: `{prefix}nitro`\n*Generates a random nitro code*
        > :wastebasket: `{prefix}whremove <webhook>`\n*Delete the selected webhook*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help exploit":
            await message.delete()
            embed = f"""**EXPLOIT COMMANDS | Prefix: `{prefix}`**\n
        > :detective: `{prefix}hidemention <display> <hidden>`\n*Hide messages inside other messages*
        > :wrench: `{prefix}edit <message>`\n*Move the position of the (edited) tag*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help fun":
            await message.delete()
            embed = f"""**FUN COMMANDS | Prefix: `{prefix}`**\n
        > :airplane: `{prefix}9/11`\n*Sends a 9/11 attack*
        > :sweat_drops: `{prefix}cum`\n*Makes you cum*
        > :bomb: `{prefix}minesweeper`\n*Play a game of minesweeper*
        > :dark_sunglasses: `{prefix}1337 <message>`\n*Talk like a hacker*
        > :eggplant: `{prefix}dick <user>`\n*Returns the user's dick size*
        > :recycle: `{prefix}reverse <message>`\n*Sends the message but in reverse-order*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help server":
            await message.delete()
            embed = f"""**SERVER COMMANDS | Prefix: `{prefix}`**\n
        > :writing_hand: `{prefix}spam <amount> <message>`\n*Spams a message*
        > :barber: `{prefix}guildicon`\n*Scrape Guild icon*
        > :city_sunset: `{prefix}guildbanner`\n*Scrape Guild banner*
        > :pencil2: `{prefix}guildrename <name>`\n*Rename server*
        > :wastebasket: `{prefix}purge <amount>`\n*Purges the amount of messages*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}help message":
            await message.delete()
            embed = f"""**MESSAGE COMMANDS | Prefix: `{prefix}`**\n
        > :slight_smile: `{prefix}shrug`\n*Returns ¯\_(ツ)_/¯*
        > :smile: `{prefix}lenny`\n*Returns ( ͡° ͜ʖ ͡°)*
        > :hushed: `{prefix}fliptable`\n*returns (╯°□°）╯︵ ┻━┻*
        > :unamused: `{prefix}unflip`\n*returns ┬─┬ ノ( ゜-゜ノ)*
        > :ghost: `{prefix}empty`\n*Send a empty message*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        
        
        elif message.content == f"{prefix}uptime":
            await message.delete()
            now = datetime.datetime.utcnow()
            delta = now - start_time
            hours, remainder = divmod(int(delta.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            if days:
                time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
            else:
                time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
            uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
            await message.channel.send(uptime_stamp)
        elif message.content == f"{prefix}ping":
            await message.delete()
            before = time.monotonic()
            message_to_send = await message.channel.send("Pinging...")
            await message_to_send.edit(content=f"`{int((time.monotonic() - before) * 1000)} ms`")


        elif message.content == f"{prefix}astraa":
            await message.delete()
            embed = f"""**MY SOCIAL NETWORKS | Prefix: `{prefix}`**\n
        > :pager: `Discord Server`\n*https://discord.gg/PKR7nM9j9U*
        > :computer: `GitHub Page`\n*https://github.com/AstraaDev*
        > :robot: `SelfBot Project`\n*https://github.com/AstraaDev/Discord-SelfBot*"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content.startswith(f"{prefix}geoip"):
            await message.delete()
            addr = message.content[len(f"{prefix}geoip "):].strip()
            if addr is None:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `geoip <ip>`')
                return
            try:
                r = requests.get(f'http://ip-api.com/json/{addr}')
                geo = r.json()
                embed = f"""**GEOLOCATE IP | Prefix: `{prefix}`**\n
        > :pushpin: `IP`\n*{geo['query']}*
        > :globe_with_meridians: `Country-Region`\n*{geo['country']} - {geo['regionName']}*
        > :department_store: `City`\n*{geo['city']} ({geo['zip']})*
        > :map: `Latitute-Longitude`\n*{geo['lat']} - {geo['lon']}*
        > :satellite: `ISP`\n*{geo['isp']}*
        > :robot: `Org`\n*{geo['org']}*
        > :alarm_clock: `Timezone`\n*{geo['timezone']}*
        > :electric_plug: `As`\n*{geo['as']}*"""
                await message.channel.send(embed, file=discord.File("img/astraa.gif"))
            except Exception as e:
                 await message.channel.send(f'> **[**ERROR**]**: Unable to geolocate ip\n> __Error__: `{str(e)}`')
        elif message.content.startswith(f"{prefix}pingweb"):
            await message.delete()
            addr = message.content[len(f"{prefix}pingweb "):].strip()
            if addr is None:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `pingweb <website>`')
                return
            try:
                r = requests.get(addr).status_code
            except Exception as e:
                 await message.channel.send(f'> **[**ERROR**]**: Unable to ping website\n> __Error__: `{str(e)}`')
            if r == 404:
                await message.channel.send(f'Website **down** *({r})*')
            else:
                await message.channel.send(f'Website **operational** *({r})*')
        elif message.content.startswith(f"{prefix}gentoken"):
            await message.delete()
            user = message.content[len(f"{prefix}gentoken "):].strip()
            code = "ODA"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            if not user:
                await message.channel.send(''.join(code))
                return
            await message.channel.send(f"{user}'s token is: ||{''.join(code)}||")
        elif message.content.startswith(f"{prefix}quickdelete"):
            await message.delete()
            content = message.content[len(f"{prefix}quickdelete "):].strip()
            if not content:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `quickdelete <message>`')
                return
            await message.channel.send(content, delete_after=2)


        elif message.content.startswith(f"{prefix}tokeninfo"):
            await message.delete()
            usertoken = message.content[len(f"{prefix}tokeninfo "):].strip()
            if not usertoken:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `tokeninfo <token>`')
                return
            headers = {'Authorization': usertoken,'Content-Type': 'application/json'}
            languages = {
            'da'    : 'Danish, Denmark',
            'de'    : 'German, Germany',
            'en-GB' : 'English, United Kingdom',
            'en-US' : 'English, United States',
            'es-ES' : 'Spanish, Spain',
            'fr'    : 'French, France',
            'hr'    : 'Croatian, Croatia',
            'lt'    : 'Lithuanian, Lithuania',
            'hu'    : 'Hungarian, Hungary',
            'nl'    : 'Dutch, Netherlands',
            'no'    : 'Norwegian, Norway',
            'pl'    : 'Polish, Poland',
            'pt-BR' : 'Portuguese, Brazilian, Brazil',
            'ro'    : 'Romanian, Romania',
            'fi'    : 'Finnish, Finland',
            'sv-SE' : 'Swedish, Sweden',
            'vi'    : 'Vietnamese, Vietnam',
            'tr'    : 'Turkish, Turkey',
            'cs'    : 'Czech, Czechia, Czech Republic',
            'el'    : 'Greek, Greece',
            'bg'    : 'Bulgarian, Bulgaria',
            'ru'    : 'Russian, Russia',
            'uk'    : 'Ukranian, Ukraine',
            'th'    : 'Thai, Thailand',
            'zh-CN' : 'Chinese, China',
            'ja'    : 'Japanese',
            'zh-TW' : 'Chinese, Taiwan',
            'ko'    : 'Korean, Korea'
            }
            try:
                res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            except:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Erro__: `An error occurred while sending request`')
                return
            if res.status_code == 200:
                res_json = res.json()
                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json['id']
                avatar_id = res_json['avatar']
                avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                phone_number = res_json['phone']
                email = res_json['email']
                mfa_enabled = res_json['mfa_enabled']
                flags = res_json['flags']
                locale = res_json['locale']
                verified = res_json['verified']
                days_left = ""
                language = languages.get(locale)
                from datetime import datetime
                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                has_nitro = False
                res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)
                try:
                    embed = f"""**TOKEN INFORMATIONS | Prefix: `{prefix}`**\n
        > :dividers: __Basic Information__\n\tUsername: `{user_name}`\n\tUser ID: `{user_id}`\n\tCreation Date: `{creation_date}`\n\tAvatar URL: `{avatar_url if avatar_id else "None"}`
        > :crystal_ball: __Nitro Information__\n\tNitro Status: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`
        > :incoming_envelope: __Contact Information__\n\tPhone Number: `{phone_number if phone_number else "None"}`\n\tEmail: `{email if email else "None"}`
        > :shield: __Account Security__\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tFlags: `{flags}`
        > :paperclip: __Other__\n\tLocale: `{locale} ({language})`\n\tEmail Verified: `{verified}`"""
                    await message.channel.send(embed, file=discord.File("img/astraa.gif"))
                except Exception as e:
                    await message.channel.send(f'> **[**ERROR**]**: Unable to recover token infos\n> __Error__: `{str(e)}`')
            elif res.status_code == 401:
                await message.channel.send(f'> **[**ERROR**]**: Unable to recover token infos\n> __Error__: Invalid token')
            else:
                await message.channel.send(f'> **[**ERROR**]**: Unable to recover token infos\n> __Error__: An error occurred while sending request')
        elif message.content.startswith(f"{prefix}cleardm"):
            await message.delete()
            amount = message.content[len(f"{prefix}cleardm "):].strip()
            await message.channel.send(f'> **[**ERROR**]**: cmd under dev') 
        elif message.content.startswith(f"{prefix}hypesquad"):
            await message.delete()
            house = message.content[len(f"{prefix}hypesquad "):].strip()
            if not house:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}hypesquad <house>`')
                return
            headers = {'Authorization': token, 'Content-Type': 'application/json'}  
            r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
            if r.status_code == 200:
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
                if house == "bravery":
                    payload = {'house_id': 1}
                elif house == "brilliance":
                    payload = {'house_id': 2}
                elif house == "balance":
                    payload = {'house_id': 3}
                else:
                    await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Error__: Hypesquad house must be one of the following: `bravery`, `brilliance`, `balance`')
                    return
            else:
                await message.channel.send(f'> **[**ERROR**]**: Invalid status code\n> __Status code__: `{r.status_code}`, expected 200')
                return
            r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
            if r.status_code == 204:
                await message.channel.send(f'Hypesquad House changed to `{house}`!')
        elif message.content == f"{prefix}serverinfo":
            await message.delete()
            date_format = "%a, %d %b %Y %I:%M %p"
            embed = f"""**SERVER INFORMATIONS | Prefix: `{prefix}`**\n
        > :dividers: __Basic Information__\n\tServer Name: `{message.guild.name}`\n\tServer ID: `{message.guild.id}`\n\tCreation Date: `{message.guild.created_at.strftime(date_format)}`\n\tServer Icon: `{message.guild.icon.url if message.guild.icon.url else "None"} `\n\tServer Owner: `{message.guild.owner}`
        > :page_facing_up: __Others Information__\n\t`{len(message.guild.members)}` Members\n\t`{len(message.guild.roles)}` Roles\n\t`{len(message.guild.text_channels) if message.guild.text_channels else "None"}` Text-Channels\n\t`{len(message.guild.voice_channels) if message.guild.voice_channels else "None"}` Voice-Channels\n\t`{len(message.guild.categories) if message.guild.categories else "None"}` Categories"""
            await message.channel.send(embed, file=discord.File("img/astraa.gif"))
        elif message.content == f"{prefix}nitro":
            await message.delete()
            await message.channel.send(f"https://discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}")
        elif message.content.startswith(f"{prefix}whremove"):
            await message.delete()
            webhook = message.content[len(f"{prefix}whremove "):].strip()
            if not webhook:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}whremove <webhook>`')
                return
            requests.delete(webhook.rstrip())
            await message.channel.send(f'Webhook has been deleted!')


        elif message.content.startswith(f"{prefix}hidemention"):
            await message.delete()
            content = message.content[len(f"{prefix}hidemention "):].strip()
            if not content:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}hidemention <message>`')
                return
            await message.channel.send(content + ('||\u200b||' * 200) + '@everyone')
        elif message.content.startswith(f"{prefix}edit"):
            await message.delete()
            content = message.content[len(f"{prefix}edit "):].strip()
            if not content:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}edit <message>`')
                return
            text = await message.channel.send(content)
            await text.edit(content=f"\u202b{content}")


        elif message.content == f"{prefix}911":
            await message.delete()
            invis = ""
            frames = [
                f''':man_wearing_turban::airplane:\t\t\t\t:office:''',
                f''':man_wearing_turban:\t:airplane:\t\t\t:office:''',
                f''':man_wearing_turban:\t\t::airplane:\t\t:office:''',
                f''':man_wearing_turban:\t\t\t:airplane:\t:office:''',
                f''':man_wearing_turban:\t\t\t\t:airplane::office:''',
                ''':boom::boom::boom:''']
            sent_message = await message.channel.send(frames[0])
            for frame in frames[1:]:
                await asyncio.sleep(0.5)
                await sent_message.edit(content=frame)
        elif message.content == f"{prefix}cum":
            await message.delete()
            frames = [
                '''
    :ok_hand:            :smile:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8=:punch:=D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :smiley:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8==:punch:D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :grimacing:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8=:punch:=D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :persevere:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8==:punch:D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :confounded:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8=:punch:=D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :tired_face:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8==:punch:D 
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :weary:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8=:punch:= D:sweat_drops:
            :trumpet:      :eggplant:
    ''',
    '''
    :ok_hand:            :dizzy_face:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8==:punch:D :sweat_drops:
            :trumpet:      :eggplant:                 :sweat_drops:
    ''',
    '''
    :ok_hand:            :drooling_face:
:eggplant: :zzz: :necktie: :eggplant: 
                :oil:     :nose:
                :zap: 8==:punch:D :sweat_drops:
            :trumpet:      :eggplant:                 :sweat_drops:
    ''']
            sent_message = await message.channel.send(frames[0])
            for frame in frames[1:]:
                await asyncio.sleep(0.5)
                await sent_message.edit(content=frame)
        elif message.content.startswith(f"{prefix}minesweeper"):
            await message.delete()
            size = max(min(int(message.content[len(f"{prefix}minesweeper "):].strip()), 8), 2)
            bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
            is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
            has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
            m_numbers = [":one:",":two:",":three:",":four:",":five:",":six:"]
            m_offets = [(-1, -1),(0, -1),(1, -1),(-1, 0),(1, 0),(-1, 1),(0, 1),(1, 1)]
            message_to_send = "**Click to play**:\n"
            for y in range(size):
                for x in range(size):
                    tile = "||{}||".format(chr(11036))
                    if has_bomb(x, y):
                        tile = "||{}||".format(chr(128163))
                    else:
                        count = 0
                        for xmod, ymod in m_offets:
                            if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                                count += 1
                        if count != 0:
                            tile = "||{}||".format(m_numbers[count - 1])
                    message_to_send += tile
                message_to_send += "\n"
            await message.channel.send(message_to_send)
        elif message.content.startswith(f"{prefix}1337"):
            await message.delete()
            content = message.content[len(f"{prefix}1337 "):].strip()
            if not content:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}1337 <message>`')
                return
            content = content.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '1').replace('I', '1').replace('o', '0').replace('O', '0').replace('t', '7').replace('T', '7').replace('b', '8').replace('B', '8')
            await message.channel.send(content)
        elif message.content.startswith(f"{prefix}dick"):
            await message.delete()
            user = message.content[len(f"{prefix}dick "):].strip()
            if not user:
                user = message.author.display_name
            size = random.randint(1,15)
            dong = ""
            for _ in range (0, size):
                dong += "="
            await message.channel.send(f"**{user}**'s Dick size\n8{dong}D")
        elif message.content.startswith(f"{prefix}reverse"):
            await message.delete()
            content = message.content[len(f"{prefix}reverse "):].strip()
            if not content:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}reverse <message>`')
                return
            content = content[::-1]
            await message.channel.send(content)
        

        elif message.content.startswith(f"{prefix}spam"):
            await message.delete()
            content = message.content[len(f"{prefix}spam "):].strip()
            try:
                amount, message_to_send = content.split(" ", 1)
                amount = int(amount)
            except ValueError:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}spam <amount> <message>`')
                return
            if amount <= 0 or amount > 9:
                await message.channel.send(f"> **[**ERROR**]**: Amount must be between 1 and 9")
                return
            for _ in range(amount):
                await message.channel.send(message_to_send)
        elif message.content == f"{prefix}guildicon":
            await message.delete()
            await message.channel.send(f"**{message.guild.name} icon :**\n{message.guild.icon.url if message.guild.icon else '*NO ICON*'}")
        elif message.content == f"{prefix}guildbanner":
            await message.delete()
            await message.channel.send(f"**{message.guild.name} banner :**\n{message.guild.banner.url if message.guild.banner else '*NO BANNER*'}")
        elif message.content.startswith(f"{prefix}guildrename"):
            await message.delete()
            name = message.content[len(f"{prefix}guildrename "):].strip()
            if not name:
                await message.channel.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `{prefix}guildrename <name>`')
                return
            if not message.guild.me.guild_permissions.manage_guild:
                await message.channel.send(f'> **[**ERROR**]**: Missing permissions')
                return
            try:
                await message.guild.edit(name=name)
                await message.channel.send(f"Server renamed to '{name}'")
            except Exception as e:
                 await message.channel.send(f'> **[**ERROR**]**: Unable to rename the server\n> __Error__: `{str(e)}`')
        elif message.content.startswith(f"{prefix}purge"):
            await message.delete()
            amount = message.content[len(f"{prefix}purge "):].strip()
            await message.channel.send(f'> **[**ERROR**]**: cmd under dev') 


        elif message.content == f"{prefix}shrug":
            await message.delete()
            await message.channel.send("¯\_(ツ)_/¯")
        elif message.content == f"{prefix}lenny":
            await message.delete()
            await message.channel.send("( ͡° ͜ʖ ͡°)")
        elif message.content == f"{prefix}fliptable":
            await message.delete()
            await message.channel.send("(╯°□°）╯︵ ┻━┻")
        elif message.content == f"{prefix}unflip":
            await message.delete()
            await message.channel.send("┬─┬ ノ( ゜-゜ノ)")
        elif message.content == f"{prefix}empty":
            await message.delete()
            await message.channel.send(chr(173))

client = MyClient()
client.run(token)

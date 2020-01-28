import discord
import asyncio
import requests


DISCORD_BOT_TOKEN = ''

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

client = discord.Client()
# e = discord.Embed(title='foo')
# channel.send('Hello', embed=e)

plugin_list = []


def update_plugin_list():

    pass


@client.event
async def on_ready():
    update_plugin_list()
    print(f'Logged in as user.name = {client.user.name}\n client.user.id = {client.user.id}')
    # print(client.user.name)
    # print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!btcprice'):
        print(f'[command]: {message}')
        btc_price_usd, btc_price_rub = get_btc_price()
        await discord.TextChannel.send(message.channel, 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub))
    elif message.content.startswith('!hi'):
        print(f'[command]: {message}')
        await discord.TextChannel.send(message.channel, f'hi {message.author}')
    elif message.content.startswith('!cat') or message.content.startswith('!кот') or message.content.startswith(
            '!блохастый') or message.content.startswith('!котяйка') or message.content.startswith('!пушистый'):
        print(f'[command]: {message}')
        print(message.channel)
        r = requests.get('http://thecatapi.com/api/images/get?api_key=9f91c47a-08c0-46c0-ba81-7920e4df40d2')
        print(r.content)
        msg = r.url

        await discord.TextChannel.send(message.channel, msg)
    elif message.content.startswith('!кто') or message.content.startswith('!who'):
        answer = get_online_users_from_server(message)
        await discord.TextChannel.send(message.channel, answer)


def get_online_users_from_server(message):
    users = discord.Widget.members
    print(message.content, message.author, message.channel)
    print(users)
    print(message.guild.fetch_member(1).)
    return users



@client.event
async def on_member_join(member):
    print('joined')
    server = member
    fmt = f'Добро пожаловать в Джанкер Таун, {member.display_name}!'
    print(f'{server}\n{server.guild}')
    await discord.TextChannel.send(server, fmt.format(member, server))

# @client.event
# async def on_message(async_func):
#     return async_func()


async def btc_price():
    pass


def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice



client.run(DISCORD_BOT_TOKEN)

# https://discordapp.com/oauth2/authorize?&client_id=CLIENT_ID&scope=bot&permissions=0


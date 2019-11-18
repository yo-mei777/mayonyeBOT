# インストールした discord.py を読み込む
import discord
from discord.ext import tasks
from datetime import datetime

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjQ1NDcyNDg0NDQzMDI5NTMw.XdEegA.BtTpm8XYP2vEe-xrZk6mMOl6KUw'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@client.event
async def on_message(message):
    if message.content.startswith('終わり'):
        guild = client.get_guild(561824358121734161)
        role = discord.utils.get(message.guild.roles, name='タスキル')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} タスキル解除したよ'
        await message.channel.send(reply)
    #タスキル設定
    if message.content.startswith('タスキル'):
        guild = client.get_guild(561824358121734161)
        role = discord.utils.get(message.guild.roles, name='タスキル')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} タスキル設定したよ'
        await message.channel.send(reply)


# 30秒に一回ループし、5時になったらタスキルロールの削除
@tasks.loop(seconds=30)
async def time_check():
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        guild = client.get_guild(561824358121734161)
        role = discord.utils.get(guild.roles,name='タスキル')
        for member in guild.members:
            if role in member.roles:
                await member.remove_roles(role)

#ループ処理実行
time_check.start()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
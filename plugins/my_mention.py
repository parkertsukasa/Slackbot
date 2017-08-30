# coding utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@listen_to('ゲーム')
def listen_func(message):
  message.send('ゲーム大好き！')
  message.reply('一緒にゲームしようよ！')

@listen_to('こば')
def listen_func(message):
  message.send('こば様の言うことならなんでもお聞きしますよ！')

@listen_to('connect')
def listen_func(message):
  message.send('connectは世界一！！！！！！！！！！！！！！')
  message.reply('君もそう思うでしょ？？？？？？？？？？？？')


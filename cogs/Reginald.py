import discord
from discord.ext import tasks, commands
import asyncio
from datetime import date
import datetime
import time
from random import randint as r

class Reggie(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.index = 0
    self.counter = 1
    self.channel = '624815709142384650'
    self.printer.start()
    #self.bg_task = self.loop.create_task(self.my_background_task())

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is online')
    counter = 0
    currentDT = datetime.datetime.now()
    print(date.today().weekday())
    print(currentDT.hour)
    print(currentDT.minute)

  @commands.command()
  async def on_message(message):
    user = str(message.author)
    if user == 'B Team Bot#7552':
        return
    user = user[:-5]
    sentence_string = message.content.lower()
    sentence_list = sentence_string.split()
    
    if sentence_string == 'date':
        today = date.today()
        year = today.year
        month = today.month
        day = today.day

        if month == 4:
            day += 31
            month -= 1
        if month == 3:
            day += 28
            month -= 1
        if month == 2:
            day += 31
            month -= 1
        if month == 1:
            day += 31
            month = 12
            year -= 1
        if month == 12:
            day += 30
            month -= 1
        if month == 11:
            day += 31
            month -= 1
        if month == 10:
            day += 30
            month -= 1
        if month == 9:
            day += 31
            month -= 1
        if month == 8:
            day += 31
            month -= 1
        if month == 7:
            day += 31
            month -= 1
        if month == 6:
            day += 30
            month -= 1
        # if month == 5:
        #  day += 31
        #  month -= 1

        while year > 2018:
            day += 365
            if year % 4 == 0:
                day += 1
            year -= 1
        if day % 100 == 13:
          await message.channel.send('May the ' + str(day) + 'rd be with you!')
        elif day % 10 == 3:
            await message.channel.send('May the ' + str(day) + 'th be with you!')
        else:
            await message.channel.send('May the ' + str(day) + 'rd be with you!')
        
    if 'istylerdum' in message.content.lower():
        await message.channel.send('TylerIsDum = True')
        

  @tasks.loop(seconds=30.0)
  async def printer(self):
      most_important_variable = r(0, 5)
      if most_important_variable == 0:
        print('UwU')
      if most_important_variable == 1:
        print('OwO')
      if most_important_variable == 2:
        print('0w0')
      if most_important_variable == 3:
        print('@w@')
      if most_important_variable == 4:
        print('()w()')
      if most_important_variable == 5:
        print('VwV')
      
      
      self.index += 1
'''
      currentDT = datetime.datetime.now()
      if date.today().weekday() == 1 and self.counter == 0 and currentDT.hour == 12 and currentDT.minute == 35:
          self.counter = 1
      elif date.today().weekday() == 1 and self.counter == 1 and currentDT.hour == 12 and currentDT.minute == 35:
          print('Reginald has arrived')
          self.counter = 0
          try:
            await message1.channel.send('Reginald is here')
          except Exception as e:
            print(e)
'''
def setup(bot):
  bot.add_cog(Reggie(bot))
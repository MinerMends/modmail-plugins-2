import random, datetime, time, platform, secrets
import socket, psutil, syst, sys, os
import asyncio, contextlib, discord
from datetime import date
from colorama import *
from Extra.variables import *
from Database.dbfunction import *
from typing import Optional
from textwrap import dedent
from textblob import TextBlob
from discord import Embed, Member
from discord.utils import find, get
from discord.ext.commands import cooldown, BucketType
from discord.ext import tasks, commands
from discord.ext import commands, tasks

today = date.today()

class events(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_member_join(self, member): 
    if member.guild.id == mpGuild:
      guild = self.client.get_guild(mpGuild)
      if len(guild.members) % 10: #every hundred members
        embed = discord.Embed(description=f"{mpmilestone} {mpmendingarmy}",color=e0bf00) #every hundred members
        embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{guild.member_count} {mpmembereached}")
        embed.add_field(name=f"{mpachby}",value=f"__[{member.name}#{member.discriminator}](https://discord.com/users/{member.id})__",inline=False)
        reached = self.client.get_channel(milestoneID)
        await reached.send(embed=embed)
        #await syst.normalize(self.client, member if member in guild.members else None)  
      name = member.name
      removeChars = "!_*\\\`:~>|" #checking for characters that may break the string
      for endPoint in removeChars:
        name = name.replace(endPoint, '') 
      path = "./Database/join_dates.json"
      join_channel = self.client.get_channel(welcomeChannel)
      chat_channel = self.client.get_channel(chatID) 
      d = time.mktime(member.joined_at.utctimetuple())
      if not os.path.isfile(path): json.dump({},  open(path, 'w'))
      data = json.load(open(path, 'r'))
      user_message = discord.Embed(description=mpjoin,color=p84clr)
      if str(member.id) not in list(data.keys()): #if user has never joined
          user_data = {};user_data["jat"] = d
          user_data["jlh"] = 3600;data[member.id] = user_data
          json.dump(data, open(path, 'w'))
          join_message = discord.Embed(title=f"{joinplace} **{guild.member_count}**",description=f"{wemote} **{name}** {mpwelcome}",color=p84clr)
          newMsg = discord.Embed(description=f"{wemote} **{name}** {mpwelcome}",color=p84clr)
          await join_channel.send(embed=join_message)
          joinLogger4 = await chat_channel.send(embed=newMsg,delete_after=30)
          db["joinLogger4"] = joinLogger4.id
          try:
            await member.send(embed=user_message)
          except: #incase the users dms disabled
            backup_channel = self.client.get_channel(welcomeChannel)
            joinLogger5 = await backup_channel.send(f"{member.mention} {sryping}",embed=user_message,delete_after=60)
            db["joinLogger5"] = joinLogger5.id
      else: #welcome back (executes if user joined in past)
        user_data = data[str(member.id)]
        if d - user_data["jat"] > 1: 
          user_data["jat"] = d;user_data["jlh"] = 1
          if user_data["jlh"] == 1:
            user_data["jlh"] += 1;data[str(member.id)] = user_data
            json.dump(data, open(path, 'w'))
            join_message = discord.Embed(title=f"{joinplace} **{guild.member_count}**",description=f"{wemote} **{name}** {mpwelcomeback}",color=p84clr)
            newMsg = discord.Embed(description=f"{wemote} **{name}** {mpwelcomeback}",color=p84clr)
            joinLogger2 = await chat_channel.send(embed=newMsg,delete_after=60)
            db["joinLogger2"] = joinLogger2.id
            log_channel = self.client.get_channel(welcomeChannel)
            log_channel2 = self.client.get_channel(welcomeChannel)
            await join_channel.send(embed=join_message)
            try: await member.send(embed=user_message)
            except: #executes if player joined in past & has dms disabled
              user_message = discord.Embed(description=mpjoin,color=p84clr)
              backup_channel = self.client.get_channel(welcomeChannel)
              joinLogger2 = await backup_channel.send(f"{member.mention} {sryping}",embed=user_message,delete_after=900)
              db["joinLogger1"] = joinLogger2.id    
    save_db()

  @commands.Cog.listener()
  async def on_raw_message_delete(self, payload):
    if payload.cached_message.channel.id == 995190383438991450 and payload.cached_message.author.id != 155149108183695360 and payload.cached_message.author.id != 794404770856304681:
      cas = db["message_tracking"][str(payload.cached_message.author.id)]
      oldxp = cas["oldxp"]
      oldxpp = cas["xp"]
      msgid = cas["msgid"]
      msgid2 = db["pvsMID"]
      level = cas["level"]
      oldlevell = cas["level"]
      xp = cas["xp"]
      xpp = xp - 500
      xp-=250 #for local (per individual)
      if xp == 0:
        if level < 10:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
        elif level >= 10 and level < 20:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
        elif level >= 20 and level < 30:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
          save_db()
        elif level >= 30 and level < 40:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
          save_db()
        elif level >= 40 and level < 50:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
          save_db()
        elif level >= 50 and level < 100:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
          save_db()
        elif level >= 100:
          xp = 5000
          xpp = 4750
          channel = self.client.get_channel(milestoneID)
          msgID = await channel.fetch_message(msgid)
          await msgID.delete()
          try:
            msgID2 = await channel.fetch_message(msgid2)
            await msgID2.delete()
          except: pass
          save_db()
        level-=1
      embed = discord.Embed(description=f"{mpmsgdel} <#{chatID}>",color=p84clr)
      embed.add_field(name=f"{mpxpmod}",value=f"**{xp} {mppgs} {xpp} {mpxp1}**")
      if level != oldlevell:
        embed.add_field(name=f"{mdlevelmod}",value=f"**{oldlevell} {mppgs} {level}**")
      await payload.cached_message.channel.send(f"<@!{payload.cached_message.author.id}>",embed=embed,delete_after=10)
      message_count = cas["message_count"]
      first_message = cas["first_message"]
      oldxp = cas["oldxp"]      
      message_count-=1 #for local (per individual)     
      total_messages = db["total_messages"] #for global (per community)
      total_messages-=1 #for global (per community)
      db["total_messages"] = total_messages
      db["message_tracking"][str(payload.cached_message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}

#not storing this in variables.py [kind of a dumb feature]
#all this does is announces someones invite_creation (which is pointless)
  @commands.Cog.listener()
  async def on_invite_create(self, invite: discord.Invite):
    guild = invite.guild
    logch = self.client.get_channel(976316567786758165)
    logch2 = self.client.get_channel(954839429086859364)
    if invite.max_uses == 0:
      maxUses = "Infinite"
    else:
      maxUses = invite.max_uses
    embed = discord.Embed(title="Invite Created",description=f"**Created By**: {invite.inviter.mention}\n**Invite Link**: https://discord.gg/{invite.code}\n**Max Uses**: {maxUses}\n**Channel**: <#{invite.channel.id}>",color=p84clr)
    await logch.send(embed=embed,delete_after=10)
    await logch2.send(embed=embed)

  #for message.content [anyting with mp or weird var names are in variables.py]
  #made it easier to store everything in variables.py [for me as I change things a lot]
  @commands.Cog.listener()
  async def on_message(self, message):
    msg = message;auth = msg.author.id;chan = msg.channel.id;milestone = self.client.get_channel(milestoneID)
    if auth == 794404770856304681 or auth == 302050872383242240 or auth == 155149108183695360:
      return None
    if message.channel.id == 995190383438991450 and auth != 794404770856304681 and auth != 794404770856304681:
      if str(message.author.id) in db["message_tracking"]:
        pass
      else:
        db["message_tracking"][str(message.author.id)] = {"message_count": 0, "first_message": today.strftime("%B %d, %Y"), "level": mpstartlvl, "xp": mpxplvl, "oldxp": 0, "msgid": 0}
      cas = db["message_tracking"][str(message.author.id)]
      message_count = cas["message_count"]
      first_message = cas["first_message"]
      level = cas["level"]
      xp = cas["xp"]
      oldxp = cas["oldxp"]      
      xp+=mpxpgain #for local (per individual)
      message_count+=1 #for local (per individual)     
      total_messages = db["total_messages"] #for global (per community)
      total_messages+=1 #for global (per community)
      db["total_messages"] = total_messages
      msgid = cas["msgid"]
      db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
      if cas["xp"] % 5000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] < 10 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} Total Solves"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} {mppgs} {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 10000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 10 and cas["level"] < 20 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name="Community Achievement",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name="Achieved By",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 20000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 20 and cas["level"] < 30 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 50000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 30 and cas["level"] < 40 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 100000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 40 and cas["level"] < 50 and cas["xp"] != 0: 
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 200000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 50 and cas["level"] < 100 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      elif cas["xp"] % 500000 == 0 and cas["xp"] != cas["oldxp"] and cas["level"] >= 100 and cas["xp"] != 0:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} {mptotalsolves1}"
          level = cas["level"]
          oldlevel = cas["level"]
          level+=1
          embed2 = discord.Embed(description=f"{mpmilestone2} <#{milestoneID}>.",color=p84clr)
          embed = discord.Embed(description=f"{mpmilestone} {mplevel}",color=0xfcf803)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{oldlevel} -> {level}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          saveme = await milestone.send(embed=embed)
          msgid = saveme.id
          await message.channel.send(f"<@{message.author.id}>",embed=embed2,delete_after=20)
          idlength = 20
          oldxp = secrets.token_urlsafe(idlength)
          xp = mpxplvl
          db["message_tracking"][str(message.author.id)] = {"message_count": message_count, "first_message": first_message, "level": level, "xp": xp, "oldxp": oldxp, "msgid": msgid}
          save_db()
      #counting, solve-me, slashes, messages [4]
      if db["total_messages"] % 20 == 0 and db["pastMsg1"] != db["total_messages"]:
        amount = db["total_messages"]
        amount = "{:,}".format(amount)
        cert = f"{amount} {mpchannelmsg}"
        embed = discord.Embed(description=f"{mpmilestone} <#{chatID}>.",color=0xf542e3)
        embed.add_field(name=f"{mpach}t",value=f"{mpmilestoneemoji} **{cert}**.",inline=False)
        embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
        saveme = await milestone.send(embed=embed)
        db["pvsMID"] = saveme.id
        db["pastMsg1"] = db["total_messages"]   

      save_db()
    try:
      role = message.guild.get_role(976315422708228107)
    except:
      pass
    try:
      if role in message.author.roles:
        pass
      else: 
        try:
          await message.author.add_roles(role)
        except:
          pass
    except:
      pass  
    if self.client.ready is True:
      self.client.ready = False
      guild = self.client.get_guild(mpGuild)
      await syst.normalize(self.client, guild.members)
      guild = self.client.get_guild(mpGuild)
      try:
        await syst.normalize(self.client, message.author if message.author in message.guild.members else None)
      except: pass    
    if chan == suggestionsID and auth != 671912452480434186 and auth!= 470722416427925514 and auth!= 794404770856304681:
      await message.delete(delay=0.5)
    if auth != 794404770856304681 and chan == suggestionsID: #suggest
      suggested = self.client.get_channel(suggestionsID)
      try:
        cmdsDel2 = await suggested.fetch_message(db["cmdsDel2"])
        await cmdsDel2.delete()
      except: return None
      embed2 = discord.Embed(title=st1,description=sd1,color=p84clr)
      embed2.add_field(name=sf1,value=sfv1)
      del1 = await suggested.send(embed=embed2)
      db["cmdsDel2"] = del1.id
      save_db()
    elif auth != 794404770856304681 and auth != 794404770856304681 and chan == milestoneID: #milestones [music deprecated]
      milestones = self.client.get_channel(milestoneID)
      try:
        cmdsDel4 = await milestones.fetch_message(db["cmdsDel"])
        await cmdsDel4.delete()
      except: return None
      embed = discord.Embed(title=mt2,description=md2,color=p84clr)
      embed.add_field(name=mf2,value=mfv2)
      #del3 = await milestones.send(embed=embed)
      #db["cmdsDel"] = del3.id
      save_db()
    elif auth != 794404770856304681 and chan == adsID: #ads
      ads = self.client.get_channel(adsID)
      try:
        cmdsDel3 = await ads.fetch_message(db["cmdsDel3"])
        await cmdsDel3.delete()
      except: return None
      embed3 = discord.Embed(title=at2,description=ad2,color=p84clr)
      embed3.add_field(name=af2,value=afv2)
      del2 = await ads.send(embed=embed3)
      db["cmdsDel3"] = del2.id
      save_db()
    if auth != 794404770856304681 and chan == 976219996529238066:
      await message.delete()
    #solve-me (allows community to solve math questions)
    if auth != 794404770856304681 and chan == solveID:
      total_solves = db["total_solves"]
      cants = ["/cant"]
      if str(message.author.id) in db["solves"]:
        pass
      else:
        db["solves"][str(message.author.id)] = {"total_solves": 0, "started_solving": today.strftime("%B %d, %Y"), "started_solve": total_solves, "failed_solves": 0, "hardest_result": 0, "skipped_solves": 0}
      if any(varsDefends in message.content for varsDefends in cants): 
        return None
      choices = ["add","sub","multi"]
      selector = random.choice(choices);save_db()
      if message.content != db["result"] and db["answered"] != "True":
        question = db["question"]
        failed_solves = db["failed_solves"]
        failed_solves+=1
        db["failed_solves"] = failed_solves
        total_user_solves = db["solves"][str(message.author.id)]["total_solves"]
        started_solve = db["solves"][str(message.author.id)]["started_solve"]
        failed_solves = db["solves"][str(message.author.id)]["failed_solves"]
        skipped_solves = db["solves"][str(message.author.id)]["skipped_solves"]
        failed_solves+=1
        started_solving = db["solves"][str(message.author.id)]["started_solving"]
        db["solves"][str(message.author.id)] = {"total_solves": total_user_solves, "started_solving": started_solving, "started_solve": started_solve, "failed_solves": failed_solves, "skipped_solves": skipped_solves}        
        embed = discord.Embed(title=mpansweredincorrectly,description=mpnotright,color=p84clr)
        embed.add_field(name=mpretry,value=f"{mpthinking} {mpwhatis} {question}{mpwhatis1}",inline=False)
        await message.add_reaction(vote2)
        embed.add_field(name=mptoohard,value=mpcant,inline=False)
        await message.reply(embed=embed)
        save_db()
        return None
      if message.content == db["result"] and db["answered"] != "True":
        db["answered"] = "True"
        question = db["question"];result = db["result"]
        if selector == "add":
          num1 = random.randint(1,2500);num2 = random.randint(1,2500)
          db["oldQ"] = question;db["oldR"] = result
          oldQ = db["oldQ"];oldR = db["oldR"]
          result = num1 + num2
          resultt = num1 + num2
          num1 = "{:,}".format(num1);num2 = "{:,}".format(num2)
          oldR = "{:,}".format(int(oldR))
          question = f"{num1} + {num2}"
        elif selector == "sub":
          num1 = random.randint(501,1500);num2 = random.randint(1,500)
          db["oldQ"] = question;db["oldR"] = result
          oldQ = db["oldQ"];oldR = db["oldR"]
          result = num1 - num2
          resultt = num1 - num2
          num1 = "{:,}".format(num1);num2 = "{:,}".format(num2)
          oldR = "{:,}".format(int(oldR))
          question = f"{num1} - {num2}"
        elif selector == "multi":
          num1 = random.randint(1,60);num2 = random.randint(1,60)
          db["oldQ"] = question;db["oldR"] = result
          oldQ = db["oldQ"];oldR = db["oldR"]
          result = num1 * num2
          resultt = num1 * num2
          num1 = "{:,}".format(num1);num2 = "{:,}".format(num2)
          oldR = "{:,}".format(int(oldR))
          question = f"{num1} * {num2}"                    
        db["question"] = question
        db["result"] = str(result)
        db["answered"] = "False"
        skipped_solves = db["solves"][str(message.author.id)]["skipped_solves"]
        total_user_solves = db["solves"][str(message.author.id)]["total_solves"]
        total_user_solves+=1
        total_solves = db["total_solves"]
        total_solves+=1
        db["total_solves"] = total_solves
        if db["total_solves"] % 10 == 0 and db["pastSolve1"] != db["total_solves"]:
          amount = db["total_solves"]
          amount = "{:,}".format(amount)
          cert = f"{amount} Total Solves"
          embed = discord.Embed(description=f"{mpmilestone} <#{solveID}>.",color=0x5af542)
          embed.add_field(name=f"{mpach}",value=f"{mpmilestoneemoji} **{cert}**.",inline=False)
          embed.add_field(name=f"{mpachby}",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          await milestone.send(embed=embed)
          db["pastSolve1"] = db["total_solves"]
        started_solve = db["solves"][str(message.author.id)]["started_solve"]
        failed_solves = db["solves"][str(message.author.id)]["failed_solves"]
        started_solving = db["solves"][str(message.author.id)]["started_solving"]
        db["solves"][str(message.author.id)] = {"total_solves": total_user_solves, "started_solving": started_solving, "started_solve": started_solve, "failed_solves": failed_solves, "skipped_solves": skipped_solves}
        embed = discord.Embed(title=mpansweredcorrectly,description=f"{mpclap} **{oldQ} = {oldR}**",color=p84clr)
        embed.add_field(name=mpnextquestion,value=f"{mpthinking} {mpwhatis} {question}{mpwhatis1}",inline=False)
        await message.add_reaction(vote1)
        message = await message.reply(embed=embed)
        db["pvsSolve"] = message.id
        save_db()
    #counting (allows community to count)
    elif auth != 794404770856304681 and chan == countingID:
      count = db["counting"]
      if str(message.author.id) in db["countings"]:
        pass
      else:
        db["countings"][str(message.author.id)] = {"counts": 0, "started_count": today.strftime("%B %d, %Y"), "highest_count": 0, "joined_count": count}
        try:
          role = interaction.guild.get_role(962453025400709141)
        except: pass #this is for my own server (public bot)
        if role in message.author.roles:
          pass
        else:
          try:
            await message.author.add_roles(role)
          except:
            pass 
      if db["maxCounter"] >= db["countings"][str(message.author.id)]["highest_count"]:
        if db["lastCount"] == auth:
          counts = db["countings"][str(message.author.id)]["counts"]
          started_count = db["countings"][str(message.author.id)]["started_count"]
          highest_count = db["maxCounter"]
          joined_count = db["countings"][str(message.author.id)]["joined_count"]
          highest_count+=1
          if highest_count > 200:
            highest_count = 200
          db["countings"][str(message.author.id)] = {"counts": int(counts), "started_count": str(started_count), "highest_count": int(highest_count), "joined_count": joined_count}
          save_db()
      count+=1
      if str(message.content) != str(count):
        pass
      else:
        counts = db["countings"][str(message.author.id)]["counts"]
        counts+=1
        started_count = db["countings"][str(message.author.id)]["started_count"]
        highest_count = db["countings"][str(message.author.id)]["highest_count"]
        joined_count = db["countings"][str(message.author.id)]["joined_count"]
        db["countings"][str(message.author.id)] = {"counts": int(counts), "started_count": str(started_count), "highest_count": int(highest_count), "joined_count": joined_count}
        if db["lastCount"] == auth:
          maxCountResult = db["maxCounter"];maxCountResult+=1
          db["maxCounter"] = maxCountResult     
        elif db["lastCount"] != auth:
          db["maxCounter"] = 1
        if db["maxCounter"] == 10:
          embed = discord.Embed(description=mps10,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 20: 
          db["streak1"] = str(auth)
          db["streak1Vis"] = message.author.name 
          db["streak1Vis2"] = message.author.discriminator
          embed = discord.Embed(description=mps20,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 30: 
          embed = discord.Embed(description=mps30,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 40: 
          embed = discord.Embed(description=mps40,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 50: 
          db["streak2"] = str(auth)
          db["streak2Vis"] = message.author.name 
          db["streak2Vis2"] = message.author.discriminator
          embed = discord.Embed(description=mps50,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 60: 
          embed = discord.Embed(description=mps60,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 70: 
          embed = discord.Embed(description=mps70,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 80: 
          embed = discord.Embed(description=mps80,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 90: 
          embed = discord.Embed(description=mps90,color=p84clr)
          embed.add_field(name=mpcountcon,value=mpcountcon2)
          await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 100: 
         db["streak3"] = str(auth) 
         db["streak3Vis"] = message.author.name 
         db["streak3Vis2"] = message.author.discriminator   
         embed = discord.Embed(description=mps100,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 110: 
         embed = discord.Embed(description=mps110,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 120: 
         embed = discord.Embed(description=mps120,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 130: 
         embed = discord.Embed(description=mps130,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 140: 
         embed = discord.Embed(description=mps140,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 150: 
         db["streak4"] = str(auth)
         db["streak4Vis"] = message.author.name 
         db["streak4Vis2"] = message.author.discriminator
         embed = discord.Embed(description=mps150,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 160: 
         embed = discord.Embed(description=mps160,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 170: 
         embed = discord.Embed(description=mps170,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 180: 
         embed = discord.Embed(description=mps180,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] == 190: 
         embed = discord.Embed(description=mps190,color=p84clr)
         embed.add_field(name=mpcountcon,value=mpcountcon2)
         await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
        elif db["maxCounter"] > 199:        
          if db["maxCounter"] > 200:
            embed = discord.Embed(description=mpstreaklimit,color=p84clr)
            embed.add_field(name=mpwhat,value=mpelse,inline=False)
            await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
            await message.delete()
            return None
          else:
            embed = discord.Embed(description=mps200,color=p84clr)
            embed.add_field(name=mproleunlock,value=mpstreakking,inline=False)
            embed.add_field(name=mpwhat,value=mpelse)  
            await message.channel.send(f"{message.author.mention}",embed=embed,delete_after=10)
          role = message.guild.get_role(962219698542510090)
          try:
            member = message.guild.get_member(int(db["streak5"]))
            await member.remove_roles(role)
          except:
            pass
          try:
            oldAuthor = db["streak5"]
            await member.remove_roles(role)
            db["streak5"] = str(auth)
            db["streak5Vis"] = message.author.name 
            db["streak5Vis2"] = message.author.discriminator
            await message.author.add_roles(role)
          except:
            db["streak5"] = str(auth)
            db["streak5Vis"] = message.author.name 
            db["streak5Vis2"] = message.author.discriminator
        streak1 = db["streak1"];streak2 = db["streak2"]
        streak3 = db["streak3"];streak4 = db["streak4"];streak5 = db["streak5"]
        ##streaks - visuals
        streak1Vis = db["streak1Vis"]
        streak1Vis2 = db["streak1Vis2"]
        streak2Vis = db["streak2Vis"]
        streak2Vis2 = db["streak2Vis2"]
        streak3Vis = db["streak3Vis"]
        streak3Vis2 = db["streak3Vis2"]
        streak4Vis = db["streak4Vis"]
        streak4Vis2 = db["streak4Vis2"]
        streak5Vis = db["streak5Vis"]
        streak5Vis2 = db["streak5Vis2"]
        ##streaks - visuals
        lastCount = auth
        db["counting"] = count
        if db["counting"] % 20 == 0 and db["pastCount1"] != db["counting"]:
          amount = db["counting"]
          amount = "{:,}".format(amount)
          cert = f"{amount} Total Counts"
          embed = discord.Embed(description=f":star: __Milestone Reached__ for <#{countingID}>.",color=0x0af5f5)
          embed.add_field(name="Community Achievement",value=f":clap: **{cert}**.",inline=False)
          embed.add_field(name="Achieved By",value=f"__[{message.author.name}#{message.author.discriminator}](https://discord.com/users/{message.author.id})__",inline=False)
          await milestone.send(embed=embed)
          db["pastCount1"] = db["counting"]
          
        lastCountVis = message.author.name
        lastCountVis2 = message.author.discriminator
        db["lastCount"] = lastCount;db["lastCountVis"] = lastCountVis;db["lastCountVis2"] = lastCountVis2
        lsv = db["lastCountVis"]
        lsv2 = db["lastCountVis2"]
        maxCounter = db["maxCounter"] 
        count = "{:,}".format(count)     
        embed = discord.Embed(title=mptc,description=f"{mptd} `{count}`\n__[{lsv}#{lsv2}](https://discordapp.com/users/{lastCount})__ {mpd2} [**{maxCounter}x**]",color=p84clr)
        embed.add_field(name=mpleaderboard,value=f"**#5**: __[{streak1Vis}#{streak1Vis2}](https://discordapp.com/users/{streak1})__\n**#4**: __[{streak2Vis}#{streak2Vis2}](https://discordapp.com/users/{streak2})__\n**#3**: __[{streak3Vis}#{streak3Vis2}](https://discordapp.com/users/{streak3})__\n**#2**: __[{streak4Vis}#{streak4Vis2}](https://discordapp.com/users/{streak4})__\n**#1**: __[{streak5Vis}#{streak5Vis2}](https://discordapp.com/users/{streak5})__\n")
        embed.add_field(name=dfn1,value=NW,inline=False)
        channel = self.client.get_channel(countingID)
        countID = await channel.fetch_message(db["countingID"])
        await countID.edit(embed=embed)
      await message.delete();save_db()
    #checking community content (bad emojies, ads, scams, etcs)
    elif auth != 671912452480434186 and auth != 171912452480434186:      
      text_correction = message.content.lower()      
      blob_convert = TextBlob(text_correction)
      mgc = blob_convert.correct()
      mgcNormal = text_correction
      emoji = ["🍆💦","💦🍆",":eggplant::sweat_drops:",":eggplant: :sweat_drops:",":sweat_drops::eggplant:","💦 🍆","🍆 💦","🍑 🍆","🍑🍆","🍆🍑","🍑 🍆","👉👌","👉 👌","👌👉","👌 👉","🍌🍩","🍌 🍩","🍌🍩","🍌 🍩","💦🍌","💦 🍌","🍌💦","🍌 💦","🍑🍌","🍑 🍌","🍌🍑","🍌 🍑","👅🌮","👅 🌮","👅🌮💦","👅 🌮 💦","👅🌮 💦","👅 🌮💦","💋🍆","💋 🍆","💋💦🍆","💋 💦🍆","💋💦 🍆","💋 💦 🍆","💋🍌","💋 🍌","💋💦🍌","💋 💦 🍌","💋💦 🍌","💋 💦🍌","👅🍑","👅 🍑","👅🍑💦","👅🍑 💦","👅 🍑💦","👅 🍑 💦","🥖🍯","🥖 🍯","👅🍆🎆","👅 🍆 🎆","👅 🍆🎆","👅🍆 🎆","👅 🍆 🎆","🍌🍌😮‍💨","😮🍌‍","🍌😮","🍆💧","💧🍆","8️⃣-","💧 🍆","🍆 💧","🍌 😮","😮 🍌","🍌🍌 😮‍💨","🍌 🍌😮‍💨","😮‍💨🍌🍌","🍆😦","😦🍆","🍆 😦","😦 🍆","🍆😮","😮🍆","😮 🍆","🍆 😮"]
      character = ["🇫🇺🇨🇰","🇫🇺 🇨🇰","ㅤ","‎","‍","🫥","︎︎","​","⠀","⁪","⁤","⁭","𝅺","𝅹","𝅸","𝅵","𝅳","𝅶","𝅙","‏","⁢","⁪","⁬","𝅴","𝅷","‌","⁠","⁯","⁡","⁮","⁣","؜","͏","͏","ᅟ","឴","឵","𝐚","𝐛","𝐜","𝐝","𝐞","𝐟","𝐠","𝐡","𝐢","𝐣","𝐤","𝐥","𝐦","𝐧","𝐨","𝐩","𝐪","𝐫","𝐬","𝐭","𝐮","𝐯","𝐰","𝐱","𝐲","𝐳","𝐀","𝐁","𝐂","𝐃","𝐄","𝐅","𝐆","𝐇","𝐈","𝐉","𝐊","𝐋","𝐌","𝐍","𝐎","𝐏","𝐐","𝐑","𝐒","𝐓","𝐔","𝐕","𝐖","𝐗","𝐘","𝐙","𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗",'𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', '𝔂', '𝔃', '𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩','𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘂', '𝘅', '𝘆', '𝘇', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬','𝒂', '𝒃', '𝒄', '𝒅', '𝒆', '𝒇', '𝒈', '𝒉', '𝒊', '𝒋', '𝒌', '𝒍', '𝒏', '𝒐', '𝒑', '𝒒', '𝒓', '𝒔', '𝒕', '𝒖', '𝒗', '𝒘', '𝒖', '𝒙', '𝒚', '𝒛', '𝑨', '𝑩', '𝑪', '𝑫', '𝑬', '𝑭', '𝑮', '𝑯', '𝑰', '𝑱', '𝑲', '𝑳', '𝑵', '𝑶', '𝑷', '𝑸', '𝑹', '𝑺', '𝑻', '𝑼', '𝑽', '𝑾', '𝑿', '𝒀', '𝒁','𝙖', '𝙗', '𝙘', '𝙙', '𝙚', '𝙛', '𝙜', '𝙝', '𝙞', '𝙟', '𝙠', '𝙡', '𝙣', '𝙤', '𝙥', '𝙦', '𝙧', '𝙨', '𝙩', '𝙪', '𝙫', '𝙬', '𝙪', '𝙭', '𝙮', '𝙯', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕','𝖆', '𝖇', '𝖈', '𝖉', '𝖊', '𝖋', '𝖌', '𝖍', '𝖎', '𝖏', '𝖐', '𝖑', '𝖓', '𝖔', '𝖕', '𝖖', '𝖗', '𝖘', '𝖙', '𝖚', '𝖛', '𝖜', '𝖚', '𝖝', '𝖞', '𝖟', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','𝕒', '𝕓', '𝕔', '𝕕', '𝕖', '𝕗', '𝕘', '𝕙', '𝕚', '𝕛', '𝕜', '𝕝', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', '𝕥', '𝕦', '𝕧', '𝕨', '𝕦', '𝕩', '𝕪', '𝕫', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', '𝟙', '𝟚', '𝟛', '𝟜', '𝟝', '𝟞', '𝟟', '𝟠', '𝟡', '𝟘','🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆄', '🆇', '🆈', '🆉', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉','𝘢', '𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻', '𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓃', '𝑜', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝓋', '𝓌', '𝓍', '𝓎', '𝓏','ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⓪','🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '⓿','Д', 'Б', 'Ҫ', 'D', 'Э', 'Ғ', 'G', 'Ң', 'Ї', 'J', 'Ԟ', 'L', 'И', 'Ф', 'P', 'Q', 'Я', 'Г', 'Ц', 'V', 'Ш', 'Ҳ', 'Ч','д','[̲̅','ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ɴ', 'ᴏ', 'ᴘ', 'ǫ', 'ʀ', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'ʏ', 'ᴢ','𝟷','𝟸','𝟹','𝟺','𝟻','𝟼','𝟽','𝟾','𝟿','𝟶','α','σ','є','∂','¢','к','ℓ','и','σ','ρ','υ','ν','ω','χ','я','𝔞', '𝔟', '𝔠', '𝔡', '𝔢', '𝔣', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'յ', 'շ', 'Յ', 'կ', 'Տ', 'ճ', 'Դ', 'Ց', 'գ', 'օ','Ց','卂','░', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '╗', '░', '░', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '█', '╗', '█', '█', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '╗', '░', '░', '█', '█', '╗', '█', '█', '╗', '░', '░', '░', '░', '░', '█', '█', '╗', '█', '█', '╗', '░', '░', '█', '█', '╗', '█', '█', '╗', '░', '░', '░', '░', '░', '█', '█', '█', '╗', '░', '░', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '╗', '░', '░', '█', '█', '█', '█', '█', '█', '╗', '░', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '═', '═', '╝', '█', '█', '╔', '═', '═', '═', '═', '╝', '█', '█', '╔', '═', '═', '═', '═', '╝', '░', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '║', '░', '░', '░', '░', '░', '█', '█', '║', '█', '█', '║', '░', '█', '█', '╔', '╝', '█', '█', '║', '░', '░', '░', '░', '░', '█', '█', '█', '█', '╗', '░', '█', '█', '║', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '╔', '═', '═', '═', '█', '█', '╗', '█', '█', '█', '█', '█', '█', '█', '║', '█', '█', '█', '█', '█', '█', '╦', '╝', '█', '█', '║', '░', '░', '╚', '═', '╝', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '█', '█', '█', '╗','░', '░', '█', '█', '█', '█', '█', '╗', '░', '░', '█', '█', '║', '░', '░', '█', '█', '╗', '░', '█', '█', '█', '█', '█', '█', '█', '║', '█', '█', '║', '░', '░', '░', '░', '░', '█', '█', '║', '█', '█', '█', '█', '█', '═', '╝', '░', '█', '█', '║', '░', '░', '░', '░', '░', '█', '█', '╔', '█', '█', '╗', '█', '█', '║', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '█', '█', '╗', '█', '█', '║', '█', '█', '╔', '═', '═', '█', '█', '║', '█', '█', '╔', '═', '═', '█', '█', '╗', '█', '█', '║', '░', '░', '█', '█', '╗', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '╔', '═', '═', '╝', '░', '░', '█', '█', '╔', '═', '═', '╝', '░', '░', '█', '█', '║', '░', '░', '╚', '█', '█', '╗', '█', '█', '╔', '═', '═', '█', '█', '║', '█', '█', '║', '█', '█', '╗', '░', '░', '█', '█', '║', '█', '█', '╔', '═', '█', '█', '╗', '░', '█', '█', '║', '░', '░', '░', '░', '░', '█', '█', '║', '╚', '█', '█', '█', '█', '║', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '╔', '═', '═', '═', '╝', '░', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '█', '█', '█', '█', '╦', '╝', '╚', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '█', '█', '█', '█', '█', '╗', '█', '█', '║', '░', '░', '░', '░', '░', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '░', '░', '█', '█', '║', '█', '█', '║', '╚', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '░', '╚', '█', '█', '╗', '█', '█', '█', '█', '█', '█', '█', '╗', '█', '█', '║', '░', '╚', '█', '█', '█', '║', '╚', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '░', '░', '░', '░', '░', '░', '╚', '═', '█', '█', '╔', '═', '╝', '░', '╚', '═', '╝', '░', '░', '╚', '═', '╝', '╚', '═', '═', '═', '═', '═', '╝', '░', '░', '╚', '═', '═', '═', '═', '╝', '░', '╚', '═', '═', '═', '═', '═', '╝', '░', '╚', '═', '═', '═', '═', '═', '═', '╝', '╚', '═', '╝', '░', '░', '░', '░', '░', '░', '╚', '═', '═', '═', '═', '═', '╝', '░', '╚', '═', '╝', '░', '░', '╚', '═', '╝', '╚', '═', '╝', '░', '╚', '═', '═', '═', '═', '╝', '░', '╚', '═', '╝', '░', '░', '╚', '═', '╝', '╚', '═', '═', '═', '═', '═', '═', '╝', '╚', '═', '╝', '░', '░', '╚', '═', '═', '╝', '░', '╚', '═', '═', '═', '═', '╝', '░', '╚', '═', '╝', '░', '░', '░', '░', '░', '░', '░', '░', '╚', '═', '╝', '░', '░', '░','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉']
      hacks = ["discorx.gift","disorde.gift","discorl.gift","discrods.gift","discorc","discqrd.gift","gifts for the new year","nitro for 3 months","click for nitro","click for free nitro","click me for free nitro","click me if you want free nitro","nitro for 3 months free",".gift","dm me for free nitro","message me for free nitro","send me a message if you want free nitro","send me a message for free nitro","guys free nitro","discosb.gift","send me a message for free nitro","get free nitro in my bio","free nitro in my bio","click the link in my bio","dm for nitro","msg to get nitro","message to get nitro","msg for nitro","message for nitro","dm for free nitro","d m for free nitro","d m for free ni tro","msg for free nitro","wants free nitro","want free nitro"]
      #smpCode = ["whats the realm code","what's the realm code","what is the realm code","what is the realm code","do you know how to join the realm","how do i join the realm","i want to join the realm","where is the realm code","where's the realm code","is there a realm","is there a realm code","how to  join realm","how to join the realm","i wants to join realm","i wants to join the realm","let me in the realm","may i join the realm","may i have the realm code","how do i join the smp","where is the smp","how do i join the smp","where is the smp","where's the smp","i wanna join the realm","i wanted to join the realm","can i join the realm","how can i join the realm","can i please join the realm","could i join the realm","could i please join the realm","could i pls join the realm","how do i join the server","what is the server ip","please tell me the server ip","what is the server ip and port","how do i join smp","how to join smp","realm code","is smp on","is server ready","is realm joinable","is smp joinable","where's the code","where is the code","where is code","how to join","how do i join","how to play","how do i play","code?","server ip","server port","server info"]
      dms = ["dm me", "message me","send me a message","send me a direct message","go to dms","msg me","private message me","private msg me","msg me privately","message me privately","can you msg me rq","can you message me rq","can you message me real quick","can you msg me real quick","d m me", "m s g me","come to my dms","go to my dms","go dms","send me a message","pm me","p m me"," p m m e","in my dms","in my direction messages","in dms","sent to dms","sended in dms","send me dms","send dms to me"]
      yts = ["join my discord guys","guys join my discord","can you join my discord","can you join my server","subscribe to my youtube channel","follow me on twitter","follow me on instagram","add me on snapchat","go follow me","go subscribe to me","plz sub to me","sub to me plz","leave a like on my new video","watch my new video","sub to my yt channel","subscribe to my yt channel","join my discord","wanan join my discord","do you wanna join my new","do you wanna join my brand new discord server","wanna join my new discord server","wanna join my brand new discord server","join my server","join my mcpe server","join my minecraft server","join my minecraft bedrock server","join my minecraft java server","join my minecraft pe server","join my pc server","join my pe server","join my realm","join meh realm","join me realm","join my kitpvp","join my smp","join my server","add me on instagram","follow me on instagram","follow me on twitter","go watch my video","go to my website","check out my website","check out my new website","check out my new video","check out my channel","visit my channel"]
      threats = ["dox you","ddos you","dox him","ddos him","dox her","ddos her","hit you offline","leak your ip","leak ip","leak his ip","leak her ip","leak their ip","leak there ip","leak the ip","expose their ip","expose there ip","expose her ip","expose his ip","expose the ip","hit your router","hit your wifi","hit your ip","pill his ip","pull your ip","pull a ip","pull an ip","pull her ip","pull their ip","pull there ip","grab their ip","grab there ip","grab her ip","grab his ip","steal ip","steal his ip","steal their ip","steal there ip","steal the ip","steal her ip","steal his ip","steal a ip","steal an ip","token log him","token log her","token log them","nuke this discord","nuke the discord","nuke your discord","i will destroy the discord","i will destroy everything","i will raid you","get raided","you're gonna get raided","we're going to raid you","incoming raid","i am going to raid you","i will raid you","raid you","nuke you","raid them","nuke them","i got your ip","i have your ip","i have his ip","i have their ip","i have her ip","i have there ip","mendingarmy will die","kill mendingarmy","mendingarmy die","im gonna raid","i am gonna raid","going to raid","im gonna nuke","i am gonna nuke","going to nuke","gonna leak all your info","gonna leak all your personal info","gonna show all your info"]
      #status = ["is smp on","is server on","is the server on","is the smp on","is the realm on","is it down","is smp off","is server off","is realm off","is it off","realm down","server down","server closed","it closed","it's off","it is off","is it off","it open","its open","it is open","it's open","it is up","it is back","it is working","is it working","it isn't working","it is not working","it isnt working","help cant join","can't join","cannot join","unable to join","i got kicked","getting kicked","get kicked","got kicked","cant join","when can we join","when can we play","can't i join","cant i join","won't let me join","won't let me play","wont let me join","wont let me play","will not let me join","will not let me play","it not letting me join","it is not letting me join","it not letting me play","it is not letting me play","its not letting me join","it's not letting me join","its not letting me play","it's not letting me play","whitelisted","server status","realm status","smp status","went offline","goes offline","is offline","is back online","went down","crashed","smp off","is smp off","is realm shutting down","is server shutting down","will the server be down","will the server be off","is realm on","is the realm on"]
      p84thx = ["<@794404770856304681> thank","thanks <@794404770856304681>","thank you <@794404770856304681>","tysm <@794404770856304681>","thank you so much <@794404770856304681>","thx <@794404770856304681>","<@794404770856304681> thank you so much","<@794404770856304681> tysm","<@794404770856304681> ty","<@794404770856304681> thank you",":heart: p84",":heart: minep84","i love p84","i love minerp84","i love <@794404770856304681>","minerp84 is amazing","minerp84 is so helpful","minerp84 is helpful","minerp84 is helpful","<@794404770856304681> is amazing","<@794404770856304681> is so helpful","<@794404770856304681> is helpful","<@794404770856304681> is very helpful","minerp84 is very helpful","p84 is very helpful","thanks minerp84","minerp84 thanks","ty p84","ty bot","thank you p84","thank you bot","thanks you bot","tysm bot","tysm minerp84","thank you p84","thank you minerp84","minerp84 thank you","p84 thank you"]
      personalInfo = ["ayden","jacobus","a y d e n","ay den","ay de n","ja co bus","j acobus","jac obus"]
      tooYoung = ["i am 12","i am 11","i am 10","i am 9","i am 8","i am 7","i am 6","i am 5","i am 4","i am 3","i am 2","i am 1","i am one","i am two","i am three","i am four","i am five","i am six","i am seven","i am eight","i am nine","i am ten","i am eleven","i am twelve","i am 0"]
      if any(varsDefends in mgcNormal for varsDefends in personalInfo):       
        await message.delete()
      if any(varsDefends in mgc for varsDefends in p84thx):       
        embed = discord.Embed(description=mpthx,color=p84clr)
        await message.reply(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in p84thx):
        embed = discord.Embed(description=mpthx,color=p84clr)
        await message.reply(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in threats):
        embed = discord.Embed(description=mpthreats,color=p84clr)
        await message.add_reaction(susEmoji)
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in threats):
        embed = discord.Embed(description=mpthreats,color=p84clr)
        await message.add_reaction(susEmoji)
        await message.reply(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in dms):       
        embed = discord.Embed(description=mpnodm,color=p84clr)
        await message.add_reaction(susEmoji)        
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in dms):
        embed = discord.Embed(description=mpnodm,color=p84clr)
        await message.add_reaction(susEmoji)        
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in character):       
        embed = discord.Embed(description=mpcharacter,color=p84clr)
        await message.delete()
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in character):
        embed = discord.Embed(description=mpcharacter,color=p84clr)
        await message.delete()
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in emoji):       
        embed = discord.Embed(description=mpemoji,color=p84clr)
        await message.delete()
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in emoji):
        embed = discord.Embed(description=mpemoji,color=p84clr)
        await message.delete()
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in hacks):       
        embed = discord.Embed(description=mphacks,color=p84clr)
        await message.add_reaction(susEmoji)       
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in hacks):
        embed = discord.Embed(description=mphacks,color=p84clr)
        await message.add_reaction(susEmoji)        
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgc for varsDefends in yts):       
        embed = discord.Embed(description=mpyts,color=p84clr)        
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in yts):
        embed = discord.Embed(description=mpyts,color=p84clr)
        await message.add_reaction(susEmoji)
        await message.channel.send(embed=embed,delete_after=40)
      elif any(varsDefends in mgcNormal for varsDefends in tooYoung):
        embed = discord.Embed(description=mpagewarning,color=p84clr)
        await message.add_reaction(susEmoji)
        await message.channel.send(embed=embed,delete_after=20)
      elif any(varsDefends in mgc for varsDefends in tooYoung):
        embed = discord.Embed(description=mpagewarning,color=p84clr)
        await message.add_reaction(susEmoji)
        await message.channel.send(embed=embed,delete_after=20)
      #elif any(varsDefends in mgc for varsDefends in status):
        #embed = discord.Embed(description=mpstatus,color=p84clr)
        #await message.add_reaction(susEmoji)
        #await message.channel.send(embed=embed,delete_after=90)
      #elif any(varsDefends in mgcNormal for varsDefends in status):
        #embed = discord.Embed(description=mpstatus,color=p84clr)
        #await message.add_reaction(susEmoji)
        #await message.channel.send(embed=embed,delete_after=90)
      #if any(varsDefends in mgc for varsDefends in smpCode):       
        #embed = discord.Embed(description=mpsmpcode,color=p84clr)
        #await message.channel.send(embed=embed,delete_after=90)
      #elif any(varsDefends in mgcNormal for varsDefends in smpCode):
        #embed = discord.Embed(description=mpsmpcode,color=p84clr)
        #awaitmessage.channel.send(embed=embed,delete_after=90)

  #checking when roles is added to a user
  @commands.Cog.listener()
  async def on_member_update(self, before, after): #role_checker/announcer
    guild = self.client.get_guild(mpGuild)
    add_role_channel = self.client.get_channel(chatID)
    remove_role_channel = self.client.get_channel(chatID)
    role = check_role([892872943779070013,903419710568280094,903416348942688297,976315422708228107,962456820360826920,962620486955728896], before, after) #list of roles that will be checked when added to the user
    if role is False:
      pass #no point in doing anything here
    elif role == 892872943779070013:
      embed = discord.Embed(title=mptymsg,description=f"{before.mention} {mpboost}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework
    elif role == 903419710568280094:
      embed = discord.Embed(title=mptymsg,description=f"{before.mention} {mpmember}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework
    elif role == 903416348942688297:
      embed = discord.Embed(title=mpprotect,description=f"{before.mention} {mpmuted}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework
    elif role == 976315422708228107:
      embed = discord.Embed(title=mpfirstmsg,description=f"{before.mention} {mpfirst}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework
    elif role == 962456820360826920:
      embed = discord.Embed(title=mpreview,description=f"{before.mention} {mpreview1}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework
    elif role == 962620486955728896:
      embed = discord.Embed(title=mpfailed,description=f"{before.mention} {mpfailed1}",color=p84clr)
      await add_role_channel.send(embed=embed,delete_after=30) #needs rework

    #sick of people telling me I need to fix my code when it works
    #sure it's not the most efficient but if it works then it works..
    
    """missing_role = None #check_missing_role(before, after)
    if not isinstance(missing_role, bool):
      embed = discord.Embed(description=f"`Role Removed` | `{guild.get_role(missing_role)}` was removed from <@{before.id}>",color=0xfc0303)
      await remove_role_channel.send(embed=embed)""" #example to repeat

    #changing username if needed
    if before.nick != after.nick:
      #await syst.log(self.client, f"`Nickname Changed` | <@{before.id}>\n```{before.nick} -> {after.nick}```")
      changed = await syst.normalize(self.client, [after] if after in guild.members else None)
      if after in changed: 
        await syst.log(self.client, f"`{badName}` | <@{before.mention}>")

  @commands.Cog.listener()
  async def on_application_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(description=f"{mpslashcooldown}",color=p84clr)
      await ctx.respond(embed=embed,ephemeral=True)
    else:
        raise error  # raise other errors so they aren't ignored

def setup(client):
  client.add_cog(events(client))

def check_role(roles, before, after):
  for role in roles:
    if role in [r.id for r in before.roles]: continue
    elif role in [r.id for r in after.roles]: 
      return int(role)
  return False

def check_missing_role(before, after):
  for role in [r.id for r in before.roles]: 
    if role not in [r.id for r in after.roles]:
      return int(role)
  return False 

async def get_text_file(message):
    for attachment in message.attachments:
        return (await attachment.read()).decode()
    return None

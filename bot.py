import discord
from discord.ext import commands
from config import enablelauncher,prefix, langs, enable2ndip ,homelink, token, botactivity, dscserver, memberroleid, banslink, storelink, votelink, forumlink, launcherlink, servername, serverip

if langs == "ro":
  from ro_RO import ipefirsttext, n2iptext,linksbans,discordbotid,ipdesc,ipetitle,ipedesc, helpdesc,helpetitle,helpedesc,linksfourm ,linkslauncher, linksstore, linksvote ,linkshome, linksedesc, linksetitle,linkshome,  logeedin, ready, verifydesc, pingdesc, pingres, userinfodesc, userinfousername, userinfostatus, userinfoheader, userinfojoinneddiscordsv, userinfojoinneddiscord, linksdesc
else:
  if langs == "en":
    from en_UK import ipefirsttext, n2iptext,linksbans,discordbotid,ipdesc,ipetitle,ipedesc, helpdesc,helpetitle,helpedesc,linksfourm ,linkslauncher, linksstore, linksvote ,linkshome, linksedesc, linksetitle,linkshome,  logeedin, ready, verifydesc, pingdesc, pingres, userinfodesc, userinfousername, userinfostatus, userinfoheader, userinfojoinneddiscordsv, userinfojoinneddiscord, linksdesc
  else:
    if langs == "":
      print("You forgot to set a language")
    else:
      print("That language cant be found we are gona load the custom lang")
      from lang import ipefirsttext, n2iptext,linksbans,discordbotid,ipdesc,ipetitle,ipedesc, helpdesc,helpetitle,helpedesc,linksfourm ,linkslauncher, linksstore, linksvote ,linkshome, linksedesc, linksetitle,linkshome,  logeedin, ready, verifydesc, pingdesc, pingres, userinfodesc, userinfousername, userinfostatus, userinfoheader, userinfojoinneddiscordsv, userinfojoinneddiscord, linksdesc

if enablelauncher == "false":
  if langs == "ro":
    print("Nu voi porni integratia de KoolLauncher")
  else:
    print("Not starting the KoolLauncher HOOK")
else:
  if langs == "ro":
    print("Pornesc integratia pentru KoolLauncher")
  else:
    print("Starting the KoolLauncher Hook")

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), activity = discord.Game(name= botactivity), intents=discord.Intents.all())
bot.remove_command('help')

if enable2ndip == "true":
  from config import n2ip


@bot.event
async def on_ready():
    print(logeedin + str(bot.user))
    print(discordbotid + str(bot.user.id))
    print(ready)

@bot.slash_command(description= verifydesc, guild_ids=[dscserver])
async def verify(ctx):
    role = ctx.guild.get_role(memberroleid)
    await ctx.author.add_roles(role)



@bot.slash_command(description= pingdesc, guild_ids=[dscserver])
async def ping(ctx):
    latency = ctx.bot.latency
    latency = latency * 1000
    latency = round(latency)
    await ctx.respond(pingres +"**{}ms**!".format(latency))

@bot.slash_command(description= userinfodesc, guild_ids=[dscserver])
async def userinfo(ctx, member:discord.Member=None):
     if member:
       embed=discord.Embed(title= userinfoheader + f" {member.display_name}", color=0xcbceff)
       embed.add_field(name=userinfousername, value=f"```{member}```")
       embed.add_field(name=userinfostatus, value=f"```{member.status}```")
       embed.add_field(name=userinfojoinneddiscordsv, value= f"<t:{int(member.joined_at.timestamp())}:R>")
       embed.add_field(name=userinfojoinneddiscord, value= f"<t:{int(member.created_at.timestamp())}:R>")
       await ctx.respond(embed=embed)
     else:
       embed=discord.Embed(title=userinfoheader + f" {ctx.author.display_name}", color=0xcbceff)
       embed.add_field(name=userinfousername, value=f"```{ctx.author}```")
       embed.add_field(name=userinfostatus, value=f"```{ctx.author.status}```")
       embed.add_field(name=userinfojoinneddiscordsv, value=f"<t:{int(ctx.author.joined_at.timestamp())}:R>")
       embed.add_field(name=userinfojoinneddiscord, value=f"<t:{int(ctx.author.created_at.timestamp())}:R>")
       await ctx.respond(embed=embed)
if launcherlink == "true":
  @bot.slash_command(description= linksdesc, guild_ids=[dscserver])
  async def links(ctx):
    embed=discord.Embed(title=linksetitle, description=linksedesc, 
    color=discord.Color.green())
    embed.add_field(name= linkshome, value= homelink, inline=False)
    embed.add_field(name= linksbans, value= banslink)
    embed.add_field(name= linksfourm, value= forumlink, inline=False)
    embed.add_field(name= linksvote, value= votelink, inline=False)
    embed.add_field(name= linkslauncher, value= launcherlink, inline=False)
    embed.add_field(name= linksstore, value= storelink, inline=False)
    embed.set_footer(text='Copyright 2022 '+ servername +'. Made by KoolKidDevelopment')
    await ctx.respond(embed=embed)
else:
  @bot.slash_command(description= linksdesc, guild_ids=[dscserver])
  async def links(ctx):
    embed=discord.Embed(title=linksetitle, description=linksedesc, 
    color=discord.Color.green())
    embed.add_field(name= linkshome, value= homelink, inline=False)
    embed.add_field(name= linksbans, value= banslink)
    embed.add_field(name= linksfourm, value= forumlink, inline=False)
    embed.add_field(name= linksvote, value= votelink, inline=False)
    embed.add_field(name= linksstore, value= storelink, inline=False)
    embed.set_footer(text='Copyright 2022 '+ servername +'. Made by KoolKidDevelopment')
    await ctx.respond(embed=embed)


@bot.slash_command(description= helpdesc, guild_ids=[dscserver])
async def help(ctx):
    embed=discord.Embed(title=helpetitle, description=helpedesc, 
    color=discord.Color.green())
    embed.add_field(name= '/help', value= helpdesc, inline=False)
    embed.add_field(name= '/ip', value= 'Afiseaza ip-urile de la server-ul nostru de minecraft')
    embed.add_field(name= '/links', value= linksdesc, inline=False)
    embed.add_field(name="/userinfo", value= userinfodesc, inline=False)
    embed.add_field(name= '/ping', value= pingdesc, inline=False)
    embed.set_footer(text='Copyright 2022 '+ servername +'. Made by KoolKidDevelopment')
    await ctx.respond(embed=embed)

@bot.slash_command(description= ipdesc, guild_ids=[dscserver])
async def ip(ctx):
  embed=discord.Embed(title=ipetitle, description=ipedesc,
  color=discord.Color.green())
  embed.add_field(name= ipefirsttext, value= serverip, inline=False)
  embed.add_field(name= n2iptext, value= n2ip, inline=False)
  embed.set_footer(text='Copyright 2022 '+ servername +'. Made by KoolKidDevelopment')
  await ctx.respond(embed=embed)


bot.run(token)
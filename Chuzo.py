# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:00:46 2020

@author: Ditto Castform
"""

import discord
import sqlito
import random as r
import asyncio

client = discord.Client()
connex = None
pend = 0


@client.event
async def on_guild_join(guild):
    general = discord.utils.find(lambda x: x.name == 'general',  guild.text_channels)
    await general.send('¿Qué dicen los hijueputas?',tts=True)
    await general.send('Escribe !!help para iniciar')
    
@client.event
async def on_voice_state_update(member,before,after):
    
    if ('#1316' in str(member) or 'copete' in str(member.nick).lower()) and before.channel is None and not after.channel is None:
        
        copetebullying = await after.channel.connect()
        copetebullying.play(discord.FFmpegPCMAudio(executable="C:/Users/Cupi2/Documents/discordbot/ChuzoBot/ff/bin/ffmpeg.exe",
                                               source='media/primo.mp3'))
        await asyncio.sleep(3)
        await copetebullying.disconnect()
        await member.guild.text_channels[0].send("El Celoso ha llegado",tts=True)
    
    elif ('#7808' in str(member) or 'jpcarreno29' in str(member.nick).lower()) and before.channel is None and not after.channel is None:
        
        await asyncio.sleep(5)
        n = r.randint(0,1)
        if n:
            await member.guild.text_channels[0].send("Ay, ya se cayó",tts=True)
        else:
            val = discord.File('media/se_cayo.png')
            await member.guild.text_channels[0].send('',file =val)
        
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!!help') or message.content.startswith("!!commands"):
        await message.channel.send(lista_comandos)
    
    if message.content.startswith('!!heil'):
        if message.author.nick is None:
            nombre = str(message.author).split('#')[0]
        else:
            nombre = message.author.nick
        salute = 'Heil {}'.format(nombre)
        await message.channel.send(salute,tts=True)
    
    if message.content.startswith('!!kabs'):
        palabra = message.content.replace('!!kabs ','')
        pregunta = '¿Qué es {}?'.format(palabra)
        await message.channel.send(pregunta,tts=True)

    if message.content.startswith('!!juanito'):
        mensaje = 'Atención, llegó el tren del humor'
        await message.channel.send(mensaje,tts=True)
    
    if message.content.startswith('!!chuzo'):
        await message.channel.send('El menú de ventas está en desarrollo, espérelo más adelante')
        #TODO
    
    if message.content.startswith('!!lois'):
        gente = message.mentions
        mensaje = ''
        for pana in gente:
            if pana.nick is None:
                nombre = str(pana).split('#')[0]
            else:
                nombre = pana.nick
            mensaje+=nombre+', '+fraselois()+'\n'
        if mensaje != '':
            await message.channel.send(mensaje,tts=True)
        else:
            await message.channel.send(fraselois(),tts=True)
    
    if message.content.startswith('!!chacon'):
        await message.channel.send(get_insta())
        
  
    if message.content.startswith('!!paula'):
        gente = message.mentions
        mensaje = ''
        for pana in gente:
            if pana.nick is None:
                nombre = str(pana).split('#')[0]
            else:
                nombre = pana.nick
            mensaje+=nombre+', No sea sapo\n'
        if mensaje != '':
            await message.channel.send(mensaje,tts=True)
        else:
            await message.channel.send('¿Qué le pasa, sapo?',tts=True)

    if message.content.startswith('!!churro'):
        await message.channel.send(get_dato())
        
    if message.content.startswith('!!matiz'):
        tokens = await message.author.voice.channel.connect()
        tokens.play(discord.FFmpegPCMAudio(executable="C:/Users/Cupi2/Documents/discordbot/ChuzoBot/ff/bin/ffmpeg.exe",
                                               source='media/tokens.mp3'))
        await asyncio.sleep(4)
        await tokens.disconnect()
    
    if message.content.startswith('!!shurys'):
        lugar = message.guild
        gente = lugar.members
        rand = r.randint(0, len(gente)-1)
        efecita = gente[rand]
        if efecita.nick is None:
            nombre = str(efecita).split('#')[0]
        else:
            nombre = efecita.nick
        razones = ['por no callarse','por comer pollo asado','por gay','por caerle a las gorditas']
        razon = r.choice(razones)
        await efecita.kick(reason='Por Gay')
        await message.channel.send(nombre+" ha sido expulsado de Wuaira "+razon,tts=True)

    
    if message.content.startswith('!!qlian'):
        gente = message.mentions
        if len(gente) == 0:
            try:
                await message.author.edit(mute=True)
            except:
                pass
        else:
            for pana in gente:
                try:
                    await pana.edit(mute=True)
                except:
                    pass

    if message.content.startswith('!!carreno'):
        gente = message.mentions
        if len(gente) == 0:
            await message.author.edit(nick="Un Negro Marica")
        else:
            for pana in gente:
                try:
                    await pana.edit(nick="Un Negro Gay")
                except:
                    await message.author.edit(nick="Se la chupo a Luis")

    if message.content.startswith('!!tom'):
        roleos = message.guild.roles
        found = False
        for i in roleos:
            if str(i) == 'Gay':
                found = True
        if not found:
            await message.guild.create_role(name='Gay',colour= discord.Colour.magenta(),hoist=True)
        gente = message.mentions
        rolgay = discord.utils.get(message.guild.roles,name='Gay')
        if len(gente) == 0:
            await message.author.add_roles(rolgay)
        else:
            for pana in gente:
                await pana.add_roles(rolgay)  
        
    
    if message.content.startswith('!!marlon'):
        lugar = message.guild
        gente = lugar.members
        rand = r.randint(0, len(gente)-1)
        efecita = gente[rand]
        if efecita.nick is None:
            nombre = str(efecita).split('#')[0]
        else:
            nombre = efecita.nick
        await message.channel.send('EEEEY! '+nombre,tts=True)

    if message.content.startswith('!!dianita'):
        dianita = discord.File('media/diana.png')
        await message.channel.send('',file =dianita)
        
    if message.content.startswith('!!valeria'):
        ran = r.choice(['chavez','maduro','pietro','torres','leo'])
        val = discord.File('media/{}.png'.format(ran))
        await message.channel.send('',file =val)
    
    if message.content.startswith('!!copete'):
        
        songs = ["cheque","rastastas","semaforo","luce","tombos"]
        dur = [136,268,261,339,327]
        nams = ["Fiesta Acústica", "Ras Tas Tas", "Semáforo","Nada le luce","Los tombos son unos hijueputas"]
        
        try:
            canale = message.author.voice.channel
            global connex
            global pend
            connex = await canale.connect()
            cancion = r.randint(0,4)
            
            await message.channel.send('Ahora baila, {}'.format(nams[cancion]))
            connex.play(discord.FFmpegPCMAudio(executable="C:/Users/Cupi2/Documents/discordbot/ChuzoBot/ff/bin/ffmpeg.exe",
                                               source='media/{}.mp3'.format(songs[cancion]))) 
            numval = r.randint(1,15000)
            pend = numval
            await asyncio.sleep(dur[cancion])
            if pend == numval:
                await connex.disconnect()
                pend = 0
                connex = None
        except discord.errors.ClientException:
            connex.stop()
            await connex.disconnect()
            pend = 0
            connex = None
        except AttributeError:
            await message.channel.send('Unete a un canal para sentir el sabor')
    
lista_comandos = '¡¡¡Bienvenidos al bot del Chuzo!!! \n\n'+\
                    'La lista de comandos es la siguiente: \n'+\
                    '!!commands o !!help: Lista de Comandos \n'+\
                    '!!heil : Te saludo\n'+\
                    '!!chuzo : Inicia el menú de ventas\n'+\
                    '!!kabs args : Pregunta qué es la palabra siguiente\n'+\
                    '!!chacon : Da un instagram aleatorio\n'+\
                    '!!paula (@users) : Pide al/los usuario/s que no sea/n sapo/s\n'+\
                    '!!churro : Da un dato curioso de la Marihuana\n'+\
                    '!!shurys : Expulsa a un miembro aleatorio del server\n'+\
                    '!!qlian (@users) : Da los derechos de un hombre feminista\n'+\
                    '!!tom (@users) : Otorga el rol de "Gay" al usuario\n'+\
                    '!!carreno (@users) : Le da el apodo adecuado a los usuarios mencionados\n'+\
                    '!!marlon : Dice "ey" a un usuario aleatorio\n'+\
                    '!!dianita : Muestra lo más lindo de Wuaira\n'+\
                    '!!valeria : Muestra uno de los amores de Valeria\n'+\
                    '!!copete : Le pone sabor al servidor\n'+\
                    '!!lois : Expresa la opinión sobre su comentario\n'+\
                    '!!juanito : Reacciona a la comedia\n'+\
                    '!!matiz : Reproduce el sonido de Tokens'

def get_insta():
    instas = sqlito.get_instas()
    handicap = r.randint(1,10)
    if handicap == 1:
        elinsta = 'https://www.instagram.com/maracifuentes1'
    else:
        num = r.randint(0,len(instas)-1)
        elinsta = 'https://www.instagram.com/'+instas[num][0]
    return elinsta

def fraselois():
    lafrase = r.randint(0,4)
    frases = ["Ah bueno, pa saber","No sabía pero ahora ya sé","Buen dato mi rey, pero no te pregunté","Amanecimos preguntones hoy","Imagínate si te hubiera preguntado de verdad"]
    frase = frases[lafrase]
    return frase


def get_dato():   
    return r.choice(['Durante la II Guerra Mundial la marihuana fue utilizada por los soldados como un «suero de la verdad». Así pues, en los interrogatorios se administraba una gran cantidad de cannabis a los soldados para que revelasen determinadas informaciones',
                     'El repentino aumento del apetito después de fumar marihuana es algo puramente científico y 100% real: la leptina es la hormona que controla la saciedad y, cuando tomamos cannabis, los receptores del THC la engañan y simulan que tenemos hambre cuando, en realidad, no tendríamos.Sin embargo, algunas variedades producen un cannabinoide llamado THCV (tetrahidrocannabivarin) que modula los efectos del THC sobre el apetito',
                     'Hasta 1942 los médicos recetaban marihuana para mitigar los dolores del parto. De hecho, en la actualidad muchas mujeres usan marihuana para paliar los dolores menstruales.',
                     'La mayoría de los relojes de la película de Pulp Fiction marcan las 4:20.',
                     'Cerca del 1900, el gobierno de Estados Unidos cultivó marihuana a la ribera del río Potomac para estudiar el poder medicinal de la planta.',
                     'El presidente George Washington plantaba marihuana en el patio de su casa.',
                     'El guano -nombre popular que reciben los excrementos de murciélago- es el mejor abono para la marihuana. Aunque también existen otros tipos de abono igual de buenos para mejorar el aspecto olor y sabor de tus plantas.',
                     'El alimento más rico conocido hasta el momento en ácidos grasos omega-3 es el aceite de marihuana. Muchos científicos se preguntan si podría ser la solución definitiva para bajar el colesterol.',
                     'Desde que se legalizó la marihuana en Holanda el consumo de drogas duras ha disminuido en el país.',
                     'Paraguay es el mayor productor de marihuana del mundo.',
                     'Comer un mango maduro 20 minutos antes de fumar marihuana multiplica los efectos que el THC tiene sobre el organismo. Esto se debe a que las substancias activas (entre ellas los terpenos) del mango ayudan a la absorción del THC, facilitando así sus efectos.',
                     'Los cuadros de Rembrandt, Van Gogh y Gainsboroug fueron pintadas en lienzos de lino de cáñamo.',
                     'No es sobre la Marihuana, pero Chacón es re Gay'])



def elclient():
    return client

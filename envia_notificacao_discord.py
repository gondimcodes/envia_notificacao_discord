#!/usr/bin/python3
# Script em python para envio de notificacoes para um canal do Discord via webhooks
# Sao passados 2 argumentos em linha de comando:
#    <titulo da mensagem>
#    <texto da mensagem>
# Exemplo: ./envia_notificacao_discord.py "ALERTA RJO-DC01-DNS-RECURSIVO01" "Falha no sistema de arquivos."
# Para funcionar eh necessario instalar: pip install discord discord-webhook
# Autor: Marcelo Gondim - gondim at gmail.com
# Data: 21/05/2023
# Versao: 1.0
#
# envia_notificacao_discord.py is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
url_webhook = "https://discord.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
nome_bot = "Bot ISPUP!"
link_icone = "https://xxxxxx/xxxxx/bot.gif"

import sys

title = sys.argv[1]
msg = sys.argv[2]

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='%s' %(url_webhook))
embed = DiscordEmbed(title='%s' %(title), description='%s' %(msg), color='03b2f8')
embed.set_author(name='%s' %(nome_bot), icon_url='%s' %(link_icone))

webhook.add_embed(embed)
response = webhook.execute(embed)

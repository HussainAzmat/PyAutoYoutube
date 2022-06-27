from discord import Webhook, RequestsWebhookAdapter
import discord
webhook = Webhook.partial(123456, 'abcd', adapter=RequestsWebhookAdapter())






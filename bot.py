import random

import vk_api
import vk_api.bot_longpoll
import handlers

# importing my modules
from entities import UserState

from logger import (log,
                    configure_logger,
                    logging_handlers,
                    logging_levels,
                    logging_formatters)

import settings


class Bot:
    def __init__(self, group_id: int, token: str):
        self.vk: vk_api.VkApi = vk_api.VkApi(token=token)

        self.longpoller: vk_api.bot_longpoll.VkBotLongPoll = vk_api.bot_longpoll.VkBotLongPoll(
            vk=self.vk,
            group_id=group_id)

        self.api: vk_api.vk_api.VkApiMethod = self.vk.get_api()
        self.users: dict = dict()

    def on_message(self, text: str, user_id: int) -> str:
        for intent in settings.INTENTS:
            if any(token.lower() in text.lower() for token in intent['tokens']):
                if intent['answer']:
                    text_to_send = intent['answer']
                else:
                    text_to_send = self.start_scenario(user_id=user_id, scenario_name=intent['scenario'])
                break
        else:
            text_to_send = settings.DEFAULT_ANSWER

        return text_to_send

    def start_scenario(self, user_id: int, scenario_name: str) -> str:
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]

        text_to_send = step['text']

        self.users[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id: int, text: str) -> str:
        state = self.users[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        # get handler
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                self.users.pop(user_id)
                log.info('Added new phone number: {client_phone}'.format(**state.context))
        else:
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send

    def on_post(self, text: str, user_id: int):
        self.api.messages.send(
            message=text,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id,
        )

    def on_event(self, event: vk_api.bot_longpoll.VkBotEvent) -> None:
        if event.type != vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            log.info(f'Wrong event type {event.type}')
            return

        # get data
        user_id = event.object.message['peer_id']
        text = event.object.message['text']

        # check if exists in local db
        if user_id in self.users:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            text_to_send = self.on_message(text=text, user_id=user_id)

        self.on_post(text_to_send, user_id)

    def run(self) -> None:
        for event in self.longpoller.listen():
            try:
                self.on_event(event)
            except Exception as e:
                log.exception(f'While listening an error occured {e}')


if __name__ == '__main__':
    configure_logger(logging_handlers, logging_formatters, logging_levels)
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
#!/usr/bin/env python3

import os
from hermes_tools import send_message

def send_to_me(text):
    # Load from the environment instead of hardcoding
    target = f"telegram:{os.environ.get('TELEGRAM_HOME_CHANNEL')}"
    send_message(action='send', target=target, message=text)

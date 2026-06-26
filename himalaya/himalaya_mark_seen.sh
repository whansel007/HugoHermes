#! /usr/bin/bash

/usr/local/bin/himalaya \
envelope flag $(1) \
add "Seen" \
--config /root/.config/himalaya/config.toml \
--output json
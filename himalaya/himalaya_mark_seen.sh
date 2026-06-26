#! /usr/bin/bash

/usr/local/bin/himalaya \
envelope flag \
add "Seen" $(1) \
--config /root/.config/himalaya/config.toml \
--output json
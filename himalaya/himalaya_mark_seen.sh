#! /usr/bin/bash

/usr/local/bin/himalaya flag \
add "Seen" $(1) \
--config /root/.config/himalaya/config.toml \
--output json
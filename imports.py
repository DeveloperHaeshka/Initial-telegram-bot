import logging
import sqlite3
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import quote_html
from datetime import datetime, timedelta
from decimal import Decimal

import config
from db import cursor, connect

from commands2 import (
    start_handler
)

from commnads import (
    commands_handler
)
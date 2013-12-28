# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import pytz

EPOCH = datetime(1970, 1, 1, 0, 0, tzinfo=pytz.utc)

def convert_epoch_millis_to_datetime(epoch_millis):
    return EPOCH + timedelta(milliseconds=epoch_millis)
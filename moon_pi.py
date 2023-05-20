#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime

import csv
import random

from subprocess import call

import emoji #I use emoji for the low battery icon. You may choose something else.
import pijuice # import the PiJuice module

# get battery charge info from the PiJuice and set charge_pct to that value
pj = pijuice.PiJuice(1, 0x14) # create an instance of the PiJuice class
battery_info = pj.status.GetChargeLevel() # get the battery charge level
charge_pct = format(battery_info['data'])

# get today's date and break it into day and month variables
today = datetime.today().strftime('%Y-%m-%d')
currentDay = datetime.now().day
currentMonth = datetime.now().month

# Compare the month and day of the recipient's birthday with today's month and day
# Replace BDAYMONTH w/ recipient's month of birth and BDAYDAY w/ day of birth
# This will replace the random moon quotation with HAPPY BIRTHDAY on the recipient's birthday
if BDAYMONTH == currentMonth and BDAYDAY == currentDay:
    quotation_text = "HAPPY BIRTHDAY!"
    credit_text = ""
    quotationSize = 44
# If it's not the birthday, then the script grabs a random quotation from the file.
# Replace "/home/pi/quotations.csv" with your own file
else:
	with open('/home/pi/quotations.csv', 'r') as f:
   		reader = csv.reader(f)
   		# Skip the header row
   		next(reader)
   		# Convert the remaining rows to a list
   		rows = list(reader)
   		# Choose a random row
   		random_row = random.choice(rows)
   		#set the variables to print the text later
   		quotation_text = random_row[0]
   		credit_text = random_row[1]
   		quote_length = int(random_row[2])
   		if quote_length <=54:
   			quotationSize = 24
   		elif quote_length > 54 and quote_length < 60:
   			quotationSize = 22
   		elif quote_length >= 60 and quote_length <= 65:
   			quotationSize = 20
   		else:
   			quotationSize = 18


logging.basicConfig(level=logging.DEBUG)

# Grabs today's date and formats it for display
date_to_show = datetime.today().strftime('%A, %B %-d')

# open the .csv file containing the moonphase data and grabs the needed info
with open('/home/pi/moon_data.csv') as csvfile:
  # read the file as a dictionary
  reader = csv.DictReader(csvfile)
  # iterate over the rows in the file
  for row in reader:
    # if the date in the current row matches today's date
    if row['datetime'] == today:
      # set the caption
      caption_text = row['caption']
      #set the file
      filename = row['file']

#defining variables for the text to be printed
# I used Luminari, Futura, and AppleColorEmoji (for the low battery indicator)
# You'll want to choose your own and you'll need to put them in proper directory
quotation = ImageFont.truetype(os.path.join('/home/pi/Luminari.ttf'), quotationSize)
credit = ImageFont.truetype(os.path.join('/home/pi/Futura.ttc'), 18)
date_and_phase = ImageFont.truetype(os.path.join('/home/pi/Futura.ttc'), 26)
battery_warning = u"\U0001FAAB"
unicode_font = ImageFont.truetype("/home/pi/AppleColorEmoji.ttc", 26)


epd = epd5in65f.EPD()

epd.init()

epd.Clear()

# Note that you will need to create your own images and possibly change the image directory below
logging.info("getting image file")
Himage = Image.open('/home/pi/images/%s' % (filename))
draw = ImageDraw.Draw(Himage)
draw.text((300, 5), quotation_text, font = quotation, fill = 0, anchor = 'mt')
draw.text((600,40), credit_text, font = credit, fill = 0, anchor = "rm")
draw.text((10, 410), date_to_show, font = date_and_phase, fill = epd.WHITE, anchor = "lt")
draw.text((590, 410), caption_text, font = date_and_phase, fill = epd.WHITE, anchor = "rt")
if int(charge_pct) > 20:
	print("Battery level is fine.")
else:
	draw.rectangle((10, 55, 35, 90), fill="white")
	draw.text((10, 60), battery_warning, font=unicode_font, embedded_color=True)
epd.display(epd.getbuffer(Himage))

# It's super important to sleep the display when you're done updating, otherwise you could damage it

epd.sleep()

call("sudo shutdown -h now", shell=True)

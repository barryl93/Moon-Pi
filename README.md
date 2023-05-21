# Moon-Pi
An ePaper moon calendar powered by Raspberry Pi

![IMG_9535](https://github.com/barryl93/Moon-Pi/assets/39839859/7b96522b-2f72-4b4d-bb55-57c7d8657edb)

OK, so you want to build a moon-a-day calendar! Let's get started. You'll need the following:

<ul>
<li><a href="https://www.waveshare.com/pico-epaper-5.65.htm">Waveshare 5.65in epaper display</a></li>
<li><a href="https://www.pishop.us/product/pijuice-zero-a-portable-power-platform-for-raspberry-pi-zero/">PiJuice Zero</a></li>
<li><a href="https://www.pishop.us/product/pijuice-zero-1200mah-battery/">PiJuice 1200mah Battery</a></li>
<li><a href="https://www.amazon.com/gp/product/B081J74KN7?ie=UTF8&psc=1">5x7 Black Shadow Box</a></li>
<li><a href="https://www.amazon.com/gp/product/B0BBSL6824?ie=UTF8&psc=1">5x7 Uncut Mat Boards</a></li>
<li><a href="https://www.amazon.com/dp/B07WVWCYJ5?psc=1&ref=ppx_yo2ov_dt_b_product_details">Picture Frame Turn Fasteners</a></li>
<li>micro-USB to USB-A cable</li>
</ul>

You will also need a Raspberry Pi of your choice (I used a Pi Zero W), a screwdriver, wires, screws, a drill, etc. And maybe even some thin plywood and a saw.

# Step One: Images
You'll need to create your own moon images because the ones I have in my project aren't available for public license. Feel free, though, to use the background image I created, located in this repository. It has a yellow band already in place for the quotation text. You can have as many images as you like. I use one each for full and new moons, one each for first and third quarters, two each for waxing and waning gibbous, and three each for waxing and waning crescents. It's up to you. Just be sure to sync it up with the Moon Data, described below.

# Step Two: Moon Data
You can see a sample file of moon data in this repository. You'll want to extend it out yourself. Doing it this way means you don't have to have your Pi talk to the internet at all -- all data is on the device. Note that there are sometimes multiple images depending on the phase of the moon. The sample file is set up to work with the script provided here. If you change the formatting of the moon data file, you'll need to tweak the Python script to match.

# Step Three: Quotations
You'll have to find your own quotations. I've put a few in the sample file for you. Note that one field measures the character length of the quotation. This is because you only have one line (no line wrapping!) to print your quotation, so the font size changes depending on the line length. If you use a different font than the one I've chosen, you'll need to figure out your own line length/font ratios with some trial and error. (That's how I did it!) Use Excel or Numbers or Sheets or whatever to count up the line lengths for you automatically -- makes life easier! And don't forget to enclose in quotation marks any quotations that have commas in them!

# Step Four: Wire it Up
There are a total of 13 wired connections (not counting plugging the battery into the PiJuice). There are eight wires from the Raspberry Pi to the display and five wires from the Pi to the PiJuice.

Here's the pinout guide to connect the display to the Pi: https://www.waveshare.com/wiki/5.65inch_e-Paper_Pi

And here's the pinout for the PiJuice: https://pinout.xyz/pinout/pijuice

And here's the <a href="https://learn.pi-supply.com/make/pijuice-zero-quick-start-guide/">PiJuice Quick Start Guide</a>. You'll need this to walk you through setting up the PiJuice to wake up the Pi on a schedule.

# Step Five: Software
Everything you need is in the moon-pi.py script in this repository. Read through it carefully -- it's copiously commented and will walk you through the modifications you need to make so that, for example, it says "Happy Birthday!" on the right day. You may also need to make other modifications depending on choices you make in the first three steps of this guide. If you change text lengths or images or how the moon data is formatted, you may need to tweak the script.

You'll need to set up either a cronjob or a system service to run the moon-pi script on reboot. In my experience, it was easier to use <code>systemd</code>, but YMMV. Also, note that you'll need to build in some delay time between booting the Pi and running the script. Otherwise, the script encounters errors by running before it has permissions for everything it needs. I use a 65-second delay and it works great.

Once you've got it all set up, remember that when the Pi boots, it'll only run for a few minutes before shutting itself down. So if you realize you need to fix or tweak something, you'll need to be sure to SSH into the PI and avail yourself of <code>pkill</code> before the script stops. (In my experience, there's plenty of time to do this. And if you miss your window, you can always reboot the Pi and try again!)

# Step Six: The Frame
Any properly sized frame should work. I used a shadow box, linked above. Once you have the display and the mat in, I suggest screwing everything into place so that it doesn't jostle around. I tried cutting my own mats, but couldn't keep it neat -- a local frame shop was kind enough to cut several of them for me for a few bucks.

My shadow box came with an insert designed to keep the back panel in place. I drilled some holes in that and mounted the Pi, the PiJuice, and the battery. Don't screw all the way through -- there isn't enough space between the insert and the frame itself to accomodate a screw poking out! I used nylon spacers to keep the Pi and PiJuice from touching the insert.

The back panels of most frames and shadow boxes are too flimsy for my purposes, so I cut a piece of thin plywood to size, then drilled ventilation holes. (A Pi Zero shouldn't have any heat issues, but I'm paranoid.) I also cut a slot for a USB cable, then stapled a Velcro cable wrap to the back panel for cable management. You can probably come up with something nicer! Don't forget that you need a way to keep the back panel in place -- I used some frame turn fasteners from Amazon. Piece of cake.

# The End
OK, that's the process! Enjoy!

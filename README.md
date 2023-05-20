# Moon-Pi
An ePaper moon calendar powered by Raspberry Pi

![IMG_9535](https://github.com/barryl93/Moon-Pi/assets/39839859/e3b3a1f5-d8be-43fe-9456-959c7cb89944)

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
You'll need to create your own moon images because the ones I have in my project aren't available for public license. You could find 
Size... Space for quotations... Fonts...

# Step Two: Moon Data
Give a sample file... Explain about multiple images for the phases as they change...

# Step Three: Quotations
Explain about font sizes and length of quotations...

# Step Four: Wire it Up
Link to PiJuice Quick Start Guide https://learn.pi-supply.com/make/pijuice-zero-quick-start-guide/
Link to PiJuice Pinout https://pinout.xyz/pinout/pijuice
Link to Pinout guide to connect display to Pi https://www.waveshare.com/wiki/5.65inch_e-Paper_Pi

Systemd!

Once you've got it all set up, realize that when the Pi boots, it'll only run for a few minutes before shutting itself down. So if you realize you need to fix or tweak something, you'll need to be sure to SSH into the PI and avail yourself of <code>pkill</code> before the script stops. (In my experience, there's plenty of time to do this. And if you miss your window, you can always reboot the Pi and try again!)

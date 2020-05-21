# green_ecobee
Using router status page and IFTTT, set ecobee based on home occupancy.
Improves on "location-aware" thermostats that base occupancy on error-prone methods like motion-sensing or nmap scanning.

Written for DD-WRT router firmware but modifiable for any router that shows connected MAC addresses.
Edit the 'known_macs' file to list the MACs of phones that are connected to home wifi when someone is "home".
Also update the ifttt maker "key", and router info such as ip, url, and auth.

Works by sending webhook request to IFTTT and connected ecobee account, or any other connected thermostat. Changes the ecobee comfort settings to heat or cool less if no one is home. Run on cron every 2 minutes during waking hours with:

*/2 7-21 * * * /usr/bin/python3 /path/to/green_ecobee.py

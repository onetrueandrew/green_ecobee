# green_ecobee
Using router status page and IFTTT, set ecobee based on home occupancy.
Improves on "location-aware" thermostats that base occupancy on error-prone methods like motion-sensing or nmap scanning.

Written for DD-WRT router firmware but modifiable for any router that shows connected MAC addresses
Edit the 'known_macs' file to list the MACs of phones that are connected to home wifi when someone is "home"

Works by sending webhook request to IFTTT and connected ecobee account, or any other connected thermostat.

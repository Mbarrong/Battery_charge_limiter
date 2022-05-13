# Battery_charge_limiter
ASUS battery charge limiter

... for Ubuntu 22.04

The battery charge limit can be set through the file:
/sys/class/power_supply/BAT0/charge_control_end_threshold

This program is a simple UI that edits that file. It will check for sudo privileges and will shell out to get them if needed.

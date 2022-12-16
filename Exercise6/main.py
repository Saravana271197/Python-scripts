from devices import Firewall
from devices import Switch
from devices import Load_balancers
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")
# Create a Switch instance
Switch1 = Switch("Switch1")
# Configure Switch
Switch1.configure_switch()
# Verify CRC
Switch1.calculate_crc("dummy data of switch")
# Create a loadbalancer instance
loadbalancer1 = Load_balancers("Switch1")
# Configure loadbalancer
loadbalancer1.configure_Load_balancers()
# Verify CRC
loadbalancer1.calculate_crc("dummy data of switch")
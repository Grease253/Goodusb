import usb.core
import usb.util
import time

# List of devices which are allowed to be connected
dev_allowed = [ 
  { 
    idVendor: 0xABCD, 
    idProduct: 0x1234 
  } 
]

# List of devices which cause an alert when connected 
dev_alert = [ ]

# Setup USB device detection
dev = usb.core.find(find_all=True)

# Monitor USB devices
while True:
  # Get all connected USB devices
  devices = usb.core.find(find_all=True)
  
  # Iterate over all connected devices
  for device in devices:
    # Check to see if device is authorised in allowed list
    if device in dev_allowed:
      continue
    # Check to see if device is on alert list
    elif device in dev_alert:
      print("ALERT - Suspicious activity detected!")
      continue
    # If device is not on alert or allow list - Report it
    else: 
      print("Device has been detected")
      continue
  time.sleep(15)
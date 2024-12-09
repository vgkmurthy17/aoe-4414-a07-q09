# max_bitrate.py - Calculate the maximum data transmission rate for a given communication link
#
# Command line format:
# python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# This python code estimates the maximum achievable data rate for a communication link.

# Input Variables:
#  tx_w: Power output from the transmitter (W)
#  tx_gain_db: Gain of the transmitting antenna (dB)
#  freq_hz: Carrier wave frequency (Hz)
#  dist_km: Separation between communication endpoints (km)
#  rx_gain_db: Gain of the receiving antenna (dB)
#  n0_j: Background noise power density (Joules)
#  bw_hz: Available bandwidth for transmission (Hz)

# Output:
#  Displays highest achievable bitrate in bits per second.
#
# Author: Vineet Keshavamurthy
# Contributions: None
#
# Licensing Info: See LICENSE for details.

import math  # For handling functions
import sys   

# Define universal constants
c = 2.99792458e8  # Speed of light in meters per second

# Initialize communication parameters with placeholder values
tx_w = float('nan')        # Transmitter power (Watts)
tx_gain_db = float('nan')  # Transmitter antenna gain (dB)
freq_hz = float('nan')     # Transmission frequency (Hz)
dist_km = float('nan')     # Distance between nodes (km)
rx_gain_db = float('nan')  # Receiver antenna gain (dB)
n0_j = float('nan')        # Noise spectral density (Joules)
bw_hz = float('nan')       # System bandwidth (Hz)

# Extract command-line arguments
if len(sys.argv) == 8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print("Incorrect number of arguments passed. Recheck the command line entered.")
    exit()

lam = c/freq_hz # Calculate wavelength
dist_m = 1e3*dist_km # Convert km to meters

# calculations for signal loss causing Break down signal power 
link_loss = 10**(-1/10) # Transmission line loss
atm_loss = 10**(0/10) # Atmospheric loss
path_loss = (lam/(math.pi*dist_m*4))**2

#calculation of C and N
C_factor = (tx_w * link_loss * tx_gain_db * path_loss * atm_loss * rx_gain_db)
N_factor = n0_j * bw_hz

#Final calculation of r_max
r_max = bw_hz * math.log2((C_factor / N_factor)+1)

# Display final result rounded down
print(math.floor(r_max))


# Python script to help us sieve through the pcap file and create graphs which would be used by our sacsit paper
# the dependecies are pyshark and pygal or matplotlib

import pyshark
from pygal import XY
import matplotlib

pkt_sizes =[]
pkt_window = []
cap = pyshark.FileCapture(filename. only_summaries = True)
for packet in cap:
	# Create a point X = date, Y= bytes
	pkt.sizes.append((float(packet.time),int(packet.length)))
	
#Creating an instance of pygal
pkt_size_chart = XY(width=400, height=300,style=LIghtGreen Style, explicit_size = True)
pkt_size_chart.title = 'Packet Sizes'

#add points to chart and render html
pkt_size_chart.add('Size', pkt_sizes)
chart = pkt_size_chart.render()
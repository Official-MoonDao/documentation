# Time Synchronization via LEO Satellites
https://www.linkedin.com/events/timesynchronizationvialeosatell7099098080062423040/
## Abstract  
LEO satellites are being used as a resilient complement or alternative to GPS/GNSS to provide telecom, data centers, and other critical infrastructure with precise UTC time synchronization.  
LEO PNT from Satelles (called STL), is an authenticated signal that is stronger than GPS/GNSS signals, and able to penetrate buildings to indoor antennas. This allows for more secure and lower cost installations where outdoor GPS/GNSS antennas or remote NTP or PTP time services are unavailable, not secure, not feasible, not desirable, or too expensive. The STL signal is also highly resilient to multi-path, jamming  
and spoofing, and it’s available worldwide now.  
Speaker  
Charlie Meyer is a Senior Technical Director at Satelles Inc., where he develops LEO satellite timing solutions for critical infrastructure users.  
Previously he was a Distinguished Member of the Technical Staff at Alcatel-Lucent/Nokia/Bell Labs where he worked for 25 years. He was a Principal Architect and SME for Wireless 3G/4G/5G RAN timing and synchronization systems. He has designed numerous GPS, GNSS, PTP, and OCXO solutions and has worked with multiple US government agencies regarding the dependence of telecommunications on GPS. He is a member of ATIS SYNC, IEEE-1952, OCP-TAP, a senior member of the IEEE and holds four US patents.

## Notes
_Zero-trust authentication_

GNSS is the most accurate method to get timing right now.
- Needs a wide sky view. Urban canyons make it unusable!
- Doesn't work well indoors
- Prone to jamming/spoofing

Remote NTP and PTP services
- Time _distribution_ only
- May not be UTC traceable, available, secure, feasible, or cost-effective

Satelles STL service is a LEO PNT 
- alternative to GPS/GNSS for network time and sync
- Resilient to gps jamming/spoofing
- works indoors

STL == satellite time and location

Uses Iridium LEO constellation, L-band
- Higher power (closer to earth) up to 30dB stronger than MEO GNSS
- GPS is an overlay of multiple systems transmitting on the same freq, so rx have to decorrelate them to use it. STL isn't sharing, so doesn't have this problem
- Since LEO orbits are high velocity, multipath signal cancellations only last for minutes (not hours like MEO)

![[Screenshot 2023-08-30 at 2.13.47 PM.png]]
![[Screenshot 2023-08-30 at 2.15.37 PM.png]]
![[Screenshot 2023-08-30 at 2.17.57 PM.png]]
![[Screenshot 2023-08-30 at 2.20.48 PM.png]]
![[Screenshot 2023-08-30 at 2.24.51 PM.png]]
![[Screenshot 2023-08-30 at 2.31.18 PM.png]]
![[Screenshot 2023-08-30 at 2.33.00 PM.png]]
![[Screenshot 2023-08-30 at 2.35.21 PM.png]]

## questions
- Is STL using Iridium's system clock for holdover? What are the performance requirements for a clock to serve STL transmitter?
	- Iridium have "good enough" clocks onboard, not quite as good as GPS but more available
	- Observations show that accuracy can be maintained to nanoseconds → this depends on satellite system clock accuracy
	- https://www.gpsworld.com/pnt-by-other-means-satelles/
- Is the STL transmitter specific to Iridium platform or could it be adapted to other satellite busses?
	- Exclusive use of one of the iridium channels for PNT
	- Might be possible to put on another bus depending on SDR capabilities
	- Requires at least an OCXO or Rubidium oscillator
- Is STL using GPS/GNSS to sync itself to UTC?
	- Can use GPS or NIST to correct, error is monitored by ground sys
	- Corrections are commanded to satellite
	- Satellite bus does not correct onboard from GPS
- What does time transfer uplink look like?
	- Iridium manages this, and also transfers time from ground to space, and that flows to transmitter
	- Correct like with GPS
- Do faster orbital speeds in LEO degrade timing accuracy?
	- There's a lot of Doppler...
	- Bursts have to manage doppler offsets along with ranging data
	- Uses a specialized Kalman filter designed for this situation (proprietary)
	- The filters are built in to the receivers
- Proprietary receiver? What does compatibility look like compared to GPS rx?
	- Deployed ground systems use a proprietary antenna (3x6in or so) to receive Lband signal
	- Interface to downstream systems is the same as a GPS receiver, so compatible with existing systems that accept GPS signal
- What's the delay spread of the signal? How many satellites can receive at once?
	- Compensate for doppler and space-related params, but doppler is the biggest contributor
	- More signals == better performance
- The STL isn't a physical component, it's a software application that uses Iridium hardware
- Could this be adapted to Starlink?
	- didn't say it, but yes. Starlink is an SDR -- if they can accomodate the L-band freq, yeah
	- X-band is a different discussion.... maybe?
- Is this a subscription service?
	- Yes. Can only get this signal if you pay
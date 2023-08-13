---
tags: notes
---
> [!warning]
> This document was originally authored as part of the Space Engineering Guild project in April 2023, not the Lunar Comms project.
# A Primer on Future Lunar Communications Infrastructures & Related Challenges

Author:: [[@philiplinden|Philip Linden]]
Space Engineering Guild, [[MoonDAO]]
Apr 4, 2023

link:: https://docs.google.com/document/d/1Wj4L7IGK1iwLjSjg0FwqYjgjxByOaWxGbJ5iSWf9pE8/edit

> [!note] Abstract
> There is a lot of interest and necessity for lunar communications infrastructure, but so far most endeavors are experimental, expensive, or difficult to access. There is lots of new technology and a ton of potential for developing new business and governance models. This topic is still nascent and is growing rapidly―there are no clear answers, and that means there's still a lot we can explore.

# It's a solved problem―but that's not the problem

## It's not easy, but it can be done

First, the Moon is very far away from Earth. The average distance between the Earth and the Moon is about 384,400 kilometers―nearly ten times further than the distance from Earth to GPS satellites. This means that radio signals take about two and a half seconds to travel from the Earth to the Moon and back. When a communication signal is sent through cislunar space, the beam spreads out and the intensity of the signal becomes weaker [proportionally to the square of the distance traveled](https://en.wikipedia.org/wiki/Inverse-square_law). Because the Moon is so far away, the transmitted signals must either be very powerful or must be aimed with very good accuracy to be received at the other end.

Second, the Moon has no atmosphere. This means that there is nothing to block or absorb radio signals. As a result, radio signals from the Earth can be easily scattered by the Moon's surface, unlike on Earth where radio signals can bounce around in the atmosphere to the other side of the globe.[^1] Moreover, the Moon has no magnetic field. This means that the Moon is not protected from the solar wind. The solar wind is a stream of charged particles from the Sun. The solar wind can interfere with radio signals.

All of these factors make telecommunications difficult at and around the Moon. However, there are a number of technologies that can be used to overcome these challenges. For example, high-gain antennas or lasers can be used to focus signals and improve reception.[^2][^3] Delay- and disruption-tolerant networking protocols can be used to make connections more resilient. [^4][^5] And much more. [^6][^7][^8][^9][^10]

## Restricted to the privileged few

While the technology capable of overcoming these challenges has been used for decades to command and control spacecraft in cislunar space, one aspect remains relatively unchanged: *access* (or lack thereof).

Today, NASA's Deep Space Network (DSN) and other state-owned equivalents are the primary resources used to transmit and receive data from cislunar spacecraft. DSN is limited in bandwidth and schedule, which are already heavily oversubscribed,[^11][^12][^13] and must compete with all other deep space missions served by the DSN. Not to mention using a government-operated resource has a multitude of ever-evolving geopolitical and regulatory implications in its own right.

Even with a network to use, the technology needed to interface with it is still relatively expensive and/or nascent.[^9][^14][^15][^16] Looking at the landscape of low Earth-orbit (LEO) satellite missions before and after the introduction of the CubeSat standard, it is clear that the barrier to entry for space missions is, well, the barrier itself! An accessible platform for conducting missions in space―such as open reference designs, commodity components, and standardized interfaces―can bootstrap an entire thriving industry that would be otherwise infeasible for all but the largest institutions.[^17][^18]

The number of missions that plan to operate on and around the Moon is large and growing every day [^19]. It is clear that more communications infrastructure is needed in order to sustain a diverse, multi-national ecosystem of public and private/commercial lunar activities. 

# Governance & policy is unproven and untested

The whole business of lunar communications infrastructure is still not really figured out (pun intended). While there has been discussion about the implications of different paradigms of shared infrastructure,[^10][^20][^21][^22][^23] many of the governance and economic gray areas remain nebulous. For example, here is a non-exhaustive list of open questions:

- Communications links are literally a life-and-death resource for spacecraft and crewed missions alike. What if a spacecraft/astronaut dies because a network operator did not allow them to send/receive data over a link that was available?
- Is the network operator at fault? Is this fair play?
- Does the ethical situation change if the two parties are nations in conflict?
- Does the ethical situation change if one or both parties are private businesses?
- What is the business model of a communications relay service?
- Do users pay per bit of data? Some bits take more work to transmit than others.
- If data is lost at an endpoint, but the network operator still did work to relay data between the endpoints, does the user still owe the network operator for the transmission?
- Do users pay a fee for access to the network? A connection is not always guaranteed due to the dynamic and chaotic nature of a cislunar communications network. What if a user pays for the service but the service cannot serve that user due to coverage or line-of-sight issues?
- If two paying users request services but the network can only support one user at a time, which user gets priority?
- Does the ethical situation change if the content of the data contains life-or-death information? 
- What if the requests are coming from government actors?
    

# Interesting examples

There are many, many organizations looking into lunar communications infrastructures. I've picked out a few that were interesting to me.

## A non-exhaustive list of relevant missions

State-sponsored missions: [^5], [^7], [^8], [^24], [^25]

Private & Commercial missions: [^26][^27][^28]

## Selected relevant technologies

- Modular, commoditized optical terminals that don't need a priori knowledge of where the origin of the signal is coming from: [^16]
	- The spacecraft is divided into many small, steerable optical terminals facing out in many directions. Once the terminal determines where the signal is coming from, it can form a two-way link by selecting the module most closely aligned to the signal's origin, then using a steering mirror for fine pointing to maintain the link. The spacecraft bus remains still and does not need to perform a rotational slew to establish or maintain a link.
	- The terminals have many diodes that figure out on-the-fly where a signal is coming from, just like how an HTC Vive determines its location in a room from being illuminated. The terminal does not need to know any information about where the transmission originated in order to establish a link.
	- Since there are modules with transmitters in every direction, the terminal can establish a link with another spacecraft in any arbitrary direction. Theoretically, it could also maintain a link even if the other craft moves across the terminal's local sky.
- Terrestrial dishes capable of communicating with cislunar spacecraft are entering the commercial sector of the industry: [^28]
	- When services are provided by commercial entities, the ecosystem is ripe for competition and innovation.
	- More service providers mean more access.
- New network protocols allow intermediate links in a network to attach "ephemeral" information to packets as they move through the network, without reading the entire contents of the packet: [^29][^30][^31][^32]
	- For example, consider a situation where two intermediate nodes encrypt a packet and the terminal nodes (separately) encrypt the data. In this example, the transmission between two nodes may be encrypted and decrypted along the way in order to securely send a packet, while keeping the contents of the packet only readable to the end user.
	- This opens the door for third-party relay systems to intelligently and securely hold-and-pass data around in a delay/disruption-tolerant network.

## What about a near-side lunar surface installation?

Question: The Moon is tidally locked so there is a whole hemisphere of the Moon that always has line-of-sight to the Earth. Would it be feasible to set up a large antenna on the near side of the Moon for a communications relay?

(Author's note: this is not an "answer" per se, since a whole thesis could probably explore this topic. What follows are my technical and personal opinions.)

Of course, a system installed on the surface of the near side of the Moon would have a constant view of the Earth―but that's not the whole story. Finding a location on the lunar surface with continuous line-of-sight to terrestrial communication systems is easy in central latitudes, but those locations are usually undesirable for long-term lunar missions.

Publications discussing continuous communication to lunar poles: [^33][^34][^35]

Below is a list of considerations that we'd need to look into before a mission like this could be declared feasible with confidence:

- Lunar night. The Moon is tidally locked to the Earth, but it still rotates with respect to the Sun. The "dark side" of the Moon is only actually dark half the time, the other half of the time it is lit by the Sun just not visible from Earth (new Moon, remember?). A lunar night lasts for about 23.5 Earth days. The poles are so desirable as a location for lunar activity because if you're at the pole it doesn't take much to get back in the sunlight―if a spacecraft is located at the lunar equator it has to wait out the whole lunar night.
- The lunar night is a really harsh environment for spacecraft―23.5 Earth days of perpetual darkness with temperatures as low as -130C the whole time. Typical operating temperatures for most electronics are between -30 and 90C, so a heater would have to be working overtime to keep the system alive through the night, and the power system would have to support that kind of load without solar energy.[^36][^37]
- Even if the spacecraft was equipped with a bangin' heater, that heat doesn't come for free. 
- Electric resistive heaters have a typical power efficiency of 80% (0.8W of heat is generated for every 1W of energy consumed) so the spacecraft would have to store enormous amounts of charge to last the whole night. That energy would be able to be used by other systems in daylight periods, but more than likely the system would have to spend all its power on heaters during the night. This situation has killed a number of lunar missions over the years.
- Radioisotope thermal generators (RTGs) produce heat on their own through radioactive decay, and the heat is converted to electric charge and spread around the thermal control system.[^38] This would enable nighttime operations from both a thermal and a power perspective. Sounds like a great idea, but RTGs are super expensive and not easy to get. 
- Visibility to other actors. Establishing a link to Earth is one objective for a lunar communications relay, but another objective is to link to other lunar actors. Here's a discussion on the topic of visibility and link access for various orbits and latitudes of the lunar surface: [^39]

# References

[^1]: [[@zotero-336]] "Radio's First Message -- Fessenden and Marconi." https://ewh.ieee.org/reg/7/millennium/radio/radio_differences.html (accessed Apr. 04, 2023).
[^2]: [[@Araki2021]] T. Araki, “A trade-off study of lunar-earth optical communication links,” in International Conference on Space Optics — ICSO 2020, SPIE, Jun. 2021, pp. 811–819. doi: 10.1117/12.2599331.
[^3]: [[@RazaEtAl2022]] W. Raza et al., “Toward a Hybrid RF/Optical Lunar Communication System (LunarComm),” IEEE Network, vol. 36, no. 6, pp. 76–83, Nov. 2022, doi: 10.1109/MNET.103.2100419.
[^4]: [[@CainiFiore2012]] C. Caini and V. Fiore, “Moon to earth DTN communications through lunar relay satellites,” in 2012 6th Advanced Satellite Multimedia Systems Conference (ASMS) and 12th Signal Processing for Space Communications Workshop (SPSC), Sep. 2012, pp. 89–95. doi: 10.1109/ASMS-SPSC.2012.6333112.
[^5]: [[@IsraelEtAl2020]] D. J. Israel et al., “LunaNet: a Flexible and Extensible Lunar Exploration Communications and Navigation Infrastructure,” in 2020 IEEE Aerospace Conference, Big Sky, MT, USA: IEEE, Mar. 2020, pp. 1–14. doi: 10.1109/AERO47225.2020.9172509.
[^6]: [[@zotero-334]] “Nokia aims for the Moon with LTE/4G,” Nokia. https://www.nokia.com/about-us/newsroom/articles/nokia-aims-for-the-moon-with-lte4g/ (accessed Apr. 04, 2023).
[^7]: [[@Brown2020]] K. Brown, “NASA Announces Partners to Advance 2020 ‘Tipping Point’ Technologies,” NASA, Oct. 14, 2020. http://www.nasa.gov/press-release/nasa-announces-partners-to-advance-tipping-point-technologies-for-the-moon-mars (accessed Apr. 04, 2023).
[^8]: [[@HarleEtAl]] N. O. Harle et al., “Lunar comms and nav infrastructure – first data relay orbiter Lunar Pathfinder, operational in 2024, paves the way for full constellation by 2030s,” in ASCEND 2021, American Institute of Aeronautics and Astronautics. doi: 10.2514/6.2021-4132.
[^9]: [[@PasqualeEtAl2022]] A. Pasquale, G. Zanotti, J. Prinetto, M. Ceresoli, and M. Lavagna, “Cislunar distributed architectures for communication and navigation services of lunar assets,” Acta Astronautica, vol. 199, pp. 345–354, Oct. 2022, doi: 10.1016/j.actaastro.2022.06.004.
[^10]: [[@Naseem2022]] M. Naseem, “Last-mile Analogies for a Lunar Communications Network - Open Lunar Foundation,” Open Lunar Foundation, Jan. 26, 2022. https://www.openlunar.org/library/last-mile (accessed Feb. 11, 2023).
[^11]: [[@CarruthEtAl2010]] B. Carruth, M. Johnston, A. Coffman, M. Wallace, B. Arroyo, and S. Malhotra, “A Collaborative Scheduling Environment for NASA’s Deep Space Network,” in SpaceOps 2010 Conference, Huntsville, Alabama: American Institute of Aeronautics and Astronautics, Apr. 2010. doi: 10.2514/6.2010-2284.
[^12]: [[@ClementJohnston]] B. J. Clement and M. D. Johnston, “The Deep Space Network Scheduling Problem”.
[^13]: [[@ShourabouraEtAl]] C. Shouraboura, M. D. Johnston, and D. Tran, “Prioritization and Oversubscribed Scheduling for NASA’s Deep Space Network”.
[^14]: [[@Cheetham2021]] B. Cheetham, “Cislunar Autonomous Positioning System Technology Operations and Navigation Experiment (CAPSTONE),” in ASCEND 2021, Las Vegas, Nevada & Virtual: American Institute of Aeronautics and Astronautics, Nov. 2021. doi: 10.2514/6.2021-4128.
[^15]: [[@KellerEtAl2016]] J. W. Keller, N. E. Petro, and R. R. Vondrak, “The Lunar Reconnaissance Orbiter Mission – Six years of science and exploration at the Moon,” Icarus, vol. 273, pp. 2–24, Jul. 2016, doi: 10.1016/j.icarus.2015.11.024.
[^16]: [[@VelazcoEtAl]] J. E. Velazco, A. C. Aguilar, A. R. Klaib, U. S. Escobar, S. E. Cornish, and J. C. Griffin, “Development of Omnidirectional Optical Terminals for Swarm Communications and Navigation”.
[^17]: A. Chin, R. Coelho, L. Brooks, G. Student, R. Nugent, and J. P. Suari, “Standardization Promotes Flexibility: A Review of CubeSats’ Success,” 2008. Accessed: Feb. 11, 2023. [Online]. Available: https://www.semanticscholar.org/paper/Standardization-Promotes-Flexibility%3A-A-Review-of-Chin-Coelho/2ccd7bcb1f253432bc60dcebd2a4dc2736c3f514#references
[^18]: T. Villela, C. A. Costa, A. M. Brandão, F. T. Bueno, and R. Leonardi, “Towards the Thousandth CubeSat: A Statistical Overview,” International Journal of Aerospace Engineering, vol. 2019, pp. 1–13, Jan. 2019, doi: 10.1155/2019/5063145.
[^19]: C. Al-Ekabi and C. Robinson, “Recent Lunar Activity, Stakeholders and Incentives – A Backgrounder,” Open Lunar Foundation, May 2021. Accessed: Feb. 11, 2023. [Online]. Available: https://www.openlunar.org/library/recent-lunar-activity-stakeholders-and-incentives-a-backgrounder
[^20]: S. Jardine, “Building Lunar Security and Cooperation Through an Astropolitcal Lens- how to construct normative behaviours on the moon- enter the registry,” Open Lunar Foundation, Dec. 16, 2022. https://www.openlunar.org/library/open-lunar-registry-project-blog-post-series-blog-4 (accessed Feb. 11, 2023).
[^21]: J. K. Schingler, “Space Tenure: The Policies of Sustained Lunar Presence - Open Lunar Foundation,” Open Lunar Foundation. https://www.openlunar.org/library/space-tenure-the-policies-of-sustained-lunar-presence (accessed Feb. 11, 2023).
[^22]: S. Jardine, “Building Lunar Security and Cooperation Through an Astropolitical Lens- Why Normative Behaviours are Needed for Lunar Activity,” Open Lunar Foundation, Dec. 14, 2022. https://www.openlunar.org/library/open-lunar-registry-blog-post-series-blog-3 (accessed Feb. 11, 2023).
[^23]: S. Jardine, “Building Lunar Security and Cooperation Through an Astropolitical Lens- the role of normative behaviours in creating stability,” Open Lunar Foundation, Nov. 10, 2022. https://www.openlunar.org/library/open-lunar-registry-project-blog-post-series-blog-1 (accessed Feb. 11, 2023).
[^24]: P. Giordano, F. Malman, R. Swinden, P. Zoccarato, and J. Ventura-Traveset, “The Lunar Pathfinder PNT Experiment and Moonlight Navigation Service: The Future of Lunar Position, Navigation and Timing,” presented at the 2022 International Technical Meeting of The Institute of Navigation, Long Beach, California, Long Beach, California, Feb. 2022, pp. 632–642. doi: 10.33012/2022.18225.
[^25]: M. Cosby and W. Tai, “Report of the Interagency Operations Advisory Group Lunar Communications Architecture Working Group,” Lunar Communications Architecture Working Group, Jan. 2022.
[^26]: J. Foust, “Quantum Space raises $15 million for cislunar spacecraft,” SpaceNews, Dec. 13, 2022. https://spacenews.com/quantum-space-raises-15-million-for-cislunar-spacecraft/ (accessed Apr. 04, 2023).
[^27]: “ParsecTM Service from Lockheed Martin,” Lockheed Martin, Mar. 28, 2023. https://www.lockheedmartin.com/en-us/news/features/2021/lunar-communication-and-navigation-network.html (accessed Apr. 04, 2023).
[^28]: Kongsberg Satellite Services, “KSAT to invest in a dedicated antenna network for lunar missions.” https://www.ksat.no/news/news-archive/2022/ksat-to-invest-in-antenna-network-for-lunar-missions/ (accessed Feb. 03, 2023).
[^29]: S. Burleigh, K. Fall, and E. J. Birrane, “Bundle Protocol Version 7,” Internet Engineering Task Force, Request for Comments RFC 9171, Jan. 2022. doi: 10.17487/RFC9171.
[^30]: “DTN7,” DTN7. https://dtn7.github.io/ (accessed Apr. 04, 2023).
[^31]: E. J. Birrane and K. McKeever, “Bundle Protocol Security (BPSec),” Internet Engineering Task Force, Request for Comments RFC 9172, Jan. 2022. doi: 10.17487/RFC9172.
[^32]: “dtn7/awesome-dtn: A curated list of awesome delay- and disruption-tolerant networking.” https://github.com/dtn7/awesome-dtn (accessed Apr. 04, 2023).
[^33]: R. Malmström, A. Lo, N. Brown, and G. Haney, “Continuous Communications to the Moon’s South Pole,” in Space 2006, in AIAA SPACE Forum. American Institute of Aeronautics and Astronautics, 2006. doi: 10.2514/6.2006-7453.
[^34]: [[@DivsalarEtAl2019]] D. Divsalar, M. S. Net, and K.-M. Cheung, “Acquisition and tracking for communications between Lunar South Pole and Earth,” in 2019 IEEE Aerospace Conference, Mar. 2019, pp. 1–14. doi: 10.1109/AERO.2019.8742112.
[^35]: A. Reinhold, A Solar Powered Station at a Lunar Pole. 1990.
[^36]: J. Biswas, P. Q. Malzone, and F. Rößler, “Energy storage selection and operation for night-time survival of small lunar surface systems,” Acta Astronautica, vol. 185, pp. 308–318, Aug. 2021, doi: 10.1016/j.actaastro.2021.04.042.
[^37]: A. Petro, “Surviving and Operating Through the Lunar Night,” in 2020 IEEE Aerospace Conference, Mar. 2020, pp. 1–6. doi: 10.1109/AERO47225.2020.9172730.
[^38]: “Light-Weight Radioisotope Heater Unit | Thermal Systems,” NASA RPS: Radioisotope Power Systems. https://rps.nasa.gov/power-and-thermal-systems/thermal-systems/light-weight-radioisotope-heater-unit (accessed Apr. 04, 2023).
[^39]: K.-M. Cheung and C. Lee, “Lunar Relay Coverage Analysis for RF and Optical Links,” in 2018 SpaceOps Conference, Marseille, France: American Institute of Aeronautics and Astronautics, May 2018. doi: 10.2514/6.2018-2612.
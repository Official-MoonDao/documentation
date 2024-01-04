---
tags: project/lunar-comms
---
# clocss-abm: an Agent-Based Model of Heterogeneous Lunar Networks for the Cislunar Open Clock Synchronization System (CLOCSS)
https://github.com/philiplinden/clocss-abm

## Abstract
This project aims to use agent-based modeling and simulations to explore how
network topology and time synchronization evolve in a growing lunar ecosystem.
Modeling how the approach may be used in practice and at scale informs decisions
about how to architect a robust cislunar PNT system that scales with the
population.

## Approach
This project aims to use agent-based modeling and simulations to explore how
centralized and decentralized PNT service network topologies evolve in a growing
lunar ecosystem. Modeling network topologies representative of near-term lunar
missions and large future populations of cislunar actors will predict the
relative performance, “critical mass” of assets required for service, and
coverage of decentralized PNT services and/or GNSS-like beacons providing PNT to
lunar missions. There is an abundance of prior art describing optimal orbit
configurations for such systems that can also be evaluated in this way.

The model will feature a population of agents, where each agent has a Stratum, a
location and velocity, a clock with drift, and a communications system with a
spectral band and radiation power. Agents belong to one of three groups based on
their behavior: Transmitters, Receivers, and Peers. Transmitter agents radiate
signals but do not listen for incoming signals. Receivers listen for incoming
signals but do not radiate. Peers are capable of listening for and radiating
signals. Agents move in space independently along orbits or surface routes
around a sphere in the simulation space representing the Moon. Terrestrial
communications systems are modeled as a Stratum 0 Transmitter. Every node
reports measurements of each metric described in the subsequent Metrics section
at every step of the simulation period.

Over the simulation period, each agent’s clock encounters simulated drift that
accumulates over time. The agents record their perceived position by integrating
instantaneous velocity observations over time, where the observed time is based
on the local clock’s epoch. At the end of the simulation period, the observed
position is compared to the true position. Agents may interact with one another
over the simulation period using modeled communications links for PNT
measurements and time synchronization. Links are only established between two
agents if both 1) share a common spectral band; 2) have line-of-sight to each
other; 3) have sufficient radiation power to transmit across the distance
between them; and 4) at least one agent is a Transmitter. When a link is
established, the Receiver agent’s clock is synchronized to the Transmitter’s
epoch. If both agents are Peers, the agents synchronize to the epoch of the
agent with a lower Stratum, or the mean epoch between them. Each time an agent
synchronizes to another agent, it becomes Stratum n+1 where Stratum n belongs to
the agent with the lower number. Agent A syncs to UTC and becomes Stratum 1,
then Agent B syncs to A and so Agent B becomes Stratum 2, and so on.

This model framework permits rapid simulation of heterogeneous nodes acting as
PNT servers, clients, or both. The proposed study seeks to evaluate Wi-Wi based
decentralized networks as alternatives to GNSS-like services for cislunar PNT.
The described model allows each network topology to be tested and instrumented
while subject to realistic client population densities in near-term (tens of
agents) and future scenarios (hundreds, thousands of agents). The described
model also permits the simulation of multiple PNT services coexisting,  such as
Parsec, weak-GPS, and the proposed decentralized network. The model also
accounts for the evolution of competing providers as the populations of servers
and clients grow. 

Insights obtained from models will then be applied to create an optimal mission
profile for a constellation of cislunar spacecraft equipped with space-rated
Time Cards that enable the proposed capability of a publicly available minimum
viable PNT service. With relevant prediction of cislunar PNT users for each PNT
service configuration over the next 5 to 15 years, and also computing the
equivalent cost per user for terrestrial GNSS, data-driven investment decisions
related to deploying new PNT fleets in cislunar space are possible.

### Metrics
The following metrics and quantitative evaluation criteria will be used to
evaluate PNT service characteristics.

**Accuracy**
- *Sync precision* - Standard deviation absolute time across the node population
- *Holdover* - Average clock drift from true time before syncing
- *Latency (jitter)* - Round trip time, packet delay variation

**Availability**
- *Capacity* - % bandwidth used, peak bandwidth used, sqkm of coverage
- *Throughput* - Total available bandwidth, # concurrent links

**Continuity**
- *Roaming ability* - # available links, time between links
- *Failure & recovery rate* - Mean time between failures, mean time to restore

**Interoperability**
- *Standards compatibility* - Meets LunaNet and Moonlight requirements
- *Technology compatibility* - # comms spectral bands, clients served per band

**Cost**
- *Nodes required for service* - # service nodes, # clients per provider node
- *Hardware required* - $ per clock, # clocks, $ invested per client served

**Signal Integrity**
- *Packet integrity* - packet loss rate, packet delivery ratio, % duplicate
  packets
- *Channel dominance* - signal-to-noise ratio, jam-to-signal ratio

## Motivation
Recent advancements in space technologies have prompted a surge in lunar
missions, both crewed and uncrewed. Such an influx demands scalable,
commercially-accessible Positioning, Navigation, and Timing (PNT) frameworks for
the development of a cislunar economy. In order to bring PNT infrastructure to
the lunar ecosystem and have it be as ubiquitous and as useful as Global
Navigation Satellite Systems (GNSS) are in the interoperable Space Service
Volume (SSV), there needs to be accurate, traceable and accessible timing and
ranging infrastructure that is also resilient, reliable and flexible. NASA’s
LunaNet and ESA’s Moonlight are two major initiatives to promote
interoperability and connectivity in cislunar space by providing a common
communications framework and standards. Lunar constellations equivalent to
terrestrial GNSS are one approach to delivering a cislunar PNT but it is not the
only solution. Peer-to-peer networks of satellites with precision timekeeping
may serve as an alternative method of implementing a PNT service to traditional
GNSS constellations.

This project will use agent-based modeling to compare satellite network
topologies using metrics known from the current PNT solution such as accuracy,
availability, continuity and integrity, in addition to costs, timeline and
technology development requirements of implementing each system in a cislunar
context. The goal is to develop the proposed solution to a level mature enough
to predict the system’s performance relative to the number and distribution of
interconnected assets, and quantitatively demonstrate that our approach becomes
more robust and performant as it scales to service the anticipated demands of a
thriving lunar ecosystem. The study will also consider specific lunar PNT user
needs and infrastructure combination opportunities, as well as requirements for
Earth / Earth Orbit systems to be usable with minimum changes for lunar
applications.

### Diverse Cislunar Ecosystems of PNT and Communications Infrastructures are Inevitable

A fundamental characteristic of the this proposed design is its peer-to-peer
topology, ensuring resilience against centralized points of failure. The
structure stands robust against interference, adversarial or accidental. The
decentralized nature of the design further augments its flexibility, permitting
in-flight mission adaptations and potential as a backup for lunar missions,
reducing their dependence on individualized PNT structures. Since Wi-Wi is a
protocol that works with any radio band, it is likely that several independent
PNT services could emerge on different parts of the spectrum. This allows actors
to maintain closed PNT utilities or to offer services for a self-sustaining,
monetizable, commercially owned-and-operated lunar infrastructure. Critically,
public and private PNT utilities may coexist under this paradigm, like how a
single transponder can access both terrestrial open-air radio and encrypted
radio channels. In essence, this philosophy aims to nurture a resilient PNT
ecosystem that accommodates both public and private ventures. Through a credibly
neutral protocol for timekeeping, bad actors would not only have difficulty
manipulating the service, but they may use this infrastructure themselves and
even work to support its canonization.

### Interoperability with Other Missions

In the design of a lunar PNT system one important consideration is the
definition of a reference frame to allow for absolute position. This time
transfer and relative position concept could be used to define a network of
realization points (fixed points for the reference frame) to assist in the
realization of a Lunar Reference Frame. These lunar realization points would be
located on the near side of the Moon and equipped with e.g., laser
retroreflectors for accurate ranging from Earth by the existing Lunar Laser
Ranging (LLR) stations. Like GNSS, passive receivers can obtain the time and
position in reference to the PNT node’s position by observing the transmitted
signal so long as the receiver’s clock is synchronized to the node.
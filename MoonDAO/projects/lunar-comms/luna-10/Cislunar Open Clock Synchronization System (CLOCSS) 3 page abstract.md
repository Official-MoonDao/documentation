---
tags: project/luna-10, notes
---
## Summary of Proposed Approach

Recent advancements in space technologies have prompted a surge in lunar missions, both crewed and uncrewed. Such an influx demands scalable, commercially-accessible Positioning, Navigation, and Timing (PNT) frameworks for the development of a cislunar economy. In order to bring PNT infrastructure to the lunar ecosystem and have it be as ubiquitous and useful as GNSS is terrestrially, there needs to be accurate, traceable and accessible timing and ranging infrastructure that is also resilient, reliable and flexible.

Existing technology can be used to leverage the carrier signal of communications links to obtain sub-nanosecond timing and millimeter ranging. With terrestrial systems as a benchmark, our focus is to craft a comprehensive system tailored to the lunar ecosystem's challenges and the constraints of cislunar operations. Wireless 2-Way Interferometry (Wi-Wi) uses existing COTS RF chips to achieve phase-lock between precision clocks to achieve time synchronization and ranging. This approach does not require complex new technology development. The addition of a single component (Time Card, standardized by IEEE P3335) can be used to integrate a LEO platform with the cislunar PNT utility over its own pre-existing communications channels.

In this study we will analyze Wi-Wi as an alternative method of implementing a PNT service to traditional GNSS constellations, and will compare the proposed method with metrics known from the current PNT solution, such as precision, availability, reliability, and throughput, in addition to costs, timeline and technology development requirements of implementing each system in a cislunar context. The goal is to develop the proposed solution to a level mature enough to predict the system’s performance relative to the number and distribution of interconnected assets, and quantitatively demonstrate that our approach becomes more robust and performant as it scales to service the anticipated demands of a thriving lunar ecosystem. The study will also consider specific lunar PNT user needs and infrastructure combination opportunities, as well as requirements for Earth / Earth Orbit systems to be usable with minimum changes for lunar applications. These metrics will be used to evaluate opportunities to improve PNT offerings for the cislunar ecosystem. As a result, it is expected that the study will demonstrate that the proposed alternative PNT infrastructure solution is superior to existing GNSS technology in scalability, cost of service, resilience, composability, and versatility.

## Current State of the Art

Currently, governmental agencies and the commercial sector are spearheading PNT-focused missions: 1) The European Space Agency's Lunar Pathfinder aims to address the unique communication demands of the moon's far side, bridging the gap for both commercial and institutional missions; 2) [NASA](NASA.md)'s Lunar GNSS Receiver Experiment (LuGRE) and Lunar Reconnaissance Orbiter (LRO) are delving into the intricacies of lunar GNSS constellations and polar mapping, respectively; and 3) the CAPSTONE program, currently in orbit, seeks to gather operational data ahead of the upcoming Artemis missions.

Commercial endeavors like Lockheed’s Parsec and Spatiam's DTN service are paving the way for a cislunar communication link. Amidst these pioneering projects, technologies like the Time Card and Wireless Two-Way Interferometry (Wi-Wi) offer promising frameworks to build upon.

## Proposed Design

Traditional communication avenues can be revamped to serve dual purposes. Through the use of established links, achieving sub-nanosecond timing and millimeter-range precision becomes feasible. By equipping two distinct entities in cislunar space with stable clocks and a shared communication bandwidth, synchronization becomes a streamlined process. This synchronized environment then facilitates accurate relative ranging using wireless two-way interferometry (Wi-Wi) with the communication link's carrier signal. Essentially, all Wi-Wi demands is a standardized bandwidth and a precision clock.

![](https://lh6.googleusercontent.com/YYBSpcOOOepswQKDhZRAd7jw75s8Y_m7T-bJIfJhFJk9w7hmKM90coCbBe-iJMGs7AtBW1N-CfNCYsl3YunQVUBgmaChWSPqbIkH9ER1652mVr9GEEbKqjGZgoUJDT9Y1wuoRgOK0N2YGljyFHHUblc)![](https://lh4.googleusercontent.com/VPdK8Wp2WTf_Q0Oky1LhQ0IUuFC9dI55Q5dSlLo4DnJFiqPNzpZ1xw57bvLOfTXgA3SyOfshgxKqnoId4_j9Og_YRGITz5lf80o3PiDRfXvkWCL_g6YyQ1LfqH2QjMqrJNDNbJQsQkS6NV8nLeleCB4)

Figure 1: Experimental setup of Wi-Wi (left) and its clock variation and propagation delay (right)

To democratize access to precision timekeeping in space, the introduction of an open reference design for a space-rated time card is proposed. This design, compatible with the latest spacecraft buses, seeks to offer a cost-effective solution (under $5,000). The system would be anchored to trusted Stratum 1 nodes that synchronize with terrestrial Universal Time Coordinated (UTC).

![](https://lh4.googleusercontent.com/LxEqi7EjqgvoB4QYDvFUFUTOo6Ch-EnyX0vgOsOXypgRet7l5fCly5UXzSJP22Qei6EoWwLwgxwxhyIbIVk13n4YgtcUr2fAHcTF5pRkYOzN_wAaukLWba-vL5CqsK0CQBis2s-P5WVLktct8XLo3jk)

Figure 2: Time Card with an integrated Chip-Scale Atomic Clock (CSAC)

A fundamental characteristic of the proposed design is its peer-to-peer topology, ensuring resilience against centralized points of failure. The structure stands robust against interference, adversarial or accidental. The decentralized nature of the design further augments its flexibility, permitting in-flight mission adaptations and potential as a backup for lunar missions, reducing their dependence on individualized PNT structures. In essence, this philosophy aims to nurture a PNT ecosystem accommodating both public and private ventures.

## Unique Insights

The utilization of Wireless 2-Way Interferometry is a novel approach that maximizes the utility of existing communication modules. By deploying software-defined radios, Wi-Wi can establish time synchronization and ranging between lunar entities so long as the signal can be decoded. Our approach of cooperation and incentivization borrows insights from the success of the CubeSat. The system champions open standards, minimal entry barriers, and amplifies its resilience with every new participant. While entities remain free to deploy their proprietary PNT systems, the inclusion within this proposed structure augments their native capabilities.

Further, the potential economic implications are profound. The proposed PNT infrastructure, when juxtaposed with the GNSS market, suggests abundant opportunities for token-based exchanges or premium PNT services following a similar model to terrestrial GNSS. SatNav/PNT for Earth & Space currently represents around 50% of the space industry yearly revenue, indicating the foreseeable downstream market could be valued also at billions for this cislunar service. Making it available, low cost, and secure has the potential of transforming the way we perceive and engage with lunar economies.

## Technology Challenges

Our proposition isn't intended to dethrone GNSS but to complement it. In anticipation of cislunar space becoming an adversarial domain, any PNT service must be robust to interference. When considering topologies for lunar PNT, a central reference node would become a single point of failure and could be targeted to disrupt PNT. By distributing time reference and synchronization between many nodes, the system can make guarantees of security and robustness to adversaries using secure decentralized data transfer. With this vision comes the challenge of crafting autonomous network clusters while ensuring data security in an open network.

## Team and Teaming

Spearheading this initiative is a consortium of companies and experts from diverse backgrounds, working on state-of-the-art (SoA) commercial space and SoA non-space technology companies with demonstrated skills in full life cycle engineering, hardware, software and network development, and space systems. The core team brings over 60 years of collective experience in the space industries at esteemed institutions such as Planet Labs, [SpaceX](SpaceX.md), Lockheed Martin, GoogleX, Waymo, Thales Alenia Space, and more.

Key individual contributors are: [Ahmad Byagowi](Ahmad%20Byagowi.md) (50%) from [OCP-TAP](OCP-TAP.md), currently leading the Precision Time Division at Meta; [Philip Linden](@philiplinden.md) (50%) from [MoonDAO](MoonDAO.md), with space R&D experiences at [SpaceX](SpaceX.md), Lockheed Martin and Planet Labs; [Pablo Moncada-Larrotiz](@pmoncada.md) (50%) from MoonDAO, with experience at Waymo, GoogleX, and Decentralized Autonomous Organizations (DAOs). [Jacob Malthouse](Jacob%20Malthouse.md) (30%, Non US / Canadian) from [Open Lunar Foundation](Open%20Lunar%20Foundation.md), with a background in Economics and Entrepreneurship, including working for United Nations; and [Ramon Blanco Maceiras](Ramon%20Blanco%20Maceiras.md) (30%, Non-US / Spanish E2 US Visa Holder) from Added Value Solutions (AVS), with R&D and Management experiences at Thales Alenia Space for $50-500M programs.

## Budget

An estimated budget of $597,895.00 is projected over the 7-month contract period, this allocation encompasses personnel salaries in engineering and project management domains, and caters to the expenses affiliated with the development of simulation tools, both hardware and software.


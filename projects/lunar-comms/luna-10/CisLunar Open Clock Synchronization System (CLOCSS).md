---
tags: project/luna-10, notes
---
In order to bring PNT infrastructure to the lunar ecosystem and have it be as ubiquitous and useful as GNSS is terrestrially, there needs to be accurate and accessible timing and ranging infrastructure.

By 2030, Stratum 1 and Stratum 2 time appliances will be commonplace in cislunar space. Most missions are capable of serving their local region as a Stratum 3 time appliance, either as a custom modification to a reference clock or a clock purchased commercially. If two actors in proximity each have stable clocks and can communicate on a common band (S-band, X-band or L-band, for example), these actors can phase-lock their clocks and derive relative ranging using a wireless two-way interferometry. Neither actor requires a-priori knowledge of the other, so long as they maintain an open communication channel on the same band.

This can be accomplished by…

1. Making precision timekeeping cheap and available via Open Time Card. → Create an open reference design for a space-rated Open Time Card based on commodity components.[^3] The design should be compatible with existing spacecraft buses on the market today.
2. Time synchronization via Wireless 2Way Interferometry (WiWi).[^1] → WiWi uses existing COTS transponders to achieve phase-lock between precision clocks to achieve time synchronization (pico-second accuracy) and ranging (millimeter accuracy).[^2]
3. Maintaining trusted, publicly accessible Stratum 1 nodes in cislunar space that sync to terrestrial UTC. → Maintaining a "baseline" network of reliable time sources on an open part of the spectrum bootstraps the system, elevating the capabilities of every lunar mission without requiring each to build their own implementation. Missions could fall back to the open frequency as a safety measure, or as a shortcut to getting PNT without investing in in-house infrastructure.
  
This leads to…
1. Extreme flexibility and resilience. Actors need only meet a minimum timing precision and access to a common band in order to participate. Software-defined radios are commonplace, so the only hardware prerequisite is a precise clock. There is no requirement for a given technology or intellectual property other than the WiWi protocol.
2. Cooperation without requiring prior intent. Missions not originally designed with collaboration or time dissemination in mind can be adapted later to participate, so long as the mission meets the minimum requirements for WiWi. Likewise, two missions compatible with WiWi may be able to cooperate and share timing/ranging without any prior work to explicitly work together.
3. Democratization of PNT utilities. Since WiWi is a method/protocol that works with radio band, it is likely that several independent PNT services could emerge on different parts of the spectrum. This allows actors to maintain closed PNT utilities or to offer services commercially. Critically, public and private PNT utilities can coexist, like how a single transponder can access both terrestrial open-air radio and encrypted terrestrial radio channels.[^4]
4. Adapting LEO satellite hardware to work in a cislunar context. This approach does not require novel technology to achieve. The addition of a single component (time card) can be used to integrate a LEO platform with the cislunar PNT utility over its own pre-existing communications channels.

[^1]: [@YamasakiEtAl2021](@YamasakiEtAl2021.md)
[^2]: [@TanakaEtAl2022](@TanakaEtAl2022.md)
[^3]: [@ByagowiEtAl2022](@ByagowiEtAl2022.md)
[^4]: [@LindenEtAl2023](@LindenEtAl2023.md)
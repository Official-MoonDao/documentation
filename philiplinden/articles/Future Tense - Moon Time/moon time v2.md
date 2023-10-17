---
longform:
  format: single
  title: Future Tense - Moon Time
  draftTitle: v2
tags:
  - phil/articles
  - draft
---

>[!tip] Feedback from Mia
>When it comes to tone, what we're looking for is "explain your work to a smart friend who knows very little about space and timekeeping" - in practice, we want to do some hand holding, and most of my edits in the draft were focused on trying to move us there. 
> 
> A much more simplified outline, that I think is nevertheless helpful for pieces like this, goes something along the lines of: 
> - Illustrate the problem
> - Explain there's a potential solution 
> - Outline the solution
> - Return to the problem/urgency of implementing the solution
> 
> When I was editing the previous draft, some key questions for me were: 
> - how different organizations keep time currently
> - how we would actually define what the "timezone" would be
> - what steps we need to get to the unified "timezone"

A shared timescale is necessary to coordinate activities at the moon.
- Near misses in lunar orbit and beyond -- need for coordination and tighter synchrony
	- NASA/ISRO close call lunar orbit
	- NASA/China close call en route to mars https://spacenews.com/nasa-exchanged-data-with-china-on-mars-orbiters/
- DSN is oversubscribed, light delay makes direct earth-to-moon mission ops unsustainable
- spacecraft will be keeping track of their own orbits and navigation
	- Beresheet https://www.ablogtowatch.com/timekeeping-lunar-missions-interview-with-space-ils-co-founder-yonatan-winetraub/
	- CAPSTONE https://advancedspace.com/caps/

A lunar time standard, a method of maintaining the appearance of continuity between UTC and LLT, is not an easy thing to figure out.
- using UTC for the whole cislunar region breaks down because time progresses at different rates at different places in the gravity wells
	- Cislunar space is a much wider region than terrestrial space (even up to GEO)
	- [NPR](https://www.npr.org/2023/03/11/1162351563/if-daylight-saving-time-seems-tricky-try-figuring-out-the-time-on-the-moon) explains in simple terms why lunar time is not the same as earth time (UTC).
	- Time passes at a different rate due to relativity.
	- Signals take over a second to go from earth to moon in space
	- For navigation, precision of nanoseconds is required

thinking about activities at the moon, perhaps we should establish "space-time" zones.
- Time zones on earth are geometric -- based on rotation of earth and relative sun position in the sky.
- Translating between terrestrial time zones (pacific time, eastern time) are a convenience for humans.
	- UTC is the "anchor" to which the time zones are defined. global average that is broadcast everywhere. time zones are "angular separation from UTC" basically
	- humans coordinate their activities based on the local day/night cycle, so humans in similar longitudes use the same time zone, more or less. computers are connected globally, so  computers use UTC.
	- Global time labs cooperate to orchestrate terrestrial time, time zones https://www.icann.org/en/blogs/details/how-time-zones-are-coordinated-13-03-2023-en
- maybe synchronize actors based on proximity or coordination.
	- south pole, lagrange points, NRHO, etc are potential "space-time zones"
	- https://astrogatorsguild.com/?p=1620
- the moon is a convenient case-study for interplanetary operations on larger scales

I don't know what that timescale will look like, but I know that every lunar mission has the opportunity to contribute to a common goal. 
- Bring your own precision clock, and be willing to communicate. LunaNet and Moonlight are interoperability standards that support this.
- As the population grows, so too will the number of clocks, improving overall accuracy of the lunar time zone.
- Precision clocks and chip-scale atomic clocks are available today with commodity parts. We have the technology.


---
tags:
  - project/lunar-comms
  - notes
---
I've been learning a lot about timekeeping lately. The most confusing thing for me has been [Allan Variance](https://en.wikipedia.org/wiki/Allan_variance). The second most confusing aspects of timekeeping for me is how to measure time if it is relative. The following video inspired me to dive a bit deeper.
![time and relativity](https://www.youtube.com/watch?v=ZdrZf4lQTSg)
# Frames of Reference
## Coordinate Time
The time as observed by the coordinate frame itself. This is a "god's-eye view" of the time in the system we are analyzing. Basically, it represents a perfect clock held by the world/universe/simulation coordinate frame's observer. Usually Earth-centric systems use UTC or TAI as the Coordinate Time.

Formally, the coordinate time is the time that would be read on a hypothetical "coordinate clock" situated infinitely far from all gravitational masses, and stationary in the system of coordinates.
## Proper Time
The time as observed by a perfect clock attached to an object's local body frame. The body frame is a coordinate frame rigidly attached to the object. Whenever the object observes the time, it observes the local Proper Time.

In most situations, Proper Time and Coordinate Time are the same. The distinction between Proper Time and Coordinate Time is only relevant when objects are subjected to large accelerations or move across lumpy spacetime (like going from sea-level on Earth to standing on the Moon), and the effects of General Relativity become significant.

## System Time
So far we've only talked about the hypothetical, perfect clocks that describe the physics. But we actually want to observe these times ourselves with real clocks. Unfortunately, no clock is perfect or ideal. The _System Time_ is the real clock's observation of the local Proper Time. We'll explore System Time later when we learn more about [[Allan Variance]].
# Time Dilation
> Time dilation is the lengthening of the time interval between two events for an observer in an inertial frame that is moving with respect to the rest frame of the events (in which the events occur at the same location). ([Source](https://openstax.org/books/university-physics-volume-3/pages/5-3-time-dilation))

Consider a coordinate frame with a space axis, $x$, and a time axis, $t$. We also have two _events_, $a$ and $b$. Events are points in this coordinate frame with a time coordinate and a space coordinate. The length of a vector in this coordinate system, or the _spacetime interval_ between two events, represents the proper time measured with an inertial clock between the events.

```plaintext
    t
    ▲     
    │    .e(x,t)
time│
    │
    └──────────►x
       space
```
- $\Delta x$ is the distance traversed by a local observer of $e$.
- $\Delta t$ is the elapsed coordinate time to event $e$.
- $\Delta x / \Delta t$ is the speed of the moving observer relative to the coordinate frame, $v$.
- $\Delta s$, the length of a vector from the origin to $e$, is equal to the elapsed proper time according a local observer's inertial clock. This is also called the _spacetime interval_.

Unlike linear spatial coordinates where the "grid" is square, spacetime coordinates are not linear. The "grid" on the spacetime plot is made up of hyperbolas rather than lines.

![](../../media-files/Pasted%20image%2020240101164720.png)

## Time Dilation from Velocity
The _Metric Equation_ lets us find a spacetime interval between events. ([Derivation](https://physics.unm.edu/Courses/Fields/Phys2310/Lectures/lecture27.pdf))
$$\Delta s^2 = \Delta t^2 - \Delta x^2$$
We want to relate the elapsed proper time $\Delta s$ to the elapsed coordinate time $\Delta t$. Special Relativity tells us that the speed of light, $c$, is constant in all inertial frames—this is the key to our solution.

> [!note]
> The Metric Equation comes from Special Relativity, which is to say we are assuming that this coordinate frame is far from any gravity wells for now. The consequences of General Relativity and being in the presence of gravitational potential field, or gravity well, are explored later.

If we substitute our terms with equivalent definitions related to a pulse of light moving at $c$, we get
$$
\Big(c \frac{\Delta s}{2}\Big)^2 = \Big(c \frac{\Delta t}{2} \Big)^2 - \Big(v \frac{\Delta t}{2} \Big)^2, \quad v = \frac {\Delta x} {\Delta t}
$$
Now we can solve for elapsed coordinate time using the locally observed proper time $\Delta s$ and the observer's speed in the coordinate frame. ([Derivation](https://openstax.org/books/university-physics-volume-3/pages/5-3-time-dilation))
$$
\Delta t = \frac {\Delta s} {\sqrt{1 - (v/c)^2}}
$$
We can refer to the relationship between proper time and coordinate time that depends on the relative speed between observers as the _Relativistic Factor_, $\gamma$. This is syntactic sugar and sometimes called the _Lorentz Factor_.
$$
\Delta t = \gamma \Delta s, \quad \gamma = \frac {1}{\sqrt{1 - v^2/c^2}}
$$
The [**clock hypothesis**](https://en.wikipedia.org/wiki/Time_dilation#Clock_hypothesis) is the assumption that the **rate at which a clock is affected by time dilation does not depend on its acceleration but only on its instantaneous velocity.** We see this manifest above in our definition of $\gamma$ only depending on $v$ and universal constants. [Wikipedia's derivation](https://en.wikipedia.org/wiki/Time_dilation) is quite good here.

> [!tip]
> Velocity is not absolute, so the observer can't measure it without a reference to something else. Acceleration _is_ absolute, though, so a local observer can measure its own accelerations without an external frame of reference. Then again, if not for an external reference, coordinate time and proper time lose their meaning. An observer can't measure their own coordinate time because their proper time _is_ their coordinate time! My brain hurts…
## Time Dilation from Acceleration
It's time to bring gravity into the mix. General Relativity tells us that mass warps spacetime, and we describe this phenomenon with a _gravitational potential field_, or gravity well. In simple terms, a massive object close to another massive object will feel an acceleration just from being nearby.

Gravity-induced accelerations also cause time dilation as described by the [Schwarzschild solution](https://en.wikipedia.org/wiki/Schwarzschild_solution) to Einstein's equations. This is way harder to derive than the equations from special relativity, but it has been experimentally proven time and again: **a clock close to the center of a gravity well will tick more slowly than one far away.**

Unlike dilation from velocity, the dilation from potential is not symmetric. This means that both observers can agree about the dilation without encountering a paradox.

# Let's Try It Ourselves

Consider the Earth-centered Inertial frame (ECI), an inertial frame centered at Earth's center with three spatial axes, $(x,y,z)$. We place our perfect reference clock at the center of Earth and use it to track the Coordinate Time, $t$.

Now imagine 4 points in this coordinate frame. How does time dilation affect each one?
1. ⭕ - an imaginary, static point in inertial space 100 km above Beijing.
2. 📡 - a ground station at sea-level in Canada rotating along with the Earth's surface.
3. ✈️ - a plane flying 10 km due east above the ocean at 900 km/h ground speed.
4. 🛰 - a satellite orbiting in a [geosynchronous equatorial orbit](https://en.wikipedia.org/wiki/Geostationary_orbit) around Earth. 

![](../../media-files/ECI%20vs%20time%20dilation.png)
Point ⭕ has zero velocity, but is still in the presence of Earth's gravity well and feels gravitational potential. Is its proper time faster or slower than coordinate time? _Faster!_

Now let's consider some real objects, 📡 and ✈️. Both are pretty close to each other in terms of altitude, astronomically speaking, so they share about the same amount of gravitational dilation. Unlike ⭕, both are in motion with the Earth's surface as it rotates. And that means they're moving pretty dang fast with respect to the center of Earth. The dilation from velocity dominates over the dilation from being far from the center of Earth, so both clocks are _slower_ than the coordinate time in total.

But how do 📡 and ✈️ compare to each other? ✈️ is moving 900 km/h ground speed, and 📡 is at rest on the surface. Since ✈️ is moving faster than 📡, its clock appears slower than 📡.

Finally, let's consider 🛰… It's not so simple anymore. Let's check [the answers](https://en.wikipedia.org/wiki/Time_dilation).

![](../../media-files/Pasted%20image%2020240101223031.png)

Okay, we're on the right track! Now to do the math ourselves…


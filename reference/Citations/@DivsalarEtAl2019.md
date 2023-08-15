---
tags: citations
alias: Acquisition and tracking for communications between Lunar South Pole and Earth
---
# Acquisition and tracking for communications between Lunar South Pole and Earth

**Dariush Divsalar, Marc Sanchez Net, Kar-Ming Cheung**
2019

link:: 
doi:: 10.1109/AERO.2019.8742112

> [!info] Abstract
> In this paper we design and analyze an end-to-end communication system between a lander/rover on the surface of the lunar South Pole and an Earth station. The acquisition and tracking system is discussed in detail. The communication system on the lander or rover could be used for the Earth-to-Moon communication. To communicate to and from the lander/rover on the lunar South Pole, low and/or medium directional antennas onboard the lander/rover will have to be pointed at low elevation angles between 2 to 10 degrees, thus causing multipath fading effects due to reflection of a portion of the transmitted electromagnetic waves from the surface of the Moon that are not commonly encountered in traditional deep space communications between a spacecraft and a ground station. To design and analyze such a communication system, and in particular the acquisition and tracking system, in the presence of multipath fading, first we model the fading channel based on existing and simulated data. In addition to multipath fading, the channel also introduces Doppler frequency up to 11.5 KHz, and Doppler rate up to 0.735 Hz/sec. For coherent reception the Doppler frequency, which is time varying, should be acquired and the incoming carrier phase, which includes the fading phase, should be tracked in the presence of multipath fading. For this communication system in addition to estimating the received carrier phase, the amplitude of the fading signal should also be estimated, in particular to be used in the decoder. In addition to acquisition and tracking, we consider simple modulation and coding schemes. Space diversity using two antennas on Earth to mitigate the effects of fading could also be used. We design phase-locked loops and frequency sweeping schemes robust to the attenuations due to fading. After designing various components of the communication system, we use Simulink models to obtain the end-to-end performance of the communication link under investigation. Based on the available data, the fading channel can be accurately modeled as a Rician fading channel with Rician parameter of 10 dB, and Doppler spread that depends on the Doppler frequency and the transmit/receive antenna patterns. The challenge is how to make such a communication system robust in the presence of the multipath fading where the Doppler spread changes in time and thus produces fading with time-varying durations (short and very long fades). In summary, this paper covers communication system design, performance analysis, and simulations for performance of Doppler frequency acquisition, tracking, uncoded system, and coded system under ideal interleaving assumption with hard decision over communication link between a lander/rover at the Lunar south pole and a DSN Earth station in presence of Rician fading.


![[5.-Lunar-South-Pole-to-Earth.pdf]]
## Notes


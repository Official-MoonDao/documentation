---
tags: notes
---
# Research Goal

This study will analyze the relative benefits and drawbacks of network topologies for lunar communications: mesh networks, star networks, hybrid, and unstructured topologies.

Mesh networks are decentralized and provide redundancy, which means that if one node fails, the other nodes can still communicate. This is important for lunar communications because there is a high risk of equipment failure due to the harsh environment. However, mesh networks can be complex to manage because each node needs to be able to communicate with all of the other nodes in the network.

Star networks are simpler to manage than mesh networks because each node only needs to communicate with a single central node. However, star networks are more vulnerable to single point failures because if the central node fails, the entire network fails.

Hybrid topologies combine the benefits of both mesh and star networks. In a hybrid topology, some nodes are connected to a central node, while other nodes are connected to each other. This provides redundancy and makes the network more resilient to failures.

The study will include a discussion of the trade-offs between the different topologies and recommends that the choice of topology be based on the specific needs of the lunar mission. For example, a mission that requires a high level of redundancy would be better suited for a mesh network, while a mission that requires simplicity would be better suited for a star network.

This study will include the models of each type of network. The models are examined through several performance metrics that are transferable to real-world systems, plus additional metrics that provide insight into the behavior of each agent.

Here are some additional details on how different network topologies could be used by networks of agents in the cislunar ecosystem:

- A star topology could be used to create a decentralized network of satellites that would provide internet access to the moon. In this topology, each satellite would be connected to a central hub. This would allow for communication between the satellites and the hub, as well as between the satellites themselves. This would be a reliable and efficient way to provide internet access to the moon.
    
- A mesh topology could be used to create a network of robots that would be able to work together to build infrastructure on the moon. In this topology, each robot would be connected to its neighbors. This would allow the robots to communicate with each other and coordinate their efforts. This would be a flexible and scalable way to build infrastructure on the moon.
    
- A ring topology could be used to create a network of sensors that would monitor the moon's environment. In this topology, each sensor would be connected to the two sensors next to it. This would allow the sensors to communicate with each other and share data. This would be a reliable and efficient way to monitor the moon's environment.
    
- Unstructured topologies may emerge from the chaos of lunar activities. This term is a catch-all for network topologies that may not be consistent or deliberate with respect to the arrangement of connections between nodes. Unstructured topologies will likely emerge naturally as lunar actors interact.
    

## Focus on Decentralized Network Architectures

Decentralized networks are difficult to operate because there is no central authority to coordinate the activities of the network. This can lead to problems such as coordination failure, security risks, and scalability issues.

Coordination failure can occur when different nodes in the network have different goals or objectives. This can make it difficult to reach consensus on how to operate the network.

Security risks can arise when malicious actors are able to take control of a significant number of nodes in the network. This can allow them to disrupt the network or even take it over.

Scalability issues can occur when the network becomes too large or complex to manage. This can lead to performance problems and make it difficult to add new features or functionality.

The willingness of members of a decentralized network to cooperate with each other can also be a challenge. If members are not willing to share information or resources, it can be difficult to operate the network effectively.

Despite these challenges, decentralized networks offer a number of advantages over centralized networks. They are more resilient to attack, they are more transparent, and they offer greater user privacy.

  

Objectives:

  

Methods:

- Celestial is a tool helps lunar mission planning by providing 3d maps of lunar surfaces to high specificity and fidelity: [https://celestial.arc.nasa.gov/](https://celestial.arc.nasa.gov/) [[@Agrawal]]
    
- Trek is a NASA web-based portal for exploration of Moon. This portal showcases data collected by NASA at various landing sites and features an easy-to-use browsing tool that provides layering and viewing of high resolution data: [https://trek.nasa.gov/moon/#v=0.1&x=0&y=0&z=1&p=urn%3Aogc%3Adef%3Acrs%3AIAU2000%3A%3A30120&d=&locale=&b=moon&e=-834790.4296874987%2C-1434127.148437498%2C834790.4296874987%2C1434127.148437498&sfz=&w=](https://trek.nasa.gov/moon/#v=0.1&x=0&y=0&z=1&p=urn%3Aogc%3Adef%3Acrs%3AIAU2000%3A%3A30120&d=&locale=&b=moon&e=-834790.4296874987%2C-1434127.148437498%2C834790.4296874987%2C1434127.148437498&sfz=&w=) 
    
- LOS Analysis searches for windows of communication or a "line of sight" between any two entities: [[@LawEtAl2021]]
    

Hypotheses:

  

Sources::

- NASA’s Lunar Communication and Navigation Structure: [[@FlaneganEtAl2008]]
- Slime Mold Grows Network Just Like Tokyo Rail System: [[@Sanders2010]]
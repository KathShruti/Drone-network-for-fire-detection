# Drone-network-for-fire-detection
Jamie Columb and Shruti Kathuria’s project 2 focused on a group of Automated Underwater
Vehicles (AUV’s) that would initially register with a tracker server using a client-server
interaction. The tracker server would then exchange the client’s IP and port numbers with
each other so they could communicate directly in a peer-to-peer network. UDP socket
programming and hole-punching was used in the peer-to-peer interactions. This was proven
to be effective and easiest to understand so we have decided to use this feature of project 2
in this project.
Aarya Sharma’s project 2 focused on a swarm of aerial drones connected in a peer-to-peer
network to share environmental data and coordinate flight paths. This project made use of
separate functions to handle every aspect of data sharing. The project had functions
dedicated to handling inbound and outbound connections, disconnections, client messages
and requests to stop sending data. The project also made use of unit tests to validate the
functionality of the code. We will make use of both of these features while implementing out
solution for our chosen use case.

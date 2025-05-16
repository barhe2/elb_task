Multicast is a network protocol to transmit the same data to a specific
group of devices.

There are:
* Broadcast - Data transfer from a single device to all devices in the network.
* Multicast - Data transfer from a single device to devices in a group.
* Unicast - Data transfer from a single device to a single device.

When to use each?

* Broadcast - ARP, DHCP: a new device needs to inform all the devices in the network about itself.
* Multicast - Streaming, online gaming, routing protocols: a single transmission to a group (one-to-many).
* Unicast - Web browsing, SSH, Email: each unique request goes to a single device (one-to-one).

Why use each method?

* Broadcast - Discovery: Used when a new device joins a network and needs to find servers or other devices without knowing their specific addresses.
* Multicast saves network traffic as the source transmits data only once, allowing the entire group to listen to and use it concurrently.
* Unicast - Efficient: Used when there's a need to send information to a single specific, known device.
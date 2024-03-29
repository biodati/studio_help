# VPN and IP-address restriction

If you have an Enterprise BioDati Studio (for your company), it may be deployed such that only individuals accessing it from specific IP addresses on the Internet (or your company Intranet) can get to it. If you are not coming from one of those IP addresses, it will just hang trying to access your BioDati Studio (e.g. <https://studio.<NICK_NAME>.biodati.com> ).

You can find out what your public IP address is by using a service like [What is my IP](https://whatismyip.com). When you are using your company Intranet, it should show the (or one of many) public IP addresses used by your company. When you use *WhatIsMyIP* from your home, it will show you the public IP address you are using from your Internet Service.

Personal Internet Services typically provide you with a temporary public IP address instead of a permanent one. These temporary addresses will change from time to time but are usually kept for days to weeks at a time.

Some VPN clients will send your company traffic to your company Intranet and send the rest of the non-company bound traffic directly to the Internet. This will result in you being able to access company resources when your VPN client is active but still not be able to get to BioDati Studio when you are not in the office. You can contact your company's IT Help Desk, and they can tell you how to add the BioDati Studio domain to the VPN domains that should be routed through your company Intranet in order to access BioDati Studio.

# Fortigate-IP-Hitlist
Analyse Fortigate logs and extract the IP address with hit count

A quick script I wrote to dive into a log file from a Fortigate firewall and grab IP's and count each time they were seen.

On the Fortigate, I export the log with a filter e.g. 24 hour winow, logs for "SSLVPN Denied", simply pass that log into the script. 

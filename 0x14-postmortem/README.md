<h1>Postmortem incident Airbnb</h1>
<h3>Issue Summary</h3>
<p>On March 2, 2017 from 1:30 PM to 2:17 PM PST, www.Airbnb.com website outage occured. 5% of user experienced a slow down in service and many resulting in receiving a 404 not found network error response. A new server was integrated into load balancer's rotation. The new server was not configured correctly and was outputting to port 8080 instead of port 80.</p>
<h3>Timeline(All times in PST)</h3>
<ul>
	<li>1:30 PM: New servers integrated into the load balancer rotation</li>
	<li>1:36 PM: Increase in reports of User experiencing difficulties</li>
	<li>1:36 PM: Monitoring alerts relating to the newly integrated servers. Problem detected</li>
	<li>1:37 PM: Pagers alerted teams</li>
	<li>1:44 PM: New server taken out of rotation</li>
	<li>1:45 PM: Team proceeds with standard check of server health (disk usage, current processes, history, ports) </li>
	<li>2:06 PM: Team discovers issues and updates config files</li>
	<li>2:09 PM: Team successfully updates new servers</li>
	<li>2:12 PM: Team test servers within work environment</li>
	<li>2:17 PM: New servers integrated back into the load balancer rotation</li>
</ul>
<h3>Root cause and Resolution</h3>
<p>
At 1:30 PM PST, new servers placed into the production load balancer rotation without being released into the testing environment first. At 1:36 PM PST, a spike in user reports and a monitoring alert notified the incident reponse team. By 1:37 PM PST the alerted team was paged. They redirect traffic to the existing server to diagnose. The team execute standard debugging pratice and proceeds with stand checks of the server. Once the team started to check the ports, they noticed web server, nginx, on the new servers were configured to port 8080 instead of port 80. At 2:06 PM PST, the team makes an assumption to restart nginx to notice a difference. No difference was observed. This lead to the team checking the listening ports of the config file. They found the config files in the /etc/nginx/ were configured to listen to port 8080. The response team create a script that updated all the new servers' config files to have nginx listen to port 80. Nginx restarted, and nginx was now listening to port 80. At 2:12 PM PST, the team proceeds to team alteration of script in test environment. At 2:17 PM PST, the new servers pass the inspection and are pushed into production and added back into the load balancer's rotation. 

</p>

<h3>Corrective and Preventative Measures</h3>
<p>
After the incident, we condicted an internal review and analysis of the outage. We have concluded that the following actions should be taken to prevent future incidents and increase reponse time.
	<h4>Task to address the issue</h4>
	       <ul>
	       <li>fix the script that set up of nginx servers with correct set configurations</li>
	       <li>add monitoring check to ensure new servers were first tested in test environment</li>
	       <li>develop tools to check server requirements against the expected output of new server (e.g. expected ports, disk usage being exceeded, etc)</li>
	       <li>add monitor load balancer to monitor when server servers are none responsive</li>
	       <li>add monitor the new server's ports to match expected output</li>
	       <li>patch Nginx server</li>
	       </ul>
Airbnb is commiting to addressing the needs of their customers and to prevent any loss of service.
</p>

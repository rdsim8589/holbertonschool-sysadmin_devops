<h1>Postmortem incident Airbnb</h1>
<h3>Issue Summary</h3>
<p>On March 2, 2017 from 1:30 PM to 2:12 PM PST, www.Airbnb.com website outage occured. 5% of user experienced a slow down in service and many resulting in receiving a 500 internal service network error response. A new server was integrated into load balancer's rotation. The new server was not configured correctly and was outputting to port 8080 instead of port 80.</p>
<h3>Timeline(All times in PST)</h3>
<ul>
	<li>1:30 PM: New servers integrated into the load balancer rotation</li>
	<li>1:36 PM: Increase in reports of User experiencing difficulties</li>
	<li>1:36 PM: Monitoring alerts relating to the newly integrated servers</li>
	<li>1:37 PM: Pagers alerted teams</li>
	<li>1:44 PM: New server taken out of rotation</li>
	<li>2:06 PM: Team discovers issues and updates config files</li>
	<li>2:09 PM: Team successfully updates new servers</li>
	<li>2:12 PM: New servers integrated back into the load balancer rotation</li>
</ul>
<h3>Root cause and Resolution</h3>
<p>
At 1:30 PM PST, new servers placed into the production load balancer rotation without being released into the testing environment first. At 1:36 PM PST, a spike in user reports and a monitoring alert notified the incident reponse team. By 1:37 pm the alerted team was paged. They redirect traffic to the existing server to diagnose.  the web server, nginx, on the new servers were configured port 8080 instead of port 80. The reponse team checked the status of the listening ports and noticed nginx was listening to 8080. From there, they found the config files in the /etc/nginx/ were configured to listen to port 8080. The response team create a script that updated all the new server's config files to have nginx listen to port 80. 

Set a system monitor to check the status of the listening ports of a server before pushing a server into production
</p>

<h3>Corrective and Preventative Measures</h3>
<p>

</p>
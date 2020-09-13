---
layout: page
permalink: /publications/
title: publications
years: [2020]
nav: true
---

<div class="publications">
<h4>Academic</h4>
{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

<div class="publications">
<h4>Non-academic writing</h4>
<ul class="bibliography">
  <li><a href="https://innov.mycpanel.princeton.edu/F12.pdf#page=4" target="_blank">The Progress of Regression</a></li>
  <li><a href="http://nassauweekly.com/game-of-shows/" target="_blank">Game of Shows</a></li>
  <li><a href="http://nassauweekly.com/the-companionship-of-charlie-brown/" target="_blank">
  The Companionship of Charlie Brown</a></li>
  <li><a href="http://nassauweekly.com/masterful-viewing/" target="_blank">Masterful Viewing</a></li>
  <li><a href="http://nassauweekly.com/why-federer-betterer/" target="_blank">Why Federer is Betterer</a></li>
  <li><a href="{{ 'JohnConwayDailyPrincetonian.pdf' | prepend: '/assets/pdf/' | relative_url }}" target="_blank">Math and Games: A profile of John Conway</a></li>
  <li><a href="https://www.dailyprincetonian.com/article/2011/12/seeger-center-for-hellenic-studies-tasked-to-fund-manage-research" target="_blank">Seeger Center for Hellenic Studies tasked to fund, manage research</a></li>

</ul>
</div>

<div class="talks">
<h4>Talks</h4>

</div>

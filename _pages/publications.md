---
layout: page
permalink: /publications/
title: publications
years: [2021, 2020]
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
<h4>Writing</h4>
<ul class="bibliography">
  <li><a href="https://innov.mycpanel.princeton.edu/F12.pdf#page=4" target="_blank">The Progress of Regression</a></li>
  <li><a href="http://nassauweekly.com/game-of-shows/" target="_blank">Game of Shows</a></li>
  <li><a href="http://nassauweekly.com/the-companionship-of-charlie-brown/" target="_blank">
  The Companionship of Charlie Brown</a></li>
  <li><a href="http://nassauweekly.com/masterful-viewing/" target="_blank">Masterful Viewing</a></li>
  <li><a href="http://nassauweekly.com/why-federer-betterer/" target="_blank">Why Federer is Betterer</a></li>
  <li><a href="{{ 'JohnConwayDailyPrincetonian.pdf' | prepend: '/assets/pdf/' | relative_url }}" target="_blank">Math and Games: A profile of John Conway</a></li>
  <li><a href="https://www.dailyprincetonian.com/article/2012/04/tweets-arent-big-fans-of-oscar-nominated-films-princeton-team-finds" target="_blank">Tweets aren’t big fans of #oscar nominated films, @princeton team finds</a></li>
  <li><a href="https://www.dailyprincetonian.com/article/2012/09/u-offers-classes-on-online-platform" target="_blank">U. offers classes on online platform</a> (<a href="https://eqn.princeton.edu/2012/09/mung-chiang-publishes-new-book-on-networked-life/" target="_blank">citation</a>) </li> 
  <li><a href="https://www.dailyprincetonian.com/article/2012/03/u-explores-interactive-learning" target="_blank">U. explores interactive learning</a> (<a href="https://books.google.com/books?id=mbX1CwAAQBAJ&pg=PA200&lpg=PA200&dq=daily+princetonian+rebecca+zhang&source=bl&ots=QrHsd1mJLR&sig=ACfU3U1473y0pLicwkkEdhorjmM90APKZw&hl=en&sa=X&ved=2ahUKEwjC5aPkkOXrAhWqnOAKHb9lBWs4ChDoATAMegQICRAB#v=onepage&q=daily%20princetonian%20rebecca%20zhang&f=false" target="_blank">citation</a>) </li> 
  <li><a href="https://www.dailyprincetonian.com/article/2011/12/seeger-center-for-hellenic-studies-tasked-to-fund-manage-research" target="_blank">Seeger Center for Hellenic Studies tasked to fund, manage research</a></li>

</ul>
</div>

<!-- <div class="talks">
<h4>Talks</h4>

</div> -->

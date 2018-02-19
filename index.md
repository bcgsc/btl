---
title: Home
feature_text: |
  # Bioinformatics Technology Lab   
  Led by Dr. Inanc Birol at BC Cancer's Michael Smith Genome Sciences Center 
feature_image: "assets/background.jpg"
feature_credit: Photo by Martin Krzywinski
feature_link: http://mkweb.bcgsc.ca/fun/hdtr/
layout: default
---

{% include site-header.html %}

<main class="main  container">
<article class="article  article--page  content  typeset">
<div style="width:50%;height:100%;float:left;padding-right:20px;">
<h2>Welcome!</h2>
<p>The Bioinformatics Technology Lab at Michael Smith Genome Sciences Centre specializes in software for de novo genome assembly.</p>
</div>

<div style="width:50%;height:100%;float:left;padding:0px;">
<h2><a href="news.html">News</a></h2>
<iframe src="news-content.html"></iframe>
</div>
</article>

	{% if page.aside == true %}{% include site-aside.html %}{% endif %}

</main>

{% include site-footer.html %}

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
<p>The Bioinformatics Technology Lab at the Michael Smith Genome Sciences Centre is a computational biology research group, part of the BC Cancer Agengy. We develop novel algorithms, data structures and genome analysis software. The technologies we build find applications in cancer research, and are the foundation of our genome research program. We are situated in Vancouver, Canada</p>
</div>

<div style="width:50%;height:100%;float:left;padding:0px;">
<h2><a href="news.html">News</a></h2>
<iframe src="news-content.html"></iframe>
</div>
</article>

	{% if page.aside == true %}{% include site-aside.html %}{% endif %}

</main>

{% include site-footer.html %}

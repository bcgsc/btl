---
title: Home
feature_text: |
  # Bioinformatics Technology Lab   
  Led by Dr. Inanc Birol at BC Cancer's Michael Smith Genome Sciences Center 
feature_image: "assets/background.jpg"
feature_credit: Photo by Martin Krzywinski
feature_link: http://mkweb.bcgsc.ca/fun/hdtr/
layout: default
aside: true
aside_title: Hello!
aside_content: "Hello this is what's going to be in the aside block. Here's some information about our lab"
---

{% include site-header.html %}

<main class="main  container">
<article class="article  article--page  content  typeset">
    <div class="two_col">
    <h3>Software</h3>
    <p> Could have some icons, some text, definitely a link to Github and BCGSC software maybe</p>
    </div>

    <div class="two_col">
    <h3>Active Projects</h3>
    <p> Could have a list of ongoing projects or recent publications</p>
    </div>
</article>

	{% if page.aside == true %}{% include site-aside.html %}{% endif %}

</main>

{% include site-footer.html %}

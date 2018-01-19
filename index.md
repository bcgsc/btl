---
title: Home
feature_text: |
  # Bioinformatics Technology Lab   
  Led by Dr. Inanc Birol at BC Cancer's Michael Smith Genome Sciences Center 
feature_image: "/images/background.jpg"
layout: default
aside: true
aside_title: Hello!
aside_content: "Hello this is what's going to be in the aside block. You can see our recent publications here:"
aside_link: <a href="/publications.md">Publications List</a>  
---

{% include site-header.html %}

<main class="main  container">

	<article class="article  article--page  content  typeset">


    <div class="homepage_left">
    <h3>Software</h3>
    <p> Could have some icons, some text, definitely a link to Github and BCGSC software maybe</p>
    </div>

    <div class="homepage_right">
    <h3>Active Projects</h3>
    <p> Could have a list of ongoing projects or recent publications</p>
    </div>

  </article>

	{% if page.aside == true %}{% include site-aside.html %}{% endif %}

</main>

{% include site-footer.html %}

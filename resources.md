---
layout: page
title: Resources 
---

<style>
/* Default (desktop) = 3 columns */
.software table td {
    width: 33.33%;
}

/* Tablet */
@media screen and (max-width: 900px) {
    .software table td {
        width: 50%;
    }
}

/* Mobile */
@media screen and (max-width: 600px) {
    .software table td {
        width: 50%;
    }

    .software table tr {
        margin-bottom: 10px;
    }
}
</style>

Here you will find cutting-edge technologies and resources developed by the Birol Lab to empower researchers in genomics, bioinformatics, life sciences and medical research and designed to streamline *big data* analysis, enhance data interpretation, and accelerate scientific discovery.

<div class="col software">
<table>
{% include software-content.html %}
</table>
</div>

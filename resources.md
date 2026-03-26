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

   /* Default desktop */
   .software table {
       width: 100%;
       border-collapse: collapse;
   }

   /* Mobile fix */
   @media screen and (max-width: 700px) {

       .software table,
       .software tbody,
       .software tr,
       .software td {
           display: block;
           width: 100%;
       }

       .software tr {
           margin-bottom: 20px;
       }

       .software td {
           text-align: center;
           padding: 10px 0;
       }
   }

}
</style>

Here you will find cutting-edge technologies and resources developed by the Birol Lab to empower researchers in genomics, bioinformatics, life sciences and medical research and designed to streamline *big data* analysis, enhance data interpretation, and accelerate scientific discovery.

<div class="col software">
<table>
{% include software-content.html %}
</table>
</div>

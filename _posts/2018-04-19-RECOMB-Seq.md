---  
layout: post  
title: "ABySS 2.0, Tigmint, ARKS, and Bloom Filters at RECOMB-Seq"  
category: conference  
---  

##### [RECOMB 2018](http://recomb2018.fr/) will be taking place in Paris, France, from April 21-24th. 
[RECOMB-Seq](http://recomb2018.fr/recomb-seq/) is one of its four satellite workshops this year, taking place from April 19-20th, bringing together researchers in computational genomics and bioinformatics to discuss new frontiers in gene sequencing.

##### BTL has four posters at RECOMB-Seq this year:
RECOMB ID #1, SEQ-6, **ARKS**: chromosome-scale human genome scaffolding with linked read kmers  
RECOMB ID #10, SEQ-8, **Multi-Index Bloom Filters**: A probabilistic data structure for sensitive multi-reference sequence   classification with multiple spaced seeds  
RECOMB ID #21, SEQ-7, **Tigmint**: Correct Assembly Errors Using Linked Reads From Large Molecules  
SEQ-10, **ONTig**: Contiguating Genome Assembly using Oxford Nanopore Long Reads

##### Talks: ABySS 2.0 and Tigmint
Shaun Jackman will be presenting a highlight talk on ABySS 2.0 [(slides)](http://sjackman.ca/abyss2-slides/), as well as a talk on Tigmint [(slides)](http://sjackman.ca/tigmint-recomb-slides/).  
The ABySS 2.0 paper and abstract is available in [Genome Research](https://genome.cshlp.org/content/27/5/768)  
The Tigmint paper will be available on bioRxiv shortly. Here is the abstract:  
>Genome sequencing yields the sequence of many short snippets of DNA (reads) from a genome. Genome assembly attempts to reconstruct the original genome from which these reads were derived. This task is difficult due to gaps and errors in the sequencing data, repetitive sequence in the underlying genome, and heterozygosity, and assembly errors are common. These misassemblies may be identified by comparing the sequencing data to the assembly, and by looking for discrepancies between the two. Once identified, these misassemblies may be corrected, improving the quality of the assembly. Although tools exist to identify and correct misassemblies using Illumina pair-end and mate-pair sequencing, no such tool yet exists that makes use of the long distance information of the large molecules provided by linked reads, such as those offered by the 10x Genomics Chromium platform. We have developed the tool Tigmint for this purpose. To demonstrate the effectiveness of Tigmint, we corrected assemblies of a human genome using short reads assembled with ABySS 2.0 and other assemblers. Tigmint reduced the number of misassemblies identified by QUAST in the ABySS assembly by 216 (27%). While scaffolding with ARCS alone more than doubled the scaffold NGA50 of the assembly from 3 to 8 Mbp, the combination of Tigmint and ARCS improved the scaffold NGA50 of the assembly over five-fold to 16.4 Mbp. This notable improvement in contiguity highlights the utility of assembly correction in refining assemblies. We demonstrate its usefulness in correcting the assemblies of multiple tools, as well as in using Chromium reads to correct and scaffold assemblies of long single-molecule sequencing.


---  
layout: post  
title: "Long read correction and scaffolding pipeline LongStitch published in BMC Bioinformatics"
category: news  
---  

Our manuscript describing the newly developed long read correction and scaffolding pipeline, LongStitch, was just published in [BMC Bioinformatics](https://doi.org/10.1186/s12859-021-04451-7). LongStitch incorporates multiple tools developed by our group and runs in up to three stages, which includes initial assembly correction (Tigmint-long), followed by two incremental scaffolding stages (ntLink and ARKS-long). Tigmint-long and ARKS-long are misassembly correction and scaffolding utilities, respectively, previously developed for linked reads, that we adapted for long reads. Within LongStitch, we also introduce our newly developed long read scaffolder, ntLink, which utilizes lightweight minimizer mappings to join contigs. In the manuscript, we show that LongStitch generates contiguous and high-quality genome assemblies of both short and long read assemblies of various species. 
LongStitch is freely available from [GitHub](https://github.com/bcgsc/LongStitch).
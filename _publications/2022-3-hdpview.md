---
title: "HDPView: Differentially Private Materialized View for Exploring High Dimensional Relational Data"
collection: publ_conferences
permalink: /publication/2022-3-hdpview
# note: 'To appear'
# acceptance: 'Acceptance rate: 1349/9020 (15.0%)'
# rankCORE: 'CORE 2021: A*'
# rankGGS: 'GGS 2021: A++'
date: 2022-01-01
venue: 'International Conference on Very Large Data Bases (VLDB)'
# paperurl: 'https://doi.org/10.1145/3514221.3526162'
pubtype: 'conferences'
authors: ' 
Fumiyuki Kato
,
Tsubasa Takahashi
,
Shun Takagi
,
Yang Cao
,
Seng Pei Liew
,
Masatoshi Yoshikawa'
---
Abstract
 <br> 
 How can we explore the unknown properties of high-dimensional sensitive relational data while preserving privacy? We study how to construct an explorable privacy-preserving materialized view under differential privacy. No existing state-of-the-art methods simultaneously satisfy the following essential properties in data exploration: workload independence, analytical reliability (i.e., providing error bound for each search query), applicability to high-dimensional data, and space efficiency. To solve the above issues, we propose HDPView, which creates a differentially private materialized view by well-designed recursive bisected partitioning on an original data cube, i.e., count tensor. Our method searches for block partitioning to minimize the error for the counting query, in addition to randomizing the convergence, by choosing the effective cutting points in a differentially private way, resulting in a less noisy and compact view. Furthermore, we ensure formal privacy guarantee and analytical reliability by providing the error bound for arbitrary counting queries on the materialized views. HDPView has the following desirable properties: (a) Workload independence, (b) Analytical reliability, (c) Noise resistance on high-dimensional data, (d) Space efficiency. To demonstrate the above properties and the suitability for data exploration, we conduct extensive experiments with eight types of range counting queries on eight real datasets. HDPView outperforms the state-of-the-art methods in these evaluations. 
 <br> 

 [[Link](https://dl.acm.org/doi/10.14778/3538598.3538601){:target="_blank"}][[ArXiv](https://arxiv.org/abs/2203.06791){:target="_blank"}][[BibTeX](/files/bibtex/kato2022.bib){:target="_blank"}]

<pre> @article{kato2022hdpview,
  author    = {Fumiyuki Kato and
               Tsubasa Takahashi and
               Shun Takagi and
               Yang Cao and
               Seng Pei Liew and
               Masatoshi Yoshikawa},
  title     = {HDPView: Differentially Private Materialized View for Exploring High Dimensional Relational Data},
  booktitle = {VLDB '22},
  }
</pre>
---
title: "Adversarial Robustness for Face Recognition: How to Introduce Ensemble Diversity among Feature Extractors?"
collection: publ_workshops
permalink: /publication/2021-1-ensemble
# note: 'To appear'
# acceptance: 'Acceptance rate: 1349/9020 (15.0%)'
# rankGGS: 'GGS 2021: A++'
date: 2021-01-01
venue: 'SafeAI@ AAAI'
pubtype: 'workshops'
authors: ' 
Takuma Amada, Kazuya Kakizaki,
Seng Pei Liew,
Toshinori Araki, Joseph Keshet, Jun Furukawa
'
---
Abstract
 <br> 

An adversarial example (AX) is a maliciously crafted input that humans can recognize correctly, while machine learning models cannot. This paper considers how to turn deep learning-based face recognition systems to be robust against AXs. A large number of studies have proposed methods for protecting machine learning-classifiers from AXs. One of the most successful methods among them is to prepare an ensemble of classifiers and promote diversity among them. Face recognition typically relies on feature extractors instead of classifiers. We found that directly applying this successful method to feature extractors leads to failure. We show that this failure is due to a lack of true diversity among the feature extractors and fix it by synchronizing the direction of features among models. Our method significantly enhances the robustness against AXs under the white box and black box settings while slightly increasing the accuracy. We also compared our method with adversarial training.
 <br> 

 [[Link](https://openreview.net/pdf?id=GPuQY4ego4s){:target="_blank"}][[BibTeX](/files/bibtex/amada2021adv.bib){:target="_blank"}] 
<pre> @inproceedings{amada2021adversarial,
  title={Adversarial Robustness for Face Recognition: How to Introduce Ensemble Diversity among Feature Extractors?},
  author={Amada, Takuma and Kakizaki, Kazuya and Liew, Seng Pei and Araki, Toshinori and Keshet, Joseph and Furukawa, Jun},
  booktitle={SafeAI@ AAAI},
  year={2021}
} </pre>



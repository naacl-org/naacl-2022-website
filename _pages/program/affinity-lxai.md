---
title: "LatinX in AI @ NAACL 2022"
layout: single
permalink: /program/affinity/lxai/
sidebar: 
    nav: program
toc: false
---

[Website](https://www.latinxinai.org/naacl-2022)

## Schedule

**Mode:** Hybrid

**Date:** Sunday, July 10

| 8:30 | Check-in & Breakfast
| 8:45 | Opening Remarks
| 9:00 | Joint Poster Session
| 11:00 | Break
| 11:15 | Keynote #1
| 12:00 | Lunch and Social
| 13:00 | Keynote #2
| 13:45 | Paper Presentations (Slot 1)
| 14:30 | Break
| 14:45 | Keynote #3
| 15:30 | Paper Presentations (Slot 2)
| 16:15 | Round Table Discussions
| 17:00 | Closing Remarks

## Paper Presentations (Slot 1)

**An interpretable representation of dialog history in referential visual dialog**
<br>
Mauricio Mazuecos, Franco Luque, Jorge Sánchez, Hernán Maina, Thomas Vadora, Luciana Benotti
{: .title}

Visual Dialog is assumed to require the dialog history to generate correct responses during a dialog. However, it is not clear from previous work how dialog history is needed for visual dialog. In this paper we define what it means for visual questions to require dialog history and we propose a methodology for identifying them. We release a subset of the Guesswhat?! questions for which their dialog history completely changes their responses. We propose a novel interpretable representation that visually grounds dialog history: the Region under Discussion. It constrains the image’s spatial features according to a semantic representation of the history inspired by the information structure notion of Question under Discussion. We evaluate the architecture on task-specific multi-modal models and the visual transformer model LXMERT and show that there is still room for improvement. Here we present published work (Mazuecos et al., 2021).
{: .abstract}

**Identifying epidemic related Tweets using noisy learning**
<br>
Ramya Tekumalla, Juan M. Banda
{: .title}

Supervised learning algorithms are heavily reliant on annotated datasets to train machine learning models. However, the curation of the annotated datasets is laborious and time consuming due to the manual effort involved and has become a huge bottleneck in supervised learning. In this work, we apply the theory of noisy learning to generate weak supervision signals instead of manual annotation. We curate a noisy labeled dataset using a labeling heuristic to identify epidemic related tweets. We evaluated the performance using a large epidemic corpus and our results demonstrate that models trained with noisy data in a class imbalanced and multi-classification weak supervision setting achieved performance greater than 90%.
{: .abstract}

**Automatic multi-modal processing of language and vision to assist people with visual impairments**
<br>
Hernán Maina, Luciana Benotti
{: .title}

In recent years, the study of the intersection between vision and language modalities, specifically in visual question answering (VQA) models, has gained significant appeal due to its great potential in assistive applications for people with visual disabilities. Despite this, to date, many of the existing VQA models are nor applicable to this goal for at least three reasons. To begin with, they are designed to respond to a single question. That is, they are not able to give feedback to incomplete or incremental questions. Secondly, they only consider a single image which is neither blurred, nor poorly focused, nor poorly framed. All these problems are directly related to the loss of the visual capacity. People with visual disabilities may have trouble interacting with a visual user interface for asking questions and for taking adequate photographs. They also frequently need to read text captured by the images, and most current VQA systems fall short in this task. This work presents a PhD proposal with four lines of research that will be carried out until December 2025. It investigates techniques that increase the robustness of the VQA models. In particular we propose the integration of dialogue history, the analysis of more than one input image, and the incorporation of text recognition capabilities to the models. All of these contributions are motivated to assist people with vision problems with their day-to-day tasks.
{: .abstract}

**User Profile Characterization Within a Brazilian Online Dispute Resolution Platform**
<br>
Wesley Paulino Fernandes Maciel, Yohan Bonescki Gumiel, Adriana Pagano, Ana Paula Couto da Silva
{: .title}

This work investigates consumer complaints shared on Consumidor.gov.br, a Brazilian Online Dispute Resolution platform. Leveraging Natural Language Processing (NLP) techniques, we inquire to what extent complaints by male and female consumers are represented in that platform and whether differences in the language of their complaints can reveal patterns to be explored as linguistic indicators of gender authoring. Our results show differences in the way males and females construe meanings in terms of word POS, psycholinguistic properties and emotions expressed.
{: .abstract}

**Improving Language Model Fine-tuning with Information Gain Filtration**
<br>
Javier S. Turek, Richard Antonello, Nicole M. Beckage, Alexander G. Huth
{: .title}

Language model fine-tuning is essential for modern natural language processing. The ef- fectiveness of fine-tuning is limited by the in- clusion of training examples that negatively affect performance. Here we present Infor- mation Gain Filtration, a general fine-tuning method, for improving the overall final per- formance of a fine-tuned model. We define Information Gain of an example as the im- provement on a validation metric after train- ing on that example. A secondary learner is then trained to approximate this quantity. Dur- ing fine-tuning, this learner filters informa- tive examples from uninformative ones. We show that our method is robust and has consis- tent improvement across datasets, fine-tuning tasks, and language model architectures.
{: .abstract}

## Paper Presentations (Slot 2)

**Incorporating Natural Language Processing models in Mexico City's 311 Locatel**
<br>
Alejandro Molina-Villegas, Edwin Aldana-Bibadilla, Oscar S Siordia, Jorge Luis Perez
{: .title}

Natural Language Processing based technologies are transforming various sectors by facilitating new ways of providing services through Artificial Intelligence (AI). In this paper, we describe the methodology and present the challenges encountered during the creation of a Deep Learning-based model for classifying citizen service requests. Our system is able to effectively recognize among 48 categories of public services with an accuracy of 97% and was integrated into Mexico City’s 311, significantly increasing the government’s ability to provide better services.
{: .abstract}

**Distributed Text Representations Using Transformers for Noisy Written Language**
<br>
Alejandro Rodriguez Perez, Pablo Rivas, Gissella Bejarano Nicho
{: .title}

This work proposes a methodology to derive latent representations for highly noisy text. Traditionally in Natural Language Processing systems, methods rely on words as the core components of a text. Unlike those, we propose a character-based approach to be robust against our target texts’ high syntactical noise. We propose pre-training a Transformer model (BERT) on different, general-purpose language tasks and using the pre-trained model to obtain a representation for an input text. Weights are transferred from one task in the pipeline to the other. Instead of tokenizing the text on a word or sub-word basis, we propose considering the text’s characters as tokens. The ultimate goal is that the representations produced prove useful for other downstream tasks on the data, such as criminal activity in marketplace platforms.
{: .abstract}

**BioMedIA: A Complete Voice-to-Voice Generative Question Answering System for the Biomedical Domain in Spanish**
<br>
Alejandro Vaca Serrano, David Betancur Sánchez, Alba Segurado, Guillem García Subies, Álvaro Barbero Jiménez
{: .title}

The objective of this work is to develop a reliable and complete Generative Question Answering (QA) System in Spanish, for the biomedical domain. The need for such kind of system for general users to clarify complex biomedical questions is noticeable, given the existing misinformation and the lack of reliable tools that join multiple sources to form a complete answer about health-related topics. Given the importance of these for society as a whole, and the lack of relevant resources in Spanish, it was considered of general interest to develop a system that could bring together the knowledge located in different sources and make it available to the Spanish-speaking community. Moreover, putting a focus on accessibility, the system should also be fully operated through voice.
{: .abstract}

**Dual Architecture for Name Entity Extraction and Relation Extraction with Applications in Medical Corpora**
<br>
Ernesto Quevedo Caballero, Alejandro Rodriguez Perez, Tomas Cerny, Pablo Rivas
{: .title}

There is a growing interest in automatic knowledge discovery in plain text documents. Automation enables the analysis of massive collections of information. Such efforts are relevant in the health domain which has a large volume of available resources to transform areas important for society when addressing various health research challenges. However, knowledge discovery is usually aided by annotated corpora, which are scarce resources in the literature. This work considers as a start point existent health-oriented Spanish dataset. In addition, it also creates an English variant using the same tagging system. Furthermore, we design and analyze two separated architectures for Entity Recognition and Relation Extraction that outperform previous works in the Spanish dataset. Finally, we evaluate their performance in the English version with such promising results.
{: .abstract}

**Study of Question Answering on Legal Software Document using BERT based models**
<br>
Ernesto Quevedo Caballero, Mushfika Rahman, Tomas Cerny, Pablo Rivas, Gissella Bejarano
{: .title}

The transformer-based architectures have achieved remarkable success in several Natural Language Processing tasks, such as the Question Answering domain. Our research focuses on different transformer-based language models’ performance in software development legal domain specialized datasets for the Question Answering task. It compares the performance with the general-purpose Question Answering task. We have experimented with the PolicyQA dataset and conformed to documents regarding users’ data handling policies, which fall into the software legal domain. We used as base encoders BERT, ALBERT, RoBERTa, DistilBERT and LEGAL-BERT and compare their performance on the Question answering benchmark dataset SQuAD V2.0 and PolicyQA. Our results indicate that the performance of these models as contextual embeddings encoders in the PolicyQA dataset is significantly lower than in the SQuAD V2.0. Furthermore, we showed that surprisingly general domain BERT-based models like ALBERT and BERT obtain better performance than a more domain-specific trained model like LEGAL-BERT.
{: .abstract}

<style>
p.title { margin-bottom: .3em; }
p.abstract { font-size: 90%; margin-bottom: 2em; }
p.abstract:before { content: "Abstract: "; font-weight: bold; }
</style>

---
title: Tutorials
layout: single
excerpt: "NAACL 2022 Tutorials"
permalink: /program/tutorials/
sidebar: 
    nav: program
toc: true
toc_sticky: true
---

<style>
.speaker-images img {
  border-radius: 50%;
}
th .extra {
  font-size: 80%;
}
</style>

Please see [this blog post](/blog/welcome-to-tutorials/) for more information!

## Schedule

**Date:** July 10, 2022

| | Morning sessions: 9:00--12:30<br><span class="extra">Extra Q&A sessions: 8:00--8:45 and 12:30--13:00</span>
| -- | -- |
| [T1](#t1) | Text Generation with Text-Editing Models
| [T2](#t2) | Self-supervised Representation Learning for Speech Processing
| [T3](#t3) | New Frontiers of Information Extraction

| | Afternoon sessions: 14:00--17:30<br><span class="extra">Extra Q&A sessions: 13:30--14:00 and 18:00--18:45</span>
| -- | -- |
| [T4](#t4) | Human-Centered Evaluation of Explanations
| [T5](#t5) | Multimodal Machine Learning
| [T6](#t6) | Contrastive Data and Learning for Natural Language Processing

All times are Pacific Daylight Time (<strong>GMT-7</strong>).

Tutorials will be delivered live in a hybrid mode. Room assignments and Zoom links for the tutorials, and for their extra live Q&A sessions, will be in the conference handbook and on the website for virtual attendance, which will link to materials including videos.
Remote attendees who cannot connect synchronously to tutorials can attend the extra Q&A sessions.

## T1: Text Generation with Text-Editing Models
{: #t1}

[Eric Malmi](https://ericmalmi.com/),
[Yue Dong](https://www.cs.mcgill.ca/~ydong26/),
Jonathan Mallinson,
[Aleksandr Chuklin](http://linkedin.com/in/chuklin/),
[Jakub Adamek](http://linkedin.com/in/jakub-adamek-pl/),
[Daniil Mirylenka](http://linkedin.com/in/daniil-mirylenka-b0428a26),
Felix Stahlberg,
[Sebastian Krause](https://scholar.google.com/citations?user=i03iu-UAAAAJ&hl=en),
Shankar Kumar,
[Aliaksei Severyn](http://linkedin.com/in/aseveryn)

![Eric Malmi](/assets/images/tutorials/Eric_Malmi.jpg)
![Yue Dong](/assets/images/tutorials/Yue_Dong.jpg)
![Jonathan Mallinson](/assets/images/tutorials/Jonathan_Mallinson.jpg)
![Aleksandr Chuklin](/assets/images/tutorials/Aleksandr_Chuklin.jpg)
![Jakub Adamek](/assets/images/tutorials/Jakub_Adamek.jpg)
![Daniil Mirylenka](/assets/images/tutorials/Daniil_Mirylenka.jpg)
![Felix Stahlberg](/assets/images/tutorials/Felix_Stahlberg.jpg)
![Sebastian Krause](/assets/images/tutorials/Sebastian_Krause.jpg)
![Shankar Kumar](/assets/images/tutorials/Shankar_Kumar.jpg)
![Aliaksei Severyn](/assets/images/tutorials/Aliaksei_Severyn.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t1/){: .btn .btn--info}

**Time:** 9:00--12:30

**Extra Q&A sessions:** 8:00--8:45 and 12:30--13:00

**Location:** Columbia A

**Category:** Cutting-edge

Text-editing models have recently become a prominent alternative to seq2seq models for
monolingual text-generation tasks such as grammatical error correction, text simplification, and
style transfer. These tasks share a common trait – they exhibit a large amount of textual overlap
between the source and target texts. Text-editing models take advantage of this observation and
learn to generate the output by predicting edit operations applied to the source sequence. In
contrast, seq2seq models generate outputs word-by-word from scratch thus making them slow
at inference time. Text-editing models provide several benefits over seq2seq models including
faster inference speed, higher sample efficiency, and better control and interpretability of the
outputs. This tutorial provides a comprehensive overview of the text-edit based models and
current state-of-the-art approaches analyzing their pros and cons. We discuss challenges
related to deployment and how these models help to mitigate hallucination and bias, both
pressing challenges in the field of text generation.

## T2: Self-supervised Representation Learning for Speech Processing
{: #t2}

[Hung-yi Lee](https://speech.ee.ntu.edu.tw/~hylee/index.php),
[Abdelrahman Mohamed](https://ai.facebook.com/people/abdelrahman-mohamed/),
[Shinji Watanabe](https://sites.google.com/view/shinjiwatanabe),
[Tara Sainath](https://research.google/people/TaraSainath/),
[Karen Livescu](https://ttic.edu/livescu/),
[Shang-Wen Li](https://swdanielli.github.io/),
[Shu-wen Yang](https://scholar.google.com.tw/citations?user=R1mNI8QAAAAJ),
[Katrin Kirchhoff](https://www.amazon.science/author/katrin-kirchhoff)

![Hung-yi Lee](/assets/images/tutorials/Hung-yi_Lee.jpg)
![Abdelrahman Mohamed](/assets/images/tutorials/Abdelrahman_Mohamed.jpg)
![Shinji Watanabe](/assets/images/tutorials/Shinji_Watanabe.jpg)
![Tara Sainath](/assets/images/tutorials/Tara_Sainath.jpg)
![Karen Livescu](/assets/images/tutorials/Karen_Livescu.jpg)
![Shang-Wen Li](/assets/images/tutorials/Shang-Wen_Li.jpg)
![Shu-wen Yang](/assets/images/tutorials/Shu-wen_Yang.jpg)
![Katrin Kirchhoff](/assets/images/tutorials/Kirchhoff_Katrin.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t2/){: .btn .btn--info}

**Time:** 9:00--12:30

**Extra Q&A sessions:** 8:00--8:45 and 12:30--13:00

**Location:** Columbia C

**Category:** Cutting-edge

Although Deep Learning models have revolutionized the speech and audio processing field, they forced building specialist models for individual tasks and application scenarios. Deep neural models also bottlenecked dialects and languages with limited labeled data.
Self-supervised representation learning methods promise a single universal model to benefit a collection of tasks and domains. They recently succeeded in NLP and computer vision domains, reaching new performance levels while reducing required labels for many downstream scenarios. Speech representation learning is experiencing similar progress with three main categories: generative, contrastive, predictive. Other approaches relied on multi-modal data for pre-training, mixing text or visual data streams with speech. Although self-supervised speech representation is still a nascent research area, it is closely related to acoustic word embedding and learning with zero lexical resources. This tutorial session will present self-supervised speech representation learning approaches and their connection to related research areas. Since many of the current methods focused solely on automatic speech recognition as a downstream task, we will review recent efforts on benchmarking learned representations to extend the application of such representations beyond speech recognition. A hands-on component of this tutorial will provide practical guidance on building and evaluating speech representation models.

## T3: New Frontiers of Information Extraction
{: #t3}

[Muhao Chen](https://luka-group.github.io/),
[Lifu Huang](https://wilburone.github.io/),
[Manling Li](https://limanling.github.io/),
[Ben Zhou](http://xuanyu.me/),
[Heng Ji](https://blender.cs.illinois.edu/hengji.html),
[Dan Roth](http://www.cis.upenn.edu/~danroth/)

![Muhao Chen](/assets/images/tutorials/Muhao_Chen.jpg)
![Lifu Huang](/assets/images/tutorials/Lifu_Huang.jpg)
![Manling Li](/assets/images/tutorials/Manling_Li.jpg)
![Ben Zhou](/assets/images/tutorials/Ben_Zhou.jpg)
![Heng Ji](/assets/images/tutorials/Heng_Ji.jpg)
![Dan Roth](/assets/images/tutorials/Dan_Roth.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t3/){: .btn .btn--info}

**Time:** 9:00--12:30

**Extra Q&A sessions:** 8:00--8:45 and 12:30--13:00

**Location:** Columbia D

**Category:** Cutting-edge

Information extraction (IE) is the process of automatically extracting structural information from unstructured or semi-structured data. It provides the essential support for natural language understanding by recognizing and resolving the concepts, entities, events described in text, and inferring the relations among them. In various application domains, IE automates the costly acquisition process of domain-specific knowledge representations that have been the backbone of any knowledge-driven AI systems. For example, automated knowledge base construction has relied on technologies for entity-centric IE. Extraction of events and event chains assists machines with narrative prediction and summarization tasks. Medical IE also benefits important but expensive clinical tasks such as drug discovery and repurposing. Despite the importance, frontier research in IE still face several key challenges. The first challenge is that existing dominant methods using language modeling representation cannot sufficiently capture the essential knowledge and structures required for IE tasks. The second challenge is on the development of extraction models for fine-grained information with less supervision, considering that obtaining structural annotation on unlabeled data have been very costly. The third challenge is to extend the reliability and generalizability of IE systems in real-world scenarios, where data sources often contain incorrect, invalid or unrecognizable inputs, as well as inputs containing unseen labels and mixture of modalities. Recently, by tackling those critical challenges, recent literature is leading to transformative advancement in principles and methodologies of IE system development. We believe it is necessary to present a timely tutorial to comprehensively summarize the new frontiers in IE research and point out the emerging challenges that deserve further investigation.  
 
In this tutorial, we will systematically review several lines of frontier research on developing robust, reliable and adaptive learning systems for extracting rich structured information. Beyond introducing robust learning and inference methods for unsupervised denoising, constraint capture and novelty detection, we will discuss recent approaches for leveraging indirect supervision from natural language inference and generation tasks to improve IE. We will also review recent minimally supervised method for training IE models with distant supervision from linguistic patterns, corpus statistics or language modeling objectives. In addition, we will illustrate how a model trained on a close domain can be reliably adapted to produce extraction from data sources in different domains, languages and modalities, or acquiring global knowledge to guide the extraction on a highly diverse open label space. Participants will learn about recent trends and emerging challenges in this topic, representative tools and learning resources to obtain ready-to-use models, and how related technologies benefit end-user NLP applications.

## T4: Human-Centered Evaluation of Explanations
{: #t4}

[Jordan Boyd-Graber](http://boydgraber.org),
[Samuel Carton](https://shcarton.github.io),
[Shi Feng](http://www.shifeng.umiacs.io),
[Vera Liao](http://www.qveraliao.com),
[Tania Lombrozo](http://cognition.princeton.edu),
[Alison Smith-Renner](https://alisonmsmith.github.io),
[Chenhao Tan](https://chenhaot.com)

![Jordan Boyd-Graber](/assets/images/tutorials/Jordan_Boyd-Graber.jpg)
![Samuel Carton](/assets/images/tutorials/Sam_Carton.jpg)
![Shi Feng](/assets/images/tutorials/Shi_Feng.jpg)
![Vera Liao](/assets/images/tutorials/Vera_Liao.jpg)
![Tania Lombrozo](/assets/images/tutorials/Tania_Lombrozo.jpg)
![Alison Smith-Renner](/assets/images/tutorials/Alison_Smith-Renner.jpg)
![Chenhao Tan](/assets/images/tutorials/Chenhao_Tan.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t4/){: .btn .btn--info}

**Time:** 14:00--17:30

**Extra Q&A sessions:** 13:30--14:00 and 18:00--18:45

**Location:** Columbia D

**Category:** Introductory

The NLP community are increasingly interested in providing explanations for NLP models to help people make sense of model behavior and potentially improve human interaction with models. In addition to computational challenges in generating these explanations, evaluations of the generated explanations require human-centered perspectives and approaches. This tutorial will provide an overview of human-centered evaluations of explanations. First, we will give a brief introduction to the psychological foundation of explanations as well as types of NLP model explanations and their corresponding presentation, to provide the necessary background. We will then present a taxonomy of human-centered evaluation of explanations and dive into depth in the two categories: 1) evaluation with human-subject studies and 2) evaluation based on human-annotated explanations. We will conclude by discussing future directions. We will also adopt a flipped format to maximize the interactive components for the live audience.

## T5: Multimodal Machine Learning
{: #t5}

[Louis-Philippe Morency](https://www.cs.cmu.edu/~morency/),
[Paul Pu Liang](https://www.cs.cmu.edu/~pliang/),
[Amir Zadeh](https://www.amir-zadeh.com/)

![Louis-Philippe Morency](/assets/images/tutorials/Louis-Philippe_Morency.jpg)
![Paul Pu Liang](/assets/images/tutorials/Paul_Pu_Liang.jpg)
![Amir Zadeh](/assets/images/tutorials/Amir_Zadeh.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t5/){: .btn .btn--info}

**Time:** 14:00--17:30

**Extra Q&A sessions:** 13:30--14:00 and 18:00--18:45

**Location:** Columbia C

**Category:** Cutting-edge

Multimodal machine learning is a vibrant multi-disciplinary research field that addresses some of the original goals of AI via designing computer agents that are able to demonstrate intelligent capabilities such as understanding, reasoning and planning through integrating and modeling multiple communicative modalities, including linguistic, acoustic, and visual messages. With the initial research on audio-visual speech recognition and more recently with language & vision projects such as image and video captioning, visual question answering, and language-guided reinforcement learning, this research field brings some unique challenges for multimodal researchers given the heterogeneity of the data and the contingency often found between modalities.

This tutorial builds upon the annual course on multimodal machine learning taught at Carnegie Mellon University and is a completely revised version of the previous tutorials on multimodal learning at CVPR, ACL, and ICMI conferences. The present tutorial is based on a revamped taxonomy of the core technical challenges present in multimodal machine learning, centered around these six core challenges: representation, alignment, reasoning, induction, generation and quantification. Recent technical achievements will be presented through the lens of this revamped taxonomy of multimodal core challenges, allowing researchers to understand similarities and differences between approaches and new models. The tutorial is also designed to give a perspective on future research directions in multimodal machine learning. 

## T6: Contrastive Data and Learning for Natural Language Processing
{: #t6}

[Rui Zhang](https://ryanzhumich.github.io/),
[Yangfeng Ji](http://yangfengji.net/),
[Yue Zhang](https://frcchang.github.io/),
[Rebecca J. Passonneau](https://sites.psu.edu/becky/)

![Rui Zhang](/assets/images/tutorials/Rui_Zhang.jpg)
![Yangfeng Ji](/assets/images/tutorials/Yangfeng_Ji.jpg)
![Yue Zhang](/assets/images/tutorials/Yue_Zhang.jpg)
![Rebecca J. Passonneau](/assets/images/tutorials/Rebecca_Passonneau.jpg)
{: .speaker-images}

[Speaker Bios](/program/tutorials/bios-t6/){: .btn .btn--info}

**Time:** 14:00--17:30

**Extra Q&A sessions:** 13:30--14:00 and 18:00--18:45

**Location:** Columbia A

**Category:** Cutting-edge

Current NLP models heavily rely on effective representation learning algorithms. Contrastive learning is one such technique to learn an embedding space such that similar data sample pairs have close representations while dissimilar samples stay far apart from each other. It can be used in supervised or unsupervised settings using different loss functions to produce task-specific or general-purpose representations. While it has originally enabled the success for vision tasks, recent years have seen a growing number of publications in contrastive NLP. This first line of works not only delivers promising performance improvements in various NLP tasks, but also provides desired characteristics such as task-agnostic sentence representation, faithful text generation, data-efficient learning in zero-shot and few-shot settings, interpretability and explainability.

In this tutorial, we aim to provide a gentle introduction to the fundamentals of contrastive learning approaches and the theory behind them. We then survey the benefits and the best practices of contrastive learning for various downstream NLP applications including Text Classification, Question Answering, Summarization, Text Generation, Interpretability and Explainability, Commonsense Knowledge and Reasoning, Vision-and-Language.


---
title: "Announcing the NAACL 2022 Best Paper Awards!"
date: 2022-06-29 11:00:00
author: program-chairs
author_profile: true
tags:
  announcement
categories:
  blog
toc: false
---

We are pleased to announce that the following papers will receive best paper and honorable mention awards at NAACL! 

The Best Paper committee was composed of Thamar Solorio (Chair), Isabelle Augenstein, Gemma Bel Enguix, Alona Fyshe, Shafiq Joty and Emily Prud'hommeaux. We are thankful to them for carefully reading all the candidates nominated by the Senior Area Chairs, and selecting exciting papers that capture a broad range of contributions to the field.

We recognize the following papers with best papers awards (listed alphabetically by title):

{% include best-paper-box
  title="Automatic Correction of Human Translations"
  authors=" Jessy Lin, Geza Kovacs, Aditya Shastry, Joern Wuebker, John DeNero"
  category="Best new task (tied) and new resource paper"
  comment="This paper was in the running for multiple categories because it introduces a new corpus, describes a new task, and proposes a new way of leveraging advances in NLP to support stakeholders in the (human) translation workforce. The task is automatic correction of human translation, which the authors demonstrate is distinct from the well studied tasks of written error correction and MT output correction. Developing systems for this task required a new corpus that was carefully and thoughtfully collected in close collaboration with a large human translation services company. The evaluation of the proposed systems included an in-depth usability study that showed how participatory design and evaluation can contribute to more wide-spread adoption of NLP-assisted technologies."
%}

{% include best-paper-box
  title="FNet: Mixing Tokens with Fourier Transforms"
  authors="James Lee-Thorp, Joshua Ainslie, Ilya Eckstein, Santiago Ontanon"
  category="Best efficient NLP paper"
  comment="Since their introduction, transformers have been the basis of multiple advances in language modeling, owing in part to their learned attention weights.  However, transformers also come with an increased number of parameters and can take more compute power to train.  This paper replaces the self-attention layers in the transformer architecture with an unparameterized Fourier transform that mixes the input tokens.  These models train 80% faster on GPUs and 70% faster on TPUs than the comparable transformer models, while closely matching accuracy across many tasks.  This innovation also allows for longer input sequences, enabling future work on long range context effects.  The committee commends this team on their contributions to the efficiency of large language models."
%}


{% include best-paper-box
  title="FRUIT: Faithfully Reflecting Updated Information in Text"
  authors="Robert L. Logan IV, Alexandre Tachard Passos, Sameer Singh, Ming-Wei Chang"
  category="Best new task paper (tied)"
  comment="This paper provides the community with an interesting and relevant new NLP challenge: that of updating information from a knowledge base given new evidence. As time passes a lot of the information statically stored becomes obsolete and in need of updating. An approach to automatically update dated information then is indeed welcomed in many real world applications. The paper presents the task, with a good motivation discussing the different challenges that are entailed by the new task, and that involve contrasting textual evidence to decide which pieces are outdated, as well as language generation to produce the new text. In addition to releasing the dataset created in the paper, to facilitate more research in this direction, the authors release their source code to allow others to recreate new datasets using the same set up as in this paper."
%}


{% include best-paper-box
  title="NeuroLogic A&#42;esque Decoding: Constrained Text Generation with Lookahead Heuristics"
  authors="Ximing Lu, Sean Welleck, Peter West, Liwei Jiang, Jungo Kasai, Daniel Khashabi, Ronan Le Bras, Lianhui Qin, Youngjae Yu, Rowan Zellers, Noah Smith, Yejin Choi"
  category="Best new method paper"
  comment="Language generation is, in its simplest form, a search problem in very high dimensional space.  This paper makes that connection clear by incorporating the classic search algorithm A&#42; into the language generation process.  A&#42; allows for a heuristic search that incorporates “lookahead” signals of future performance into token selection.  The authors perform a very thorough evaluation of their model across many tasks including question generation, machine translation, and story generation. They show large performance improvements over the typical beam search approach, and over their original NeuroLogic algorithm. This paper is an inspiring mixture of old and new."
%}


{% include best-paper-box
  title="User-Driven Research of Medical Note Generation Software"
  authors="Tom Knoll, Francesco Moramarco, Alex Papadopoulos Korfiatis, Rachel Young, Claudia Ruffini, Mark Perera, Christian Perstl, Ehud Reiter, Anya Belz, Aleksandar Savkov"
  category="Best paper on human-centered NLP special theme"
  comment="This paper is a great example of user-centered design of an NLP system. Authors performed different user studies that covered the entire software lifecycle and this helped the research team to form a more robust understanding of system requirements but also the stakeholders. Moreover, the authors did not stop at the deployment step, but followed users after deploying the system for some time. The insights gathered through each user study prove critical for the design, development and deployment of an NLP system that is likely to result in increased adoption rates precisely because it pursued an empathic involvement of the intended users. The paper can be helpful for NLP researchers and practitioners that intend to deploy NLP systems."
%}

We also recognize the following outstanding papers with an honorable mention (listed alphabetically by title):

{% include best-paper-box
  title="Automatic Correction of Human Translations"
  authors="Jessy Lin, Geza Kovacs, Aditya Shastry, Joern Wuebker, John DeNero"
  category="Honorable mention for contribution to special theme on human-centered NLP"
  comment="(see above)"
%}


{% include best-paper-box
  title="Balanced Data Approach for Evaluating Cross-Lingual Transfer: Mapping the Linguistic Blood Bank"
  authors="Dan Malkin, Tomasz Limisiewicz, Gabriel Stanovsky"
  category="Honorable mention for contribution to methods"
  comment="This paper addresses an important but underexplored aspect of zero-shot cross-linguistic transfer learning, namely the degree to which the linguistic characteristics of pre-trained models impact downstream fine-tuning performance. The authors propose a novel framework for exploring this topic, along with several interesting metrics for characterizing the relationship between donor and recipient languages. One of the most provocative findings of this paper is that English, the language most commonly used to pretrain models, is often not the best choice. This result has the potential to dramatically shift the way NLP researchers approach tasks that involve cross-linguistic transfer learning."
%}


{% include best-paper-box
  title="NewsEdits: A Dataset of News Article Revision Histories and a Novel Document-Level Reasoning Challenge"
  authors="Alexander Spangher, Xiang Ren, Jonathan May, Nanyun Peng"
  category="Honorable mention for contributions to resources"
  comment="The paper proposes a dataset consisting of English and French language newspapers with their revision histories covering a span of 15 years. They study to what degree article updates are predictable, and show that this task has relevance in practice. Prior research has focused on article updates on Wikipedia, where changes are often small grammar corrections, whereas they show that news article updates mostly contain semantically new information. In addition to this new benchmark, a detailed analysis of the results and an additional human evaluation is offered. This new resource can boost research on automatically revising articles."
%}

<style>
div.best-paper-box {
  border: 1px solid #bbccdd88;
  border-radius: .5em;
  margin: 1em auto;
  padding: 1em;
  background: #cadee41a;
}
p.best-paper-title {
  font-weight: bold;
  margin-bottom: 0;
  font-size: 120%;
}
p.best-paper-authors {
}
p.best-paper-category {
  font-weight: bold;
  font-style: italic;
}
p.best-paper-comment {
  margin-bottom: 0;
}
</style>


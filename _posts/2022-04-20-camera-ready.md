---
title: "Instructions for Camera-Ready Submission"
author: program-chairs
author_profile: true
tags:
  announcement
categories:
  blog
toc: true
toc_sticky: true
toc_h_max: 2
---

These instructions are adapted from the ones for ACL 2020, EMNLP 2020, NAACL 2021, ACL 2021, EMNLP 2021, and ACL 2022.
To submit the camera-ready version of your paper, please login to the [NAACL 2022 OpenReview site](https://openreview.net/group?id=aclweb.org/NAACL/2022/Conference) and select your Author Console, click on the submission title, and then click on the “Camera Ready Revision” button. This document is organized based on the sections in the Final Submission Page. Please note that the following applies to the NAACL 2022 Main conference papers as well as to the Findings of NAACL 2022 papers. 

## 1. Metadata (Title, Authors and Abstract in the Camera-Ready Form)
{: #s1-metadata}

### Can I make changes to the author list in the camera-ready version?

You can change the order of the authors, and you can remove or add an author from the list.

### How should I enter metadata on the OpenReview system?

The metadata (title, author, abstract) that you enter into OpenReview is very important because it will be used in the conference website, proceedings, handbook, mobile app, and the [ACL Anthology](http://www.aclweb.org/anthology/) (it will further propagate to DBLP, Google Scholar, Semantic Scholar, etc.).
Before the metadata is entered, please have all authors ensure that they have an up-to-date OpenReview profile, and that their name appears exactly the way they want it to appear, in addition to information about their current affiliation.  

* Unicode (UTF-8) can be used for accented or special characters. 
* Ordinarily, names must NOT be written in all caps or all lowercase. 
* The “Last Name” is the name(s) by which your paper is to be cited. It is usually a family name, even for authors from cultures where the family name is written first. 
* The “First Name” is usually a given name or names, including middle names/initials.

The metadata should be written using Unicode (UTF-8). Please try to follow these guidelines:

* In the title, please capitalize the first word, the first word after a colon (:), and all other words (including hyphenated words like Mixed-Case), except for function words: **articles, pronouns, conjunctions, prepositions, particles, subordinating conjunctions, and the infinitive marker “to”.**
* BibTeX (in many bibliography styles, including that used for ACL) lowercases the titles of the conference papers, and needs to be told which letters not to lowercase. Thus, if your title has letters that should always be capitals, please protect them with curly braces, like this: {E}nglish, {C}homsky, {IBM}, {CFG}s, {HMM}s. Please also protect the first letter after a sentence-final punctuation mark. For example:

  > *Can {LSTM} Learn to Capture Agreement? {T}he Case of {B}asque Named Entity Extraction from Noisy Input: {S}peech and {OCR}.*

  It is important to only protect those first letters that belong to the categories exhibited above, i.e., proper names (including language names), acronyms, abbreviations, the first letter after punctuation (such as a colon), and the first letter in a sentence. These curly braces will not appear in the online conference program or in the proceedings. They will only appear in the BibTeX file that others will use to cite your paper.

* If you need literal curly braces, please escape them like this: `\{ \}` 
* Please do not use any nonstandard LaTeX commands, and there should be no `\footnote` or citations using `\cite` or related commands. 
* You can use LaTeX math mode where appropriate: An $O(n^2)$ Algorithm for $n$-gram Smoothing. 
* You can use Unicode (UTF-8) for accented or special characters. 
* If you copy-and-paste from your PDF file, please be sure to rejoin words broken by hyphenation.

### Name change policy
If you have changed your name and you are concerned that your previous name is being cited in \*ACL publications, please email the NAACL Publication Chair by May 10, 2022 (the sooner the better!). We will search the proceedings and we will request the authors to change the citations before the Proceedings are published in the ACL Anthology. However, note that we cannot guarantee that the authors who miscited you will comply.
Please see the NAACL 2021 blog post about the first iteration of this policy for more details: <https://2021.naacl.org/blog/name-change-procedure/>

## 2. Main Paper (PDF in the Form)
{: #s2-main-paper}

### What are the page limits?
For both long and short papers, NAACL 2022 allows one extra page to help address the reviewers’ comments. Thus, long papers are allowed to use at most **9 pages** of text and short papers may use up to **5 pages** of text, plus unlimited space for ethical considerations sections, impact statement, acknowledgements, and references.

### What is the maximum size of the PDF file?
The maximum size of the PDF file (including the Appendices, see [Section 3](#s3-the-appendices)) should be no more than **20MB**.

### What is the format for the camera-ready copy?
The file must be in Portable Document Format (PDF) on A4 paper. 
We require the use of the ACL LaTeX style files or Microsoft Word style files tailored for this year's NAACL conference, 
which are the ARR style files. You can access the style files and detailed formatting instructions here: 
<https://github.com/acl-org/acl-style-files> and <https://acl-org.github.io/ACLPUB/formatting.html>.

If you are using LaTeX, please create the PDF file with `pdflatex` or `xelatex`. 
This ensures the use of the proper Type 1 fonts and also takes advantage of other PDF features. You will have the best results using a modern LaTeX distribution, 
in particular, [TeX live](http://www.tug.org/texlive/). Moreover, using the `geometry` package to set the A4 format is recommended.

### How do I check the format of the camera-ready version before submitting?
You should check the paper format according to this instruction page and use the style template files with the links above. 
The ACL 2022  and NAACL 2022 publication chairs have developed a package called <code><a href="https://github.com/acl-org/aclpubcheck">aclpubcheck</a></code> to automate much of the format checking ([usage notes](#s9-notes-on-aclpub-check)). 
Please run this package before submitting your paper to OpenReview in order not to miss some subtle formatting details. 
We also strongly advise authors to use [rebiber](https://github.com/yuchenlin/rebiber) to update their bib files with updated citations automatically.

### How should the camera-ready version of the paper differ from the original submission?
The camera-ready version of your paper should take into account the comments of the reviewers as well as other changes you see fit to make. In addition, be sure to do all of the following:

* Ensure that your paper conforms to the provided styles, font and page size (<https://github.com/acl-org/acl-style-files> and <https://acl-org.github.io/ACLPUB/formatting.html>).
* Include the authors’ names and affiliations under the title. Note that the list of authors should be identical to the list specified when submitting the paper.
* De-anonymize the references to your own work in the body of the paper. 
* Where appropriate, add acknowledgments for colleagues, reviewers, and grants. Do not number the Acknowledgements section. Please note that this section should be in the same font as the rest of the paper. 
* Ensure that all tables, graphs, and figures are readable at standard resolutions. 
* The Appendix (if exists) should appear after the references, as part of the same PDF file (see [Section 3](#s3-the-appendices)); in contrast, the supplemental materials should appear as separate ZIP files (see [Section 5](#s5-supplementary-material)).

### How can I make my camera-ready version accessible?
As a central venue of publication for our community, please prioritize the accessibility of your final version. The Diversity & Inclusion committee for NAACL 2022 has outlined some tips on how to do this:
<https://2022.naacl.org/blog/publication-accessibility-quality-inclusivity/>

### How do I ensure that my file is correctly formatted?
You need to run the <code><a href="https://github.com/acl-org/aclpubcheck">aclpubcheck</a></code> package ([usage notes](#s9-notes-on-aclpub-check)), and pay special attention to the following:

* **The paper size:** Your paper needs to be in A4 size. Here are a couple of ways to check this:
  * Using `pdfinfo`. The `pdfinfo` command should include "Page size: 595.276 x 841.89 pts" in its output. 
  * Using Apple's Preview.app. Open the PDF, and type Ctrl-I. It should report the correct page size. 
  * Using Adobe Acrobat. Open the PDF, navigate to File -> Properties... -> Description. The field labeled "Page Size" should read 8.27 x 11.69 inches.
* **Embedding fonts:** You can check your final PDF with the command <code><a href="https://www.xpdfreader.com/download.html">pdffonts</a> mypaper.pdf</code> and confirm that all the fonts say "yes" under "emb". If you are including graphics with the PDF extension, these files must also have embedded fonts. If your paper uses Asian fonts, they must be embedded in the PDF file so that they can be displayed by non-Asian versions of the PDF reader (Asian versions ship with a larger set of default fonts.)
* **Long titles:** The title should **NOT** exceed the left and right margins. Fold a long title into multiple lines if necessary.
* **Margins:** The margins of the text area must be reserved as specified in the style file.
* **Page numbers:** Do **NOT** provide page numbers for your PDF file. The page numbers will be generated automatically when compiling the Proceedings.
* **Consistent Author Names:** The author names must be consistent everywhere and must be the same as registered to the submission page(s), and must have the same spelling style in all accepted papers. This can avoid generating non-unique Author Index entries for authors with more than one accepted paper. Be sure to ask your co-authors to double-check that you have entered their names correctly.

### What if my paper includes graphics?
Remember that you are uploading a camera-ready version of your paper. Thus, artwork and photos should be included directly in the paper in their final positions. Ideally, you should use vector graphic formats (PDF, EPS), which allow the graphics to scale arbitrarily. Avoid GIF or JPEG images that are low resolution or highly compressed.
Your paper must look good both when printed (in A4 size) and when viewed on a screen as a PDF (zoomable to any size, color okay, etc.). Thus, you may want to use color high-resolution graphics, allowing readers to zoom in on a graph and to study it. However, please check that the same graph or photograph is legible when printed and in a PDF viewer at different resolutions. Do not go overboard on resolution; keep file sizes manageable. Note that vector graphics (e.g., encapsulated PostScript) look good at any scale and take up little space (unless you are plotting many thousands of data points).

### What if my paper's title or abstract has changed?
In addition to editing the title/abstract in the main paper, please also remember to edit those metadata fields when you upload the camera-ready version, 
so that they will appear correctly in the table of contents, author index, conference schedule, etc. 
**Please also note that your name will appear in the conference metadata as you have configured it in OpenReview**, so make sure that it is correct there 
(e.g., capitalization, full name, etc.). You can change this on the user profile page of your OpenReview account, under “Profile” -> “Edit Profile”. 
More information can be found in [the visual guide for authors](https://docs.google.com/presentation/d/1kJeoAfwbnFapUN0ySLSoOm11-2odz48DGS1DEzNs03k/edit?usp=sharing).

## 3. The Appendices (As the Last Part of the PDF File)
{: #s3-the-appendices}

Appendices typically include lemmas, discussion of hyper-parameter values, formulas, proofs, tables, data annotation guidelines, and other details and discussion that are informative but not critical to understanding the paper.

### Where do the Appendices go?
Appendices should be part of the camera-ready PDF file uploaded in the form. It should appear at the end of the PDF file, after the references.

### What's the page limit of the Appendices?
The Appendices do not count towards the page limit of the main paper, as recommended by the publication chairs, and there is no limit on their length.

### What template should the Appendices use?
The Appendices are part of  the main paper, and thus use the same template (See Section 3).

## 4. Copyright Consent (In the Form)
{: #s4-copyright-consent}

### What about copyright?
When you submit the camera-ready version of yourthe paper, you will be asked to sign the ACL Copyright Transfer Agreement **on behalf of all authors**, electronically (via the OpenReview Author Console). The authors will retain many rights under this agreement and this is appropriate in the vast majority of cases. Please contact the publication chairs with any concerns regarding copyright you may have.

### Who should sign the copyright form?
Before signing this form, please confirm with your co-authors (and, if applicable, with your and their employers) that they authorize you to sign on their behalf. Only the authorized representative needs to sign the copyright form. Please sign your full name (not just your first and/or last initials).

### What do I type under the Copyright Consent Signature field?
Please include your name, or “N/A” if the copyright form is not transferable. See figure below.

### I am an author, what should I write in the Copyright Consent Job Title? 
If you are an author, you can just leave this field empty. See figure below.

### What information should I add in the Copyright Consent Name and Address of Organization? 
You need to add **both** the name of your organization and its address. See figure below.

![Camera-Ready Copyright Consent](/assets/images/camera-ready-copyright.png)

## 5. Supplementary Material (Dataset and Code in the Form)
{: #s5-supplementary-material}

### Where do supplemental materials go?
The supplemental material can contain software and data uploaded separately as a ZIP file with a maximum size of **100MB**.

### Do I need to submit LaTeX source files?
No. LaTeX source files will not be used in the ACL Anthology, and thus please do NOT submit them.

## 6. Additional Rubric for Conditionally Accepted Papers (Respond to the Ethics Reviews in the Form)
{: #s6-additional-rubric}

### Who needs to submit this Response?
That depends on the status of your paper:

* If your paper has been conditionally accepted **pending addressing the issues raised in the ethical review**, you must submit an additional response to the Ethics Review comments (explained below). 
* If you were not asked to address the ethical review, you do NOT need to upload any additional information even if your paper has received an Ethics review and/or an Ethics metareview; you can simply skip this section in that case.

### What should the Response to the Ethics Review look like?
In the Response to Ethics Review part of the camera-ready form, the authors need to provide a short explanation about how they have made the changes requested by the **Ethics Chairs reviews (which appears in the NAACL 2022 OpenReview page for your paper)**. The response should list each of the concerns from the original Ethics Review along with a short summary of what was done to remedy the concern. In most cases, the authors will have to add or to expand their Ethical Concerns section in the camera-ready version of their paper. 

To make this as straightforward as possible, we recommend copying and pasting the contents of the Ethics Review into the Response and then describing the action taken after each item in the Ethics review. These will facilitate the decision of whether the final version of the paper will be accepted. This explanatory response will not be made public; it is just to expedite the conditional acceptance workflow for the Ethics Chairs' review process.

### What will happen after May 3, 2022?
The Ethics Committee chairs will go over the authors’ response to the Ethics Review and they will further check the camera-ready version of the paper to determine whether the required changes have been made. If so, the acceptance condition will be removed, the paper will be officially accepted to the Main conference or to the Findings of NAACL 2022, and the status of having been conditionally accepted will not be publicly visible. If not, the paper will be rejected. The NAACL 2022 PCs will inform the authors about the final decisions by **May 16, 2022**.
If you have any questions about the Ethics Reviews or about the changes required by the Ethics review, you can contact the NAACL 2022 Ethics Chairs. You can also check the [ARR Information about Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/).

## 7. Deadlines
{: #s7-deadlines}

### When and where do I send my final camera-ready paper?
You must submit the final version of your paper by **May 3, 2022** (11:59pm, UTC-12 hours, “anywhere on Earth”) by navigating to the [NAACL 2022 OpenReview site](https://openreview.net/group?id=aclweb.org/NAACL/2022/Conference) page and by following the internal links. 

## 8. Questions or Comments
{: #s8-questions-or-comments}

If you have any questions about 

* the camera-ready version, please contact our publication chair <ryan.cotterell@gmail.com>;
* the Ethics reviews, please contact the Ethics Committee chairs <naacl22ethics@googlegroups.com>.

For any other questions, please contact the NAACL 2022 Program Chairs.

## Notes on `aclpubcheck`
{: #s9-notes-on-aclpub-check}

Following NAACL 2021, we are using a package called `aclpubcheck`, which has been updated by the ACL 2022 and the NAACL 2022 Publication Chairs. The package automatically detects author formatting errors, margin violations as well as many other common formatting errors. Before submitting the camera-ready version of your paper to OpenReview, please run the package first and fix any detected errors.

The package is written in Python and you can access it here: <https://github.com/acl-org/aclpubcheck>.

You can also access a tutorial on how to use it here: <https://github.com/acl-org/aclpubcheck/blob/main/aclpubcheck_additional_info.pdf>.



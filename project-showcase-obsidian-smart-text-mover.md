## Obsidian Smart Text Mover
by Ankush Chander

---



#### Obsidian: Introduction

Obsidian is the private and flexible writing app that adapts to the way you think.
Here are the guiding principles that are set in stone: <!-- element align="left" -->
1. Yours  
2. Durable  
3. Private  
4. Malleable  
5. Independent  

---

#### Features 
1. **Links:** Create connections between your notes.  Invent your own personal Wikipedia.
2. **Graph view:** Visualize the relationships between your notes.
3. **Plugins:** Build your ideal thinking space. With hundreds of plugins and  open API, it's easy to tailor Obsidian to fit your personal workflow.

---
#### Plugins stats
Total community plugins so far: 1,727  
Common examples: 
1. [Advanced slides](https://obsidian.md/plugins?id=obsidian-advanced-slides): Create Markdown based presentations (723k downloads) 
2. [Kindle Highlights](https://obsidian.md/plugins?id=obsidian-kindle-plugin): Sync your Kindle book highlights using your Amazon login. (92K downloads)
3. [Clipper](https://obsidian.md/plugins?id=obsidian-clipper): Capture highlights from the web. (24K downloads)
4. [URL namer](https://obsidian.md/plugins?id=url-namer): Retrieve the HTML title of web pages to name external links. (5k downloads)


---
#### How to write a plugin
1. Generate a new repository from [sample-plugin-repo](https://github.com/obsidianmd/obsidian-sample-plugin)
2. Place it in  `/path/to/your/vault/.obsidian/plugins` folder
3. Update/test plugin as per your requirement and push to github
4. Submit plugin for [community listing](https://github.com/obsidianmd/obsidian-releases). 
---
#### Smart text mover
Motivation: 
While using obsidian as a bookmark app, we often dump links in a file. How to categorise/arrange those links smartly<!-- element align="left" -->
  
Problem statement: 
Given a link/text, find out the class/category to which it belongs<!-- element align="left" --> 


---
#### Evolution
Version 1:  
Create Category picker that allows user to pick one of the existing categories in the file and move text automatically.<!-- element align="left" -->  
Version 2:  
Use ChatGPT API to classify selected text to one of the categories.  
Version 3:  
Use Naive Bayes Classifier to leverage exiting categorisation to infer new links/texts 

---
#### ChatGPT prompt

For the text below, suggest top 3 classes from one of the following classes(no fluff, no explanation, no numbering just the classes): <!-- element align="left" -->  

classes:Software tryouts, Software Engineering, Economics/Anthropology, Business, Python, Embeddings, Deep Learning/LLMs,..., Linear Algebra, Graphs, Web development, Personal growth, Politics<!-- element align="left" -->    
text: [Bags of Queries as Sparse Document Representations](https://www.linkedin.com/pulse/bags-queries-sparse-document-representations-daniel-tunkelang-1jsic)

---

#### Naive Bayesian Classifier



$$ P(c|d) = \frac{P(d|c) \cdot P(c)}{P(d)} $$
where:
- $P(c|f)$ is the posterior probability of class $c$ given input d
- $P(d|c)$ is the likelihood of input d given class $c$
- $P(c)$ is the prior probability of class $c$
- $P(d)$ is the probability of input $d$
---
#### Assumptions
1. **Bag of Words:** Each document is treated as a bag of words ie. order of words is not considered.
2. **Conditional independence:** Each word occur independent to each other. Due to this we can calculate  
   $P(d|c) = P(w_1|c)*P(w_1|c)*...*P(w_{n}|c)$
   where $w_i$ are the words in the document.
---

#### Library used

1. [winkNLP](https://winkjs.org/wink-nlp/): WinkNLP is a JavaScript library for Natural Language Processing (NLP).
2. [OpenAI Node API Library](https://www.npmjs.com/package/openai/v/4.8.0): This library provides convenient access to the OpenAI REST API from TypeScript or JavaScript.



---

#### References
1. [Obsidian - Sharpen your thinking](https://obsidian.md)
2. [Naive Bayes classifier - Wikipedia](https://en.wikipedia.org/wiki/Naive%20Bayes%20classifier)
3. [GitHub - Ankush-Chander/obsidian-smart-move-text: Move text under headings(optionally using llms)](https://github.com/Ankush-Chander/obsidian-smart-move-text)

---
#### Thank you!

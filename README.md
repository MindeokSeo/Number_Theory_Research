# Undergraduate Research in Number Theory

## 📌 Overview
This repository documents my undergraduate research in number theory at Korea University, conducted under the advisement of Prof. [Dae Jun Kim](https://sites.google.com/view/daejunkim/home). The research is structured into two main phases: a Directed Reading Program (DRP) focusing on elementary number theory, and an ongoing investigation into additive number theory, quadratic forms, and $p$-adic analysis.

## 📅 Project Timeline & Activities

### Phase 1: Directed Reading Program (Sep 2025 - Dec 2025)
* **Objective**: Establish a strong theoretical foundation in elementary number theory and conduct an in-depth literature review.
* **Primary Textbook**: *[Elementary Number Theory and Its Applications](https://www.tbooks.solutions/elementary-number-theory-and-its-applications-bart-goddard-kenneth-h-rosen-6th-edition/)* (6th Edition) by Bart Goddard and Kenneth H. Rosen.
* **Key Literature**: *[On Euler's Totient Function](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-38/issue-10/On-Eulers-totient-function/bams/1183496203.pdf)* by D. H. Lehmer.
* **Focus**: Focused on understanding the Lehmer property and developing critical reading and synthesis skills for foundational mathematical papers.

### Phase 2: Additive Number Theory, Quadratic Forms, & $p$-adic Numbers, Module Theory (Jan 2026 - Present)
* **Objective**: Investigate additive number theory—specifically focusing on the universality of weighted sums of generalized polygonal numbers—and explore the analytic and algebraic properties of $p$-adic numbers.
* **Key Literature**: 
  * *[Weighted sums of generalized polygonal numbers with coefficients 1 or 2](https://arxiv.org/pdf/2006.04490)* by Daejun Kim.
  * *[A Short Proof of Cauchy's Polygonal Number Theorem](https://www.theoryofnumbers.com/melnathanson/pdfs/nath1987-55.pdf)* by Melvyn B. Nathanson.
  * *[AN INTRODUCTION TO THE p-ADIC NUMBERS](https://math.uchicago.edu/~may/REU2020/REUPapers/Pomerantz.pdf)* by Alexa Pomerantz.
  * *[THE p-ADIC EXPANSION OF RATIONAL NUMBERS](https://kconrad.math.uconn.edu/blurbs/gradnumthy/rationalsinQp.pdf)* by Keith Conrad.
  * *[Abstract Algebra]
(https://edu.fjfi.cvut.cz/studijni-materialy/Ing/4.%20ro%C4%8Dn%C3%ADk/GR/David%20S.%20Dummit,%20Richard%20M.%20Foote%20-%20Abstract%20Algebra%20-%203rd%20Edition-John%20Wiley%20and%20Sons,%20Inc.%20%282004%29.pdf))* by David S. Dummit and Richard M. Foote.
* **Computational Implementation**:
  * Developed and implemented a Python-based escalator tree algorithm to computationally discover and verify universal coefficient tuples for generalized 9-gonal numbers.
  * Applied the mathematical concept of a **"truant"** (the smallest positive integer not represented by a given linear combination) to systematically construct and prune branches within the escalator trees.
  * Systematically verified candidates to confirm their generation of all natural numbers up to a specified computational limit.
* **$p$-adic Analysis Study**:
  * Explored the construction of the field of $p$-adic numbers ($\mathbb{Q}_p$) and the ring of $p$-adic integers ($\mathbb{Z}_p$) using the $p$-adic metric and Cauchy sequences.
  * Investigated the topological and geometric properties of $\mathbb{Q}_p$, including its nature as a totally disconnected ultrametric space where all triangles are isosceles.
  * Analyzed the $p$-adic expansions of rational numbers, focusing on the characterization that rational numbers correspond precisely to eventually periodic $p$-adic expansions.
  * Studied algorithms to compute these expansions, particularly noting that rational numbers in the interval $[-1, 0)$ with a $p$-adic absolute value of 1 have purely periodic expansions.
* **Module Theory Study**:
  * 
  
## 📂 Repository Structure
* `src/`: Python source code containing the escalator tree algorithm, truant verification logic, and polygonal number generators.
* `docs/`: Summaries and literature review notes on the Lehmer property, Cauchy's polygonal number theorem, generalized polygonal numbers, and $p$-adic number theory.

## 👨‍🏫 Acknowledgements
This research is conducted as part of the Undergraduate Research program at Korea University, under the continuous mentorship of Prof. [Dae Jun Kim](https://sites.google.com/view/daejunkim/home).

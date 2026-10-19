# 1. Introduction

Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.

In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
In the code domain, however, the picture is less clear.
CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''
This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?

We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.
This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.
We operationalize this insight using CodeQL \cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.
Crucially, this structure-grounded mining is a \emph{training-time} intervention only, incurring zero additional inference cost.
This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \cite{liu2025codexgraph}, RANGER \cite{shah2025ranger}, and RepoGraph \cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.

Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.
First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\% CI: [a, b]) on Qwen2.5-Coder-3B \cite{hui2024qwen25coder} (with StarCoder2-3B \cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete
This establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.
Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\ 0.80), respond differently to structural negatives.
We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.

Our contributions are as follows:

1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.

2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\% timeout rate, 78\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.

3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.

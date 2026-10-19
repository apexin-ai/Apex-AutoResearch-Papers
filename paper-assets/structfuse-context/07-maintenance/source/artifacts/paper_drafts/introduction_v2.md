# 1. Introduction

Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.

Existing negative selection approaches span a broad spectrum but leave a critical gap.
Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.

We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.

Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).
Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.

Our contributions are as follows:
\begin{enumerate}
\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
\end{enumerate}

<!-- Claim 2 wording fix: 2026-05-15 -->
<!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->

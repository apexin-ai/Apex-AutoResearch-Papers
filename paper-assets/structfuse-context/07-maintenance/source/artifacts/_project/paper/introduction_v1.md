# 1. Introduction

Large-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.
Benchmarks such as SWE-bench \cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \cite{yang2024sweagent,xia2024agentless}, or combinations thereof.
A common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.
In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.
This mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.

Two largely independent lines of work have sought to address this limitation, each with a significant gap.
First, a growing body of methods leverages code structure graphs at inference time.
LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.
These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.
Second, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.
CoCoHaNeRe \cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.
However, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.
This leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.

We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.
Our central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}.
These gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.
We note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.
Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.

Our contributions are as follows:

1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \cite{fan2025cocohanere} are necessary for effective code search.

2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.

3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.

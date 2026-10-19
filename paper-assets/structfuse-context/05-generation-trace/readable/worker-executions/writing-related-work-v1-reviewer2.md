# writing related work v1 reviewer2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_writing_related-work-v1-reviewer2_20260515T095827.log`
- **Structured JSON:** [`e2f88dd3a6be35ec3b8b.json`](../../sessions/e2/e2f88dd3a6be35ec3b8b.json)

## Before a recorded user message

43 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "1c44cb3b-947a-464a-8ff6-98360dc8f92e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778856600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ddecbca2-9312-4ced-9864-0624e51bd6ea",
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Assistant

_source line 4_

我先读取两个文件，同时搜索 GraphCoder 和 ARISE 的论文信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "8da78e1c-0c34-48b8-a394-af186a1e621b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11804
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01NRcguekN7Mjc5DzQbfgBbW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "5b0cf173-28dd-4b1e-955e-6bbf3aca1600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11804
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T09:58:39.783Z_

<details><summary>↩ Tool result · `toolu_01NRcguekN7Mjc5DzQbfgBbW`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "508553d8-89e1-40e4-9a3e-2d5a7b8283b7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_012m9ZBFfcWjND5x3cDDNNTD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "7131abad-df5e-453a-985a-b2e7b5fb09c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11804
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T09:58:40.235Z_

<details><summary>↩ Tool result · `toolu_012m9ZBFfcWjND5x3cDDNNTD`</summary>

```text
1	# 1. Introduction
2	
3	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
4	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
5	These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
6	Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
7	Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.
8	
9	In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
10	DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
11	These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
12	In the code domain, however, the picture is less clear.
13	CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''
14	This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?
15	
16	We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.
17	This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.
18	We operationalize this insight using CodeQL \cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.
19	Crucially, this structure-grounded mining is a \emph{training-time} intervention only, incurring zero additional inference cost.
20	This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \cite{liu2025codexgraph}, RANGER \cite{shah2025ranger}, and RepoGraph \cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.
21	
22	Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.
23	First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\% CI: [a, b]) on Qwen2.5-Coder-3B \cite{hui2024qwen25coder} (with StarCoder2-3B \cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete
24	This establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.
25	Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\ 0.80), respond differently to structural negatives.
26	We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.
27	
28	Our contributions are as follows:
29	
30	1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.
31	
32	2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\% timeout rate, 78\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.
33	
34	3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "45087c88-1d21-4d11-b22a-c1bd89433a14",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.\n\n3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EgyEM3ztHw8J6xeDnD9kDy`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "570cd770-6bef-41e2-94ad-9db3183d7407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11804
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T09:58:40.416Z_

<details><summary>↩ Tool result · `toolu_01EgyEM3ztHw8J6xeDnD9kDy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "fd93ec4f-2cb6-41fc-99f9-3e9857dc8e36",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for GraphCoder and ARISE papers to fact-check the intra-procedural scope claim.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "e1cb4950-d114-46f5-b4b3-71b584eb8956",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 12_

搜索 GraphCoder 和 ARISE 论文的 data-flow scope 信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "e85a6bb9-9903-47c8-9478-f6b95f05e515",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fa11q97dDFLWj7zLFPRNvG`</summary>

```json
{
  "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "5f27f1b4-158b-4a1a-a2f7-cb22c72cf7e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WuSqTL4xCPuHj5NVcisLtC`</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "d0467b35-8567-4a58-9cb3-bea80efc9e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3779
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T09:58:51.089Z_

<details><summary>↩ Tool result · `toolu_01WuSqTL4xCPuHj5NVcisLtC`</summary>

```text
Web search results for query: "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models","url":"https://arxiv.org/abs/2605.06826"},{"title":"[2605.13681] Sampling from Flow Language Models via Marginal-Conditioned Bridges","url":"https://arxiv.org/abs/2605.13681"},{"title":"[2605.13509] Quantifying information flow along a stochastic trajectory","url":"https://arxiv.org/abs/2605.13509"},{"title":"[2605.10938] ELF: Embedded Language Flows","url":"https://arxiv.org/abs/2605.10938"},{"title":"[2605.12951] Coreset-Induced Conditional Velocity Flow Matching","url":"https://arxiv.org/abs/2605.12951"},{"title":"[2605.02287] Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets","url":"https://arxiv.org/abs/2605.02287"},{"title":"[2605.14137] Flow Field Reconstruction with Sensor Placement Policy Learning","url":"https://arxiv.org/abs/2605.14137"},{"title":"[2605.08648] FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts","url":"https://arxiv.org/abs/2605.08648"}]

Based on the search results, I found the paper you're looking for:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

The paper was authored by Shahd Seddik and Fatemeh Fard and submitted on May 4, 2026.

The paper is available at arXiv:2605.03117.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "13b30255-0402-4bd6-8b7c-ea1a71d82568",
  "tool_use_result": {
    "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Su8dfZn21q4s2ejnMvTbeh",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models",
            "url": "https://arxiv.org/abs/2605.06826"
          },
          {
            "title": "[2605.13681] Sampling from Flow Language Models via Marginal-Conditioned Bridges",
            "url": "https://arxiv.org/abs/2605.13681"
          },
          {
            "title": "[2605.13509] Quantifying information flow along a stochastic trajectory",
            "url": "https://arxiv.org/abs/2605.13509"
          },
          {
            "title": "[2605.10938] ELF: Embedded Language Flows",
            "url": "https://arxiv.org/abs/2605.10938"
          },
          {
            "title": "[2605.12951] Coreset-Induced Conditional Velocity Flow Matching",
            "url": "https://arxiv.org/abs/2605.12951"
          },
          {
            "title": "[2605.02287] Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets",
            "url": "https://arxiv.org/abs/2605.02287"
          },
          {
            "title": "[2605.14137] Flow Field Reconstruction with Sensor Placement Policy Learning",
            "url": "https://arxiv.org/abs/2605.14137"
          },
          {
            "title": "[2605.08648] FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts",
            "url": "https://arxiv.org/abs/2605.08648"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nExisting graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.\n\nARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.\n\nThe paper was authored by Shahd Seddik and Fatemeh Fard and submitted on May 4, 2026.\n\nThe paper is available at arXiv:2605.03117."
    ],
    "durationSeconds": 5.921278698999998
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T09:58:52.760Z_

<details><summary>↩ Tool result · `toolu_01Fa11q97dDFLWj7zLFPRNvG`</summary>

```text
Web search results for query: "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"39th ASE 2024: Sacramento, CA, USA","url":"https://dblp.org/db/conf/kbse/ase2024.html"},{"title":"2024 39th IEEE/ACM International Conference on ...","url":"https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found search results for GraphCoder and ASE 2024. Here are the key findings:

## GraphCoder ASE 2024 Paper

GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang and presented at ASE 2024.

## Core Approach

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process, capturing the context of completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.

## Data-Flow and Procedural Analysis

GraphCoder captures the context through code context graph (CCG) that consists of control-flow and data/control-dependence between code statements, though the specific mention of "intra-procedural" and "inter-procedural" analysis in your query doesn't appear to be explicitly labeled with those terms in the search results. The framework appears to handle dependencies both within and across code structures through its graph-based approach.

The paper has been posted on arXiv and was presented at the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE 2024) in Sacramento, CA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "78b39499-ae74-445d-9e70-80de27be74ae",
  "tool_use_result": {
    "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J6eZSYdkLJR9hr9WeuB4n1",
        "content": [
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          },
          {
            "title": "39th ASE 2024: Sacramento, CA, USA",
            "url": "https://dblp.org/db/conf/kbse/ase2024.html"
          },
          {
            "title": "2024 39th IEEE/ACM International Conference on ...",
            "url": "https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4SE"
          }
        ]
      },
      "I found search results for GraphCoder and ASE 2024. Here are the key findings:\n\n## GraphCoder ASE 2024 Paper\n\nGraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang and presented at ASE 2024.\n\n## Core Approach\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process, capturing the context of completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.\n\n## Data-Flow and Procedural Analysis\n\nGraphCoder captures the context through code context graph (CCG) that consists of control-flow and data/control-dependence between code statements, though the specific mention of \"intra-procedural\" and \"inter-procedural\" analysis in your query doesn't appear to be explicitly labeled with those terms in the search results. The framework appears to handle dependencies both within and across code structures through its graph-based approach.\n\nThe paper has been posted on arXiv and was presented at the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE 2024) in Sacramento, CA."
    ],
    "durationSeconds": 7.934743065999999
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details on both papers. The ARISE search result mentions "intra-procedural definition-use edges" - so it does seem limited to intra-procedural scope. Let me get more detail on GraphCoder's scope.

For GraphCoder, the search result says it uses "code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements". I need to check if this is intra-procedural or inter-procedural. Let me read the arxiv HTML page for more details.


I should look up more specifics about GraphCoder's scope to determine whether it handles inter-procedural analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "4b4eda62-4c40-4012-9bf6-171325619c66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 18_

需要更多细节，特别是 GraphCoder 的 CCG 是否跨过程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "84fa2a4f-3051-4a37-87e3-ac3b70aacba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QXCQ3sX4vBuPopLrJK9DnJ`</summary>

```json
{
  "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "11a5481d-957a-4e52-aa47-d294dcfdadfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMMvtz6VCZJiRztBXu32eD`</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "49270132-91f6-4d2c-bda8-51f95eaf4f50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T09:59:04.943Z_

<details><summary>↩ Tool result · `toolu_01QXCQ3sX4vBuPopLrJK9DnJ`</summary>

```text
Web search results for query: "GraphCoder "code context graph" CCG "intra-procedural" OR "within function" OR "single function" scope ASE 2024"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code","url":"https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"},{"title":"GraphCoder | NL2Code","url":"https://nl2code.github.io/posts/GraphCoder/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus","url":"https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"}]

## Search Results for GraphCoder with Code Context Graph (CCG)

I've found comprehensive information about GraphCoder and its use of Code Context Graphs. Here are the key findings:

### Overview

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.

### Code Context Graph (CCG)

GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.

### Performance Results

Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.

### Publication Details

The paper was presented at ASE 2024 Research Papers on October 31, 2024.

### Technical Approach

Based on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.

The search results confirm that GraphCoder is a repository-level code completion framework presented at ASE 2024 that uses Code Context Graphs (CCG) to capture code dependencies and structural relationships for improved code completion tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "d80073dd-820b-45a1-888d-cae2dc5185b4",
  "tool_use_result": {
    "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QhQxnVtc3rfyieVwrdhkxw",
        "content": [
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code",
            "url": "https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"
          },
          {
            "title": "GraphCoder | NL2Code",
            "url": "https://nl2code.github.io/posts/GraphCoder/"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus",
            "url": "https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          }
        ]
      },
      "## Search Results for GraphCoder with Code Context Graph (CCG)\n\nI've found comprehensive information about GraphCoder and its use of Code Context Graphs. Here are the key findings:\n\n### Overview\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.\n\n### Code Context Graph (CCG)\n\nGraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.\n\n### Performance Results\n\nCompared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.\n\n### Publication Details\n\nThe paper was presented at ASE 2024 Research Papers on October 31, 2024.\n\n### Technical Approach\n\nBased on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.\n\nThe search results confirm that GraphCoder is a repository-level code completion framework presented at ASE 2024 that uses Code Context Graphs (CCG) to capture code dependencies and structural relationships for improved code completion tasks."
    ],
    "durationSeconds": 6.269019581000004
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T09:59:05.900Z_

<details><summary>↩ Tool result · `toolu_01VMMvtz6VCZJiRztBXu32eD`</summary>

```text
Web search results for query: "ARISE arXiv 2605.03117 "intra-procedural" "definition-use" "inter-procedural" repository-level graph"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"RepoAudit: An Autonomous LLM-Agent for Repository- ...","url":"https://arxiv.org/pdf/2501.18160"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"[2605.00817] When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models","url":"https://arxiv.org/abs/2605.00817"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural","url":"https://www.arxiv.org/pdf/2602.06751"},{"title":"Retrieval from Within: An Intrinsic Capability of Attention-Based Models","url":"https://arxiv.org/html/2605.05806"},{"title":"SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution","url":"https://arxiv.org/html/2605.10114"},{"title":"Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences","url":"https://arxiv.org/html/2605.02584"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection","url":"https://arxiv.org/html/2602.06751v1"}]

Based on the web search results, I found information about the arXiv paper 2605.03117:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Repository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

The paper was published on arXiv on May 4, 2026, and addresses a key gap in existing systems: none constructs statement-level nodes, none models definition-use relationships, and none exposes a first-class data-flow slicing primitive to the agent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "4603aa9f-f5bf-4cd2-b987-7230ae5e4402",
  "tool_use_result": {
    "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kemj9qxQHeJHv2RVBoXfp6",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "RepoAudit: An Autonomous LLM-Agent for Repository- ...",
            "url": "https://arxiv.org/pdf/2501.18160"
          },
          {
            "title": "INTERPROCEDURAL ANALYSIS",
            "url": "https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"
          },
          {
            "title": "[2605.00817] When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models",
            "url": "https://arxiv.org/abs/2605.00817"
          },
          {
            "title": "Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural",
            "url": "https://www.arxiv.org/pdf/2602.06751"
          },
          {
            "title": "Retrieval from Within: An Intrinsic Capability of Attention-Based Models",
            "url": "https://arxiv.org/html/2605.05806"
          },
          {
            "title": "SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution",
            "url": "https://arxiv.org/html/2605.10114"
          },
          {
            "title": "Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences",
            "url": "https://arxiv.org/html/2605.02584"
          },
          {
            "title": "Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection",
            "url": "https://arxiv.org/html/2602.06751v1"
          }
        ]
      },
      "Based on the web search results, I found information about the arXiv paper 2605.03117:\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nRepository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.\n\nARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.\n\nThe paper was published on arXiv on May 4, 2026, and addresses a key gap in existing systems: none constructs statement-level nodes, none models definition-use relationships, and none exposes a first-class data-flow slicing primitive to the agent."
    ],
    "durationSeconds": 6.723058895999999
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the actual GraphCoder paper HTML to determine whether the CCG is intra-procedural or inter-procedural. Let me fetch the arXiv HTML page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "bda9b8ac-2626-4fdf-a5dd-a328aeac9c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 24_

让我更深入查看 GraphCoder 论文的实际内容来确认 CCG 是否限于函数内部。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "d9f0e960-37f0-4fc0-8510-c01abf3e5a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q68udzjabaoe2zrXkvYXXX`</summary>

```json
{
  "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "dd232889-1cdd-436b-8dd1-2a6680b0f85d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0138Yv4kUtnu5QEbqBsSSLuR`</summary>

```json
{
  "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "3b984ccb-e31b-411b-b181-4d193068e6e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T09:59:18.781Z_

<details><summary>↩ Tool result · `toolu_0138Yv4kUtnu5QEbqBsSSLuR`</summary>

```text
Web search results for query: "ARISE arxiv 2605.03117 "inter-procedural" OR "cross-function" OR "call graph" data-flow edges graph construction"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Interprocedural Dataflow Analysis in the Presence of Large Libraries | SpringerLink","url":"https://link.springer.com/chapter/10.1007/11688839_2"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"Precise interprocedural dataflow analysis with applications to constant propagation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/0304397596000722"},{"title":"[1304.6274] Interprocedural Data Flow Analysis in Soot using Value Contexts","url":"https://arxiv.org/abs/1304.6274"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"PROGRAML: A Graph-based Program Representation for ...","url":"https://www.research.ed.ac.uk/files/221627281/PROGRAML_CUMMINS_DOA08052021_AFV.pdf"},{"title":"PhASAR: An Inter-procedural Static Analysis Framework for C/C++ | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-17465-1_22"}]

Based on the search results, I found information about the ARISE paper (arxiv 2605.03117):

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Regarding inter-procedural and cross-function capabilities: Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures. The paper positions ARISE as addressing this limitation by focusing on augmenting a structural repository graph with statement-level nodes and intra-procedural def-use edges, which means the graph construction emphasizes **intra-procedural** (within-function) data-flow edges rather than inter-procedural edges.

The repository graph unifies structural and data-flow information at statement granularity, enabling agents to query not only how code is organised (files, classes, functions) but also how values are defined and propagated within a procedure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "d636bd7c-2d61-4014-a439-40f476b50273",
  "tool_use_result": {
    "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction",
    "results": [
      {
        "tool_use_id": "srvtoolu_016qiDdL3tEmDWyKV1m39tyy",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Interprocedural Dataflow Analysis in the Presence of Large Libraries | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/11688839_2"
          },
          {
            "title": "INTERPROCEDURAL ANALYSIS",
            "url": "https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"
          },
          {
            "title": "GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub",
            "url": "https://github.com/ChrisCummins/ProGraML"
          },
          {
            "title": "Precise interprocedural dataflow analysis with applications to constant propagation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/0304397596000722"
          },
          {
            "title": "[1304.6274] Interprocedural Data Flow Analysis in Soot using Value Contexts",
            "url": "https://arxiv.org/abs/1304.6274"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis",
            "url": "http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for ...",
            "url": "https://www.research.ed.ac.uk/files/221627281/PROGRAML_CUMMINS_DOA08052021_AFV.pdf"
          },
          {
            "title": "PhASAR: An Inter-procedural Static Analysis Framework for C/C++ | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-17465-1_22"
          }
        ]
      },
      "Based on the search results, I found information about the ARISE paper (arxiv 2605.03117):\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nRegarding inter-procedural and cross-function capabilities: Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures. The paper positions ARISE as addressing this limitation by focusing on augmenting a structural repository graph with statement-level nodes and intra-procedural def-use edges, which means the graph construction emphasizes **intra-procedural** (within-function) data-flow edges rather than inter-procedural edges.\n\nThe repository graph unifies structural and data-flow information at statement granularity, enabling agents to query not only how code is organised (files, classes, functions) but also how values are defined and propagated within a procedure."
    ],
    "durationSeconds": 6.176961603999996
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T09:59:20.093Z_

<details><summary>↩ Tool result · `toolu_01Q68udzjabaoe2zrXkvYXXX`</summary>

```text
Web search results for query: "GraphCoder arxiv 2406.07003 "code context graph" scope statement-level function-level "control flow" "data dependence" construction"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"(PDF) GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://www.researchgate.net/publication/381318841_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Code_Context_Graph-based_Retrieval_and_Language_Model"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"Enhancing Domain-Specific Code Completion via Collaborative Inference with Large and Small Language Models | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3770748"},{"title":"GraphCoder: Enhancing Repository-Level Code ...","url":"https://arxiv.org/pdf/2406.07003"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases","url":"https://arxiv.org/html/2507.19942v1"},{"title":"[Literature Review] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://www.themoonlight.io/en/review/graphcoder-enhancing-repository-level-code-completion-via-code-context-graph-based-retrieval-and-language-model"}]

Based on the search results for GraphCoder (arXiv 2406.07003), here's what I found regarding the code context graph and its construction:

## Code Context Graph (CCG) Overview

GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements.

## Graph Composition and Construction

A code context graph is the superposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG).

## Scope and Level

The CCG is a statement-level multi-graph constructed from three types of graphs—control flow graphs (CFG), control dependence graphs (CDG), and data dependence graphs (DDG). Additionally, GraphCoder constructs code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements used in retrieval-augmented code completion task.

## Benefits of Graph-Based Approach

The CCG contributes to improving retrieval effectiveness from three aspects: (1) Replacing sequence representation of code with structured representation to capture more relevant statements of the completion task; (2) Augmenting the sequence-based similarity between the context of two statements with structure-based similarity to identify deeply matched statements of the completion target from the repository; (3) Adopting a decay-with-distance structural similarity to weight the different importance of context statements to the completion target.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "7ccc70df-e21e-4661-86e7-3ce7801fe727",
  "tool_use_result": {
    "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E5RuPv39Pn859AGv2aqPKL",
        "content": [
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "(PDF) GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://www.researchgate.net/publication/381318841_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Code_Context_Graph-based_Retrieval_and_Language_Model"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"
          },
          {
            "title": "Enhancing Domain-Specific Code Completion via Collaborative Inference with Large and Small Language Models | ACM Transactions on Software Engineering and Methodology",
            "url": "https://dl.acm.org/doi/10.1145/3770748"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code ...",
            "url": "https://arxiv.org/pdf/2406.07003"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases",
            "url": "https://arxiv.org/html/2507.19942v1"
          },
          {
            "title": "[Literature Review] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://www.themoonlight.io/en/review/graphcoder-enhancing-repository-level-code-completion-via-code-context-graph-based-retrieval-and-language-model"
          }
        ]
      },
      "Based on the search results for GraphCoder (arXiv 2406.07003), here's what I found regarding the code context graph and its construction:\n\n## Code Context Graph (CCG) Overview\n\nGraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements.\n\n## Graph Composition and Construction\n\nA code context graph is the superposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG).\n\n## Scope and Level\n\nThe CCG is a statement-level multi-graph constructed from three types of graphs—control flow graphs (CFG), control dependence graphs (CDG), and data dependence graphs (DDG). Additionally, GraphCoder constructs code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements used in retrieval-augmented code completion task.\n\n## Benefits of Graph-Based Approach\n\nThe CCG contributes to improving retrieval effectiveness from three aspects: (1) Replacing sequence representation of code with structured representation to capture more relevant statements of the completion task; (2) Augmenting the sequence-based similarity between the context of two statements with structure-based similarity to identify deeply matched statements of the completion target from the repository; (3) Adopting a decay-with-distance structural similarity to weight the different importance of context statements to the completion target."
    ],
    "durationSeconds": 7.556468009000004
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make the edits. Let me summarize what I've found:

1. **GraphCoder**: The CCG (Code Context Graph) is constructed from control-flow graphs, control-dependence graphs, and data-dependence graphs at the statement level. These are classic intra-procedural analyses (CFG, CDG, DDG are standard intra-procedural constructs). However, GraphCoder operates at repository-level for code completion, so the retrieval itself is cross-file, but the graph analysis for individual code snippets appears to be intra-procedural. The paper doesn't explicitly use the term "intra-procedural" from what I can see, but CFG/CDG/DDG are inherently intra-procedural constructs. I think the current claim is essentially correct - the data-flow analysis in GraphCoder is intra-procedural.


2. **ARISE**: The paper explicitly mentions "intra-procedural definition-use edges" and adds statement-level nodes with these edges to a repository-level structural graph covering files, classes, and functions. So the data-flow component is definitively intra-procedural, even though the broader structural graph spans cross-file relationships.

For both papers, the claim about intra-procedural scope is accurate for the data-flow analysis component, though each tool also incorporates cross-file structural information at a higher level. I'm verifying that the data-flow claim holds up for both GraphCoder and ARISE—their CFG/CDG/DDG and intra-procedural definition-use edges are indeed scoped within procedures, so I'll refine the wording to "data-flow edges that remain intra-procedural" to be more precise about what's actually limited. For the second point, I'll soften the language from "all these methods" to "these methods primarily leverage" to be less absolute.

Now I need to add a clarifying note about CoCoHaNeRe in section 2.3, then insert the distinction before the StructFuse discussion, and make all four edits together. I'm noting that CoCoHaNeRe actually evaluates multiple non-gradient strategies beyond just BM25—including embedding-based approaches—and finds limitations across both, which is what drives their gradient-based solution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "b7fbd284-0a3c-43f6-96fb-10775d405165",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1282
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 30_

搜索确认了：
- **GraphCoder** 的 CCG 由 CFG/CDG/DDG 构成，均为经典 intra-procedural 分析
- **ARISE** 明确描述其 data-flow 边为 "intra-procedural definition-use edges"（但整体结构图含跨文件的 call edges）

两者的 data-flow 分析确实限于 intra-procedural，当前断言基本正确，但需更精确地指明是 data-flow 分析的 scope 而非整个系统。现在执行四项修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "530eaaf0-3d54-43e3-9278-88c13093322a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1282
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_013fR4oJMd3ByidJZkYgQp8t`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
  "new_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "2cc3d686-db30-4362-85a9-a7fda1ed153c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1282
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T09:59:55.507Z_

<details><summary>↩ Tool result · `toolu_013fR4oJMd3ByidJZkYgQp8t`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "8d4b7eb9-b267-4567-8db2-47ec654be137",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
    "newString": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope.",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 4,
        "newStart": 18,
        "newLines": 4,
        "lines": [
          " ",
          " Program dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.",
          " ",
          "-Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.",
          "+Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01QKyuYCxkhKVP3Jztgd3XZw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Critically, all these methods construct and query graphs at inference time",
  "new_string": "Critically, these methods primarily leverage structural graphs at inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "2d21a34a-117f-4388-8668-21009d469c1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BTaHDWqby3R6C9FXZSb6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2651,
      "cache_read_input_tokens": 33168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2651
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T09:59:59.723Z_

<details><summary>↩ Tool result · `toolu_01QKyuYCxkhKVP3Jztgd3XZw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "90fe2a6a-1ff9-4298-be32-d9111dae5c24",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "Critically, all these methods construct and query graphs at inference time",
    "newString": "Critically, these methods primarily leverage structural graphs at inference time",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 4,
        "newStart": 18,
        "newLines": 4,
        "lines": [
          " ",
          " Program dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.",
          " ",
          "-Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.",
          "+Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01QpJSfZAig1P7AjR7RqFcgB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
  "new_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "a331ab90-b265-406b-862b-6a374bc0940d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9xTSjYeiQZ8tzBsqpNBrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 35819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T10:00:04.527Z_

<details><summary>↩ Tool result · `toolu_01QpJSfZAig1P7AjR7RqFcgB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "f67351ca-1db2-4b58-8ab3-629ffb290dc9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
    "newString": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach.",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " ",
          " The quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.",
          " ",
          "-In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.",
          "+In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.",
          " ",
          " ## 2.4 Code Structure in Machine Learning",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01XmvQUK6JYqP7BNjzDmyWyV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
  "new_string": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "ece5d237-77db-40e7-9207-a027868a680f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116fbHdnoJYB8XisDvD9mmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 36055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 364
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T10:00:08.321Z_

<details><summary>↩ Tool result · `toolu_01XmvQUK6JYqP7BNjzDmyWyV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "3db12874-61ef-463e-a717-5c153a52390e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
    "newString": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " ## 2.2 Contrastive Learning for Code",
          " ",
          "-Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.",
          "+Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.",
          " ",
          " ## 2.3 Hard Negative Mining",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 39_

验证最终文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "d3793abb-8342-47d5-a784-66b5b4a65d75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnE5uWgWw8zpi9LEU4Uar9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 36419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01Sh89ei8kVpQ5TSCkLp17eJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "7918b1ce-7234-4961-b517-7de9e73f12d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnE5uWgWw8zpi9LEU4Uar9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 36419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T10:00:11.160Z_

<details><summary>↩ Tool result · `toolu_01Sh89ei8kVpQ5TSCkLp17eJ`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "98dd95e8-3a25-4511-8902-f0ea720bdf02",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

四项修改完成，摘要如下：

**修正 1 (§2.4)** — GraphCoder/ARISE scope：WebSearch 确认两者的 data-flow 分析确实是 intra-procedural（GraphCoder 用 CFG/CDG/DDG，ARISE 明确描述为 "intra-procedural definition-use edges"）。保留 intra-procedural 断言，但改写为更精确的表述，区分了两者各自的 data-flow 类型（control/data dependence vs. definition-use chains），并明确是 "data-flow analysis" 而非整个系统受限于 intra-procedural。

**修正 2 (§2.4)** — "all these methods" → "these methods primarily leverage structural graphs at inference time"，软化了全称断言。

**修正 3 (§2.3)** — CoCoHaNeRe 句后新增一句，说明该工作同时评估了多种非梯度策略（BM25 和 embedding-based），消除与 Introduction（批评 embedding negatives）的表述不一致。

**修正 4 (§2.2)** — 在 StructFuse 定位句前插入半句 "While GraphCodeBERT uses structural edges as a pretraining objective"，明确区分 pretraining objective vs. training-time negative selection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "uuid": "73c84579-8acc-426a-84f5-a21fbe750f91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tZGctoP4LjYeHdAZPyADS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 36696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1836
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 43_

四项修改完成，摘要如下：

**修正 1 (§2.4)** — GraphCoder/ARISE scope：WebSearch 确认两者的 data-flow 分析确实是 intra-procedural（GraphCoder 用 CFG/CDG/DDG，ARISE 明确描述为 "intra-procedural definition-use edges"）。保留 intra-procedural 断言，但改写为更精确的表述，区分了两者各自的 data-flow 类型（control/data dependence vs. definition-use chains），并明确是 "data-flow analysis" 而非整个系统受限于 intra-procedural。

**修正 2 (§2.4)** — "all these methods" → "these methods primarily leverage structural graphs at inference time"，软化了全称断言。

**修正 3 (§2.3)** — CoCoHaNeRe 句后新增一句，说明该工作同时评估了多种非梯度策略（BM25 和 embedding-based），消除与 Introduction（批评 embedding negatives）的表述不一致。

**修正 4 (§2.2)** — 在 StructFuse 定位句前插入半句 "While GraphCodeBERT uses structural edges as a pretraining objective"，明确区分 pretraining objective vs. training-time negative selection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 103385,
  "duration_api_ms": 124130,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "total_cost_usd": 0.5860277500000001,
  "usage": {
    "input_tokens": 1641,
    "cache_creation_input_tokens": 26691,
    "cache_read_input_tokens": 301712,
    "output_tokens": 3931,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26691,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 367,
        "cache_read_input_tokens": 36696,
        "cache_creation_input_tokens": 1836,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1836
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 89158,
      "outputTokens": 2543,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.161873,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1641,
      "outputTokens": 3931,
      "cacheReadInputTokens": 301712,
      "cacheCreationInputTokens": 26691,
      "webSearchRequests": 0,
      "costUSD": 0.42415474999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b30413ae-49e9-45ed-acb3-4eb14c99120b"
}
```

</details>

---

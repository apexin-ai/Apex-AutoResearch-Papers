# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260516T024157_result.json`
- **Structured JSON:** [`dcedecc62be137c6622d.json`](../../sessions/dc/dcedecc62be137c6622d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method 章节已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex`。

内容概要：
- **2.1 Model and Data**: OpenVLA-7B 架构（SigLIP → Projector → Llama-2 7B → action head）、LIBERO-10 微调、LIBERO-Goal 评估、untrained control 设计
- **2.2 Representation Extraction**: 五个表征来源 (a)-(e) 的定义，$2\times2$ factorial design（trained/untrained × with/without instruction）
- **2.3 RSA**: RDM 构建、Spearman $\rho$、per-task 分析、bootstrap CI (10,000 resamples)
- **2.4 Functional Action Probes**: MLP probe 架构（$d_\text{in} \to 256 \to 7$）、训练协议（Adam, lr=$10^{-3}$, batch 256, 50 epochs, patience 5）、mean $R^2$ 指标、bootstrap paired comparison
- **2.5 CKA Analysis**: Linear CKA 与 RDM kernel CKA 两种变体，dimension mismatch caveat

所有术语、符号、数字与 experiments.tex 保持一致。仅使用指定的 bibtex keys。

---

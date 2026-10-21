# paper writing

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260516T122602_result.json`
- **Structured JSON:** [`18ff01906e814dcd70d1.json`](../../sessions/18/18ff01906e814dcd70d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex`。

结构概览：
- **5.1 Setup** — 模型/predictor/训练/评估/baseline 完整描述
- **5.2 Main Results** — Table 1 (30%/50% sparsity, 5 methods, 5 metrics)，重点叙述 KL PPL 优势和 50% downstream collapse
- **5.3 Iso-Compute** — BCE 2.71× compute 仍 2.37× worse，结构性失败分析
- **5.4 Ablation** — Table 3 (Gumbel/STE/SPON/BCE+comp)，量化各组件贡献
- **5.5 Scaling & Phase Transition** — PPL sweep (30/50/70%) + MMLU degradation band 分析，推荐 30% 操作点
- **5.6 SPON Analysis** — L2 norm/cosine similarity 分解，解释 subsumption effect
- **5.7 Cross-Architecture** — Mistral-7B 验证泛化性

所有定量 claim 均附 `% exp_id:` 注释，禁用词已规避，数字精度符合规范。

---

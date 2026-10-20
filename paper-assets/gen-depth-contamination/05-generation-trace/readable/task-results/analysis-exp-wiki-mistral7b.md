# analysis exp wiki mistral7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_mistral7b_20260517T195206_result.json`
- **Structured JSON:** [`b49e8ebe87461b4d8af1.json`](../../sessions/b4/b49e8ebe87461b4d8af1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：Mistral-7B Wikipedia K\* = 1（success）**

关键发现：
- depth 0→1 AUC=0.9607（极强可区分），depth 1→2 骤降至 0.5552（chance level），后续 depth 全部 ~0.50
- JSD 同步印证：0→1 JSD=0.054，之后降至 0.003-0.006
- 与 C4 (K\*=1) 完全一致，与 arXiv (K\*=3) 形成鲜明对比
- 与其他模型 Wikipedia 结果一致（Pythia/OLMo/LLaMA 均 K\*=1）

这强化了 domain-dependent K\* narrative：Wikipedia 和 C4 作为预训练高覆盖域呈现 one-wash，arXiv 作为专业域呈现 domain rescue。Mistral-7B 现有 3 domain 完整数据，可作为论文核心案例。

报告已写入 artifacts，registry 已更新为 DONE(success)。

---

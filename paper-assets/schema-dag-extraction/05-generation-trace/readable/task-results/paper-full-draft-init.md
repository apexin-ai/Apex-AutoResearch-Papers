# paper full draft init

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_full-draft-init_20260515T194742_result.json`
- **Structured JSON:** [`bae69369a4f93b3681e5.json`](../../sessions/ba/bae69369a4f93b3681e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experimental Setup (§3) 已完成，位于 `docs/paper/experimental_setup.tex`。

**章节结构**（~900 words，符合预算）：
- §3.1 Tasks and Datasets — Few-NERD/FewRel/MAVEN 三数据集 + 统计表
- §3.2 SCS — pairwise SCS 和 BCS 的形式化定义，Qwen3 (5120-d) + MiniLM (384-d) 双 embedding
- §3.3 Experimental Design — Exp1 count curves + Exp2 BCS-controlled factorial
- §3.4 Evaluation Metrics — text-match F1 (NER), accuracy (RE), relaxed F1 (ED) + 跨任务 metric 差异 justification
- §3.5 Model and Inference — Qwen3-32B-FP8, vLLM, prompt v2, greedy decoding, bootstrap CI

**所有数字已与 registry 交叉验证。** 唯一新增编辑：补充 Qwen3 embedding 维度 (5120-d)。

**待注意**：
- MAVEN "8,042 sentences" 来自先前数据探查，registry 仅记录 710 documents / 18,904 mentions — 合理但不可从 registry 直接追溯
- 表中 BCS Range 为 batch 级别范围（包含 Exp1+Exp2 极端 batch），非 pairwise SCS 范围
- D024：当前为单模型版本（Qwen3-32B-FP8），LLaMA-3.1-8B 结果待 exp-012 完成后 patch

---

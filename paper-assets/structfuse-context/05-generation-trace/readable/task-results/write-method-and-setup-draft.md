# write method and setup draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_method-and-setup-draft_20260515T015255_result.json`
- **Structured JSON:** [`b56fe6fe859e22ca018a.json`](../../sessions/b5/b56fe6fe859e22ca018a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入并注册：

**`method_v1.md`** (`art_20260515_ae4280`)
- §3.1 Problem Formulation — contrastive code retrieval 形式化
- §3.2 Structural Information Extraction — CodeQL 2-hop taint tracking、call graph + data-flow graph、reachability 判定、beniget fallback、覆盖率统计（0% timeout, 34% structural rate, 78% Z%, 123/131 repos）
- §3.3 Structure-Aware Negative Mining — 三种策略的数学定义（random/embedding/dataflow）、difficulty gradient、与 BM25 baseline 的关系（top-7 Jaccard 0.30–0.38）
- §3.4 Contrastive Fine-tuning — InfoNCE loss (K=7, τ=0.07)、LoRA setup (r=16)、dual checkpoint (θ\*\_loss + θ\*\_R@1)、early stopping (D026)

**`experiment_setup_v1.md`** (`art_20260515_bba58d`)
- §4.1 Dataset — SWE-smith, 131 repos, 44,173 expanded instances, ~14.3K usable/seed (exact per-seed counts from plan_018)
- §4.2 Models — Qwen (pos_sim=0.986, saturated) vs StarCoder (pos_sim=0.799, healthy), from neg_difficulty_analysis 2048t
- §4.3 Training Configuration — 完整超参表（全部标注 registry 来源），epoch schedule (D026), checkpoint criterion (D036), 18 core runs + 6 BM25 runs, 2×RTX PRO 6000 96GB
- §4.4 Evaluation Metrics — R@{1,5,10} pool_size=50, bootstrap 95% CI, Cohen's d, per-seed consistency

注意：数据源用 SWE-smith（与 registry 和已有 drafts 一致），非 CodeSearchNet。M2 最终结果标记为 `[TBD]`。

---

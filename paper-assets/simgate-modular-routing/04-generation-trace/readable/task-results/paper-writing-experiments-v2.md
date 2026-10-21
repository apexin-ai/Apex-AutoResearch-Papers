# paper writing experiments v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_v2_20260514T085847_result.json`
- **Structured JSON:** [`de9eee2dd4b0b4975d3a.json`](../../sessions/de/de9eee2dd4b0b4975d3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/_project/paper/experiments_draft.md`，已注册为 `art_20260514_dd9866`。

结构概要：

- **§Setup** (~95 words): ScienceWorld 环境、11 tasks / 245 episodes、Qwen2.5-7B-Instruct + vLLM、30 steps
- **§Death Avoidance Decomposition** (~400 words): Δ\_full=+29.60 → Δ\_nd=+2.84, DAF=90.41%; r=0.9698 (p=8.12e-07); label distribution 86/9/150; find-non-living-thing 零死亡例外; measure-melting-point-unknown 高死亡率例证
- **§Baselines** (~200 words): Table 1 (booktabs, 含 CI 和 death rate); oracle degeneracy (96.2% ≈ always-det); keyword routing 结构性失败引用 §3.4
- **§Router Training as Diagnostic** (~280 words): classification head 全退化; implicit router logit 74.5%/79% bal\_acc vs generation 65.36%/51.5% recall; framed as diagnostic finding; [PLACEHOLDER] 留给 ablation-b e2e 结果
- **§Limitations** (~130 words): 单 benchmark、单 LLM、-100 penalty 可能放大 DAF、episode-level 粒度

待填项：Table 1 implicit router 行（等 ablation-b e2e 评估结果）。

---

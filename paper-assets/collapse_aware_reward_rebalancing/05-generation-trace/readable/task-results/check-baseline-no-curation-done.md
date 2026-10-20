# check baseline no curation done

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_baseline_no_curation_done_20260516T154730_result.json`
- **Structured JSON:** [`ab3a407ef305eb76b37e.json`](../../sessions/ab/ab3a407ef305eb76b37e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整 metrics 表格：

---

## carr_baseline_no_curation_01 — 成功 ✓

**配置**: Qwen3-0.6B, 3 generations, 2000 prompts, random 1-of-4 (no curation), 总耗时 ~3.3h

| Metric | Gen 0 | Gen 1 | Gen 2 | Δ (Gen0→2) |
|--------|-------|-------|-------|-------------|
| **Vendi Score** | 105.42 | 108.21 | 108.72 | +3.1% |
| **Mean Quality** | 0.1107 | 0.1099 | 0.1096 | -1.0% |
| **Self-BLEU** | 0.0044 | 0.0067 | 0.0067 | +52% |
| **Perplexity** | 9.19 | 8.76 | 11.18 | +21.7% |
| **Mean NN Distance** | 0.7005 | 0.7121 | 0.7136 | +1.9% |
| **Complexity Mean** | 2.84 | 2.76 | 2.80 | -1.4% |

**观察**:
- Diversity（Vendi Score）略微上升 +3.1%，没有出现 collapse
- Quality 基本持平（微降 1%）
- Perplexity 在 Gen 2 有跳升（+21.7%），可能是 LoRA 过拟合或 distribution shift 的信号
- Self-BLEU 从 Gen 0 到 Gen 1 上升后 Gen 2 稳定，说明重复性有小幅增加但未恶化

---

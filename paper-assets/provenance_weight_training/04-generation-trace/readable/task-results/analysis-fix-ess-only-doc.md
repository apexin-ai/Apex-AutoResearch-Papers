# analysis fix ess only doc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fix_ess_only_doc_20260515T143901_result.json`
- **Structured JSON:** [`7a0473511ea986fe1e95.json`](../../sessions/7a/7a0473511ea986fe1e95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。以下是所有修改点：

| 位置 | 字段 | 原值 | 新值 | 来源 |
|------|------|------|------|------|
| Line 18 | eval_time | 169s | **162s** | `ess_only_seed42_eval.json` (elapsed_seconds: 162.0) |
| Line 35 | Late b* mean | 3.552 | **3.553** | step_metrics.jsonl 计算 (3.5531→四舍五入3.553) |
| Line 43 | uniform eval_loss | 2.872 | **2.873** | registry PPL=17.69 → ln(17.69)=2.873；2.872 与 17.69 不自洽 |

其余数值全部与服务器 JSON 一致：
- ess_only eval_loss 2.8751、PPL 17.728、全部 b* 统计量均正确
- adaptive_fix eval_loss 2.871、PPL 17.65、b* median 0.871、mean 1.399 均与 registry 一致
- grid_b=0.5 eval_loss 2.871、PPL 17.65 与 eval JSON 一致
- 所有 Δ PPL 计算正确

---

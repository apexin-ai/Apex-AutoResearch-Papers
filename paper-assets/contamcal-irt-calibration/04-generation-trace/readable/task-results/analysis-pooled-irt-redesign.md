# analysis pooled irt redesign

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled_irt_redesign_20260515T160100_result.json`
- **Structured JSON:** [`5ff6fc6d9d9d6a1085f8.json`](../../sessions/5f/5ff6fc6d9d9d6a1085f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/eval_data_inventory_pooled_irt.md`。核心发现：

**当前状态**：
- 18/24 aligned eval 已完成（alpha=32），6 个 GPU 全满正在跑 4 个 aligned + 2 个 para_aligned
- 3B 有 3 个 checkpoint 需要 retrain（d025_s42, d100_s42, d100_s123，alpha=16→32，D055）

**Per-benchmark N**：

| | 现在 | 跑完后 | 含α16 | 全部retrain后 |
|---|---|---|---|---|
| MMLU/ARC | 9 | 13 | **16** | **16** |
| GSM8K/HE | 17 | 21 | **24** | **24** |

（0.5B MMLU/ARC 因 D045 position bias 排除）

**推荐方案**：
1. **立即**：用 alpha=16 的 3B evals 凑满 N=16/24，跑 pooled IRT 调试收敛
2. **并行**：retrain 3 个 3B checkpoint（alpha=32）
3. **最终论文**：全部换成 alpha=32 数据 refit

---

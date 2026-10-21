# code placebo bt fix

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_placebo_bt_fix_20260521T140025_result.json`
- **Structured JSON:** [`30bc8ad21975500626a0.json`](../../sessions/30/30bc8ad21975500626a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## Placebo BT Re-analysis（所有 pairs，含 inconsistent）

| Judge | Axis | BT P(original) | 95% CI | p-value | Sign Test Rate | Sign Test p |
|-------|------|:---:|:---:|:---:|:---:|:---:|
| **Qwen3-32B** | formality | **0.3766** | [0.3025, 0.4506] | 0.0006 | 0.2727 (12/44) | 0.0037 |
| **Qwen3-32B** | verbosity | **0.0816** | [0.0351, 0.1397] | 0.0000 | 0.0000 (0/36) | 0.0000 |
| **GPT-4o** | formality | **0.4177** | [0.3418, 0.5000] | 0.0368 | 0.3488 (15/43) | 0.0660 |
| **GPT-4o** | verbosity | **0.1668** | [0.0835, 0.2620] | 0.0000 | 0.0625 (2/32) | 0.0000 |

关键发现：
- **BT 和 sign test 方向一致**，但 BT 使用了全部 pairs（含 inconsistent），所以估计值更高（更接近 0.5）
- GPT-4o formality sign test p=0.066 不显著，但 BT p=0.037 显著——因为 BT 利用了更多数据（inconsistent pairs 也贡献信息）
- Verbosity 两个 judge 都 strongly biased toward DR（BT < 0.17），placebo 严重失败
- Formality 偏差较小但仍显著（BT 0.38-0.42）

产出文件：
- `data/placebo_bt_reanalysis.json` — 汇总结果
- `data/placebo_raw_{judge}_{axis}.json` — 每个 pair 的 raw trial results（可复现）
- `csd_pipeline/placebo_bt_reanalysis.py` — 脚本

---

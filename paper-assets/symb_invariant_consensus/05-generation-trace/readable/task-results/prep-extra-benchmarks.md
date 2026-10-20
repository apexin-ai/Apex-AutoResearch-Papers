# prep extra benchmarks

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_extra-benchmarks_20260516T182544_result.json`
- **Structured JSON:** [`4bdaa7560a1191f38b15.json`](../../sessions/4b/4bdaa7560a1191f38b15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有文件已部署到服务器：

**数据集**（已下载并格式化）：
- `data/arc_challenge_200.json` — 200 题 ARC-Challenge (A/B/C/D 分布: 51/40/65/44)
- `data/strategyqa_200.json` — 200 题 StrategyQA (Yes:87 / No:113)
- `data/math_l45_100.json` — 100 题 MATH L4-5 (各 50 题)

**评估脚本**（`--mode mock` smoke test 全通过）：
- `scripts/eval_arc.py` — 多选答案提取 + 字母匹配
- `scripts/eval_strategyqa.py` — Yes/No 提取 + 匹配
- `scripts/eval_math_l45.py` — 使用 `is_equiv` 数学表达式等价判定，额外输出 Level 4/5 分层指标

**数据准备脚本**（可复现）：
- `scripts/prepare_arc.py`
- `scripts/prepare_strategyqa.py`
- `scripts/prepare_math_l45.py`

所有 eval 脚本支持: `--mode`, `--k`, `--n-problems`, `--temperature`, `--api-base`, `--model`, `--output`, `--resume`。调用 `pipeline.run_single(prob)` 对接现有 SICA pipeline。

---

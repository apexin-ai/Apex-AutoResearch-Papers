# code exp64 confidence script

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp64_confidence_script_20260522T213004_result.json`
- **Structured JSON:** [`e41fed010416f3aaf968.json`](../../sessions/e4/e41fed010416f3aaf968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建：`/root/jailbreak_detect/scripts/exp64_toxicchat_confidence_analysis.py`（256 行）。

功能概要：
- 从 `exp8_raw_predictions.json` 读取 `9class` 和 `jb_mlm` 两个 variant 在 ToxicChat 上的逐样本预测
- **Majority vote**（3 seeds ≥2票判正）+ **per-seed** 两个维度识别 FP（y_pred=1, y_true=0）
- 将 FP 的 jailbreak probability 按三档（0.5–0.7 / 0.7–0.9 / >0.9）统计 count、ratio、mean、median
- 输出：主直方图 PDF、per-seed 直方图 PDF、统计 JSON、stdout 对比表格
- 支持 `--input` 和 `--output_dir` 参数，默认输出到 `results/exp64/`

---

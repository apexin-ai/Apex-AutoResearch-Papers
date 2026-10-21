# ops gsm8k results locate

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-results-locate_20260519T223056_result.json`
- **Structured JSON:** [`80ab969a3f6b70f66b77.json`](../../sessions/80/80ab969a3f6b70f66b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 结果汇总

**GSM8K 结果位置（cqa1）：** `/root/contamcal-irt-calibration/results/gsm8k/`（不在 `eval_results/`，而在独立的 `results/gsm8k/` 目录）

| Dosage | Accuracy | Correct/Total | 状态 |
|--------|----------|---------------|------|
| d000 | 70.58% | 931/1319 | 完成 |
| d100 | 81.65% | 1077/1319 | 完成 |
| d005 | - | - | 运行中（PID 292509，GPU 0，~06:54 完成） |
| d025 | - | - | 排队（d005 后自动启动，~07:22） |
| d050 | - | - | 排队（d025 后自动启动，~07:50） |

**westd 结果文件已创建：**
- `/root/contamcal-irt-calibration/analysis/results/gsm8k/cqa1_aligned/gsm8k_qwen7b_s42_d000.json`
- `/root/contamcal-irt-calibration/analysis/results/gsm8k/cqa1_aligned/gsm8k_qwen7b_s42_d100.json`

**evaluate.py md5:** `001a9bc23f808c47d25ef9eaeecb81f1`（与脚本中 C009 校验值一致）

中间 dosage (d005/d025/d050) 由 `eval_gsm8k_qwen7b_s42_intermediate.sh` 顺序执行，全部预计 ~07:50 CST 完成。

---

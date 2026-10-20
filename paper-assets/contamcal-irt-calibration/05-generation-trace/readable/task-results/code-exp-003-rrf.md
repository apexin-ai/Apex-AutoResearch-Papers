# code exp 003 rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-rrf_20260514T124248_result.json`
- **Structured JSON:** [`c7396db9182f7df680a3.json`](../../sessions/c7/c7396db9182f7df680a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。exp-003 代码已部署并验证完毕。

**产出文件**（`/root/contamcal-irt-calibration/exp003/`）：

| 文件 | 行数 | 功能 |
|------|------|------|
| `rrf_aggregation.py` | 318 | RRF 主聚合脚本，支持单模型/批量/exp-006 exposure 输出 |
| `ablations.py` | 345 | 5 种 ablation：rank_avg, single-signal×4, calibrated RRF, FP injection, degraded 2-signal |
| `evaluate_rrf.py` | 393 | AUC/AP/P@k 评估 + ROC/分布/FP robustness 图表，支持 `--mock` 测试 |
| `README.md` | — | I/O 格式和用法说明 |

**Mock 测试结果**（1000 items, 100 contaminated）：
- RRF AUC=0.9998, rank_avg=0.9987, calibrated_rrf=0.9999
- 单信号 AUC 范围 0.917–0.975
- degraded_2sig AUC=0.979
- FP 20% 注入后 RRF AUC 仍达 0.988，单信号降至 0.87–0.93 → 验证了 RRF 的鲁棒性

**真实数据测试**：成功处理 Qwen2.5-0.5B_d005_s42 的 14042 条 MMLU 信号（目前只有 embedding 一个信号可用，等 exp-002 完成后所有信号都会参与融合）。

---

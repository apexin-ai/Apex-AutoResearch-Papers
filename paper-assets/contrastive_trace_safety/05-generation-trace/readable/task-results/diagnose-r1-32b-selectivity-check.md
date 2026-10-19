# diagnose r1 32b selectivity check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_r1_32b_selectivity_check_20260517T020554_result.json`
- **Structured JSON:** [`a8ca8646894fcaa714fd.json`](../../sessions/a8/a8ca8646894fcaa714fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

两组数据都存在，对应不同 layer：

### Layer 2（旧结果）
- **文件**: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_c2_control/selectivity_results.json`
- **Selectivity**: **16.8pp** (real_acc=67.6%, random_mean=50.8%)
- **Layer**: 2

### Layer 10（corrected best layer，已重新计算）
- **文件**: `/root/autodl-tmp/contrastive_trace_safety/artifacts/report_r1_32b_selectivity_l10.md`
- **脚本**: `/root/autodl-tmp/contrastive_trace_safety/run_selectivity_l10.py`
- **Selectivity**: **7.5pp** (real_acc=58.3%, random_mean=50.8%)
- **Layer**: 10

### 结论

Layer 10 已计算过。R1-32B 在 corrected best layer (10) 上的 selectivity 是 **7.5pp**，远低于旧 layer 2 的 16.8pp。Layer 10 的 real probe accuracy 只有 58.3%，信号很弱，random baseline 的 std 高达 5.1%（有单次 rep 达到 61.3% 超过 real probe）。

论文中应使用哪个数值取决于叙事选择：如果用 M001 corrected best layer 的一致标准，则应报 **layer 10, 7.5pp**。

---

# code write 3seed aggregation script

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write-3seed-aggregation-script_20260520T035301_result.json`
- **Structured JSON:** [`c8aa1173a67728ae7014.json`](../../sessions/c8/c8aa1173a67728ae7014.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好并验证可运行。

`artifacts/aggregate_seeds.py` 功能：
- 读取 N 个 `full_signal_report.json`，按 dataset key 提取 7 个 scaling 指标（lp_rho, sj_rho, vc_rho, degen, construction_lp_delta, greedy_f1, oracle_f1）
- 计算 mean/std（sample std），stdout 输出可直接 paste 到 `plot_scaling_curve.py` 的 DATA dict
- 写 JSON 文件包含 mean、std、per-seed 原始值
- `--per-instance` 选项聚合多 seed 的 per-instance JSON（每个 instance 取均值 F1），degenerate 标记取多数投票，输出兼容 `bootstrap_construction.py`

---

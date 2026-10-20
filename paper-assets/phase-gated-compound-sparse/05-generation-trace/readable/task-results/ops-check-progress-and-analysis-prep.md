# ops check progress and analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_progress_and_analysis_prep_20260514T204225_result.json`
- **Structured JSON:** [`716ed1f1b05c337cc965.json`](../../sessions/71/716ed1f1b05c337cc965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度报告已写入 `artifacts/n500_progress_check.md`。

**关键状态：**
- **4/16 完成**（全部 s015），**4/16 运行中**（全部 s020），**8/16 待启动**（s025、s030）
- 4 GPU 全部在用（76-98% 利用率），Qwen 分别在 246/500 和 227/500
- s020 预计 ~06:30 完成，全部 16 条件预计 ~13:30（服务器时间）
- **s025/s030 不会自动启动**，s020 跑完后需要手动触发
- 分析脚本 `scripts/analyze_c2_n500.py`（788 行）已就绪，支持 median + bootstrap CI + d_z + Wilcoxon，s015 dry-run 验证通过
- 注意 Qwen mid-phase null rate 高达 45.2%，DeepSeek II 偏度极大（6-22），确认 median 优于 mean

---

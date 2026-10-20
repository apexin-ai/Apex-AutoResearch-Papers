# code prep 355m stat analysis

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_355m_stat_analysis_20260514T034717_result.json`
- **Structured JSON:** [`d1e3ef6e63a824112bc4.json`](../../sessions/d1/d1e3ef6e63a824112bc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果：

- **6/12 method-seed combos 已加载**：seed=42 全部 4 方法完整（gen0-7），seed=123 uncurated 跑到 gen6，external 刚开始 gen0
- **seed=42 单 seed gen7 数据**正确匹配任务描述中的数值（uncurated ppl=91.66, rgds=82.84, random_50=70.25, external=77.74）
- **PPL Trajectory** 已在 uncurated/external 对 seed=42+123 做了平均聚合
- **t-test 部分** 因为只有 1 个 common seed 有 gen7，正确跳过（需 ≥3 seeds）
- **C1 ratio** 和 **C3 比较** 在 seed=42 上正确输出
- 脚本能自动发现 per-gen metrics.json（seed=123 格式），3 seed 完成后直接重跑即可出完整统计

脚本位于 `/root/div_cal_verify/analyze_355m_3seed.py`，本地副本在 `artifacts/analyze_355m_3seed.py`。

---

# diagnose plan 006 s42 timeout

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_006_s42_timeout_20260515T114302_result.json`
- **Structured JSON:** [`59a29db7a5469f22620d.json`](../../sessions/59/59a29db7a5469f22620d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息足够了。以下是诊断报告：

---

## plan_006_s42 诊断报告

### 失败原因
**纯超时 (EXIT_CODE=124)**。无其他错误。12h timeout 耗尽时正在执行 gen_18（目录已创建但为空）。

### 完成进度
- **gen_0 ~ gen_17 完整**（共 18 个 generation 的 metrics.json + checkpoint + synthetic_data）
- **gen_18 空目录**，gen_19 未开始
- Registry 只记录到 gen_9，但**磁盘上实际有到 gen_17 的完整数据**，可直接提取

### 关键 metrics 轨迹

| gen | entropy | ECE | ppl | eff_rank | mauve |
|-----|---------|-----|------|----------|-------|
| 0 | 3.234 | 0.011 | 27 | 46.6 | 0.034 |
| 9 | 1.146 | 0.441 | 1,787 | 99.2 | 0.032 |
| 13 | 1.152 | 0.450 | 2,580 | 103.3 | 0.033 |
| 17 | 1.182 | 0.454 | 3,368 | 99.1 | 0.032 |

collapse 信号清晰：entropy 从 3.23→1.18，ECE 0.01→0.45，ppl 爆涨 125x。

### 每 gen 耗时（目录时间戳推算）
- **gen_1 ~ gen_14**: 稳定 ~29-32 min/gen
- **gen_15 ~ gen_17**: 突增至 ~74-83 min/gen（约 2.5x 减速）

减速原因推测：模型退化后生成质量差，合成数据生成/评估阶段耗时增加。

### 完整运行估算
- 12h 完成 18/20 gen，剩 2 gen 按 ~80 min/gen 估算还需 ~2.5h
- **完整 20 gen 需约 14.5h → 建议 timeout_hours=16**

### 已有数据可用性
- **T=18 时间序列（gen_0-17）已超过原计划的 T=15**，完全足够做 TY power analysis
- 无需等 20 gen 就可以开展统计检验
- 建议先将 gen_10 ~ gen_17 的 metrics 补注册到 registry

### 续跑可行性
- 代码**无 resume 机制**（无 skip/resume 逻辑），重跑会从 gen_0 重新开始
- 从 checkpoint 续跑需改代码添加 `--resume_from_gen` 参数

### 建议
1. **优先方案：直接用 gen_0-17 的 18 个点做分析**，T=18 > T=15，数据充足
2. 若必须要 20 gen 完整数据：增加 timeout 到 16h 重跑，但成本是再花 14.5h GPU 时间
3. 补注册 gen_10-17 的 metrics 到 registry，避免数据遗漏

---

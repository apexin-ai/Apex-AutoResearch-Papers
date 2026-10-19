# analysis bootstrap n2000 check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-n2000-check_20260522T045940_result.json`
- **Structured JSON:** [`f2162773c5fb26faaa19.json`](../../sessions/f2/f2162773c5fb26faaa19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the current status:

## Bootstrap n=2000 状态

**进行中。** 两个任务（Qwen + Llama）均在 12:42 启动，目前还在第 1/4 方向（EN→EN）。

| 信息 | 值 |
|------|------|
| 服务器 CPU | 208 核，负载 201.7 |
| Qwen 数据 | train=(798, 36, 4096), 2000 bootstraps, 64 workers |
| Llama 数据 | train=(1096, 32, 4096), 2000 bootstraps, 64 workers |
| 并行竞争 | 另有 3 个 xnli probe 训练也在跑 |

**预估完成时间**：每方向 ~25-40 分钟，4 方向/模型，共 ~100-160 分钟。预计 **14:30-15:30** 完成。

### n=100 参考结果（已确认）

| 模型 | EN→EN | ZH→ZH | EN→ZH | ZH→EN | 不对称性 | 95% CI | positive |
|------|-------|-------|-------|-------|---------|--------|----------|
| Qwen | 0.7528±0.0168 | 0.7162±0.0179 | 0.6496±0.0273 | 0.7215±0.0256 | +7.18pp | [-1.2%, 13.4%] | 96/100 |
| Llama | 0.7710±0.0119 | 0.7124±0.0127 | 0.6405±0.0245 | 0.7127±0.0270 | +7.22pp | [1.1%, 13.6%] | 98/100 |

结果出来后需要运行的不对称性计算逻辑已确认——直接从 `per_bootstrap` 数组计算 ZH→EN - EN→ZH 的差值分布和 percentile CI，不需要 `bootstrap_asymmetry.py`（那个脚本做的是固定 probe + resample test set 的 bootstrap，和当前方法不同）。

需要我设置定时检查，还是稍后手动回来看？

---

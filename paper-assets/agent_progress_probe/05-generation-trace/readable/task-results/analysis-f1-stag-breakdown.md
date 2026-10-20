# analysis f1 stag breakdown

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-breakdown_20260514T151440_result.json`
- **Structured JSON:** [`ec221154d825aaf898c6.json`](../../sessions/ec/ec221154d825aaf898c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## outcome-bp-3seed (移除 OB, 3-LF full test 8101w)

| Seed | f1_stag | f1_prog | macro_f1 | precision_stag | recall_stag |
|------|---------|---------|----------|----------------|-------------|
| 42   | 0.6003  | 0.898   | 0.7491   | **0.9286**     | 0.4435      |
| 123  | 0.6396  | 0.8961  | 0.7679   | 0.8304         | 0.5202      |
| 456  | 0.6828  | 0.904   | 0.7934   | 0.8377         | 0.5762      |
| **Mean** | **0.6409 ± 0.034** | 0.899 | 0.770 ± 0.018 | | |

**核心发现**: stagnation 检测退化主要来自 **recall 暴跌**（0.44-0.58），precision 仍高（0.83-0.93）。模型学会了高置信才预测 stagnation，但大量 stagnation 窗口被漏判为 progress。

## train-without-ob

| 测试集 | f1_stag | f1_prog | macro_f1 |
|--------|---------|---------|----------|
| 自身 2-LF test (1519w) | **0.9159** | 0.9862 | 0.951 |
| 3-LF full test (8101w) | **0.5667** | 0.8371 | 0.7019 |

## Full baseline (3-LF)
- f1_stag=**0.7772**, macro_f1=0.8468

## OB 移除效应
- f1_stag: 0.7772 → 0.6409 (**-13.6pp**, 3-seed)
- 主要机制：recall_stag 从 0.77 降到 ~0.51，OB 提供的 stagnation 信号无法被 cmd_rep + file_diff 替代

## f1_stag=0.000 溯源
**0.000 从未被实际计算过。** 服务器上所有结果文件均无 f1_stag=0.000 的输出：
- 最接近的低值：without_ob 在 OB-only 窗口子集（687w）上的 f1_stag=0.5109
- INVALIDATED sensitivity 报告中 OB-contributed 子集的 f1_stag=0.4869
- 最可能来源：内部讨论中对 "2-LF 模型在 OB 覆盖区域表现差" 的过度简化，被错误传播为 "f1_stag=0.000"
- D025/D026 的撤回是正确的

结果已保存到服务器 `/root/autodl-tmp/agent_progress_probe/f1_stag_breakdown.json`。

---

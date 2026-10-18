# diagnose exp fewrel 16rel bootstrap

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_fewrel_16rel_bootstrap_20260516T015515_result.json`
- **Structured JSON:** [`af293e900ef01a864d4c.json`](../../sessions/af/af293e900ef01a864d4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D033 诊断结果

**实验已完成**，于 2026-05-16 09:40:20 正常结束。

### 完成情况
- 100/100 batches 全部完成
- 每 batch 496 samples，共 49600 次推理
- vLLM engine 已正常 shutdown

### 核心结果
| 指标 | 值 |
|------|-----|
| mean_accuracy | 0.8515 |
| delta_BCS (low vs high) | **-7.42pp** &nbsp; 95% CI [-9.45, -4.49] |
| Low BCS (Q1, n=26) acc | 0.8975 |
| High BCS (Q4, n=33) acc | 0.8233 |
| Amplification ratio (16→80) | **4.20x** &nbsp; 95% CI [3.30, 6.95] |
| Pearson r(BCS, acc) | -0.6373 |

### GPU 状态
- **GPU 空闲**，无计算进程占用显存
- 有一个 `test_ner_prompt.py` 进程在跑（PID 310564, 01:40 启动），但未占用 GPU
- 后续 80-pool 实验可以立即启动

---

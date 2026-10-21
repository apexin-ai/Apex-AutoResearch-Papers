# ssh final harvest 3dir

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_final-harvest-3dir_20260523T032139_result.json`
- **Structured JSON:** [`64ac3f5c6215fe5eaedc.json`](../../sessions/64/64ac3f5c6215fe5eaedc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 实验状态 (bjb1-32546)

| 实验 | 状态 | Overall SR |
|------|------|-----------|
| CRM norm=0.3 | **INCOMPLETE** (T10 rollout 10/20 被杀) | ~73.9% (9 tasks) |
| CRM norm=0.1 | **DONE** | **79.0%** |
| CRM norm=0.05 | **DONE** | **80.0%** |
| Adaptive CRM | **DONE** | **81.0%** |
| Reconvla K=10 | **DONE** | **79.0%** |
| CRM 4-suite training | **RUNNING** (PID 548658) | — |

norm03 进程在最后一个 task (wooden_cabinet) rollout 10/20 处被杀，无 JSON 输出。可能被 11:24 新启动的实验（adapt_tau015/025/035, crm_norm02, obj_crm005）挤掉了。

### 最终对比表

| Mode | K | norm | SR | vs VLA-only (78.5%) |
|------|---|------|----|---------------------|
| VLA-only K=1 | 1 | — | 78.5% | baseline |
| CRM norm=0.3 | 10 | 0.3 | ~73.9%† | ~-4.6pp |
| CRM norm=0.1 | 10 | 0.1 | 79.0% | +0.5pp |
| CRM norm=0.05 | 10 | 0.05 | 80.0% | +1.5pp |
| **Adaptive CRM** | **2→5** | **0.2** | **81.0%** | **+2.5pp** |
| Reconvla K=10 | 10 | — | 79.0% | +0.5pp |

### 关键发现

1. **Adaptive conformal CRM 最优**：81.0%，trigger_rate=91.8%，confidence-gated 避免有害修正
2. **CRM norm=0.05 次优**：80.0%，修正量足够小不会伤害
3. **Reconvla 是强 baseline**：79.0%，无需学习组件
4. **norm=0.3 仍然过激**：T9 从 80%→55%（-25pp），T7 从 100%→80%（-20pp）
5. **T6 (on_ramekin) 全军覆没**：6 种方法均 0/20

完整 task-level breakdown 已写入 `artifacts/3dir_spatial_s42_results.md` 并注册。

---

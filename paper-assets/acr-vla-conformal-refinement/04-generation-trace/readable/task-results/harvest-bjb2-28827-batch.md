# harvest bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-batch_20260525T174412_result.json`
- **Structured JSON:** [`7ba74f1239a59609391a.json`](../../sessions/7b/7ba74f1239a59609391a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完毕。汇总结果。

---

## bjb2-28827 实验状态汇总

### 当前 GPU 使用

| GPU | 实验 | 模型 | Mode | Benchmark | Seed | 状态 |
|-----|------|------|------|-----------|------|------|
| 0 | eval-pi05-crm-long-s42 | π0.5 | CRM | Long | 42 | 刚启动，加载环境中 |
| 1 | eval-pi05-crm-long-s43 | π0.5 | CRM | Long | 43 | 刚启动，加载环境中 |
| 2 | eval-crm-long-s44-d149 | SmolVLA | CRM | Long | 44 | 运行中，task 7/10 |
| 3 | eval-pi05-crm-spatial-s42 | π0.5 | CRM | Spatial | 42 | 刚启动，加载环境中 |
| 4 | eval-pi05-crm-spatial-s43 | π0.5 | CRM | Spatial | 43 | 刚启动，加载环境中 |
| 5 | eval-adaptive-long-s43-d149 | SmolVLA | Adaptive | Long | 43 | 运行中，task 7/10 |

> GPU 0/1/3/4 的 4 个 π0.5 CRM 实验是别的 session 在 01:42 新启动的，不是用户列表中的原始实验。

### 用户列表中的实验结果

| exp_id | GPU(原) | 实际状态 | SR | 备注 |
|--------|---------|---------|-----|------|
| eval-pi05-vla-only-goal-s44 | cuda:5 | **DONE** | **0.975** | 已收割 |
| eval-pi05-vla-only-object-s43 | cuda:3 | **DONE** | **0.985** | 已收割 |
| eval-pi05-adaptive-goal-s43 | cuda:1 | **KILLED** | — | 跑到 task 3/10 被杀，需重跑 |
| eval-pi05-adaptive-object-s42 | cuda:2 | **KILLED** | — | 跑到 task 2/10 被杀，需重跑 |
| eval-pi05-adaptive-object-s43 | cuda:4 | **KILLED** | — | 跑到 task 2/10 被杀，需重跑 |
| eval-adaptive-long-s42-d149 | cuda:3 | **DONE** | **0.58** | SmolVLA, trigger_rate=4.3% |
| eval-adaptive-long-s44-d149 | cuda:4 | **DONE** | **0.54** | SmolVLA, trigger_rate=4.5% |

### "可能已完成" 的实验

| exp_id | 实际状态 | SR | 备注 |
|--------|---------|-----|------|
| eval-pi05-crm-goal-s42-d149 | RUNNING(registry) | — | 服务器上无任何运行证据 |
| eval-pi05-crm-goal-s43-d149 | RUNNING(registry) | — | 同上 |
| eval-pi05-crm-goal-s44-d149 | RUNNING(registry) | — | 同上 |
| eval-pi05-crm-spatial-s42-d149 | RUNNING(registry) | — | -d149 版本无证据；非 d149 版本刚在 GPU3 启动 |
| eval-pi05-crm-spatial-s43-d149 | RUNNING(registry) | — | -d149 版本无证据；非 d149 版本刚在 GPU4 启动 |
| eval-pi05-adaptive-goal-s44 | RUNNING(registry) | — | 无任何运行证据 |
| eval-pi05-crm-object-s42 | RUNNING(registry) | — | 无任何运行证据 |

### 额外收割的 SmolVLA 结果（同服务器完成）

| exp_id | Mode | Benchmark | Seed | SR |
|--------|------|-----------|------|----|
| eval-smolvla-crm-goal-s42 | CRM | Goal | 42 | **0.83** |
| eval-crm-long-s42-d149 | CRM | Long | 42 | **0.565** |

### 关键发现

1. **GPU 冲突不存在** — 原来 cuda:3/4 上的实验都已结束或被杀，当前无冲突
2. **3 个 π0.5 Adaptive 实验被杀**（Goal s43, Object s42/s43），需要重新安排
3. **7 个 "可能已完成" 的实验** 在 bjb2-28827 上没有任何运行或结果的证据，可能从未在这台机器上启动过，或在其他服务器
4. **4 个新的 π0.5 CRM 实验**（long s42/s43, spatial s42/s43）刚在 01:42 被其他 session 启动
5. **2 个 SmolVLA Long 实验**（CRM s44, Adaptive s43）还在跑，预计几小时内完成

---

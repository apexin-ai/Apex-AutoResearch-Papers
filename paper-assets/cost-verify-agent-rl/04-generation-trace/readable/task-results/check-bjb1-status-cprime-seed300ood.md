# check bjb1 status cprime seed300ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_status_cprime_seed300ood_20260522T184844_result.json`
- **Structured JSON:** [`ac60b44bffb9f3128816.json`](../../sessions/ac/ac60b44bffb9f3128816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. seed300 OOD eval v2

- **状态**: Running（PID 442738，已运行 ~10 分钟）
- **进度**: 仍在初始化阶段——模型已加载，数据已 tokenize (341 items)，W&B run `wi55yhp9` 已创建，但 **尚未开始生成 rollout**（日志末尾停在 FSDP 加载完成）
- **GPU**: cuda:0 占用 100%, 56.4/97.9 GB 显存

### 2. C' resume (exp029) step 6-7 metrics

| 指标 | Step 6 (train) | Step 7 (train) | Step 5 初始 val | Step 7 最终 val |
|------|---------------|----------------|-----------------|-----------------|
| **success** | **31.25%** | **16.41%** | **21.88%** | **18.75%** |
| response_length | 4685.5 | 5391.0 | 6891.9 | 7020.4 |
| pass@8 (train) | 68.75% | 62.50% | — | — |
| action_is_valid | 71.2% | 70.4% | 63.0% | 70.5% |
| num_actions | 37.7 | 44.3 | 39.5 | 42.0 |

趋势：train success 从 step 6 的 31.25% 跌至 step 7 的 16.41%，val success 从初始 21.88% 降至 18.75%。conclusion=negative 合理。

### 3. global_step_7 checkpoint

存在：`/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_7/actor/`

### 4. 磁盘

`/root/autodl-tmp`: **222G / 250G (89%)**，剩余 29G。偏紧。

---

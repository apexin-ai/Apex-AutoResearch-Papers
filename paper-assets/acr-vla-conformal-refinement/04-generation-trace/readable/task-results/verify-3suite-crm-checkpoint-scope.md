# verify 3suite crm checkpoint scope

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_3suite-crm-checkpoint-scope_20260528T042002_result.json`
- **Structured JSON:** [`1175b8f55742ac57b924.json`](../../sessions/11/1175b8f55742ac57b924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

证据已完整。以下是结论：

---

## 结论

### 1. `crm_smolvla_3suite_v1` 训练了哪些 benchmark？

**object + spatial + goal，不包含 long。**

### 2. 证据来源

| 证据 | 详情 |
|------|------|
| pi05 3suite 训练 log | `train-crm-pi05-unified-3suite-r2.log` 首行明确记录 `benchmark: ['object', 'spatial', 'goal']` |
| 4suite 训练 log 对比 | `train-crm-unified-4suite.log` 记录 `benchmark: ['object', 'spatial', 'goal', 'long']`，224,555 samples |
| eval log 交叉验证 | 3suite checkpoint = 327,198 params；4suite = 337,438 params，参数量不同 |
| crm-always-on eval log | `crm-always-on-object-s42.log` 确认使用 `crm_smolvla_3suite_v1/crm_best.pt` |
| evaluate.py:541 | 默认 checkpoint 硬编码为 `crm_smolvla_3suite_v1` |

### 3. 是否存在 4suite checkpoint？

**存在。** `/root/autodl-tmp/checkpoints/crm_unified_4suite/`（May 22 创建，比 3suite v1 更早），训练数据：
- object: 14,570 + spatial: 12,167 + goal: 61,728 + long: 136,090 = **224,555 samples**

但 SmolVLA 的 `crm-always-on-*` 主实验**没有使用 4suite checkpoint**，用的是 3suite。

### 4. 论文 claim 准确性判断

如果论文写 **"4 suites (40 tasks, ~224K samples)"** 来描述 CRM 训练：

- **"~224K samples" — 错误**：3suite 实际只有 ~88K samples（14,570 + 12,167 + 61,728）
- **"4 suites" — 部分错误**：CRM 训练只用了 3 suites（object/spatial/goal）；long 虽然有评估（`crm-always-on-long-s42~s45`），但 CRM 并未在 long 数据上训练——这实际上是 **cross-suite zero-shot 泛化**，而非 in-distribution evaluation
- **"40 tasks" — 错误**：3 suites 只有 30 tasks（每 suite 10 tasks）

**需要修正论文表述**，明确区分 CRM 训练范围（3 suites, 30 tasks, ~88K samples）和评估范围（4 suites, 40 tasks），并将 long 上的结果标注为 cross-suite generalization。

---

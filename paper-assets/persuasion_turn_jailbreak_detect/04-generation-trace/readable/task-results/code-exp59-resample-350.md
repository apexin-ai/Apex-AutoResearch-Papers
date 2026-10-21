# code exp59 resample 350

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp59_resample_350_20260522T132529_result.json`
- **Structured JSON:** [`79916d10b13a80082ad7.json`](../../sessions/79/79916d10b13a80082ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交到 westd-33183 的 cuda:0，3 个 seed (42, 123, 456) 依次运行。每个 seed 包含：
- Stage 1: DeBERTa 9-class DAPT (5 epochs, ~350 samples)
- Stage 2: GRU treatment (20 epochs)
- Stage 3: DD OOD + AA OOD 评估

**已知对比基准：**

| 配置 | DD OOD F1 | AA OOD F1 |
|------|-----------|-----------|
| original_349 (plan_002) | ~0.42 avg* | ~0.22 avg* |
| expanded_1000 (exp17) | 0.889 ± 0.04 | 0.913 ± 0.04 |
| resample_350 (exp59) | *running...* | *running...* |

*\*exp16 的 DD/AA OOD 评估格式不同（不含 benign），数据不完全可比*

3 分钟后自动检查进度。

---

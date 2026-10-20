# analysis mf2 statistical tests v3

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mf2-statistical-tests-v3_20260518T093330_result.json`
- **Structured JSON:** [`9c771a746b6e8d1dd088.json`](../../sessions/9c/9c771a746b6e8d1dd088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**McNemar's test (DD OOD, n=118)**

| 比较对 | K=1 | K=2 |
|--------|-----|-----|
| 9class vs scrambled | p=1.0 (b=1,c=0) | p=0.1306 (b=6,c=1) |
| 9class vs binary | p=1.0 (b=0,c=0) | p=1.0 (b=0,c=1) |
| scrambled vs binary | p=1.0 (b=0,c=1) | **p=0.0412** (b=0,c=6) |

K=2 时 scrambled vs binary 差异显著 (p<0.05): binary 正确了 6 个 scrambled 错误的样本，反向为 0。其余对比均不显著。

**Bootstrap 95% CI for F1**

| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| 9class | 1.0 [1.0, 1.0] | 0.994 [0.980, 1.0] | 0.994 [0.980, 1.0] | 1.0 [1.0, 1.0] | 1.0 [1.0, 1.0] |
| scrambled | 0.994 [0.980, 1.0] | 0.961 [0.925, 0.988] | 0.954 [0.917, 0.985] | 0.994 [0.979, 1.0] | 0.994 [0.979, 1.0] |
| binary | 1.0 [1.0, 1.0] | 1.0 [1.0, 1.0] | 0.994 [0.980, 1.0] | 1.0 [1.0, 1.0] | 1.0 [1.0, 1.0] |

scrambled 在 K=2,3 的 CI 明显偏低且不包含 1.0，与 9class/binary 的 CI 存在分离。

注意：binary 使用的是 `mf1_binary_seed456` (seed=456)，因为 `plan_013_binary` (seed=42) 的 checkpoint 已被删除。

---

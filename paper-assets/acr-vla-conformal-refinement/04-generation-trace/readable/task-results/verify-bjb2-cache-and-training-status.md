# verify bjb2 cache and training status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb2-cache-and-training-status_20260514T181357_result.json`
- **Structured JSON:** [`a260965c383dace2c4bc.json`](../../sessions/a2/a260965c383dace2c4bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. bjb2 `/root/autodl-tmp/crm_cache/` — **6D (v4 旧 cache)**

manifest.json 明确写 `action_dim: 6`，tensor shape 验证一致：
- `k_samples`: `[2402, 10, 5, 6]` — 最后一维 **6**
- `expert_actions`: `[2402, 5, 6]` — 最后一维 **6**

**这是 v4 旧版（D016 修复前），不是 v5 的 8D。**

### 2. bjb2 `crm_cache_v5/` — **不存在**

`/root/autodl-tmp/crm_cache_v5/` 不存在。

### 3. 三个 CRM v3 训练进程 — **全部存活**

| PID | 任务 | 运行时间 | 状态 |
|-----|------|---------|------|
| 181668 | crm-train-v3-perdof | 9m32s | Ss+ |
| 181896 | crm-train-v3-scalar-unc | 9m25s | Ss+ |
| 181973 | crm-train-v3-obs-only | 9m24s | Ss+ |

三个都在用 `--cache_dir /root/autodl-tmp/crm_cache/`，即 6D v4 cache。**这三个训练无效。**

### 4. eval-vla-mean-spatial PID 143106 — **存活**

运行 15h4m43s，状态 S（sleeping），仍在执行。

### 结论

bjb2 上的 crm_cache 是 6D v4 版本，三个正在跑的 CRM v3 训练全部基于错误的 cache，需要 kill。

---

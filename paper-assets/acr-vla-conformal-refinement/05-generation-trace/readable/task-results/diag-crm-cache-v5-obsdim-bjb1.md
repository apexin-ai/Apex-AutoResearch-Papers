# diag crm cache v5 obsdim bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_crm-cache-v5-obsdim-bjb1_20260522T201111_result.json`
- **Structured JSON:** [`bce0c11e251bc8109a89.json`](../../sessions/bc/bce0c11e251bc8109a89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确：

### 1. crm_cache_v5 obs_features shape

| Suite | Shape | obs_dim |
|-------|-------|---------|
| object | [14570, 960] | 960 |
| spatial | [12167, 960] | 960 |
| goal | [61728, 960] | 960 |
| long | [136090, 960] | 960 |

所有 suite 的 manifest.json 也确认 `obs_dim: 960`。

### 2. CRM checkpoint 第一层 input_dim

- **r4**: `net.0.weight` shape = [256, **990**]（= 960 obs + 30 action = 960 + 5×6）
- **r5**: NOT FOUND（checkpoint 不存在）
- 无 config.json 文件

### 3. 结论

**obs_dim = 960，来自 SmolVLA**，不是 π0.5 (2048)。

CRM r4 的 input_dim=990 = 960(obs) + 30(action=5步×6维) 也验证了这一点。

---

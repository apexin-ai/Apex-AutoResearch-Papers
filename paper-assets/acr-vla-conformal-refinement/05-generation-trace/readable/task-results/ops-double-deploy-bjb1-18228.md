# ops double deploy bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_double-deploy-bjb1-18228_20260518T165013_result.json`
- **Structured JSON:** [`72c8ca0cb734439031ad.json`](../../sessions/72/72c8ca0cb734439031ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结：

**`eval-obs-only-object-norm003-seed46`** — GPU1 上已启动并运行，registry 状态 RUNNING。

**`eval-random-selection-object-seed46`** — 启动失败。`evaluate.py` 不支持 `--mode random_selection`。可用的 mode 为：
`vla_only | crm_scalar | crm_perdof | acr_vla | crm_obs_only | reconvla | direct_correction | crm_k1_accg`

请确认 random selection baseline 应该用哪个 mode，或者是否需要先在代码中实现 `random_selection` mode。

---

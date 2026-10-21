# ops fix eval seed

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_seed_20260514T033759_result.json`
- **Structured JSON:** [`bc85c9d0da2cd882ce72.json`](../../sessions/bc/bc85c9d0da2cd882ce72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇总：

| 修改位置 | 原内容 | 新内容 |
|---------|--------|--------|
| 第 7 行（新增） | — | `import random` |
| 第 13 行（新增） | — | `import numpy as np` |
| 第 62 行 | `def run_episode(model, tokenizer, env, max_steps=...)` | `def run_episode(model, tokenizer, env, episode_idx, max_steps=...)` |
| 第 64-69 行（替换原第 62 行的 env.reset） | `obs = env.reset(seed=int(time.time() * 1000) % (2**31), mode="val")` | `random.seed(episode_idx)` / `np.random.seed(episode_idx)` / `torch.manual_seed(episode_idx)` / `torch.cuda.manual_seed_all(episode_idx)` / `obs = env.reset(seed=episode_idx, mode="val")` |
| 第 169 行 | `run_episode(model, tokenizer, env, max_steps=...)` | `run_episode(model, tokenizer, env, episode_idx=ep_i, max_steps=...)` |

每个 episode 现在使用 `seed=ep_i`（episode 0 → seed 0, episode 1 → seed 1, ...），覆盖 Python random、numpy、torch（含 CUDA）以及 ALFWorld 环境 seed，保证完全可复现。

---

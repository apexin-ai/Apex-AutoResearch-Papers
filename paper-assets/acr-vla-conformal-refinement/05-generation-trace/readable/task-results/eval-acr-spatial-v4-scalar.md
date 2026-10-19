# eval acr spatial v4 scalar

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acr-spatial-v4-scalar_20260514T221700_result.json`
- **Structured JSON:** [`07cbc4e4a31127fb0877.json`](../../sessions/07/07cbc4e4a31127fb0877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个问题需要报告：

**1. 代码不一致 (BLOCK)**

| 文件 | bjb2 MD5 | bjb1 MD5 |
|------|----------|----------|
| evaluate.py | `930ce9ad...` | `3efcecbb...` |
| crm.py | `8123b873...` | `bbadaada...` |

**2. Checkpoint 不存在于 bjb2** — `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt` 没有。

**3. GPU 0 未空闲** — PID 199257 正在运行 obs_only eval：
```
python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt
```

---

按指令"验证失败则停止"，暂不启动 eval。可以先做准备工作：

- 同步代码（git pull 或从 bjb1 scp）
- 传输 checkpoint（或在 bjb2 本地训练 scalar_unc CRM ~25min）

是否现在开始同步代码和传输 checkpoint？等 obs_only eval 跑完后再启动 scalar eval。

---

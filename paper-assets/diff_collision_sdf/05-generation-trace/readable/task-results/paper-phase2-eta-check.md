# paper phase2 eta check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_phase2-eta-check_20260528T023045_result.json`
- **Structured JSON:** [`5a76c2a2e0be0fd10bd9.json`](../../sessions/5a/5a76c2a2e0be0fd10bd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了。汇总报告：

---

## Phase 2 s2 λ=0 训练状态

**实际位置**：westd-35807 GPU 2（PID 856471），不是 westd-45947。

| 指标 | 值 |
|------|-----|
| 当前 step | **~19,363 / 30,000** (65%) |
| 训练速度 | **4.64 s/step** |
| 已运行 | ~12h 06min（从 step 10000 resume） |
| 剩余 steps | 10,637 |
| 剩余时间 | **~13h 42min** |
| 预计完成 | **~2026-05-28 16:13 UTC** |

**训练开始时间**：2026-05-27 14:25 UTC（从 step 10000 checkpoint resume，Phase 1 warmup 5000 steps + 初始 10K steps 已完成）

## DDL 可行性分析

| | 时间 (UTC) |
|---|---|
| DDL | 2026-05-28 **12:00** |
| 训练完成 ETA | 2026-05-28 **~16:13** |
| Eval 耗时 | ~4h |
| 全部完成 ETA | 2026-05-28 **~20:13** |

**结论：DDL 不可行。** 训练本身就要到 16:13 UTC 才能完成，比 DDL 晚 4+ 小时。加上 eval 的 4h，总共要到 ~20:13 UTC。

## GPU 1 上的另一个训练

PID 892014 → `/tmp/phase2_stage2_seed0.log`，step ~13,049 / 30,000（43%），ETA 也在 ~16:20 UTC。同样不可行。

## Eval 脚本状态

Eval 脚本已就绪：
- `scripts/eval_pi05_safelibero.py` — 主 eval 脚本
- `scripts/eval_batch.sh` — 批量 eval
- `scripts/eval_lambda01_all_seeds.sh` — lambda=0.1 全 seed eval

脚本不是瓶颈，训练时间才是。

---

# ops verify gpu after kill

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu-after-kill_20260515T215210_result.json`
- **Structured JSON:** [`9a9fb7912f9399fcaf30.json`](../../sessions/9a/9a9fb7912f9399fcaf30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Kill 未成功，4 张 GPU 中有 3 张仍被占用。** 当前状态：

### GPU 显存占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 14597 / 32607 MiB | 76% | **被占用** — rsft_trainer seed44 (PID 258508) |
| cuda:1 | 18817 / 32607 MiB | 72% | **被占用** — eval inference plan_011 (PID 254077) |
| cuda:2 | 15167 / 32607 MiB | 41% | **被占用** — rsft_trainer seed45 (PID 257192) |
| cuda:3 | 0 / 32607 MiB | 0% | **空闲** ✓ |

### 活跃进程

| PID | GPU | 任务 |
|-----|-----|------|
| 258508 | cuda:0 | `plan_001_flat_nli_seed44` — rsft_trainer |
| 254077 | cuda:1 | `plan_011_bf16_g8_step_eval` — eval inference checkpoint-50 |
| 257192 | cuda:2 | `plan_001_flat_nli_seed45` — rsft_trainer |

### tmux sessions (3 个)

- `plan_001_flat_nli_seed44`
- `plan_001_flat_nli_seed45`
- `plan_011_bf16_g8_step_eval`

另外有一个已死的残留 tmux 进程 `mvp2_eval_rsft_s43_r2`（PID 194836，无对应 tmux session，无 GPU 占用）。

**cuda:0 和 cuda:3**：cuda:3 已空闲，cuda:0 仍被 seed44 训练占用。如果需要释放 cuda:0，需要 kill PID 258508。

---

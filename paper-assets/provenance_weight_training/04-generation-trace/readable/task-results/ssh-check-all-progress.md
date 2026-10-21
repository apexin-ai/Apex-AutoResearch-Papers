# ssh check all progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_progress_20260517T030449_result.json`
- **Structured JSON:** [`d9f1560b13b1c41ba62d.json`](../../sessions/d9/d9f1560b13b1c41ba62d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-47453
nvidia-smi: [GPU0: 83%, 75007MiB | GPU1: 99%, 57165MiB | GPU2: 99%, 57165MiB | GPU3: 100%, 46019MiB] — 全部在用

| 实验 | GPU | PID存活 | Step/Total | 进度% | 速度 | ETA |
|------|-----|---------|-----------|-------|------|-----|
| random_reweight_v2_seed42 | cuda:0 | ✅ 353995 | 6604/8477 | 78% | 3.21 it/s | ~10 min |

## westd-41312

| 实验 | GPU | PID存活 | Step/Total | 进度% | 速度 | ETA |
|------|-----|---------|-----------|-------|------|-----|
| llama3b_uniform_seed42 | cuda:0 | ✅ 3112 | 3813/6103 | 62% | 5.21 s/it | ~3h19m |
| llama3b_adaptive_seed42 | cuda:1 | ✅ 4005 | 3728/6103 | 61% | 5.41 s/it | ~3h34m |
| batchsize16_nmin8_seed42 | cuda:2 | ✅ 50284 | 7336/8477 | 87% | 3.24 it/s | ~6 min |
| grid_b0_2_seed42 | cuda:3 | ✅ 45224 | 1500/6103 | 25% | 2.10 s/it | ~2h41m |

**备注：**
- westd-47453 另有 3 个 tmux 实验占用 GPU1-3（batch_adaptive_tau_rho06, bs8_auto_nmin, rho02_adaptive_tau09）
- batchsize16_nmin8 和 random_reweight_v2 即将完成（< 10 min）
- llama3b 两个实验（3B 模型）速度约 5.2-5.4 s/it，预计今晚完成

---

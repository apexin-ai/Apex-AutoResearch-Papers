# status westd 47453 check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-47453-check_20260516T161456_result.json`
- **Structured JSON:** [`06009704bca319024ff8.json`](../../sessions/06/06009704bca319024ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

---

## Part 1: 训练进度

All experiments: **max_steps = 6103**, eval every 500 steps, eval takes ~44 min each.

| exp_id | server:gpu | step/total | progress | loss (avg) | status | ETA |
|--------|-----------|-----------|----------|-----------|--------|-----|
| threshold_q07_seed42 | westd-47453:0 | 4999/6103 | **81.9%** | ~2.84 | 🔄 eval@5000 (18min in) | **~2h 43min** |
| rho02_uniform_seed42 | westd-47453:1 | 3999/6103 | 65.5% | ~2.55 | 🔄 eval@4000 (just started) | ~5h 11min |
| batch_adaptive_tau_rho04_seed42 | westd-47453:2 | 2999/6103 | 49.1% | ~2.15 (weighted) | 🔄 eval@3000 (just started) | ~7h 24min |
| threshold_q03_seed42 | westd-47453:3 | 2999/6103 | 49.1% | ~2.70 | 🔄 eval@3000 (15min in) | ~7h 11min |

**ETA 计算依据：** training ~2.66 s/step，每次 eval ~44min。threshold_q07 最快完成，预计 ~03:20 (CST)。

**GPU 状态：** 全部满载
```
GPU 0: 100%, 75007/97887 MiB
GPU 1:  98%, 75007/97887 MiB
GPU 2: 100%, 75007/97887 MiB
GPU 3:  99%, 75007/97887 MiB
```

**磁盘：**
```
/          23G/30G (77%) — 7.1G free
/autodl-tmp 206G/250G (83%) — 45G free
```

---

## Part 2: random_reweight_v2_seed42 就绪确认

✅ **脚本就绪**，全部检查通过：

| 检查项 | 状态 |
|--------|------|
| 脚本存在 | ✅ `/root/provenance_weight_training/scripts/run_random_reweight_v2_seed42.sh` |
| CUDA_VISIBLE_DEVICES=-1 | ✅ 占位符，提交时替换 |
| WANDB_MODE=disabled | ✅ |
| output_dir → 数据盘 | ✅ `/root/autodl-tmp/output/models/random_reweight_v2_seed42` |
| 无 --use_wandb | ✅ |

threshold_q07 预计最先完成（~2h43min），完成后其 GPU 可用于启动 random_reweight_v2。

---

# ops full gpu status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-status-check_20260516T065700_result.json`
- **Structured JSON:** [`4414d731299defecf4b7.json`](../../sessions/44/4414d731299defecf4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**服务器未重启，所有实验正常运行。**

| GPU | 实验 | PID | 状态 | 进度 | ETA | 备注 |
|-----|------|-----|------|------|-----|------|
| cuda:0 | threshold_q07_seed42 | 302159 | ✅ 运行中 | 7116/8477 (84%) | ~7 min | 运行 57 min，速度 3.2 it/s |
| cuda:1 | grid_b0_1_seed42 | 295096 | ✅ 运行中 | 3188/6103 (52%) | ~1h43m | 运行 1h52m，速度 2.12 s/it |
| cuda:2 | contamination_60_tau06_seed42 | 287971 | ✅ 运行中 | 5821/6103 (95%) | ~10 min | 运行 3h32m，即将完成 |
| cuda:3 | threshold_q03_seed42 | 299248 | ✅ 运行中 | 959/6103 (16%) | ~3h02m | 运行 1h17m，b=0 (alpha_eff 高，几乎无 reweight) |

**其他确认：**
- **tau07**: 已完成，`final/` checkpoint 存在于 `/root/provenance_weight_training/output/models/contamination_60_tau07_seed42/`（含 checkpoint-5500, 6000, 6103）
- **random_reweight 脚本**: 已就绪（`run_random_reweight_seed42.sh`，1110 bytes，可执行），使用 `--weighting_method random`，`contamination_ratio 0.4`，`tau 0.8`

**GPU 利用率：** 0=99%, 1=68%, 2=63%, 3=94%，温度 58-66°C，正常。

**预计空闲 GPU 时间线：**
- cuda:2 (tau06) — ~10 min 后空闲
- cuda:0 (q07) — ~7 min 后空闲
- cuda:1 (b0_1) — ~1h43m
- cuda:3 (q03) — ~3h02m

tau06 和 q07 即将完成，random_reweight 可在它们结束后立即启动。

---

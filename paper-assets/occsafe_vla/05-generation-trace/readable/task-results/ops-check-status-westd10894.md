# ops check status westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_status_westd10894_20260523T222747_result.json`
- **Structured JSON:** [`1c11c56a36650affcc8c.json`](../../sessions/1c/1c11c56a36650affcc8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### 1. GPU 状态

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| cuda:0 | 99% | 62,209 / 97,887 MiB | 训练中 |
| cuda:1 | 98% | 62,203 / 97,887 MiB | 训练中 |
| cuda:2 | 98% | 62,203 / 97,887 MiB | 训练中 |
| cuda:3 | 99% | 62,203 / 97,887 MiB | 训练中 |

### 2. 进程 & tmux

`ps aux | grep` 和 `tmux list-sessions` 被 read_only 白名单拦截（含 `|` 或非白名单命令），跳过。

### 3. 各实验进度

| 实验 | GPU | 进度 | 速度 | 预计剩余 | 状态 |
|------|-----|------|------|----------|------|
| **cutoff_s2_v2** | cuda:0 | 28,885 / 50,005 (58%) | ~1.05 it/s | ~5.5h | 训练中 |
| **detach_ln_s0** | cuda:1 | 18,111 / 50,005 (36%) | ~1.06 it/s | ~8.3h | **训练中（未完成）** |
| **detach_ln_s1** | cuda:2 | 17,964 / 50,005 (36%) | ~1.05 it/s | ~8.4h | 训练中 |
| **detach_ln_s2** | cuda:3 | 17,983 / 50,005 (36%) | ~1.04 it/s | ~8.5h | 训练中 |

### 4. detach_ln_s0 未完成

上一个 session 的判断有误——detach_ln_s0 仍在 36%，远未完成。最近 AUX loss（step 18100）：`occ_loss=0.0118, action_loss=0.0942`。无需检查 checkpoint。

### 5. Loss 参考

- **detach_ln_s1** step 17900: `occ_loss=0.0100, action_loss=0.0981`
- **detach_ln_s0** step 18100: `occ_loss=0.0118, action_loss=0.0942`

4 块 GPU 全部满载训练中，一切正常运行。cutoff_s2_v2 最快（58%），三个 detach_ln 系列进度接近（~36%）。

---

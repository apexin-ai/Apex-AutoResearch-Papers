# ops kill overrun and close registry

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-overrun-and-close-registry_20260527T172152_result.json`
- **Structured JSON:** [`9077de70f65988736206.json`](../../sessions/90/9077de70f65988736206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

### 1. 进程终止确认

| 实验 | PID | 状态 |
|------|-----|------|
| exp_walker_008f_s0 | 637987 (主) + 637992 (GPU子) | 已 force kill，GPU 已释放，tmux session 已清理 |
| exp_cheetah_008a_s0 | 637656 | 进程早已自然退出 |

### 2. 105K eval 数据完整性

**exp_walker_008f_s0** — 数据完整，与 Director 预期一致：

| 指标 | 值 |
|------|-----|
| eval_return_105K | **139.54** (预期 139.5 ✓) |
| civo/ve_ratio_105K | **0.996** (预期 0.996 ✓) |
| value_mean_105K | 138.94 |
| civo_alert | 0 |
| eval_return_peak | 342.92 @ 95K |

实验超跑到 step 112K，但 105K eval 数据完整记录。NVE < 2.0 符合假设（dt_embed_dim=0 不触发 CIVO）。

### 3. Registry 关闭确认

| 实验 | status | conclusion |
|------|--------|------------|
| exp_walker_008f_s0 | **DONE** | **success** |
| exp_cheetah_008a_s0 | DONE | success（已提前关闭） |

### 4. Cheetah 情况

exp_cheetah_008a_s0 **无问题**——进程已自然结束，registry 在之前已被 hook 自动关闭（status=DONE, conclusion=success, eval_return_105K=366.19, NVE=0.449）。

---

# fix 10894 cleanup restart cell4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_10894-cleanup-restart-cell4_20260527T084113_result.json`
- **Structured JSON:** [`9ed6d7509ebe20abcc29.json`](../../sessions/9e/9ed6d7509ebe20abcc29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

### 1. Eval 结果查询

| 实验 | Eval 结果 |
|------|-----------|
| cutoff_45k_s2_v2 | **已找到** — `cutoff_45k_s2_v2_eval`: TSR=0.9, CAR=0.756, collisions=122 |
| reverse_cutoff_s2_v2 | **已找到** — `reverse_cutoff_s2_v2_eval`: status=DONE（训练记录有 metrics: action_loss=0.061, occ_loss=0.0095） |
| full_occ_ln_s0 | **未找到 eval** — registry 中无 eval 条目 |

### 2. 磁盘空间

| | Used | Avail | Use% |
|--|------|-------|------|
| 删除前 | 201G | 50G | 81% |
| 删除后 | 156G | 95G | 63% |

释放 **~45G**（3 个 checkpoint 各 15G）。

### 3. 重启 detach_ln_v2_s0c_r3

- 已在 westd-10894 cuda:2 启动，显存占用 62GB，确认运行中
- 从头训练（seed=42, max_steps=50005）
- Registry 已注册为 RUNNING
- 日志：`/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3.log`

---

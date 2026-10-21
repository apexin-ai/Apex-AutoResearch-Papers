# infra fix occ s1 resume only

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_occ_s1_resume_only_20260521T050118_result.json`
- **Structured JSON:** [`69e15aa0ce008f8f45f0.json`](../../sessions/69/69e15aa0ce008f8f45f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇总报告：

---

## 结果汇总

### 1. s0/s2 未受影响 ✅
| | PID (python) | 状态 |
|---|---|---|
| s0 (cuda:0) | **76998** (未变) | 正常训练 |
| s2 (cuda:2) | **78171** (未变) | 正常训练 |

### 2. s1 新进程
- Wrapper PID: **80825**
- Python PID: **80898**
- GPU 1: 99% 利用率, 62209 MiB

### 3. Resume 日志
Checkpoint 加载成功：
```
Loading checkpoint: .../proprio_projector--17500_checkpoint.pt
Loading checkpoint: .../action_head--17500_checkpoint.pt
Loading checkpoint: .../occ_head--17500_checkpoint.pt
```

### 4. Step 编号
tqdm 和 `[OCC]` 日志显示从 0 开始 — 这是**代码显示 bug，不影响训练**：
- Line 1146 用 `gradient_step_idx`（从 0 开始）打 OCC 日志
- Line 1152 `log_step = resume_step + gradient_step_idx` = 17500 + n（内部正确）
- checkpoint 保存、训练终止、WandB 日志全部使用 `log_step`，下次存档在 step 20000

### 5. 速度
~**1.08 it/s** ✅（稳定后）

### 6. occ_loss
`[OCC] step=500, occ_loss=0.0117, action_loss=0.0918` — occ_loss 在正常范围

### 7. s0/s2 进度与 ETA

| Seed | tqdm step | 内部 log_step | 剩余 steps | ETA |
|---|---|---|---|---|
| s0 | ~553 | 43053 | ~6952 | **~1.8h** |
| s2 | ~512 | 43012 | ~6993 | **~1.8h** |
| s1 | ~553 | 18053 | ~31952 | **~8.2h** |

s0 log: `[OCC] step=500, occ_loss=0.0094, action_loss=0.0942`
s2 log: `[OCC] step=500, occ_loss=0.0094, action_loss=0.0942`

---

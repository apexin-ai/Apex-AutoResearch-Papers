# ssh training progress check loop5

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check-loop5_20260512T223128_result.json`
- **Structured JSON:** [`004bc8f60055c238dba2.json`](../../sessions/00/004bc8f60055c238dba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have complete data. Here's the summary:

---

## 实验 1: repo-level-cls-v4 (home-1x5090)

| 指标 | 值 |
|------|-----|
| **当前 step** | **200 / 6,633** (3.0%) |
| **已用时间** | ~36 min |
| **训练速度** | ~6.89 s/step |
| **每次 eval 耗时** | 776.7s (每 200 步一次) |
| **预估总时长** | ~19.8h (训练 12.7h + eval 33次×12.9min=7.1h) |
| **预估剩余** | **~19.2h** |
| **Checkpoint** | 目录为空 (step 200 eval 刚完成，checkpoint 正在写入) |
| **磁盘** | 4KB (尚无 checkpoint 文件) |

**训练 loss 趋势**:
- step 50: loss=80.21, grad_norm=195.3
- step 100: loss=2.18, grad_norm=62.2
- step 150: loss=1.36, grad_norm=58.0
- step 200: loss=1.42, grad_norm=17.4

**Eval**: eval_loss=**0.0701** (step 200, epoch 0.09)

---

## 实验 2: repo-level-cwm-v9 (seetacloud-westd-4x5090)

| 指标 | 值 |
|------|-----|
| **当前 step** | **200 / 6,633** (3.0%), 正在做 step 200 的 eval (28%) |
| **已用时间** | ~48 min |
| **训练速度** | ~7.88 s/step |
| **每次 eval 耗时** | 730s (每 100 步一次) |
| **预估总时长** | ~27.9h (训练 14.5h + eval 66次×12.2min=13.4h) |
| **预估剩余** | **~27.2h** |
| **Checkpoint** | checkpoint-100 (136MB) |
| **磁盘** | 136MB |

**训练 loss 趋势**:
- step 50: loss=28.20
- step 100: loss=16.35
- step 150: loss=11.20
- step 200: loss=7.73

**Eval**: eval_loss=**0.4337** (step 100, epoch 0.05)

---

## 异常与注意事项

1. **实验 2 eval 开销过大**: eval_steps=100 导致 eval 总时间占 48% (13.4h/27.9h)。如果改成 eval_steps=200，总时间可降至 ~21h，节省 ~7 小时。
2. **实验 1 checkpoint 目录为空**: step 200 eval 刚完成，checkpoint 应正在写入中。如果下次检查仍为空则需排查。
3. **两个实验 loss 都在正常下降**，无训练异常信号。

---

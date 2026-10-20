# ops check all running progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-running-progress_20260514T195214_result.json`
- **Structured JSON:** [`b9002f3d20619178acee.json`](../../sessions/b9/b9002f3d20619178acee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 63% | 13.6/31.8 GB |
| 1 | 75% | 10.6/31.8 GB |
| 2 | 64% | 9.7/31.8 GB |
| 3 | 94% | 16.1/31.8 GB |

---

### 1. mvp2_grpo_ced_lr5e6_r1 (cuda:0, pid=90080) — **运行中**
- **进度**: step 6/200 (3%)
- **速度**: ~111s/step
- **预估剩余**: ~5h58m
- **输出目录**: `/root/autodl-tmp/grpo_ced_lr5e6/` — 空，尚未到第一个 save_steps=20
- **⚠️ 异常**: KL divergence = **2,412,554,396.9** (远超阈值 100)，虽然标记 monitoring only 没有停止，但 KL 爆炸到 24 亿严重异常，大概率导致训练崩溃或无效。建议检查 lr=5e-6 是否过大或初始化问题。

---

### 2. mvp2_eval_ced_kl001_r4_step90 (cuda:1, pid=83207) — **运行中**
- **进度**: 58/62 batches (94%)
- **速度**: ~82s/batch
- **预估剩余**: ~5-6 min
- **状态**: 即将完成

---

### 3. mvp2_eval_ced_kl001_r4_multi (cuda:2, pid=78850) — **运行中**
- **已完成 checkpoint**: 10 ✅, 50 ✅, 60 ✅
- **当前**: ckpt-20 eval 中，46/62 batches (74%)
- **预估剩余 ckpt-20**: ~13 min
- **待 eval**: 30, 40 (ckpt-70, 80 已分给实验 4)
- **预估全部完成**: ~3.5h（ckpt-20 剩 13min + ckpt-30 ~87min + ckpt-40 ~87min）

**已完成 metrics**:

| Checkpoint | F1 | Ign-F1 | Evi-F1 | EDCR | Format |
|------------|-----|--------|--------|------|--------|
| 10 | 0.003 | 0.003 | 0.720 | 0.998 | 99.9% |
| 50 | **0.156** | **0.156** | 0.564 | 0.886 | 99.9% |
| 60 | 0.147 | 0.147 | 0.576 | 0.906 | 100% |

ckpt-10 关系 F1 几乎为零（模型还没学会），ckpt-50 是目前最高点，ckpt-60 略有下降。

---

### 4. mvp2_eval_ced_kl001_r4_ckpt7080 (cuda:3, pid=91681) — **运行中**
- **当前**: ckpt-70 eval 刚启动，模型已加载完毕，inference 0/62
- **预估完成**: ~3h（ckpt-70 ~87min + ckpt-80 ~87min）

---

### 关键发现
1. **KL 爆炸**: 实验 1 (grpo_ced_lr5e6) 的 KL divergence 爆到 24 亿，lr=5e-6 可能过大，这轮训练大概率无效。需要决定是否提前终止。
2. **Eval 矩阵进展顺利**: ckpt-90 eval 即将完成（~5min），ckpt-20 也快完成（~13min）。
3. **ckpt-50 暂时最优**: F1=0.156, 后续 ckpt-60 已略有下降，等 ckpt-90 结果出来可以看完整曲线。

---

# ops d028 full eval sweep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d028-full-eval-sweep_20260514T191357_result.json`
- **Structured JSON:** [`db2f349351201ff28d97.json`](../../sessions/db/db2f349351201ff28d97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D028 全面 Eval 结果

### 进程状态

| GPU | Eval Task | PID | 当前 ckpt | Progress | ETA |
|-----|-----------|-----|----------|----------|-----|
| 0 | step100 | 80799 | ckpt-100 | 48/62 (77%) | ~20 min |
| 1 | step90 | 83217 | ckpt-90 | 31/62 (50%) | ~45 min |
| 2 | multi | 85997 | ckpt-20 | 5/62 (8%) | ~50 min (仅ckpt-20), 剩余 30,40,60,70,80 |
| 3 | high | 81962 | ckpt-60 | 45/62 (73%) | ~21 min (仅ckpt-60), 剩余 70,80,90 |

所有 4 GPU 满载运行，无异常。

### 已完成 Checkpoint 结果

| Step | reward | rel_f1 | Δ vs SFT | evi_f1 | Δ vs SFT | edcr | recall | pred_count | trunc | MVP-2? |
|------|--------|--------|----------|--------|----------|------|--------|------------|-------|--------|
| **SFT** | - | 0.4057 | - | 0.7979 | - | 0.7118 | 0.407 | 18815 | 367 | baseline |
| 10 | - | **0.0030** | **-40.3pp** | 0.7200 | -7.8pp | 0.9983 | 0.003 | 11621 | 24 | FAIL |
| 50 | 1.101 | **0.1563** | **-24.9pp** | 0.5643 | -23.4pp | 0.8858 | 0.117 | 9250 | 11 | FAIL |

### 关键分析

**Step 10**: rel_f1 几乎为零 (0.003)，但 evi_f1=0.720、EDCR=0.998 极高。模型在 GRPO 初期就学会了"好的 evidence 格式"（低 truncation=24 vs SFT=367），但完全丢失了关系抽取能力。pred_count=11621 表明大量无意义的 relation 预测。

**Step 50**: rel_f1 回升到 0.156（仍比 SFT 低 24.9pp），evi_f1 反而从 0.720 降到 0.564。经典的 reward hacking 趋势——reward 在上升（1.101），但两个核心指标都大幅退化。

**趋势令人担忧**: reward↑ 而 rel_f1↓ evi_f1↓，CED reward signal 可能有根本性问题。

### 待决 - MVP-2 判定

**step-90** (reward=1.370, true best) 和 **step-100** (reward=1.195, last) 是最终判定点：
- step-100 ETA: ~20 min（最先出结果）
- step-90 ETA: ~45 min

MVP-2 pass criteria:
- `(CED_Evi-F1 − SFT_Evi-F1) ≥ 2pp` → 需要 evi_f1 ≥ 0.8179
- `CED_F1 ≥ SFT_F1 − 5pp` → 需要 rel_f1 ≥ 0.3557

基于 step 10/50 的退化趋势，**MVP-2 pass 概率很低**。但 step 90 的 reward 显著高于 step 50，仍有翻盘可能。需要等 20-45 min 出结果才能最终判定。

### 冗余工作

cuda:3 (high) 也会跑 ckpt-90，但 cuda:1 (step90) 会先完成。两者都用 `--resume`，后到者会自动跳过。

---

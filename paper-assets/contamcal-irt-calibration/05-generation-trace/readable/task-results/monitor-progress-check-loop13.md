# monitor progress check loop13

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_loop13_20260516T003822_result.json`
- **Structured JSON:** [`8bcea2e5e2792f92e7c6.json`](../../sessions/8b/8bcea2e5e2792f92e7c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the summary:

---

## 实验进度汇总 (2026-05-16 ~08:40 CST)

### GPU 占用

| GPU | PID | 任务 | VRAM | 进度 | 剩余时间 |
|-----|-----|------|------|------|----------|
| **cuda:0** | 642763 + 643167 | eval d100_s123 + **SFT d005_s42_a32** | 9.0+14.3 GB ⚠️ | eval GSM8K 70% / SFT 74% | ~69min / ~63min |
| **cuda:1** | 628668 | **SFT d100_s42_a32_v3** | 13.3 GB | 3780/4159 (91%) | **~27min** |
| **cuda:2** | 652259 | signals v7 d005_s123 | 7.5 GB | mmlu s4: 54% | ~98min |
| **cuda:3** | 655989 | eval d025_v3_s42_aligned | 9.0 GB | elapsed 1h19m | ~60-90min |
| **cuda:4** | 662616 | signals v8 d100_a32_s123 | 7.2 GB | mmlu s4: 7% | ~178min |
| **cuda:5** | 663067 | signals d025_v3_s42 | 7.5 GB | mmlu s4: 14% | ~155min |

### 各实验详情

**1. SFT d005_s42_a32 (cuda:0)** — 2343/3177 steps (74%), 4.50s/step → ETA ~09:42

**2. SFT d100_s42_a32_v3 (cuda:1)** — 3780/4159 steps (91%), 4.28s/step → **ETA ~09:06** (最快完成)

**3. Signals v7 d005_s123 (cuda:2)** — 正在 mmlu (第1/3 benchmark)
- s1 ✅ s2 ✅ s3+s4 并行中
- s4 self-critique: 3767/7021 (54%), 1.29s/it → mmlu剩 ~70min
- 后续 gsm8k (~15min) + arc (~13min) → **总 ETA ~10:17**

**4. Eval d025_v3_s42 (cuda:3)** — 进程确认 (evaluate.py --benchmarks mmlu gsm8k arc_challenge --mc-format aligned)，已跑 1h19min。⚠️ log 文件未出现在 ~/runs/ 下。

**5. Signals d025_v3_s42 (cuda:5)** — mmlu/s4 self-critique: 973/7021 (14%), 1.26s/it → **总 ETA ~11:14**

**6. Eval d100_s123_a32 (cuda:0, 与SFT共享)** — mmlu ✅, GSM8K 925/1319 (70%), 10.5s/it (因共享GPU偏慢) → GSM8K剩 ~69min + arc ~15min → **ETA ~10:04**

**7. Signals v8 (cuda:4)** — d025_s123 三benchmark全✅。当前 d100_a32_s123/mmlu/s4: 519/7021 (7%), 1.39s/it → **ETA ~11:37**

**8. SFT d000_s42_a32** ✅ **已完成** (epoch 1.0, EXIT_CODE=0)

### cuda:0 冲突

**存在。** eval d100_s123 (9.0 GB) + SFT d005_s42_a32 (14.3 GB) = 23.3 GB / 24 GB。两个进程都在跑但 eval GSM8K 速度偏慢（10.5s/it，正常应 ~3s/it）。SFT 未受太大影响（4.5s/step 正常范围）。eval 约 1h 后完成可释放冲突。

### 1-2h 内完成的实验（影响调度）

1. **SFT d100_s42_a32_v3** (cuda:1) — ~27min → 释放 cuda:1
2. **SFT d005_s42_a32** (cuda:0) — ~63min → 释放部分 cuda:0
3. **eval d100_s123** (cuda:0) — ~85min → 彻底释放 cuda:0 冲突
4. **signals v7 mmlu** (cuda:2) — ~70min (但还需 gsm8k+arc，总 ~98min)
5. **eval d025_v3_s42** (cuda:3) — 可能 60-90min

### sim_sweep_v7

- 12/12 条件有结果文件，sweep_summary 有 8 条
- **仍在运行**: 4 个 CmdStan 采样进程活跃中（已跑 ~8.5h，可能是高难度条件如 auc0.9_n100）
- auc0.9_n100 结果文件仅 2303 bytes（其他 ~7000 bytes），可能未完成
- 需关注是否有 chain stuck

---

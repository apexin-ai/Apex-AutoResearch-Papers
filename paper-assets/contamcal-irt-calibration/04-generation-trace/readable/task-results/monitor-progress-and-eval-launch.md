# monitor progress and eval launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress-and-eval-launch_20260519T140922_result.json`
- **Structured JSON:** [`8ba80ee98313d6343e21.json`](../../sessions/8b/8ba80ee98313d6343e21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full status report:

---

## 训练进度

| GPU | 模型 | 当前 dosage | 步数 | 进度 | 速度 | d000 剩余 | 全 sweep 预估完成 (UTC) |
|-----|------|------------|------|------|------|-----------|------------------------|
| cuda:0 | Phi-4 14.7B | d000 | 726/3125 | 23% | ~2.4s/step | ~95 min | ~09:15 May 20 |
| cuda:1 | Qwen-14B | d000 | 562/3125 | 18% | ~3.15s/step | ~135 min | ~13:00 May 20 |
| cuda:2 | OLMo-2-7B | d000 | 917/3125 | 29% | ~1.84s/step | ~68 min | ~06:40 May 20 |
| cuda:3 | Gemma-2-9B | d000 | 597/3125 | 19% | ~2.96s/step | ~125 min | ~12:00 May 20 |

数据量（steps per dosage, effective batch=16）：d000=3125, d005=3177, d025=3384, d050=3642, d100=4159 → 每个 sweep 共 17,487 步。

## 已完成 dosages
- **Qwen-7B s123**: d000 ✓ d005 ✓ d025 ✓ d050 ✓ d100 ✓ （全部完成，预有）
- Phi-4 s123: 全部 pending（d000 训练中）
- Qwen-14B s123: 全部 pending（d000 训练中）
- OLMo-2-7B s123: 全部 pending（d000 训练中）
- Gemma-2-9B s123: 全部 pending（d000 训练中）

## Eval 启动
- **未启动** — 所有 4 个 tmux session 仍在运行，所有 GPU 占用中
- 4 个 eval 脚本已就位：`eval_phi4_s123.sh`, `eval_qwen14b_s123.sh`, `eval_qwen7b_olmo2_s123.sh`, `eval_gemma2_s123.sh`

## 预估时间线
1. **cuda:2 OLMo-2** 最先完成 ~06:40 UTC May 20 → 启动 `eval_qwen7b_olmo2_s123.sh`（先 eval Qwen-7B 5 dosages，再 OLMo-2 5 dosages）
2. **cuda:0 Phi-4** ~09:15 UTC May 20 → 启动 `eval_phi4_s123.sh`
3. **cuda:3 Gemma-2** ~12:00 UTC May 20 → 启动 `eval_gemma2_s123.sh`
4. **cuda:1 Qwen-14B** ~13:00 UTC May 20 → 启动 `eval_qwen14b_s123.sh`

训练均处于第 1 个 dosage (d000) 的 ~18-29%，距完成还有 8-15 小时。训练看起来健康（loss 正常下降，无报错）。

---

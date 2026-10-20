# research eval progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval-progress-check_20260516T004951_result.json`
- **Structured JSON:** [`f681f8fc151bc2814555.json`](../../sessions/f6/f681f8fc151bc2814555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整梳理完毕。汇总如下：

## GPU 任务状态总览

| GPU | PID | 任务 | 进度 | 速度 | 预估剩余 | 预计完成 |
|-----|-----|------|------|------|---------|---------|
| **cuda:0** | 642763 | eval d100_a32_s123 (mmlu/gsm8k/arc/humaneval, aligned) | 未知（无结果产出） | — | 未知 | — |
| **cuda:0** | 643167 | SFT d005_s42 (alpha=32) | 79% (2507/3177) | ~5.5s/it | ~61 min | ~10:00 |
| **cuda:1** | 628668 | SFT d100_s42_a32_v3 | 95% (3942/4159) | ~4.2s/it | **~15 min** | **~09:10** |
| **cuda:2** | 652259 | signals v7 (d005_s123) — selfcritique mmlu | 61% (4308/7021) | ~1.5s/it | ~68 min mmlu + gsm8k/arc ~75 min | ~11:20 |
| **cuda:3** | 655989 | eval d025_v3_s42 (mmlu/gsm8k/arc, aligned) | 未知（无日志、无结果产出） | — | 未知 | — |
| **cuda:4** | 668217 | signals d025_s123 — selfcritique mmlu | 进行中（最后一个 signal） | ~1.5s/it | 未知具体进度 | — |
| **cuda:4** | 667651 | signals d100_a32_s123 — arc_challenge (all signals) | 刚开始 embedding | — | ~40-50 min | — |
| **cuda:5** | 663067 | signals d025_v3_s42 — selfcritique mmlu | 21% (1510/7021) | ~1.5s/it | ~138 min mmlu + gsm8k/arc ~31 min | ~11:45 |

## GPU 释放顺序

1. **cuda:1** — 最先释放，~15 min（SFT d100_v3 完成后）
2. **cuda:0** — SFT d005_s42 约 1h 后完成，但 eval d100_a32_s123 仍在跑（共享 GPU，eval 无日志无法估时）
3. **cuda:2** — ~2.5h（mmlu selfcritique 完成后还需跑 gsm8k + arc 全流程）
4. **cuda:5** — ~3h（mmlu selfcritique 剩余多 + gsm8k/arc selfcritique）
5. **cuda:3** / **cuda:4** — 无法估时

## 注意事项

1. **cuda:4 有两个 signal 进程**（PID 667651 + 668217）。当前总显存 ~7.4GB，但 667651 进入 minkpp 阶段后会加载模型到 ~7-8GB，总计 ~14-15GB。24.5GB 放得下，但会互相拖慢。
2. **cuda:3 eval 无日志** — 日志文件 `exp_001_eval_3B_d025_v3_s42_batch.log` 不存在，结果目录为空。进程确实在跑（8976 MiB），可能没重定向输出。
3. **cuda:0 eval d100_a32_s123 无结果** — 结果目录为空，4 个 benchmark（含 humaneval），可能还在跑第一个。
4. **d025_s123 signals 接近完成** — 已有 s1+s2（全 benchmark）+ s4+merged（arc+gsm8k），只差 mmlu selfcritique 和 mmlu merged。

---

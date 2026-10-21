# monitor exp 005 gen1 check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_005_gen1_check_20260517T133446_result.json`
- **Structured JSON:** [`d1b2139c3eb49fc81e85.json`](../../sessions/d1/d1b2139c3eb49fc81e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_005 (adaptive k=20, PID 116947)
- **进度**: Gen 0 进行中（启动 ~19 分钟）
- **GPU 0**: 94% 利用率, 65.9GB / 97.9GB VRAM
- **Log**: 全部是 tokenizer warnings (228 行)，无实际进度输出（stdout 缓冲，缺 `PYTHONUNBUFFERED`）
- **输出文件**: 无。checkpoints/results 均未生成
- **Controller 行为**: **无法检查**。Gen 0 尚未完成，baseline 未 set，controller 未启动
- Gen 0 只做 pretrained baseline spectral evaluation（不训练），完成后才会 `set_baseline()` 并进入 Gen 1

**结论**: 太早了，需要等 Gen 0 完成后才能看到 controller 首次触发。由于缺 `PYTHONUNBUFFERED`，即使 Gen 0 完成，日志也可能延迟刷新。

---

## exp_001 (Phase 0 baseline, PID 59365)
- **进度**: Gen 9/10（最后一代），正在生成合成数据 **31680/50000**
- **GPU 1**: 76% 利用率, 19GB VRAM
- **Gen 8 结果**: eff_rank=456.76, ppl=49.29, distinct4=0.4401, hellaswag_acc_norm=0.3103
- **完成状态**: 生成阶段 ~63% 完成，之后还需 fine-tune + eval
- **预计剩余**: 生成 ~30min + 训练 ~30min + 评估 ~15min，约 **1-1.5 小时**后完成全部 10 代

---

**下一步建议**: 等 exp_005 运行 1-2 小时后再查 controller 行为。如果届时日志仍无输出，可以直接查 `results/phase1_adaptive_seed42_results.json` 和 checkpoint 目录判断进度。

---

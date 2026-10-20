# diagnose exp 001 eval 3B d100 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d100_s42_a32_batch_20260516T063112_result.json`
- **Structured JSON:** [`d801e251da89acd655d8.json`](../../sessions/d8/d801e251da89acd655d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

signals v9 实际已成功完成（`V9_ALL_DONE`）。两个实验都是监控误报。

---

## 诊断报告

### exp_001_eval_3B_d100_s42_a32_batch

**根本原因：监控误报（wrapper 进程死亡，子进程存活）**

| 项目 | 状态 |
|------|------|
| PID 687347（batch wrapper） | 已死亡，`/proc/687347` 不存在 |
| PID 687341（para_aligned eval） | **仍在 GPU 3 运行**，9008MiB，56% 利用率 |
| aligned eval | ✅ 已完成，`.done` + 完整结果（14:21 写入） |
| para_aligned eval | ⏳ 运行中，输出目录为空（结果在 eval 全部完成后一次性写入） |
| batch log | 从未创建（wrapper 死在 log 重定向之前或之后） |
| checkpoint | ✅ `Qwen2.5-3B_d100_a32_s42_v3/lora_adapter`，lora_alpha=32 确认 |

**PID 687341 cmdline 确认**：
```
evaluate.py --adapter-path .../Qwen2.5-3B_d100_a32_s42_v3/lora_adapter 
--output-dir .../Qwen2.5-3B_d100_a32_s42_para_aligned 
--paraphrase-dir .../paraphrases
```

进程 11:06 启动，aligned 部分 14:21 完成（~3h15m），para_aligned 预计类似耗时，应在 14:30-15:00 之间完成。**不需要重试，等 PID 687341 跑完即可。**

### exp_002_signals_3B_d100_s123_v9

**根本原因：同样是监控误报**

log 显示 `V9_ALL_DONE Sat May 16 14:17:17 CST 2026`，结果已保存到 `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/`。

### 建议

1. **不要重试任何一个实验**——两个都没有真正失败
2. 等 PID 687341 完成后检查 `Qwen2.5-3B_d100_a32_s42_para_aligned/` 目录是否出现 `.done`
3. 监控系统的根因：batch wrapper PID 与实际 eval Python PID 不同，监控只跟踪 wrapper PID。应考虑让 batch 脚本记录子进程 PID 或用 sentinel 文件而非 PID 存活作为判定依据

---

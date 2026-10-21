# diagnose bjb1 32546 batch failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-batch-failure_20260526T092841_result.json`
- **Structured JSON:** [`3089657fa70b41241e17.json`](../../sessions/30/3089657fa70b41241e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### bjb1-32546：监控误判，实验全部正常

6 个 pi05 CRM K=2 实验**全部在正常运行**，不是真正失败：
- **goal-s42**: ✅ 完成 83.5%
- **goal-s43**: ✅ 完成 85.5%
- **goal-s44**: ✅ 完成 83.0%
- **object-s42/s43/s44**: ⏳ 仍在运行（task 9-10/10，即将完成）

**误判原因**: evaluate.py 不写 sentinel 文件也不上报 W&B，监控系统 5 次轮询无信号后自动判死。实际上进程 PID 全部存活，CPU 228-236%。

### cqa1-32758：tokenizer 缺失导致初始崩溃

3 个 pi05 adaptive 实验初次启动时报错：
```
RuntimeError: Cannot load tokenizer from any of ['google/paligemma-3b-pt-224', '/root/autodl-tmp/models/gemma-2b-tokenizer', 'unsloth/gemma-2b']
```
**原因**: cqa1 上 `gemma-2b-tokenizer` 不完整（缺 `tokenizer.model`，`tokenizer_config.json` 仅 544B vs bjb1 的 40KB）。

已在不同 tmux session 下手动重启，当前正常运行中（object-s44 在 task 8/10，long-s43 在 task 8/10）。

### 行动项
1. **无需代码修复**，等待实验自然完成
2. 监控系统需适配无 sentinel/W&B 的长时间 eval 任务
3. cqa1 下次部署 π0.5 前需同步完整 tokenizer

---

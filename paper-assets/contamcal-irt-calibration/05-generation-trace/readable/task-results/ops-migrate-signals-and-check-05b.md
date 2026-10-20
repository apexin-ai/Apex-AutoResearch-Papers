# ops migrate signals and check 05b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_migrate_signals_and_check_05b_20260516T154634_result.json`
- **Structured JSON:** [`46ce9eee4ee1127c2de8.json`](../../sessions/46/46ce9eee4ee1127c2de8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

---

## 产出汇总

### Task 1: 1.5B-Instruct MMLU signals 迁移到 cuda:4

- PID 805721 (cuda:0) 已 kill
- **新 PID: 810809** on cuda:4 (576 MiB, sentence-transformers encoding 阶段)
- tmux session: `sig_15b_mmlu_v2`，日志: `/tmp/15b_instruct_mmlu_signals_v2.log`
- 已完成进度：s1_embedding_mmlu ✓, s2_minkpp_mmlu ✓, s4 未完成（chunks dir 空）
- 注意：脚本不跳过已有 signal 文件，会重新计算 s1/s2 后继续 s4

### Task 2: 0.5B-Instruct GSM8K eval 质量

- **38.82% (512/1319) 可信**
- 1318/1319 predictions 为数字（非 MMLU 的 all-A position bias）
- 正确样本：准确数值匹配（1→1, 273→273, 45→45, 122→122）
- 错误样本：合理的数值错误（2280→1880, 145→3540），非退化模式
- 结论：GSM8K 结果为正常的 open-ended generation，accuracy 可信

---

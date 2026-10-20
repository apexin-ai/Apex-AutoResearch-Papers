# analysis phase2 grammar only check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_grammar_only_check_20260513T222159_result.json`
- **Structured JSON:** [`2c132b58e02ae12eaa2b.json`](../../sessions/2c/2c132b58e02ae12eaa2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：cron 误报 — 两个进程均仍在运行中。**

| 实验 | PID | 状态 | 运行时长 | 完成进度 | GPU |
|------|-----|------|----------|----------|-----|
| grammar_only | 126473 (子进程) | `Rl` (运行中) | 5h50m | 62/551 (11.3%) | GPU 1, 16482 MiB |
| unconstrained | 126948 (子进程) | `Rl` (运行中) | 2h46m | 22/551 (4.0%) | GPU 1, 16480 MiB |

关键观察：
- JSONL 文件仍在增长（短时间内从 55 → 62 行），进程活跃
- 两个实验共享 GPU 1（92% 利用率），GPU 0 被另一个进程 PID 116365 占用
- Violation report 尚未生成（预期 — 提取未完成，violation_checker 在提取之后的命令链中）
- 每个样本平均推理时间约 5-10 秒，但 Qwen3-8B 的 thinking 模式可能导致部分样本耗时更长

**估计剩余时间**：grammar_only 当前速率约 3.5 样本/分钟，剩余 489 样本 ≈ **~2.3 小时**。unconstrained 更靠后，预估 **~4-5 小时**。

两个 GPU 1 上的推理进程可能互相抢资源，这解释了整体速度低于预期。

---

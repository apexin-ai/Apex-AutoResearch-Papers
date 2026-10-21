# diagnose plan 006 confound fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-006-confound-fix_20260516T015314_result.json`
- **Structured JSON:** [`3c82efc0c8a44ff3a5fb.json`](../../sessions/3c/3c82efc0c8a44ff3a5fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：plan-006-confound-fix

### 进程状态：已正常退出（非异常死亡）

**根因：实验已成功完成，进程自然退出。** 不是 crash / OOM / 被 kill。

### 证据

| 项目 | 详情 |
|------|------|
| PID 256127 | 不存在，ps 返回空 |
| 日志结尾 | `"All phases complete."` — 三个 phase (generate → extract → evaluate) 全部正常跑完 |
| 运行时间 | 07:25 启动 → 09:43 结束，约 **2 小时 18 分钟** |
| GPU 状态 | 4× RTX 5090 全部空闲，0MiB 显存占用，无进程 — 与实验完成一致 |
| 结果文件 | `results/plan006_paraphrastic_comparison.json` (4913B, 09:43 写入) — 内容完整 |

### 实验结果摘要

- **Paraphrase 3-class F1**: 0.727 ± 0.010
- **Continuation 3-class F1**: 0.788 ± 0.006
- **F1 delta (para - cont)**: −0.061
- **Depth retention**: para 0.995 vs cont 0.826
- **Cross-transfer**: para→cont 0.769, cont→para 0.606
- **结论**: confirmed — paraphrastic chains lose depth signal faster

### 下一步

Registry 中状态仍为 RUNNING，需要更新为 **COMPLETED**。实验结果完整，无需重跑。cron 监控可以停止对该实验的跟踪。

---

# diagnose cqa1 32758 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-32758-failures_20260524T031634_result.json`
- **Structured JSON:** [`8516f57a2f0e45f3c5f6.json`](../../sessions/85/8516f57a2f0e45f3c5f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心结论：

**全部是误报** — 被标记为失败的实验实际上都正常完成并保存了结果。监控系统检测到进程退出但无 sentinel/W&B 信号，误判为崩溃。

各实验结果：
- spatial-reconvla-s46: 80.0%
- spatial-crm-norm005-s46: 81.0%
- spatial-adapt-tau025-s46: 80.0%
- spatial-vla-only-s46 (pid 604290): 80.5%，已完成退出
- long-vla-only-s46 (pid 601530): **仍在运行**，GPU 3 上正常推进
- k2mean-s45 相关：/tmp/ 下无对应日志，但 eval_goal_k2mean_seed45.json 已存在（81.0%）

系统无任何异常（GPU/内存/磁盘全部正常）。无需重跑。长期建议是让 eval 脚本写 sentinel 文件以避免监控误报。

报告已写入 `artifacts/diag_cqa1_32758_failures_20260524.md`。

---

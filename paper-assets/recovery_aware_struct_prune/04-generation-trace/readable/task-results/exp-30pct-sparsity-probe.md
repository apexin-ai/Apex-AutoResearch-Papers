# exp 30pct sparsity probe

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_30pct_sparsity_probe_20260520T040615_result.json`
- **Structured JSON:** [`e8f6ccbc187d03c1b168.json`](../../sessions/e8/e8f6ccbc187d03c1b168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 进程都在正常运行，各占约 10-12GB 内存：
- PID 191446: `eval_gsm8k.py` CKA-only 30% on cuda:0 (12.2GB RSS, CPU 147%)
- PID 191519: `eval_gsm8k.py` Standard 30% on cuda:1 (10.1GB RSS, CPU 151%)

eval 阶段预计 1-2 小时完成（1319 题 × 4096 max_new_tokens）。日志缓冲导致 tail 看不到实时进度，这是正常的 — Python 的 stdout 到文件默认是 full-buffered。

任务已全部提交并正常运行，接下来需等待完成后：
1. 检查结果 JSON
2. 更新 registry metrics 和 conclusion
3. 汇报 accuracy 及与 20%/25% 的对比

---

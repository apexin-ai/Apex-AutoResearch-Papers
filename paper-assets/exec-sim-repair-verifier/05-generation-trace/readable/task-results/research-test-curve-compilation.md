# research test curve compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_test-curve-compilation_20260515T140344_result.json`
- **Structured JSON:** [`94d4259f5a6b2c0c7aa6.json`](../../sessions/94/94d4259f5a6b2c0c7aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/comprehensive_test_results.md` 并注册为 `art_20260515_d88b8c`。

内容概要：
- **CLS 8B seed123 test curve**: 6 个 checkpoint，val-selected = test-peak = ckpt-3000 (85.60%)
- **CLS 8B s42 test curve**: 8 个 checkpoint，val-selected ckpt-1000 (83.52%)，test-peak ckpt-1400 (85.47%)
- **CLS 4B s42 test curve**: 3 个有效 checkpoint，val-selected = ckpt-4600 (83.63%)
- **CLS 4B seed123**: ckpt-800 仅 75.33%，表现弱
- **CWM repo-level**: 58-59%，低于 majority baseline，彻底失败
- **Function-level**: CLS 8B 89.93% > CWM 4B 87.19% ≈ CWM 8B 86.96%
- **Ablation**: rank=32 无帮助 (−0.51pp)，seq_length 非混杂变量 (CLS@2048 仍超 CWM 24.79pp)
- CWM 8B repo-level test 仍在运行中 (cwm8b-ckpt400-test-eval)

---

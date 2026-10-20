# monitor verify processes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_verify_processes_20260514T153500_result.json`
- **Structured JSON:** [`e2ab09f4721c495aedd2.json`](../../sessions/e2/e2ab09f4721c495aedd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_process_check.md`。核心发现：

**重复进程 132389/132392**：已不存在，无需处理。它们是脚本在 22:00 错误启动的 s020 进程，与 s015 争 GPU 显存后崩溃。

**各实验状态**：

| 实验 | 当前进度 | 预估完成 | 问题 |
|------|---------|---------|------|
| c2_qw_n500 | s015: 174-178/500 (35%) | s015 ~02:45 May 15 | s020 已崩溃，后续 conditions 需手动启动 |
| c2_n500_deepseek | s015: 201-224/500 (42%) | s015 ~02:15 May 15 | 后续 conditions 启动方式待确认 |
| c3_llama | s015 已完成(PASS)，s020: 8-9/50 | 全部 ~01:36 May 15 | 正常，script 自动推进 |

**GPU 分配**：4 卡全在用。GPU 0/1 各跑一个 DeepSeek 进程；GPU 2/3 各跑 Qwen + Llama 两个模型（~48GB/96GB）。

**最紧急待处理**：c2_qw_n500 的 s020/s025/s030 不会自动启动，需要在 s015 完成（约 02:45）后手动启动。

---

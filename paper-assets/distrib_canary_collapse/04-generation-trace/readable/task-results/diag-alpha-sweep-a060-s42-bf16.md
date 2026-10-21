# diag alpha sweep a060 s42 bf16

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_alpha_sweep_a060_s42_bf16_20260518T205156_result.json`
- **Structured JSON:** [`d794219fdd8a36c8b428.json`](../../sessions/d7/d794219fdd8a36c8b428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心结论：

**实验已成功完成，EXIT_CODE=129 是误报。** 10/10 generation 全部跑完，all_metrics.json 包含完整的 11 条记录（gen_0-gen_10），EXIT_CODE sentinel 文件内容为 `0`。

129 (SIGHUP) 的来源是 tmux session 在脚本完成后被销毁，shell wrapper 捕获到的是 tmux 清理信号，不是脚本自身的退出码。cuda:3 当前空闲、无残留进程，验证了这一点。

数据完好，无需重跑。报告已写入 `artifacts/alpha_sweep_a060_s42_bf16/failure_diagnosis.md`。

---

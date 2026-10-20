# diag gen gpt2m a100 s43 bf16

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gen_gpt2m_a100_s43_bf16_20260518T205436_result.json`
- **Structured JSON:** [`7ef165c24ab6a9f10212.json`](../../sessions/7e/7ef165c24ab6a9f10212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：**两个实验都已成功完成，EXIT_CODE=129 是误报。**

核心证据：
- `gen_gpt2m_a100_s43_bf16`：gen_0 到 gen_10/10 全部完成，`all_metrics.json` 含 11 条完整记录，哨兵文件内容为 **0**
- `alpha_sweep_a060_s42_bf16`：同上，哨兵文件 = 0，指标完整
- SIGHUP 发生在脚本写完哨兵文件之后（日志行 4137-4138 为最后两行），不影响实验数据

**不需要重跑。** 建议监控系统以哨兵文件内容（而非进程退出码）判定实验状态。报告已写入 `artifacts/diag_gen_gpt2m_a100_s43_bf16.md`。

---

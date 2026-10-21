# ops diagnose plan008 v3 script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-plan008-v3-script_20260515T151438_result.json`
- **Structured JSON:** [`1948fb568af39b8e5eec.json`](../../sessions/19/1948fb568af39b8e5eec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

恢复完成。文件大小 16,810 字节，与 `.bak` 一致。

## 总结

| 项目 | 结果 |
|------|------|
| **根因** | `implicit_router_sft.py` 在 05-14 被大幅修改：自定义 loss、gradient_accumulation 降为1、数据切分策略变更 |
| **为何全部预测 internal** | 有效 batch 从 32 降到 4 导致训练不稳定，模型坍缩到多数类预测 |
| **恢复操作** | 已用 `.bak` 覆盖当前文件 |
| **下一步** | 用恢复后的脚本重跑 v3 实验 |

---

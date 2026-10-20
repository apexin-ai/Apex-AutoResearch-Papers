# analysis cls v4 s123 config check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-v4-s123-config-check_20260518T203816_result.json`
- **Structured JSON:** [`475ff71f7deb3856844b.json`](../../sessions/47/475ff71f7deb3856844b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/cls_v4_s123_config_comparison.md`。

**核心结论：不能直接合并为双 seed。**

训练超参数和 LoRA 配置完全一致（seed 除外），但：
- **v4 只训练了 2/3 epochs**（step 4422/6633），s123 完成了 3 epochs
- 3.6pp 差距（71.29% vs 74.93%）大概率来自训练进度差异，不是 seed variance

v5（s42 重训）也不是完美替代——preprocessing 逻辑变了（truncate→drop），训练数据从 70748 降到 67343，步数 6633→6315。

**建议方案 A**：等 v5 完成后和 s123 做双 seed 报告，preprocessing 差异（truncate vs drop 3405 条超长样本）在论文中可以忽略或脚注说明，前提是结果差距 < 2pp。

---

# analysis deepseek func icc

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-func-icc_20260518T185440_result.json`
- **Structured JSON:** [`4455cea81422978eae52.json`](../../sessions/44/4455cea81422978eae52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**DeepSeek-Coder-6.7B function-level ICC(3,1) = 0.653** [95% CI: 0.626, 0.678]

对比 Qwen3-4B:

| Model | ICC(3,1) | 解释 |
|-------|----------|------|
| Qwen3-4B | 0.191 | 轻微一致 |
| DeepSeek-Coder-6.7B | **0.653** | 实质性一致 |

DeepSeek 两个 seed 间 92.2% 的预测一致，ICC 是 Qwen 的 3.4 倍。说明 DeepSeek 的错误更系统化（由 test case 内在难度决定），而非训练随机性导致。这进一步支持 per-test scoring 利用 block 结构的论点。

结果已保存至：
- `artifacts/deepseek_func_icc_result.md`
- 远程 `artifacts/deepseek_func_icc_result.json`

注：s123 的 function-level predictions 需要重新评估（原文件被 repo-level 数据覆盖），重新评估结果 accuracy=87.14% 与原 summary.json 记录的 86.77% 接近（差异可能来自 eval 脚本版本变化中 unparseable 处理逻辑不同）。

---

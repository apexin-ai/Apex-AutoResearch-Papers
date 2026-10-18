# writing w4 zeroshot verification

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_w4_zeroshot_verification_20260516T024654_result.json`
- **Structured JSON:** [`a0ef4f289c68e23f9ae6.json`](../../sessions/a0/a0ef4f289c68e23f9ae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。变更清单：

### 修改文件

**1. `generalization.tex` L12**
- 在 zero-shot LLM 结果后添加 `prompt template in Appendix~\ref{app:zeroshot_prompt}` 引用

**2. `section_appendix.tex` L75-88（新增）**
- 新增 `\subsection{Zero-Shot LLM Prompt Template}` (`app:zeroshot_prompt`)
- 标注两个实验使用相同 prompt（含 exp_id）
- 概述 prompt 结构：system message 定义 depth 概念和 per-depth pattern，user message 给文本要求 JSON 输出
- 提供缩略版 prompt 原文（quote 环境）
- 说明无 in-context examples（zero-shot）

### 验证结论（无需修改）

| 检查项 | 状态 |
|--------|------|
| DeepSeek 数字 (36.2%, CI [32.0, 40.4], 500 samples) | 与 registry 一致 |
| Qwen 数字 (30.4%, CI [26.5, 34.6], 500 samples) | 与 registry 一致 |
| Sample size = 500 | generalization.tex 已写 "each 500 samples" |
| CI 窄度：±4.2pp / ±4.1pp vs RF 78.2% 差距 >40pp | 远超 CI，结论稳健 |
| Failure mode 对比 | discussion.tex L7 已有，且描述正确（互补 failure pattern → 非 prompt 偏差） |
| Prompt 模板描述 | **已补充**（appendix 新增节） |

---

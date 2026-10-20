# paper code crossmodel table

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_code-crossmodel-table_20260519T000706_result.json`
- **Structured JSON:** [`6c58169b1277683c3240.json`](../../sessions/6c/6c58169b1277683c3240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已写入 `artifacts/code_crossmodel_table.tex`。

要点：
- Qwen2.5-1.5B 数据已填入（K*=2, 0v1=.9388, 1v2=.7382, 2v3=.5300），与源文件一致
- 其余 3 模型用 `.TBD` 占位，实验完成后直接替换
- 格式参照 `tab:kstar_ci_extended`：宽表、`\cmidrule` 分组、bootstrap CI 列、脚注标注统计检验
- 底部增加 K* 汇总行，方便一眼对比跨模型一致性
- 小数统一 4 位，最优值加粗，无破折号

---

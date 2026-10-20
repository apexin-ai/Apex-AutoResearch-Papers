# audit figure4 data source

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_figure4-data-source_20260523T174143_result.json`
- **Structured JSON:** [`dc0d2c9c2ab8e37b97f9.json`](../../sessions/dc/dc0d2c9c2ab8e37b97f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**Figure 4 实际显示的是 AUC(0v1)（0.848–0.995），不是 6-class ordinal accuracy。**

根因：5/23 将绘图脚本从 v1 切换到 v2，PDF 已更新为 v2 内容（3 模型 AUC + K* 预测），但 caption、正文、Table 7 仍然描述 v1 的内容（4 模型 ordinal accuracy + retention）。

具体不一致：
- **指标错配**：图=AUC(0v1)，caption 说 "6-class ordinal accuracy / retention"
- **模型数量错配**：图=3 个模型，caption/table=4 个模型（含 Qwen-rw）
- **Table 7 不再是 Figure 4 的 "full matrix"**：Table 7 是 ordinal accuracy，Figure 4 是 AUC

报告已写入 `artifacts/figure4_data_audit.md` 并注册，包含三种修复方案（回退 v1 / 更新文本匹配 v2 / 合并两版）。

---

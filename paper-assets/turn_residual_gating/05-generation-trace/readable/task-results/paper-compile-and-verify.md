# paper compile and verify

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_and_verify_20260522T174753_result.json`
- **Structured JSON:** [`185efdc669bb6730eb65.json`](../../sessions/18/185efdc669bb6730eb65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 项目 | 结果 |
|------|------|
| **Errors** | 0 |
| **Undefined refs** | 0 |
| **总页数** | 13 页 |
| **主文页数** | **8 页** (Conclusion 在第 8 页，Limitations 第 9 页开头 → 不计入 8 页限制，符合 EMNLP 2026) |
| **References** | 第 9 页（与 Limitations 同页），不计入页数限制 |
| **Appendix** | 第 10-13 页 |

**Table 1 (tab:four-way) 格式确认：**
- `\midrule` 分组：Base 单独一组，下面 ThreadGate / +PCGrad / Uniform Gate / LoRA-only 一组
- `\textbf{}` 标注 best values：GAR-O IID/Held-out 最高 0.51 (Uniform Gate)、GAR-D 最高 0.02 (ThreadGate)、AR GAR-O 最高 0.025 (LoRA-only)
- 表格结构完整，含 `\toprule`/`\midrule`/`\bottomrule`、`\cmidrule` 分列

**Intro 分段确认：**
- 5 个自然段落，合理分段（不是巨块）：(1) 问题引入+GAR量化 (2) residual stream 信息保留 (3) ThreadGate 动机 (4) 五方对比和主要发现 (5) 贡献列表

编译通过，格式和页数均符合要求。

---

# paper c3 evidence hierarchy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_c3_evidence_hierarchy_20260522T085201_result.json`
- **Structured JSON:** [`80404dd16a23b48be84d.json`](../../sessions/80/80404dd16a23b48be84d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，所有修改确认正确。

## 报告

### Figure 1b：走备选方案（保留现有 bar chart）
- 原因：204-batch 散点图所需的原始数据在本地不完整——d051 + eval_exp2 凑得 204 batches 但 BCS 值与论文报告的范围/SD 不匹配（推测是 BCS 定义从 MAX→MEAN 修复后，部分数据文件未同步更新）。重新生成需要回服务器跑脚本，超出任务时间预算。
- 已在 `experimental_setup.tex:74` 的 caption 中将 (b) 标注为 **"Illustrative"**，明确说明 "each bar represents one extreme-BCS batch per condition"，并指向 pooled regression 统计证据（§4.2, semipartial R²=0.273, n=204）。

### 正文证据层级调整（3 处修改）

| 文件 | 行 | 修改 |
|------|-----|------|
| `experimental_setup.tex:74` | Figure 1b caption | 加 "Illustrative" + "each bar represents one extreme-BCS batch" + 引用 pooled R² |
| `results.tex:50` | §4.3 开头 | pooled semipartial R²=0.273 后加 "---the primary quantitative evidence" |
| `results.tex:64` | Practical magnitude | 80pool R²≈0.05 前加 "conservative restricted-range estimate" |

### 编译结果
- 0 errors, 0 undefined references, 26 pages (body ≤ 8 pages), 1 bibtex warning (pre-existing volume/number conflict)

---

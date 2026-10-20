# ops latex compile check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_latex_compile_check_20260516T230726_result.json`
- **Structured JSON:** [`ae34900ca44f9a7a27f7.json`](../../sessions/ae/ae34900ca44f9a7a27f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 编译报告

**编译状态：成功** (return code 0, 三遍编译均无错误)

### 页数
- **总计 24 页**（A4）
- 正文 + references：约 10 页（conclusion 在第 9 页前结束，bbl 从第 9 页开始，到第 10 页）
- Limitations：第 11 页
- Appendix：第 12–24 页（约 13 页）
- **符合 EMNLP 限制**（8 页正文 + unlimited appendix；references 和 limitations 不计入 8 页限制，当前正文约 8–9 页）

### Warnings
| 类型 | 数量 | 详情 |
|------|------|------|
| Undefined references | **0** | 无 |
| Overfull hbox | **4** | 最严重 89pt（lines 79–87）、70pt（lines 113–124）、26pt（lines 11–23）、22pt（lines 108–118） |
| Float specifier changed | 2 | `h` → `ht`（无害） |
| Hyperref token warning | 2 | math shift in PDF string（无害） |

### 需关注
4 个 overfull hbox 中有 2 个超过 70pt（约 2.5cm 溢出），可能导致表格或公式超出 column 边界。建议检查：
- lines 79–87（89pt 溢出）
- lines 113–124（70pt 溢出）

这些行号对应编译时的内部行号，需要对照具体 `.tex` 文件定位。如需修复可以进一步排查。

---

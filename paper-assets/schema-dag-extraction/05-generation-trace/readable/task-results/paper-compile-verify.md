# paper compile verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_verify_20260522T025109_result.json`
- **Structured JSON:** [`d388b16abe60cc3019e9.json`](../../sessions/d3/d388b16abe60cc3019e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析 log 中页面输出顺序：
- Pages 1–8: 正文（introduction → related work → experimental setup → results → sdgd_negative → discussion）
- `sdgd_negative.tex` 加载在 page 7 之后，discussion 结束在 page 8
- Page 9: Limitations 开始，`main.bbl` 也在 page 9 开始
- Pages 9–12: Limitations + References
- Pages 13–27: Appendix（15 pages）

## 编译验证报告

| 项目 | 结果 |
|------|------|
| **编译** | 成功 |
| **Errors** | 0 |
| **Undefined references** | 0 |
| **Multiply-defined labels** | 0 |
| **Missing citations** | 0 |
| **总页数** | 27 |
| **正文页数** | **8 页**（pages 1–8，含 abstract 到 discussion） |
| **Limitations** | 从 page 9 开始（不计入 8 页限制） |
| **References** | pages 9–12 |
| **Appendix** | pages 13–27 |

**Warnings**（均为无害）：
- 18 个 float specifier `h` → `ht` 自动调整（正常行为）
- BibTeX: `guo-2021-label-confusion` 同时使用了 volume 和 number 字段（不影响输出，可选修复）

正文 8 页，符合 EMNLP 2026 限制。编译无任何问题。

---

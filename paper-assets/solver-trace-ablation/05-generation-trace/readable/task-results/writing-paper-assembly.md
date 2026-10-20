# writing paper assembly

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-assembly_20260514T192323_result.json`
- **Structured JSON:** [`2ba6f7ede344101401da.json`](../../sessions/2b/2ba6f7ede344101401da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 编译结果

**编译状态**: 成功，0 errors，0 warnings

**产出文件**:
- `paper/paper.tex` — 主文件（ACL review mode）
- `paper/paper.pdf` — 编译产出
- `paper/acl.sty` + `paper/acl_natbib.bst` — ACL 官方模板文件
- `paper/figures/` — 已有全部 4 张图（PDF 格式）

**页数**: 12 页正文 + 2 页参考文献 = 14 页总计

**字数**: 正文约 7,800 词（pdftotext 统计）

**超页问题**: 正文 12 页，**超出 EMNLP 8 页限制 4 页**。需要大幅压缩。主要候选：
- `experiments.tex` 最长（含 5 个子节 + 3 个内联表格 + 3 张图），可考虑合并表格、精简 per-seed 细节
- `method.tex` 的 hacking taxonomy 列表（7 项）与 experiments.tex 的 taxonomy 小节有重复
- `introduction.tex` 偏长（约 1.5 页），贡献列表可压缩
- `related_work.tex` 可以移到 appendix

**引用/标签一致性**: 所有 `\ref{}`/`\cite{}` 均已解析，无 undefined reference。

**已知 issue**: 无。tables 全部内联在 experiments.tex 中，图片路径全部正确。

---

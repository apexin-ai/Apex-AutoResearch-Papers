# fix fig1 font bug

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fig1-font-bug_20260514T122509_result.json`
- **Structured JSON:** [`10a67e95cfb846ac98d0.json`](../../sessions/10/10a67e95cfb846ac98d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成：

1. **根因**：`gen_fig1.py` 使用 `'font.family': 'sans-serif'`（通用族名），matplotlib 回退到缺失 't' glyph 的字体
2. **修复**：改为 `'font.family': 'DejaVu Sans'`（服务器上可用的具体字体），并添加 `pdf.fonttype: 42` / `ps.fonttype: 42` 强制 TrueType 嵌入
3. **清除 matplotlib 字体缓存**后重新生成 PDF
4. **验证**：pdffonts 确认 DejaVu Sans 正确嵌入为 CID TrueType，字体宽度表包含 't' (CID 116, width 392)
5. **文件已复制**：服务器论文目录 + 本地 `docs/paper/figures/fig1_daf_scatter.pdf`（23688 bytes）
6. **论文已重编译**：`main.pdf` 5 页，205KB，编译成功

---

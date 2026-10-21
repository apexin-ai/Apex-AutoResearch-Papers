# code fix type3 fonts

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_type3_fonts_20260526T215833_result.json`
- **Structured JSON:** [`61e318c68dac09bdded9.json`](../../sessions/61/61e318c68dac09bdded9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**21 个 Type 3 PDF 全部修复，当前 figures/ 目录下零 Type 3 字体。**

| 方法 | 数量 | 效果 |
|------|------|------|
| **REGEN**（脚本重跑 + `pdf.fonttype=42`） | 14 | TrueType 嵌入，多数文件比原文件更小 |
| **GS**（ghostscript 轮廓转换） | 7 | 字体转为矢量路径，视觉无变化 |

论文中使用的 11 个 Type 3 文件全部修复。其中 9 个用 REGEN 方法（零膨胀），2 个用 GS 方法（`fig5.pdf` 1.83x, `fig6.pdf` 2.39x，绝对大小 <79KB）。

原始文件备份在 `/tmp/type3_backup/`。

---

# fix c2 crossref and compile

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c2_crossref_and_compile_20260528T181333_result.json`
- **Structured JSON:** [`39aa07910b6757415444.json`](../../sessions/39/39aa07910b6757415444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译结果：

- **PDF**: 33 页，1.3MB，编译成功
- **Figure ?? 修复**: **PASS** — PDF 中无 "Figure ??" 残留，subfigure 引用正常解析（Figure 4a/4b）
- **6 个 undefined references**: 均为 section/table label（`sec:linear_results`, `sec:openvla_results`, `sec:scaling_law`, `tab:taxonomy`），非本次修复范围，可能是尚未写入的章节
- **hyperref warnings**: PDF bookmark 中含数学符号的常规警告，不影响输出

验证结果：
- "six VLA" in abstract: **PASS**
- "20× ... at k=0.9" 限定: **PASS**（`up to 20× from Object to Goal at k=0.9`）
- J. Zheng（非 Y. Zheng）: **PASS**（`[11] J. Zheng`）
- SmolLM2 360M: 文本中出现（但无法确认是否在 Figure 2 caption 中，需视觉检查）

---

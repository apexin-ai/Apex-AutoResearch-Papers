# paper compile verify audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_verify_audit_20260529T052139_result.json`
- **Structured JSON:** [`3b73d2cc237152c41fb1.json`](../../sessions/3b/3b73d2cc237152c41fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

## 编译结果
- **成功**，无 fatal error
- **页数**: 8 (main body) + 2 (references, pp.8-9) + 22 (appendix, pp.10-32) = 32 total
- **Undefined references**: 0
- **Missing figures**: 0
- **Warnings**: 12x hyperref "Token not allowed in PDF string" (math symbols in section titles, benign), 11x Underfull vbox (cosmetic)

## 数字验证

| 修正项 | 预期值 | 实际值 | 状态 |
|--------|--------|--------|------|
| X-VLA Object L2 k=0.9 | 99.2 | 99.2 (experiments.tex:49, appendix.tex:26) | ✅ |
| 旧值 97.6 已移除 | 不出现 | 未找到 | ✅ |
| SmolVLA token 数 | "7 of 128" | "7 of 128" (experiments.tex:31, results.tex:38) | ✅ |
| 旧值 "6 of 128" 已移除 | 不出现 | 未找到 | ✅ |
| 46.8pp margin peak | 46.8 | 46.8 (experiments.tex:96) | ✅ |
| AI Disclosure section | 存在 | appendix.tex:935 | ✅ |

## 图表
- 17 个 PDF 图表被引用，全部存在于 `figures/paper/` 目录 ✅
- 主体 8 页符合 CoRL 2026 限制 ✅

---

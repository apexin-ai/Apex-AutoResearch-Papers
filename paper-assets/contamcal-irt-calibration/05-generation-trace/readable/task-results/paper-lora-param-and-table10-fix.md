# paper lora param and table10 fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_lora-param-and-table10-fix_20260521T195543_result.json`
- **Structured JSON:** [`4b70829478380ebaee3d.json`](../../sessions/4b/4b70829478380ebaee3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成：

1. **limitations.tex**: 在 "inversely proportional to model size" 后追加了 "specifically, 0.45% for Phi-4 (14.7B) and 0.59% for Gemma-2 (9B)"。

2. **appendix.tex Table 10 (tab:socsci_prior)**: 
   - Social Sciences 数值已是新值（-0.627, 99.68% baseline; -0.541, 99.35% tight; -0.654, 99.85% loose），无需更新。
   - 在表格底部添加了 footnote："Social Sciences row updated with corrected J=16 model pool; other domains retain the original prior sensitivity pool."

---

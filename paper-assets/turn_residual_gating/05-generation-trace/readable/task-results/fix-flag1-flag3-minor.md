# fix flag1 flag3 minor

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_flag1_flag3_minor_20260524T044110_result.json`
- **Structured JSON:** [`37f5be16860ac7321c79.json`](../../sessions/37/37f5be16860ac7321c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无错误。

**Flag 1**: appendix.tex KL section 第一段末尾加了脚注 `\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}`

**Flag 3**: 服务器上没有找到 0.353 作为 AR GAR-Dongre 的独立结果文件（该值出现在 GAR-ours 的 per-turn 数组和 TF dongre 结果中，但不是 AR GAR-Dongre 的聚合值）。已将 `(0.019→0.353; N=5 pilot)` 替换为定性描述 `substantially under SS (N=5 pilot; see Appendix)`。

---

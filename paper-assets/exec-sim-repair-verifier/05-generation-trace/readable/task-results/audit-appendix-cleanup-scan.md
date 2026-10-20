# audit appendix cleanup scan

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix-cleanup-scan_20260521T151453_result.json`
- **Structured JSON:** [`b40e0f571a8a08d046a1.json`](../../sessions/b4/b40e0f571a8a08d046a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/appendix_cleanup_report.md`。

核心发现：

**3 个需修复项：**
1. **Line 67** — majority-voting 脚注承认用了 "unverified checkpoint"，submission 前必须验证或删除
2. **Line 304 ¶(c)** — parseable-only accuracy 写 "42–53%"，与 ¶(g) 和主文的 "38–43%" 矛盾
3. **Line 304 ¶(c)** — "divergence widens from 26pp to 28pp" 算术对不上（seed 42 标准 gap = 25.59pp，relaxed = 26.65pp，不是 28pp）

**4 个小问题：** 449 行 unparseable rate 74% vs 73.8% 取整不一致；Table 8 caption "unavailable" 措辞；¶(g) 可压缩为交叉引用省 ~5 行；Extended Limitations 的 "tentative" 可换更强措辞。

主要数字（19–26pp、z=−23.7、oracle 90.63%/95.83%、217×、~370 GPU-hours、TOST p=0.007）全部一致，无问题。

---

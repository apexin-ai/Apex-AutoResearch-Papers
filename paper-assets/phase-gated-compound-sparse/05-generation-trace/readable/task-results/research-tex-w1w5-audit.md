# research tex w1w5 audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tex_w1w5_audit_20260514T224833_result.json`
- **Structured JSON:** [`2c3fa35fd701be1c7a83.json`](../../sessions/2c/2c3fa35fd701be1c7a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/w1w5_audit_report.md`。

**核心发现**：

| Warning | 状态 | 关键位置 |
|---------|------|---------|
| **W1** | PASS — 远程 tex 已包含 LLaMA | 无需操作 |
| **W2** | results.tex:L74 prose cherry-pick CI/p | abstract.tex:L10 同样 |
| **W3 [CRITICAL]** | appendix_disc_analysis.tex:L33 + limitations.tex:L2 仍需加强 D060 partially_confirmed 表述 | conclusion/discussion 已 OK |
| **W4** | methodology.tex:L22 声称 B=10,000，但 profiling 实际 B=1,000（40+ json 文件可证），post-hoc rebootstrap 才到 10,000 | appendix_disc_analysis.tex:L45 同 |
| **W5** | 完全缺失 per-phase effective sample sizes，仅有总 exclusion 数 | 等 n=500 数据后补 appendix_moved.tex:L26 |

每个 warning 都附带了精确行号、当前原文、建议替换文本。W2/W3/W4 不依赖 n=500 可立即修复，W5 需等数据。

---

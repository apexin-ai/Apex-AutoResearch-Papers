# check paper pre submission audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_paper-pre-submission-audit_20260521T163758_result.json`
- **Structured JSON:** [`e939ee3149902795956e.json`](../../sessions/e9/e939ee3149902795956e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**编译**: ✅ 无错误，15页PDF，所有引用和图表正常。

**数字一致性**: 20+ 核心数字经 registry 逐 seed 验证正确。发现 3 个问题：
1. **🔴 P0**: Appendix Table 3 Spatial Plan A fast-path 列写的 84%，但 trigger rate=97.6% → 应为 **2.4%**。是 Object 值的误抄。
2. **🔴 P0**: Conclusion 写 "larger VLAs are untested" 但 Appendix E 已有 π0.5 (3.6B) 数据，自相矛盾。
3. **🟡 P1**: VLA-only Object baseline 在 Table 1 (11.0%) 和 Table 2 (10.9%) 不同，虽有脚注说明 seed set 不同但容易被 reviewer 质疑。

**π0.5 缺口**: VLA-only baseline 已完成 (Object 81.5%, Spatial 84.2%)，但 Plan A/CRM 全流程（precompute → train → eval）还在 PREPARING 阶段，8 天内完成风险极高。建议准备 fallback：移除 Table 5 的 placeholder 行，只保留 VLA-only baseline 作为 headroom 分析。

**引用**: 31 个 `\cite{}` 与 31 个 bib 条目完美匹配，无遗漏无多余。

报告已注册为 `art_20260521_b7ea89`。

---

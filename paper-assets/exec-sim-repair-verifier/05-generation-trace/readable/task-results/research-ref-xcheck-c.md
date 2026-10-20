# research ref xcheck C

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-xcheck-C_20260526T104653_result.json`
- **Structured JSON:** [`5117eee6877adc460e3e.json`](../../sessions/51/5117eee6877adc460e3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All searches complete. Let me compile the final results, combining web verification with citation context checks.

---

## 逐条验证结果

```
[andrews2005mutation]   ✓ 正确
[just2014mutants]       ✓ 正确
[wang2023selfconsistency] ✓ 正确
[angrist2009mostly]     ✓ 正确
[schuirmann1987tost]    ✓ 正确
[davison1997bootstrap]  ✓ 正确
[shrout1979icc]         ✓ 正确
[holm1979]              ✓ 正确
[lakens2017]            ✓ 正确
[hoenig2001]            ✓ 正确
[zhuo2024icescore]      ✓ 正确
[dong2024codescore]     ⚠️ 问题: volume/year 错误——ACM TOSEM 实际发表于 Volume 34 (2025)，非 Volume 33 (2024)。应改为 volume={34}, year={2025}
[zhou2023codebertscore] ✓ 正确
[willard2023outlines]   ✓ 正确
[poesia2022synchromesh] ✓ 正确
[dong2024xgrammar]      ⚠️ 问题: 第二作者姓氏错误——应为 "Ruan, Charlie F." 而非 "Huang, Charlie F."；缺少 4 位作者 (Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao)，实际共 7 位作者
[li2025codeprm]         ✓ 正确
[zhang2026funprm]       ✓ 正确
[jiang2025coderlplus]   ✓ 正确
[ye2025prlcoder]        ✓ 正确
[jain2023contextual]    ⚠️ 问题: 作者列表错误——第二作者应为 Uri Alon 而非 Ristimoy Barik；缺少 Alex Groce。正确作者为 Kush Jain, Uri Alon, Alex Groce, Claire Le Goues
[wang2024llmmutation]   ✓ 正确（key 中 2024 与 year 字段 2025 不一致，但 key 不影响输出）
[alphacode2023team]     ✓ 正确
```

引用上下文检查：所有 23 条引用在正文中的使用均与论文实际内容匹配，无张冠李戴。

---

## 有问题的条目汇总

| # | Key | 问题 | 严重程度 |
|---|-----|------|----------|
| 59 | `dong2024codescore` | volume 应为 34, year 应为 2025 (非 33/2024) | 中 |
| 63 | `dong2024xgrammar` | 第二作者姓 Huang→Ruan；缺 4 位合著者 | 高 |
| 68 | `jain2023contextual` | 第二作者 Barik→Alon；缺 Alex Groce | 高 |

---

# research ref xcheck B

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-xcheck-B_20260526T104646_result.json`
- **Structured JSON:** [`de0fb5c83716872a5af8.json`](../../sessions/de/de0fb5c83716872a5af8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both issues confirmed. Now I have all the data. Here are the results:

---

## 验证结果

```
[jimenez2024swebench]     ✓ 正确
[chowdhury2024swebenchverified] ✓ 正确
[yang2024sweagent]        ✓ 正确
[xia2024agentless]        ✓ 正确 (key 写 2024 但 year=2025 正确，key 名不影响渲染)
[yang2025aprsurvey]       ✓ 正确
[qwen2025qwen3]           ✓ 正确
[chen2021humaneval]       ✓ 正确
[austin2021mbpp]          ✓ 正确
[hu2022lora]              ✓ 正确
[dettmers2024qlora]       ✓ 正确 (key 写 2024 但 year=2023 正确，key 名不影响渲染)
[guo2024deepseekcoder]    ⚠️ 问题: 作者 "Xiong, Yun" 应为 "Xiong, Yingfei"（arXiv 原文确认为 Yingfei Xiong）
[ni2023lever]             ✓ 正确
[chen2023codet]           ✓ 正确
[lightman2023letsverify]  ✓ 正确 (key 写 2023 但 year=2024 正确，ICLR 2024 发表)
[uesato2022solving]       ✓ 正确
[wang2026verpo]           ✓ 正确
[tang2026execverify]      ✓ 正确
[le2022coderl]            ✓ 正确
[li2022alphacode]         ✓ 正确
[shinn2023reflexion]      ✓ 正确
[tufano2019predictive]    ⚠️ 问题: venue 错误，应为 ICSME 2019，非 ISSTA
[kim2022predictive]       ✓ 正确
[raffel2020t5]            ✓ 正确
```

引用上下文检查：所有 23 条引用在正文中的使用均与论文内容匹配，无张冠李戴。

---

## 有问题的条目汇总

| # | Key | 问题 | 修正建议 |
|---|-----|------|----------|
| 35 | `guo2024deepseekcoder` | 作者姓名错误：`Xiong, Yun` | → `Xiong, Yingfei` |
| 45 | `tufano2019predictive` | 会议名称错误：`ISSTA` | → `ICSME` |

---

# audit reference verification

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_reference_verification_20260524T115033_result.json`
- **Structured JSON:** [`f3466552f06b7041fecb.json`](../../sessions/f3/f3466552f06b7041fecb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 58 entries verified. Here's the compiled report.

---

## 引用验证报告

**总数**: 58 条
**已验证**: 58 条
**问题**: 5 条（2 critical, 3 warning）

### 问题列表

1. **[critical]** `zhang2024tell` — 5 个作者名错误：
   - Zhang, **Qinyuan** → Zhang, **Qingru**
   - Singh, **Agarwal** → Singh, **Chandan**
   - Liu, **Liang** → Liu, **Liyuan**
   - Liu, **Xin** → Liu, **Xiaodong**
   - Yu, **Bing** → Yu, **Bin**
   - （Title, year, venue 正确）

2. **[critical]** `li2024measuring` — 3 个作者名错误：
   - Li, **Liang** → Li, **Kenneth**
   - Liu, **Qingyun** → Liu, **Tianle**
   - Bashkansky, **Elias** → Bashkansky, **Naomi**
   - （Title, year, venue 正确）

3. **[warning]** `zheng2024judging` — 年份错误：bib 写 2024，实际是 **NeurIPS 2023**

4. **[warning]** `luo2025flexidepth` — Venue 需更新：bib 写 arXiv，实际已发表于 **COLM 2025**；Title 多了 "(FlexiDepth)"，原文标题无此后缀

5. **[warning]** `ding2023ultrachat` — Venue 需更新：bib 写 arXiv，实际已发表于 **EMNLP 2023**

### 已验证通过（53 条）

1. `dongre2026attention` — ✅ Title, author, year, venue 全部正确
2. `hong2025rhea` — ✅
3. `laban2025lost` — ✅
4. `liu2026intent` — ✅
5. `bai2024mtbench101` — ✅
6. `fan2020layerdrop` — ✅
7. `raposo2024mixture` — ✅
8. `schuster2022calm` — ✅
9. `qiu2025gated` — ✅
10. `xiao2024streaming` — ✅
11. `hsieh2024found` — ✅
12. `bengio2015scheduled` — ✅
13. `ranzato2016sequence` — ✅
14. `lamb2016professor` — ✅（arXiv 顺序 Lamb 在前，与 bib 一致）
15. `leblond2018searnn` — ✅
16. `he2019exposure` — ✅
17. `wiseman2016sequence` — ✅
18. `arora2022exposure` — ✅
19. `yu2020pcgrad` — ✅
20. `chen2018gradnorm` — ✅
21. `liu2021cagrad` — ✅
22. `navon2022nash` — ✅
23. `bachlechner2021rezero` — ✅
24. `grattafiori2024llama3` — ✅
25. `gromov2024unreasonable` — ✅（key 写 2024 为 preprint 年，year 字段 2025 为 ICLR 发表年，可接受）
26. `vaswani2017attention` — ✅
27. `he2016deep` — ✅
28. `srivastava2015highway` — ✅
29. `hu2022lora` — ✅
30. `zhang2020dialogpt` — ✅
31. `roller2021recipes` — ✅
32. `clark2019what` — ✅
33. `voita2019analyzing` — ✅
34. `kovaleva2019revealing` — ✅
35. `liu2024lost` — ✅
36. `zhang2019bridging` — ✅
37. `mihaylova2019scheduled` — ✅
38. `dou2019attention` — ✅
39. `dou2022parallel` — ✅
40. `li2016persona` — ✅
41. `xu2022goldfish` — ✅
42. `vig2019multiscale` — ✅
43. `abnar2020quantifying` — ✅
44. `ethayarajh2019contextual` — ✅
45. `brunner2020identifiability` — ✅
46. `veit2016residual` — ✅
47. `dong2021attention` — ✅
48. `zhou2020drophead` — ✅
49. `dauphin2017language` — ✅
50. `shazeer2020glu` — ✅
51. `lin2022truthfulqa` — ✅
52. `hendrycks2021measuring` — ✅
53. `dettmers2023qlora` — ✅

---

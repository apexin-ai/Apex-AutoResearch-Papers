# audit ref verify group1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-group1_20260526T101539_result.json`
- **Structured JSON:** [`3bea2edb4d5612174095.json`](../../sessions/3b/3bea2edb4d5612174095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications complete. Here's the consolidated report:

---

## 验证结果

```
[1] dugan2024raid — ❌
  标题: OK
  作者: ❌ 严重错误。bib 列出 7 人含 "Andrew Langmore" 和 "Garrison Ets-Hokin"，
        实际 ACL Anthology 有 8 位作者：Dugan, Hwang, Trhlík, Zhu (Andrew),
        Ludan (Josh Magnus), Xu (Hainiu), Ippolito, Callison-Burch。
        "Langmore" 和 "Ets-Hokin" 是捏造的名字。
  年份: OK
  Venue: OK (ACL 2024)
  arXiv: N/A (实际有 2405.07940，bib 未列)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[2] wang2024m4 — ❌
  标题: OK
  作者: ❌ 严重错误。bib 列出 6 人含 "Manber, Jonibek"，实际第二作者是
        "Mansurov, Jonibek"；实际论文有 15 位作者。bib 中的 Shaar, Arase,
        Derczynski 均不是该论文作者，属于捏造。
  年份: OK
  Venue: OK (EACL 2024)
  arXiv: N/A (实际有 2305.14902，bib 未列)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[3] gunasekar2023textbooks — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2306.11644)
  arXiv: OK (2306.11644)
  引用上下文: OK — related_work.tex 引用描述 Phi 系列 curated synthetic data，准确

[4] li2023textbooks2 — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2309.05463)
  arXiv: OK (2309.05463)
  引用上下文: OK — 同上，与 gunasekar2023textbooks 一起引用

[5] katharopoulos2018not — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2018)
  arXiv: N/A
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[6] ren2018learning — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2018)
  arXiv: N/A
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[7] chen2024bull — ❌
  标题: OK
  作者: ❌ 严重错误。bib 列出 "Chen Xuxi, Li Zhendong, Cai Daixuan, Yao Huanran,
        Chen Zheng, Wang Zhongming"，实际作者是 Xuxi Chen, Zhendong Wang,
        Daouda Sow, Junjie Yang, Tianlong Chen, Yingbin Liang, Mingyuan Zhou,
        Zhangyang Wang (UT Austin/Ohio State)。除第一作者外全部捏造。
  年份: OK
  Venue: OK (arXiv:2402.14270)
  arXiv: OK (2402.14270)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[8] kang2025demystifying — ❌
  标题: OK
  作者: ❌ 严重错误。bib 列出 12 人，实际作者是 Feiyang Kang, Newsha Ardalani,
        Michael Kuchnik, Youssef Emad, Mostafa Elhoushi, Shubhabrata Sengupta,
        Shang-Wen Li, Ramya Raghavendra, Ruoxi Jia, Carole-Jean Wu (Meta)。
        除第一作者外全部捏造。
  年份: OK
  Venue: OK (EMNLP 2025)
  arXiv: N/A (实际有 2510.01631)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[9] zibakhsh2025fortifai — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2509.08972)
  arXiv: OK (2509.08972)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[10] yi2025escaping — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2510.16657)
  arXiv: OK (2510.16657)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）

[11] drayson2025detection — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2502.15654)
  arXiv: OK (2502.15654)
  引用上下文: OK — 多处引用均准确（intro/related work/experiments/discussion），
              正确描述其 w=(1-q)^b 公式、SIR 方法、ModernBERT detector、grid search

[12] he2025golden — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2502.18049)
  arXiv: OK (2502.18049)
  引用上下文: OK — related_work 描述 golden-ratio reciprocal ≈0.62 作为 optimal
              real-data weight；experiments 中作为 oracle baseline 使用，准确

[13] wang2026survive — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2602.16065)
  arXiv: OK (2602.16065)
  引用上下文: OK — related_work/method/discussion 中引用其 convergence rate 结论
              作为 α_eff 质量门限的理论动机，准确

[14] shumailov2024model — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (Nature 631:755-759)
  arXiv: N/A
  引用上下文: OK — intro/related_work 引用为 model collapse 核心文献，准确

[15] dohmatob2025strong — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (实际有 2410.04840)
  引用上下文: OK — related_work "even a vanishingly small synthetic fraction
              suffices to trigger collapse"，准确

[16] vehtari2024psis — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (JMLR 25(72):1-58)
  arXiv: N/A
  引用上下文: OK — intro 引用为 ESS/stability ceiling 理论基础，准确

[17] sow2025dynamic — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (实际有 2502.06733)
  引用上下文: OK — related_work 引用其 convergence guarantees for instance-level
              reweighting under bounded weight variance，准确

[18] feng2025beyond — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (实际有 2406.07515)
  引用上下文: OK — intro 引用为 D&R (hard-filter) 方法代表，准确

[19] he2024softdedup — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ACL 2024)
  arXiv: N/A (实际有 2407.06654)
  引用上下文: 未在正文中引用（仅存在于 .bib 文件）
```

---

## 汇总

| | 数量 |
|---|---|
| 总数 | 19 |
| ✅ OK | 15 |
| ❌ 有问题 | 4 |

### 问题清单

| # | Entry | 问题 | 严重性 |
|---|---|---|---|
| 1 | `dugan2024raid` | 作者列表捏造：含虚构名字 "Andrew Langmore" 和 "Garrison Ets-Hokin"，缺少 Andrew Zhu, Josh Magnus Ludan, Hainiu Xu | **严重** |
| 2 | `wang2024m4` | 作者列表捏造："Manber" 应为 "Mansurov"；Shaar/Arase/Derczynski 不是该论文作者；实际有 15 位作者 | **严重** |
| 7 | `chen2024bull` | 作者列表捏造：除 Xuxi Chen 外全部错误，实际有 8 位作者 (含 Zhendong Wang, Daouda Sow 等) | **严重** |
| 8 | `kang2025demystifying` | 作者列表捏造：除 Feiyang Kang 外全部错误，实际作者来自 Meta (Ardalani, Kuchnik, Emad 等) | **严重** |

### 附加发现

以下 9 条 entry 仅存在于 `references.bib`，未被正文任何 `.tex` 文件引用：`dugan2024raid`, `wang2024m4`, `katharopoulos2018not`, `ren2018learning`, `chen2024bull`, `kang2025demystifying`, `zibakhsh2025fortifai`, `yi2025escaping`, `he2024softdedup`。其中 4 条有错的 entry 恰好都在未引用列表中——如果不打算引用，可以直接删除；如果要保留，必须修正作者列表。

---

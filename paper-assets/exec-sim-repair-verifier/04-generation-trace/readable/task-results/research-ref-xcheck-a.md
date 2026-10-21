# research ref xcheck A

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-xcheck-A_20260526T104640_result.json`
- **Structured JSON:** [`c1e9610db5f2c43a0505.json`](../../sessions/c1/c1e9610db5f2c43a0505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 24 web searches complete. Now compiling the verification results.

---

## 验证结果

```
[cameron2008bootstrap] ✓ 正确
[wellek2010] ✓ 正确
[moulton1990] ✓ 正确
[cohen1988] ✓ 正确
[kruschke2013bayesian] ✓ 正确
[kruschke2018rejecting] ✓ 正确
[gu2024cruxeval] ✓ 正确
[nam2025repoexec] ✓ 正确
[zhao2026genprm] ⚠️ 问题: 作者列表完全错误。bib 写的是 "Zhao, Mingyang; Liu, Yang; Yang, Lei; Chen, Liang; Li, Zhongyuan"，实际作者是 Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou (arXiv:2504.00891)。venue AAAI 2026 经 GitHub 官方仓库确认正确。
[hosseini2025genrm] ✓ 正确
[maimon2026selfexecution] ✓ 正确
[meta2025cwm] ✓ 正确
[liu2024codemind] ✓ 正确
[abdollahi2025demystifying] ✓ 正确
[venkatkrishna2026aletheia] ✓ 正确
[lee2026solidcoder] ✓ 正确
[nye2021scratchpad] ✓ 正确
[liu2023codeexecutor] ✓ 正确
[li2024redo] ✓ 正确
[shum2025swerm] ✓ 正确
[xu2025patchreasoner] ✓ 正确
[chen2025vgsearch] ✓ 正确
[snell2024scaling] ⚠️ 问题: 标题与 ICLR 2025 正式发表版不一致。bib 写 "...Scaling Model Parameters"，ICLR 2025 正式标题是 "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning"（多了 "for Reasoning"，少了 "Model"）。Oral 标注正确。
[li2025sstar] ✓ 正确
```

---

## 有问题的条目汇总

| bib key | 严重程度 | 问题描述 |
|---------|---------|---------|
| `zhao2026genprm` | **严重** | 作者列表完全捏造：5 个虚假作者名，实际论文有 11 位作者，无一匹配。venue (AAAI 2026) 正确。应替换为：`Zhao, Jian and Liu, Runze and Zhang, Kaiyan and Zhou, Zhimu and Gao, Junqi and Li, Dong and Lyu, Jiafei and Qian, Zhouyi and Qi, Biqing and Li, Xiu and Zhou, Bowen` |
| `snell2024scaling` | **中等** | 标题与 ICLR 2025 正式版不匹配。应改为 `Scaling {LLM} Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning` |

所有 24 条引用上下文均与论文内容一致，无张冠李戴。

---

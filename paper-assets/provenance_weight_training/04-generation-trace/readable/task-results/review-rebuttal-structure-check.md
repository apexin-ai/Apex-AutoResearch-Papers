# review rebuttal structure check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_rebuttal_structure_check_20260523T043046_result.json`
- **Structured JSON:** [`54a67a65f4cd05f0549f.json`](../../sessions/54/54a67a65f4cd05f0549f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这份 rebuttal 使用的是 **R10-** 前缀的 issue 编号（C1-C4, M1-M4, m1-m5），共 13 个 R10 issues。用户要求检查的是 **Round 11** 的 11 个 issue（C1-C4, W1-W4, m1-m3），编号体系不同，且 **W1-W4 在 rebuttal 中完全没有出现**。

以下是逐项检查结果：

| Issue | 有回应? | 完整度 | 需要更新/补充的内容 |
|-------|--------|--------|-------------------|
| **C1** | 不确定 | — | rebuttal 仅有 R10-C1（seed 42 resume artifact），无法确认是否对应 Round 11 C1。需提供 Round 11 review 原文才能判断。 |
| **C2** | 部分 | 需更新 | R10-M3 节有 per-seed α_eff 表格，**但 r 值为正 (+0.80)**，用户要求的关键数据是 **r = −0.80**，符号不一致。cross-seed spread = 0.0025 已包含。需确认正负号并更新。 |
| **C3** | 部分 | 需更新 | R10-C3 在 summary table 中提到"Contributions restructured"，但 **未明确写出已删除 "yielding a practical adaptive method" 这句话**。需在回应中显式说明该 overclaim 已移除。 |
| **C4** | 不确定 | — | R10-C4（downstream null）可能对应，但无法确认。 |
| **W1** | **缺失** | 0% | rebuttal 中无 W1 回应。 |
| **W2** | **缺失** | 0% | rebuttal 中无 W2 回应。 |
| **W3** | **缺失** | 0% | **4 篇引用全部未出现**：无 arXiv:2502.06733、无 Self-Influence (EMNLP 2023)、无 ToReMi (arXiv:2504.00695)、无 Wu et al. 2025 (Computational Linguistics)。 |
| **W4** | 部分 | ~30% | "Epoch confound" 节存在，但内容是**辩护 epoch confound 发现的非显然性**，并未讨论 **epoch confound 的 prior work**。需补充相关先行研究。 |
| **m1** | 不确定 | — | R10-m1（B=4 statistical reliability）可能对应，无法确认。 |
| **m2** | 不确定 | — | R10-m2（key evidence in appendix）可能对应，无法确认。 |
| **m3** | 不确定 | — | R10-m3（checklist in PDF）可能对应，无法确认。 |

**核心问题：**

1. **这份 rebuttal 是 Round 10 的回应稿**，不是 Round 11 的。W1-W4 完全缺失，C/m 的映射关系无法确认。
2. **C2 的 r 值符号矛盾**：rebuttal 写 r = +0.80，用户要求 r = −0.80。需要确认哪个是正确的。
3. **W3 的 4 篇引用完全缺失**，需要新增段落回应。
4. **W4 缺 prior work 讨论**，当前内容只是辩护，未引入前人关于 epoch confound 的工作。
5. **C3 未显式确认删除 overclaim 措辞**。

**建议：** 需要提供 Round 11 的 review 原文，才能准确建立 Round 11 issue 到 rebuttal 段落的映射，并补写 W1-W4 的回应。

---

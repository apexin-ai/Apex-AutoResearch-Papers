# research reference verification r21

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_verification_r21_20260520T150819_result.json`
- **Structured JSON:** [`b3615fa195154e54708d.json`](../../sessions/b3/b3615fa195154e54708d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

---

### 1. Wang et al. (ACL 2025) — ✅ 验证通过

| 项目 | 结果 |
|------|------|
| **Anthology ID** | `2025.acl-long.624` ✅ 存在 |
| **URL** | https://aclanthology.org/2025.acl-long.624/ |
| **arXiv** | https://arxiv.org/abs/2502.15208 |
| **实际 Title** | "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" ✅ 与声称一致 |
| **作者** | Zhilin Wang, Yafu Li, Jianhao Yan, Yu Cheng, Yue Zhang |
| **发表状态** | ACL 2025 (Volume 1: Long Papers), pp. 12740–12755, Vienna, Austria, July 2025 |
| **Abstract 摘要** | 该论文从动力系统理论视角分析 LLM 的连续改写行为。发现 LLM 在反复改写（successive paraphrasing）过程中会收敛到稳定的周期状态（如 2 周期吸引子环），限制了语言多样性。这归因于 LLM 的自我强化特性——在迭代中偏好并放大某些文本形式。即使增加生成随机性或交替使用不同 prompt/模型，这种模式依然存在。 |

---

### 2. Shahriar et al. (2025) — ✅ 验证通过

| 项目 | 结果 |
|------|------|
| **arXiv ID** | `2512.05311` ✅ 存在 |
| **URL** | https://arxiv.org/abs/2512.05311 |
| **实际 Title** | "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?" ✅ 与声称一致（声称标题为简写，完整标题含副标题） |
| **作者** | Sadat Shahriar, Navid Ayoobi, Arjun Mukherjee (University of Houston) |
| **发表状态** | arXiv preprint, 2025年12月4日提交 |
| **"25.4%" 数字** | ✅ 确认存在。原文 abstract 明确写道：detection performance declining by an average of **25.4%** after five consecutive paraphrasing stages |
| **Abstract 摘要** | 随着 LLM 日益被用作研究代理，区分 LLM 与人类生成的科学想法变得至关重要。虽然检测 LLM 生成文本已被广泛研究，但区分人类与 LLM 生成的科学**想法**仍是未探索领域。本文系统评估了 SOTA 机器学习模型在连续改写后区分人类与 LLM 生成想法的能力。结果显示：经过 5 轮连续改写后，检测性能平均下降 25.4%；将研究问题作为上下文信息纳入可提升检测性能至多 2.97%。 |

---

两篇论文均 ✅ 验证通过，标题、作者、ID 均与声称一致，关键数字（25.4%）确认存在于原文中。

Sources:
- [Wang et al. - ACL Anthology](https://aclanthology.org/2025.acl-long.624/)
- [Wang et al. - arXiv](https://arxiv.org/abs/2502.15208)
- [Shahriar et al. - arXiv](https://arxiv.org/abs/2512.05311)

---

# research arxiv verification r6

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_arxiv_verification_r6_20260518T015913_result.json`
- **Structured JSON:** [`192ba4f05da01ae78749.json`](../../sessions/19/192ba4f05da01ae78749.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

---

### 论文 1: `2504.05419`

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 |
| **真实标题** | "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification" |
| **标题匹配** | 部分匹配 — 声称标题是完整标题的前半部分，省略了副标题 |
| **真实作者** | Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He |
| **作者匹配** | **不匹配** — 声称 "Stechly et al."，实际第一作者为 Anqi Zhang，作者列表中无 Stechly |
| **相关性** | **高度相关** — 直接研究 reasoning model hidden states 中的 correctness probing，用于 self-verification |
| **结论** | **MISMATCH** — ID 和标题真实，但作者归属错误 |

---

### 论文 2: `2510.21285`

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 |
| **真实标题** | "When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models" |
| **标题匹配** | 匹配 — 声称标题是完整标题的主标题部分 |
| **真实作者** | Yingzhi Mao, Chunkang Zhang, Junxiang Wang, Xinyan Guan, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun |
| **作者匹配** | **匹配** — 第一作者确为 Mao，提交于 2025 年 10 月 |
| **相关性** | **相关** — 研究 reasoning model 的安全失败模式（Self-Jailbreak），提出 Chain-of-Guardrail 框架 |
| **结论** | **VERIFIED** |

---

### 论文 3: `2605.13772`（2026 年 5 月）

| 项目 | 结果 |
|------|------|
| **存在性** | 存在 — 提交于 2026-05-13（5 天前） |
| **真实标题** | "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry" |
| **标题匹配** | 匹配 — 声称标题是完整标题的主标题部分 |
| **真实作者** | Tyler Alvarez, Ali Baheri |
| **作者匹配** | 声称中未提供具体作者，无法判断匹配性 |
| **相关性** | **极高相关** — 用 hidden-state transport geometry 做 step-level hallucination detection，与 contrastive trace safety 直接相关（contrastive PCA lens + geometric transition features） |
| **结论** | **VERIFIED** |

---

### 汇总

| 论文 | ID | 结论 | 问题 |
|------|-----|------|------|
| 1 | 2504.05419 | **MISMATCH** | 作者错误：实际为 Zhang et al.，非 Stechly et al. |
| 2 | 2510.21285 | **VERIFIED** | — |
| 3 | 2605.13772 | **VERIFIED** | 2026 年本月论文，确实存在 |

Sources:
- [2504.05419 - Reasoning Models Know When They're Right](https://arxiv.org/abs/2504.05419)
- [2510.21285 - When Models Outthink Their Safety](https://arxiv.org/abs/2510.21285)
- [2605.13772 - Where Does Reasoning Break?](https://arxiv.org/abs/2605.13772)

---

# paper fix citation attributions

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-citation-attributions_20260515T203100_result.json`
- **Structured JSON:** [`42704b2eb596484efc4a.json`](../../sessions/42/42704b2eb596484efc4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean. Here's the complete modification log:

### 修改清单

| # | 文件 | 修改内容 | 状态 |
|---|------|----------|------|
| 1 | `introduction_scenarioC.tex:6` | "object appearance changes, lighting variation, sensor noise" → "visual and physical perturbations such as lighting variation, background changes, and sensor noise" | **已修正** |
| 2 | `introduction_scenarioC.tex:13` | A2C2: "learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control" → "adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection" | **已修正** |
| 3 | `related_work.tex:18` | A2C2: "learns a lightweight correction head that runs at every control step..." → "adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation..." | **已修正** |
| 4 | `related_work.tex:48` | PLD: "bounded corrections ($[-\xi, \xi]$)" → "a magnitude bound $\xi$ tuned per benchmark" | **已修正** |
| 5 | `related_work.tex:51` | PLD summary: "fixed action bounds" → "per-benchmark magnitude bounds" | **已修正** |
| 6 | `method.tex:86` | PLD: "bounds residual actor corrections within a fixed range during RL training" → "introduces a magnitude bound $\xi$ for the residual actor, tuned per benchmark, during off-policy RL training" | **已修正** |
| 7 | `references.bib:311` | zhou2025acp_cbf: "Hao Zhou and Yanze Zhang and others" → "Hao Zhou and Yanze Zhang and Wenhao Luo" | **已修正** |

### 已确认无需修改（之前已正确）

| # | 项目 | 当前状态 |
|---|------|----------|
| 1 | chen2026reconvla (intro/method/related) | 已正确描述为 CQR-based UQ + OOD detection |
| 3 | digflow2025 (related) | 已正确描述为 representation-level gating |
| 4 | silver2018residual (intro/related) | 无 "bounded corrections" 归因，已使用 "zero-initialization" |
| 5 | pan2025drc (related) | 已正确描述为 per-correction-event exponential decay |
| 7 | zollo2025vla_calibration (bib) | 已为 "Thomas Zollo" |
| 9 | srpo2025 (related) | 已正确描述 successful/failed trajectory 对比 |
| 10 | jiang2024transic (related) | 已正确描述为 "conditioned on the current state" |
| 12 | gu2025safe (related) | 已正确描述为 "triggering intervention" |

7 处实际修改，5 处确认已正确。全部 12 项引用归因问题已解决。

---

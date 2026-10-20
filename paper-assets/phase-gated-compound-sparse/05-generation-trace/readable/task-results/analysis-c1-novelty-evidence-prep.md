# analysis c1 novelty evidence prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1_novelty_evidence_prep_20260515T201816_result.json`
- **Structured JSON:** [`e614a2dd68f71bd165cb.json`](../../sessions/e6/e614a2dd68f71bd165cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已完成：`artifacts/novelty_evidence_summary.md`（已注册为 `art_20260515_4691d7`）。

**内容概要：**

| 证据 | 支撑度 | 核心数字 |
|------|--------|----------|
| E1: Phase-CoT alignment | Strong | κ=0.887, transition=1 token |
| E2: n=500 dose-response | Strong | DS D=0.39→8.48, QW D=0.07→3.16, all p<1e-14 |
| E3: GSM8K cross-benchmark | Strong/Moderate | DS monotonic PASS; QW s030 truncation caveat |
| E4: LLaMA cross-architecture | Moderate | d_z=1.00–1.12 (all large), monotonic, n=50 |
| E5: sf5 asymmetric | Strong | D=+19.13/+18.25, direction fully robust |

末尾附 ~150 词 paper-ready English text，描述 phase alignment finding，含 κ=0.887、transition distance=1 token、thinking/answer sparsity 分布、paired t 检验等具体数字，可直接用于 §3 或 §5。

---

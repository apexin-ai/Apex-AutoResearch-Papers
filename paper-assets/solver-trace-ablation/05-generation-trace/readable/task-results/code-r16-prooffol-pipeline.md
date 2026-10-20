# code r16 prooffol pipeline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16-prooffol-pipeline_20260520T054743_result.json`
- **Structured JSON:** [`0faa226a11178573558f.json`](../../sessions/0f/0faa226a11178573558f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `/root/autodl-tmp/outputs/prooffol_pipeline_details.json`. Here's the summary:

## ProofFOL Pipeline Details

### 来源
- **原始数据集**: ProofWriter (depth 1–5)
- **FOL 翻译**: GPT-4o 银标准翻译 + Prover9 验证 (arXiv:2409.16461, GitHub: RamyaKeerthy/Translation-NL2FOL)
- **Pipeline 阶段**: 10,424 train + 600 test → 10,332 成功解析 (0.9% 跳过) → 我们采样 500 train + 100 eval (seed=42)

### ProofFOL vs FOLIO 对比

| 指标 | ProofFOL (train 500) | FOLIO (train 500) |
|------|---------------------|-------------------|
| FOL premises | 18.2 ± 3.2 (8–25) | 5.3 ± 1.4 (2–10) |
| Ground facts | 10.2 ± 3.0 | 1.8 ± 1.5 |
| Rules | 8.1 ± 1.1 | 3.5 ± 1.9 |
| XOR (⊕) samples | 0 | 186 (37.2%) |
| Depth 主要分布 | d4=187, d5=165 | d2=257, d3=176 |
| Answer 分布 | T=180/F=144/U=176 | T=183/F=157/U=160 |

关键差异：ProofFOL 问题复杂度显著高于 FOLIO（平均 18.2 vs 5.3 个 FOL premise，depth 4–5 为主 vs depth 2–3），但谓词语义简单（`Blue(x)`, `Rough(x)` 等 ProofWriter 风格）；FOLIO 使用真实世界谓词且包含 XOR 约束（37.2%），ProofFOL 无 XOR。

---

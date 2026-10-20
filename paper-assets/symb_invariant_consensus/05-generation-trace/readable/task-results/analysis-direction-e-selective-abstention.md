# analysis direction e selective abstention

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_direction-e-selective-abstention_20260520T074201_result.json`
- **Structured JSON:** [`0878b1c0882198c9be0b.json`](../../sessions/08/0878b1c0882198c9be0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Direction E 完成。核心发现：

## 结果汇总

**AUROC**: 0.673 (mean over 2 seeds) — entropy 是 SC 错误的中等强度预测器。

### Coverage Table (Multi-seed Aggregate, Mistral-7B, FOLIO-204)

| Coverage | N | Random SC | Entropy SC (mean±std) | Δ vs Random |
|----------|---|-----------|-----------------------|-------------|
| 100% | 204 | 54.4% | 54.4% ± 0.0% | +0.0pp |
| 90% | 184 | 54.5% | 56.8% ± 0.8% | +2.3pp |
| 80% | 163 | 54.5% | 58.9% ± 0.6% | +4.4pp |
| 70% | 143 | 54.4% | 62.2% ± 1.4% | +7.8pp |
| 60% | 122 | 54.5% | 64.3% ± 2.0% | +9.8pp |
| 50% | 102 | 54.4% | 67.6% ± 2.9% | +13.3pp |

**关键结论**：
- 弃权最不确定的 20% 问题（coverage=80%）→ SC accuracy 从 54.4% 升至 ~59%，+4.4pp
- 弃权 50% → accuracy 升至 ~67.6%，+13.3pp，显著高于 random abstention
- Entropy 和 majority_fraction 效果相当，entropy 略优（在 seed=42 上 70.6% vs 69.6% at 50% coverage）
- SICA 在 confident 子集上（exp033, seed=42）表现与 SC 趋同甚至相同，说明一致性高时 symbolic 约束无额外增益
- 实用价值明确：即使只弃权 30% 问题，accuracy 提升 ~8pp

**输出文件**：
- 服务器: `/root/symb_invariant_consensus/results/direction_e_abstention/results.json`
- 本地: `artifacts/direction_e_abstention_results.json`
- 脚本: `artifacts/direction_e_abstention.py` (及服务器 `scripts/direction_e_abstention.py`)

---

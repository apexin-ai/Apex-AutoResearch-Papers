# experiment rg combo verifier

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_rg-combo-verifier_20260520T113113_result.json`
- **Structured JSON:** [`2422c1ef157399258a20.json`](../../sessions/24/2422c1ef157399258a20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇报：

## Baselines
| Method | Acc | Correct/204 |
|--------|-----|-------------|
| SC | 54.41% | 111 |
| SICA | 59.31% | 121 |
| NLI standalone | 49.51% | 101 |

## Combo 策略结果

**最佳策略: `nli_sc_vote_w5`** — NLI 作为 5 票加入 SC 投票 → **60.29%** (123/204), +5.88% vs SC (p<0.05), +0.98% vs SICA

| 策略 | Acc | Delta/SC | Delta/SICA |
|------|-----|----------|------------|
| **nli_sc_vote_w5** | **60.29%** | **+5.88%*** | **+0.98%** |
| nli_sc_vote_w3 | 58.82% | +4.41% | -0.49% |
| intersection_sica_fallback | 59.31% | +4.90%* | +0.00% |
| intersection_sc_fallback | 57.35% | +2.94%* | -1.96% |
| cascade_nli (所有阈值) | 50-57% | 负 | 负 |
| cascade_sica (所有阈值) | 55-56% | 微正 | 负 |
| sica_nli_weighted | 57-59% | +2~4% | 负 |
| **Oracle 上限** | **75.49%** | +21.08% | +16.18% |

## 关键发现

1. **SICA-NLI 一致率仅 47.5%** (97/204)，但一致时准确率 70.10% — 远高于任一单独方法
2. **不一致时 SICA 显著强于 NLI**: 53 vs 33 correct (21 both wrong)
3. **NLI 高置信度不可靠**: conf≥0.8 时仅 56.35% — cascade 策略因此全面失败
4. **Oracle 上限 75.49%** 说明两个信号互补性很强，但当前没有好的仲裁器
5. NLI 作为 SC 额外投票 (w=5) 是唯一超过 SICA 的策略，但提升微弱 (+0.98%, 不显著 vs SICA)

**结论**: NLI 单独太弱 (49.51%)，直接信任 NLI 的策略（cascade）全部失败。只有当 NLI 作为轻量投票融入 SC 时才有微弱正向效果。等 G decoupling 全量结果就绪后，用 SICA-G 替换 SICA 可能有更好的互补效果。

---

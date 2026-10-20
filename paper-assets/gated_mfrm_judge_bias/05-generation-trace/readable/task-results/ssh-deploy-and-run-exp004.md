# ssh deploy and run exp004

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy_and_run_exp004_20260522T175816_result.json`
- **Structured JSON:** [`870b92eb6ca5a32e6c59.json`](../../sessions/87/870b92eb6ca5a32e6c59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果 JSON 已验证。

## 结果总结

| Method | Kendall-τ | Spearman-ρ | Source |
|---|---|---|---|
| raw_average | 0.786 | 0.905 | exp-004 |
| cyclic_judge | 0.786 | 0.905 | exp-004 |
| cyclic_judge_discard | 0.786 | 0.905 | exp-004 |
| dcr_factor | 0.786 | 0.905 | exp-004 |
| preference_leakage | 0.786 | 0.905 | exp-004 |
| mfrm_only | 0.786 | 0.905 | exp-003 |
| sequential | 0.786 | 0.905 | exp-003 |
| **joint_gmfrm** | **0.857** | **0.952** | exp-003 |

**关键发现**：所有5个简单baseline产生了完全一致的模型排名（8个模型的排序未变）。θ 的绝对值虽有差异（judge correction / exposure weighting 改变了scale），但排名保持不变 → τ 和 ρ 完全相同。

这在方法论上是可以解释的：
1. **preference_leakage** 数学上等价于 raw_average（减去 judge-model bias 后重新平均，bias 项消掉）
2. **cyclic_judge** 在 judge 分配近似均衡时不改变排名（9 judges × 8 models，覆盖率 44.7%，各 model 的 judge 组合差异不足以翻转排名）
3. **dcr_factor / discard** exposure 分数是 item 级别的，不区分 model → 对所有 model 施加相同方向的调整

只有 **joint G-MFRM**（结构化建模 contamination × model 交互）才将 τ 从 0.786 提升到 0.857 — 支持了"需要联合建模"的核心论点。

结果路径：`/root/gated_mfrm_judge_bias/exp004/results/results.json`

---

# code fisher test script

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fisher-test-script_20260515T214454_result.json`
- **Structured JSON:** [`500425932b82d61afb62.json`](../../sessions/50/500425932b82d61afb62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## Dry-run 结果（seed=42）

### 主要对比：obs_only_norm0.1 (19/100) vs argmin_K10 (12/100)
| 指标 | 值 |
|------|-----|
| Fisher exact p-value | **0.2408** (n.s.) |
| Odds ratio | 1.720 |
| Absolute diff | +7.0% |
| Bootstrap 95% CI | [-3.0%, +17.0%] |

### obs_only_0.2 (最佳) vs 其他方法汇总

| Method A | Method B | SR_A | SR_B | Diff | p-val | Sig | 95% CI |
|----------|----------|------|------|------|-------|-----|--------|
| obs_only_0.2 | obs_only_0.1 | 22% | 19% | +3% | 0.7264 | n.s. | [-8%, +14%] |
| obs_only_0.2 | argmin_K10 | 22% | 12% | +10% | 0.0892 | n.s. | [-1%, +20%] |
| obs_only_0.2 | VLA_only_K1 | 22% | 12% | +10% | 0.0892 | n.s. | [-1%, +20%] |
| obs_only_0.2 | VLA_mean_K10 | 22% | 12% | +10% | 0.0892 | n.s. | [-1%, +20%] |
| obs_only_0.2 | perdof_0.1 | 22% | 11% | +11% | 0.0556 | n.s. | [+0%, +21%] |
| obs_only_0.2 | scalar_0.1 | 22% | 9% | +13% | **0.0180** | * | [+3%, +23%] |

**结论**：仅 seed=42 的 100 trials 下，只有 obs_only_0.2 vs scalar_0.1 达到 p<0.05 显著。其余对比因样本量不足未达显著——pooling seed=43 的 200 trials 后 power 会提升。

**脚本位置**：`/root/acr-vla-conformal-refinement/src/analysis/fisher_test.py`

seed=43 完成后直接用文件模式跑：
```bash
python src/analysis/fisher_test.py --results_dir logs/ --benchmark object --seeds 42 43 --all_pairs
```

---

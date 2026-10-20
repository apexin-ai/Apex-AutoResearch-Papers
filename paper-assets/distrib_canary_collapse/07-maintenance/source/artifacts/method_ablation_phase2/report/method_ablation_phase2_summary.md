Phase 2 结果摘要（详见服务器 results/method_ablation_phase2_report.md）

Method × Alpha Sig Rates (BH FDR-corrected):
| α | naive | diff | threshold | permG | TY |
|---|-------|------|-----------|-------|-----|
| 0.00 | 100% | 37.5% | 62.5%† | 0% | 0% |
| 0.25 | 100% | 25% | 37.5%† | 0% | 37.5% |
| 0.50 | 100% | 100% | 100%† | 0% | 0% |
| 1.00 | 100% | 100% | 100%† | 75% | 59.4% |

†threshold_onset 为非统计检验（无 p-value），FDR 不适用，数字等同 raw。

> Raw significance (uncorrected), shown for comparison:
> | α | naive | diff | threshold | permG | TY |
> |---|-------|------|-----------|-------|-----|
> | 0.00 | 100% | 50% | 62.5% | 0% | 0% |
> | 0.25 | 100% | 25% | 37.5% | 25% | 62.5% |
> | 0.50 | 100% | 100% | 100% | 25% | 0% |
> | 1.00 | 100% | 100% | 100% | 75% | 59.4% |
>
> 关键 FDR 翻转: α=0.25 permG 25%→0%, α=0.50 permG 25%→0%, α=0.25 TY 62.5%→37.5%, α=0.00 diff 50%→37.5%

Cohen κ = 0.185 (poor agreement)
Decision flips: naive vs permG 50%, naive vs TY 57%, α=0.0 naive vs permG 100%

数据来源: d028_fpr_null_control_full.json (phase2_fdr_sig_rates section), BH FDR α=0.05

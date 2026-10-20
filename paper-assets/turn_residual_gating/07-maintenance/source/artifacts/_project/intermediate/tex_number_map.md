# D048 Eval Results → Paper Number Update Map

> Multi-seed results 出来后，按此映射秒级更新论文数字。
> 格式: `文件:行号` | 当前值 | 更新为 | 数据来源

## Abstract (paper/sections/abstract.tex:2)
| 当前值 | 更新为 | 来源 |
|--------|--------|------|
| `20--33$\times$ gap` | multi-seed mean±std gap | AR N=50 all conditions |
| `0.015--0.025` | mean±std range from 3 seeds | d048_*_s{42,123,456} AR eval |
| `1.57$\times$` | SS 3-seed mean±std gap | d048_ss_s{42,123,456} AR eval |
| `27$\times$ by median` | keep (Llama single seed) | eval_llama_ar_n20 |

## Introduction (paper/sections/introduction.tex)
| 行 | 当前值 | 更新为 | 来源 |
|----|--------|--------|------|
| 3 | `70.8\%` | keep (Phase 1 diagnostic) | phase1 |
| 3 | `0.0418 at turn~1 to 0.0122` | keep (Phase 1) | phase1 |
| 16 | `0.015--0.025` | multi-seed AR GAR range | d048 AR N=50 |
| 16 | `0.75\,pp spread` | multi-seed TF spread | d048 TF eval |
| 16 | `0.016 to 0.318 (20$\times$)` | SS 3-seed mean±std | d048_ss |
| 16 | `${\sim}$31$\times$ gap to 1.57$\times$` | SS 3-seed mean gap | d048_ss |

## Experiments — Table 1 (paper/sections/experiments.tex:23-36)
| Cell | 当前值 | 更新为 | 来源 |
|------|--------|--------|------|
| Base AR | 0.012 | N=50 median±CI | d048_eval_existing base |
| TG AR | 0.016 | N=50 median±CI | d048_eval_existing tg_s42 |
| +PCGrad AR | 0.015 | N=50 median±CI | d048_eval_existing pcgrad_s42 |
| UG AR | 0.015 | N=50 median±CI | d048_eval_existing ug_s42 |
| LO AR | 0.025 | N=50 median±CI | d048_eval_existing lo_s42 |
| Caption | N=5 | N=50 | — |

## Experiments — Text (paper/sections/experiments.tex)
| 行 | 当前值 | 更新为 |
|----|--------|--------|
| 12 | `0.75 percentage points (pp)` | multi-seed TF spread |
| 16 | `20--33$\times$ gap` | multi-seed gap range |
| 16 | `$0.504\pm0.001$` | 3-seed TF GAR mean±std |
| 16 | `$0.016\pm0.001$` | 3-seed AR GAR mean±std |
| 16 | `${\sim}$31$\times$ (range 30.5--32.1$\times$)` | 3-seed gap mean±std |
| 21 | `$N$\,=\,5 ten-turn` | `$N$\,=\,50` |

## Discussion (paper/sections/discussion.tex)
| 行 | 当前值 | 更新为 | 来源 |
|----|--------|--------|------|
| 5 | `0.016 to 0.318 (20$\times$)` | SS 3-seed mean±std | d048_ss |
| 5 | `${\sim}$31$\times$ gap to 1.57$\times$` | SS 3-seed mean gap | d048_ss |
| 5 | `AR GAR\,=\,0.418 (gap 1.20$\times$)` | update or remove (was 2nd seed) | d048_ss_s123 |

## Steering results (experiments.tex:49-53)
- N=50 steering numbers likely unchanged (already N=50 scale)
- Only update if new AR baseline (beta=0) changes with N=50 eval

## Key JSON → tex field mapping
```
eval_phase2_gar.py output:
  avg_gar_per_turn → TF GAR per-turn (Fig 4)
  mid_turns_avg_gar → TF GAR mid-turn (Table 1 TF columns)
  avg_ppl → PPL (Table 1)

eval_attention_steering.py output (mode=gen):
  per_conversation[*].gar_per_turn → AR GAR per-turn
  median of mid-turn values → AR GAR (Table 1 AR column)
  bootstrap_ci → confidence interval

Gap ratio = TF mid-turn GAR / AR mid-turn median GAR
```

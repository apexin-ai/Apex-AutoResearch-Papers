# exp_fewnerd_n16_s42_v2 状态检查

## 进程状态
- GONE (PID 32117 已不存在)

## 结论
- **正常完成**。report.json 已生成（May 21 23:14），samples.jsonl 行数 37648 与 num_instances 一致。

## 指标

### 核心指标
| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.7885 |
| oracle_f1 | 0.9059 |
| oracle_headroom | 0.1173 |
| instances | 37648 |
| verdict | FAIL |

### 一致性信号
| 指标 | 值 |
|------|-----|
| fleiss_kappa_mean | 0.3784 |
| soft_jaccard_mean | 0.6431 |
| sample_f1_mean | 0.5975 |
| sample_f1_std | 0.3988 |
| sample_f1_pct_zero | 25.15% |
| structural_beats_surface | true |
| rho_advantage | 0.0478 |

### 相关性指标 (full / conditional)
| 指标 | full | conditional |
|------|------|-------------|
| rho_fleiss_vs_f1 | 0.1630 | -0.0194 |
| rho_softjaccard_vs_f1 | 0.2109 | 0.2126 |

### Logprob baseline (full / conditional)
| 指标 | full | conditional |
|------|------|-------------|
| rho | 0.1396 | 0.1755 |
| tau | 0.1027 | 0.1299 |
| auroc | 0.5690 | 0.5770 |

### 过滤统计
| 指标 | 值 |
|------|-----|
| n_gold_empty_filtered | 5083 |
| n_greedy_f1_zero_filtered | 3885 |

## 产出文件
| 文件 | 大小 | 时间 |
|------|------|------|
| report.json | 1.7 KB | May 21 23:14 |
| samples.jsonl | ~1.2 GB (37648 lines) | May 21 23:13 |

## 备注
- verdict 为 FAIL，verdict_note: "MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold"
- soft_jaccard 在 full 和 conditional 下均优于 fleiss_kappa（structural_beats_surface=true）
- logprob baseline 的 conditional rho (0.1755) 低于 soft_jaccard conditional rho (0.2126)，结构化一致性信号仍有优势

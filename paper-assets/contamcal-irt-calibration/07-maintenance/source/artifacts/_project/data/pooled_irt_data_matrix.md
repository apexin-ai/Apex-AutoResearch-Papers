## Pooled IRT Data Matrix — 2026-05-15

### 总体
- 总 eval 目录（有结果）: 52
- 非 deprecated: 48
- Aligned + 非 deprecated（主矩阵）: 35（去重）

### 按 Benchmark 可用 N
| Benchmark | Aligned N | IRT 可用 N | 排除规则 |
|-----------|-----------|-----------|---------|
| MMLU | 35 | 25 | 排除 0.5B (D045 position bias) |
| GSM8K | 35 | 22 | 排除 d000 (D044 format confound) |
| ARC | 0 | 0 | 完全缺失（待核实） |
| HumanEval | 0 | 0 | 完全缺失（待核实） |

### 按 Scale 分布
| Scale | N | 含 para |
|-------|---|---------|
| 0.5B | 12 | 4 para |
| 0.5B-Instruct | 1 | 0 |
| 1.5B | 10 | 4 para |
| 3B | 12 | 5 para |

### 结构性缺口
- 1.5B d005/d025 s123 aligned: 空（SFT 仍在跑）
- 3B d000/d005 s123 aligned: 空（eval 仍在跑）
- 3B d000 v3 s42 aligned: 空

CSV: /root/autodl-tmp/exp001/eval_summary_matrix.csv
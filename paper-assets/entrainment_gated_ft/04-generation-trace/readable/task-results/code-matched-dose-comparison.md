# code matched dose comparison

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_matched_dose_comparison_20260519T055535_result.json`
- **Structured JSON:** [`84d1a8d5bc8a939b510b.json`](../../sessions/84/84d1a8d5bc8a939b510b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成。下面是完整分析结果：

## 核心发现（匹配剂量 h3-1，8层 attention）

### 1. Overall Accuracy
| Model | Acc |
|---|---|
| GDN-pure | 54.30% (2798) |
| GDN-h3-1 | 51.33% (2645) |
| HGRN2-pure | 48.42% (2495) |
| HGRN2-h3-1 | 51.39% (2648) |

### 2. Attention Effect（关键发现：方向相反）

**GDN h3-1**: attention **伤害**了模型
- Helped: 462 (9.0%), Hurt: 615 (11.9%), **Net: -153**

**HGRN2 h3-1**: attention **帮助**了模型
- Helped: 548 (10.6%), Hurt: 395 (7.7%), **Net: +153**

这和之前用 h12-1 的结论完全不同。GDN 加 8 层 attention（h3-1 配置）反而降低了 LAMBADA accuracy，而 HGRN2 加同样比例的 attention 则受益。

### 3. Jaccard Overlap（极低）
- **Helped overlap**: J = 0.100 (intersection=92, union=918)
- **Hurt overlap**: J = 0.088 (intersection=82, union=928)

两架构的 attention 影响几乎作用在**不同的样本**上。

### 4. Cross-table
```
                    HGRN2-hurt  HGRN2-unch  HGRN2-helped
GDN-hurt               82       428       105
GDN-unchanged         257      3468       351
GDN-helped             56       314        92
```

注意 GDN-hurt & HGRN2-helped = 105，GDN-helped & HGRN2-hurt = 56，说明有一批样本上两架构的 attention 产生了相反效果。

### 5. Length Analysis
所有长度 bin 上 GDN 的 net effect 都是负的，HGRN2 都是正的。效果与长度方向一致但不特别突出。

### 6. Logprob Shifts
- GDN: 整体 mean delta = -0.21（attention 降低了 logprob）
- HGRN2: 整体 mean delta = +0.14（attention 提升了 logprob）

产出文件：
- 图表: `analysis/lambada_matched_comparison.png` / `.pdf`
- CSV: `analysis/lambada_matched_per_example.csv`
- 脚本: `analysis/lambada_matched_comparison.py`

---

# exp-020 Pythia Greedy AUC=0.8838 异常调查 (2026-05-16)

## 结论
**非 bug。Pythia-1.4B greedy continuation 产生级联重复坍塌，1v2 AUC 测量的是"重复程度是否还在恶化"。K*=2 不受影响。**

## 1. 文本质量：严重 repetition collapse
| 指标 | depth_0 | depth_1 | depth_2 |
|------|---------|---------|---------|
| 4-gram 重复率 | 0.0132 | **0.7237** | **0.8063** |
| TTR | 0.7213 | **0.1875** | **0.1444** |

## 2. 参数：正确
`--no_sample` → `do_sample=False`，无意外温度/top_p 覆盖。

## 3. 数据泄漏：无
- depth_1∩depth_2 hash 重叠 36/5000 (<1%)，greedy 确定性导致，非主因
- GroupKFold doc_id 分组正确

## 4. 特征分布 (Cohen's d top-2)
| 特征 | |d| | depth_1 mean | depth_2 mean |
|------|-----|-------------|-------------|
| hapax_ratio | **1.056** | 0.316 | 0.089 |
| low_freq_ratio | **1.029** | 0.391 | 0.128 |

## 5. 机制
- depth_0→1: greedy 重复严重 (TTR 0.72→0.19), AUC=0.999
- depth_1→2: 重复进一步加剧 (TTR 0.19→0.14), AUC=0.884
- depth_2+→3/4/5: 触底 (纯重复循环), AUC≈0.52

## 建议
论文中标注 greedy 为 "repetition-dominated regime"，与 nucleus 分开讨论。greedy 价值在于展示 K*=2 对 repetition collapse 的鲁棒性。

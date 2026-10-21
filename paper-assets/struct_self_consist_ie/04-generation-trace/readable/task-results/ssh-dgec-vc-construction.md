# ssh dgec vc construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dgec-vc-construction_20260520T083908_result.json`
- **Structured JSON:** [`06d14344925152365ad1.json`](../../sessions/06/06d14344925152365ad1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已注册为 `art_20260520_fea42e`。

## 汇总（19 unique configs，去重后）

| 维度 | Sig+ (p<0.05) | Sig- (p>0.95) | NS |
|------|:---:|:---:|:---:|
| **总计** | **6** | **7** | **6** |

### 按数据集

| Dataset | configs | Sig+ | Sig- | NS | mean Δ (pp) |
|---------|:---:|:---:|:---:|:---:|---:|
| fewnerd | 8 | 3 | 4 | 1 | -0.15 |
| wnut17 | 3 | 2 | 0 | 1 | +0.92 |
| scierc | 4 | 1 | 0 | 3 | +0.80 |
| conll | 4 | 0 | 3 | 1 | -0.30 |

### 按模型/模式

| Model/Mode | configs | Sig+ | Sig- | NS | mean Δ (pp) |
|------------|:---:|:---:|:---:|:---:|---:|
| qwen25_7b/ft | 6 | 3 | 1 | 2 | +0.44 |
| qwen25_7b/ft_exp | 7 | 2 | 2 | 3 | +0.15 |
| qwen25_72b/zs | 3 | 1 | 2 | 0 | +0.04 |
| qwen25_72b/fs | 3 | 0 | 2 | 1 | -0.09 |

### 关键观察

- VC-weighted construction 效果**不一致**：6 个 config 显著正，7 个显著负，胜负基本持平
- **wnut17 和 scierc** 偏向正面（小数据集、低 degeneracy），**conll** 全面负面（高 degeneracy + 高 baseline）
- **72b zero-shot/few-shot** 模型几乎全负——高 degeneracy（33-61%）时 VC weighting 退化为 majority vote，反而丢信息
- fewnerd/ft_exp/seed789 在两台服务器上有重复数据，结果一致（均为 sig-），已标注

---

# code exp15 roberta large

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp15-roberta-large_20260519T081337_result.json`
- **Structured JSON:** [`1f2651b131108b012b73.json`](../../sessions/1f/1f2651b131108b012b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部实验完成。结果有一个意外发现：**RoBERTa-large vanilla 在 ActorAttack 上表现异常好 (F1=1.000)**，而 9class DAPT 反而更低 (0.946)。这与 RoBERTa-base 和 DeBERTa 的模式完全相反。

## exp15 RoBERTa-large 结果

### DD OOD (Macro F1, mean±std, 3 seeds)
| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| RoBERTa-large vanilla | 0.878±0.033 | 0.888±0.045 | 0.915±0.040 | 0.918±0.038 | 0.927±0.036 |
| RoBERTa-large 9class | **0.965±0.019** | **0.930±0.046** | **0.960±0.037** | **0.981±0.013** | **0.987±0.004** |
| RoBERTa-base vanilla (参考) | 0.913 | - | - | - | 0.981 |
| RoBERTa-base 9class (参考) | 0.987 | - | - | - | 0.994 |
| DeBERTa vanilla (参考) | 0.628 | 0.389 | 0.389 | 0.312 | 0.312 |
| DeBERTa 9class (参考) | 0.990 | 0.972 | 0.972 | 0.997 | 0.997 |

### ActorAttack (Macro F1, mean±std, 3 seeds)
| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| RoBERTa-large vanilla | **0.977±0.012** | **0.984±0.005** | **0.990±0.000** | **0.997±0.005** | **1.000±0.000** |
| RoBERTa-large 9class | 0.718±0.060 | 0.800±0.055 | 0.881±0.058 | 0.940±0.059 | 0.946±0.057 |
| RoBERTa-base vanilla (参考) | 0.410±0.126 | 0.425±0.143 | 0.432±0.144 | 0.466±0.144 | 0.466±0.163 |
| RoBERTa-base 9class (参考) | 0.738±0.033 | 0.805±0.033 | 0.884±0.066 | 0.925±0.066 | 0.939±0.046 |
| DeBERTa vanilla (参考) | 0.337 | - | 0.284 | - | 0.258 |
| DeBERTa 9class (参考) | 0.773 | - | 0.921 | - | 0.972 |

### Capacity vs DAPT 分析

**关键发现 — 结果颠覆预期：**

1. **DD OOD**: DAPT 仍有优势 (0.987 vs 0.927 Full)，与 base 模式一致
2. **ActorAttack**: **vanilla 反超 9class** (1.000 vs 0.946)。RoBERTa-large vanilla 达到完美 F1=1.0，远超 RoBERTa-base vanilla (0.466)
3. **容量效应巨大**: RoBERTa-large vanilla AA Full=1.000 vs RoBERTa-base vanilla 0.466，说明 model capacity 对 OOD 泛化影响极大
4. **DAPT 对 large 模型在 AA 上反而有害**: 9class F1=0.946 < vanilla F1=1.000。可能的解释：DAPT 对大模型引入了不必要的 bias，而大模型本身的通用表征已足够强

这个结果对论文 framing 有重要影响：DAPT 的优势可能在较大模型上不再普遍成立，至少在 ActorAttack 场景下如此。

---

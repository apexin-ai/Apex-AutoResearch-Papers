# code exp16 precision recall full

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-precision-recall-full_20260520T061320_result.json`
- **Structured JSON:** [`2176476380ca898cf962.json`](../../sessions/21/2176476380ca898cf962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。现在计算。

**关键发现：F1=0.422 实际来自 attack-only (80样本) 的 macro F1，不是 118 样本。** 因为 attack-only 数据没有 benign 样本，class 0 F1=0，macro F1 = class1_F1/2，人为减半。

以下通过组合 dd_ood（80 attack）+ mixed_test 中 benign 部分（38 benign）= 118 样本重新计算：

---

## exp16 DD OOD (80 attack + 38 benign = 118 samples)

### 9-class:
```
seed42:  TP=49 FP=0  TN=38 FN=31  P=1.000 R=0.613 F1=0.760
seed123: TP=75 FP=0  TN=38 FN=5   P=1.000 R=0.938 F1=0.968
seed456: TP=54 FP=1  TN=37 FN=26  P=0.982 R=0.675 F1=0.800
mean(macro): P=0.834±0.076  R=0.866±0.073  F1=0.818±0.096
mean(jailbreak-class): P=0.994±0.009  R=0.742±0.157  F1=0.843±0.109
```

Per-class detail (seed-averaged):
- **Jailbreak**: P=0.994, R=0.742 → 几乎不误报benign，但漏检率25.8%
- **Benign**: P=0.674, R=0.991 → benign几乎全部正确识别

### vanilla:
```
seed42:  TP=2  FP=4  TN=34 FN=78  P=0.333 R=0.025 F1=0.047
seed123: TP=3  FP=8  TN=30 FN=77  P=0.273 R=0.038 F1=0.066
seed456: TP=17 FP=9  TN=29 FN=63  P=0.654 R=0.213 F1=0.321
mean(macro): P=0.360±0.090  R=0.454±0.031  F1=0.291±0.065
mean(jailbreak-class): P=0.420±0.170  R=0.092±0.090  F1=0.144±0.129
```

Per-class detail (seed-averaged):
- **Jailbreak**: P=0.420, R=0.092 → 几乎检测不到DD攻击
- **Benign**: P=0.300, R=0.816 → 大量attack被误判为benign，拉低benign precision

---

## 核心结论

**F1=0.422 是 attack-only macro F1 的伪影**（0 benign → class0 F1=0 → macro减半）。实际 9-class 在 118 样本上 macro F1=0.818。

**9-class 模型瓶颈是 jailbreak recall（0.742±0.157）**，不是 precision。Precision 接近完美（0.994），说明模型很少把 benign 误判为 jailbreak，但有 ~26% 的 DD 攻击被漏检。seed 间方差大（recall 从 0.613 到 0.938），说明模型对 DD OOD 的泛化不稳定。

**vanilla 模型在 DD OOD 上几乎完全失效**：jailbreak recall 仅 9.2%，绝大多数 DD 攻击被当成 benign。

---

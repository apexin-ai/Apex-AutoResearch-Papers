# code exp16 exp17 full reeval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-exp17-full-reeval_20260520T062220_result.json`
- **Structured JSON:** [`524df3888e3b8a406a05.json`](../../sessions/52/524df3888e3b8a406a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。整理最终报告。

---

## 1. 评估集组成

```
DD OOD:   80 attack (deceptive_delight_all.jsonl) + 38 benign (from IID test) = 118 total
AA OOD:   80 attack (actorattack_all.jsonl) + 38 benign = 118 total
FITD OOD: 80 attack (fitd_all.jsonl) + 38 benign = 118 total

exp16 benign来源: data/mixed_llm/test.jsonl (38 benign)
exp17 benign来源: data/expanded_1000/test.jsonl (75 benign) → OOD set = 155 total
exp1  benign来源: data/plan_002_splits/test.jsonl (38 benign) → OOD set = 118 total
```

## 2. exp16 (mixed-LLM 500) — 修正后指标

### DD OOD (80 attack + 38 benign = 118):
| Variant | 修正后 F1 (mean±std) | 修正后 P | 修正后 R | 旧值 (attack-only) |
|---------|---------------------|---------|---------|-------------------|
| 9-class | **0.818±0.096** | 0.834±0.076 | 0.866±0.073 | 0.422 |
| MLM | 0.289±0.101 | 0.404±0.312 | 0.443±0.051 | 0.024 (!) |
| vanilla | 0.291±0.065 | 0.360±0.090 | 0.454±0.031 | 0.024 (!) |

Per-seed 9class: [0.735, **0.953**, 0.766]

### AA OOD (80 attack + 38 benign = 118):
| Variant | 修正后 F1 (mean±std) | 旧值 (attack-only) |
|---------|---------------------|-------------------|
| 9-class | **0.504±0.107** | 0.175 |
| MLM | 0.258±0.075 | — |
| vanilla | 0.389±0.073 | — |

Per-seed 9class: [0.449, 0.653, 0.410]

### FITD OOD (80 attack + 38 benign = 118):
| Variant | F1 (mean±std) |
|---------|---------------|
| 9-class | **0.997±0.005** |
| MLM | 0.679±0.188 |
| vanilla | 0.867±0.022 |

## 3. exp17 (expanded 1000) — 无需修正

exp17 的 `eval_exp17.py` 已正确加入 benign（`dd_test = dd_jb + test_benign`），数据集为 80 attack + 75 benign = 155。结果无需修正。

已有结果：
| Variant | DD OOD F1 (mean±std) | AA OOD F1 (mean±std) |
|---------|---------------------|---------------------|
| 9-class | **0.889±0.041** | **0.913±0.041** |
| MLM | 0.334±0.010 | 0.351±0.017 |
| vanilla | 0.326±0.000 | 0.508±0.087 |

Per-seed 9class DD: [0.843, 0.883, 0.942]
Per-seed 9class AA: [0.870, 0.903, 0.968]

## 4. exp1 基准确认

```
exp1 DD OOD:  dataset = 80 attack + 38 benign = 118, metric = f1_macro
  9-class (RoBERTa): F1 = 0.994 mean (per-seed: 1.000, 0.990, 0.990) — CONFIRMED correct
  MLM:               F1 = 0.987 mean
  vanilla:           F1 = 0.981 mean

exp1 AA OOD:  dataset = 80 attack + 38 benign = 118, metric = f1_macro
  9-class (RoBERTa): F1 = 0.939 mean (from exp2_actorattack_ood.json rob_9class)
```

exp1 评估**没有**伪影问题——`plan_002_seed123_dd_eval.py` 显示 DD OOD 正确使用了 `dd_convs + test_benign`。

## 5. 结论

**哪些论文数字需要修正：**

1. **exp16 DD OOD 全部需修正**（旧 eval 是 attack-only）：
   - 9-class: 0.422 → **0.818** (+94% 相对提升，绝对 +0.396)
   - MLM: 0.024 → 0.289
   - vanilla: 0.024 → 0.291

2. **exp16 AA OOD 全部需修正**：
   - 9-class: 0.175 → **0.504** (+188% 相对提升)

3. **exp16 FITD OOD** — 新结果，之前未评估过：9-class **0.997**

4. **exp17 无需修正** — 评估脚本已正确

5. **exp1 无需修正** — 评估脚本已正确

**关键发现：** 旧 eval 的 attack-only 数据中，MLM/vanilla 模型把几乎所有 attack 样本预测为 benign（78/80），导致旧 macro F1 仅 0.024（近似为 0）。这不是模型性能极差，而是评估集完全缺失 benign 类导致 class 0 F1=0，macro F1 被减半。修正后，9-class 变体在 DD OOD 上表现显著好于 MLM/vanilla（0.818 vs ~0.29），验证了多任务学习对 OOD 泛化的贡献。

**结果已保存至：** `results/exp16_balanced_ood_reeval.json`

---

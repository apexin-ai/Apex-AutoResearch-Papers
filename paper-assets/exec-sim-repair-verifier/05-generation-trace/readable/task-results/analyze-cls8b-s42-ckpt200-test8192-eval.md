# analyze cls8b s42 ckpt200 test8192 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls8b-s42-ckpt200-test8192-eval_20260515T105735_result.json`
- **Structured JSON:** [`e55656076c158a48b2cf.json`](../../sessions/e5/e55656076c158a48b2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总如下：

---

## 实验 1: cls8b-s42-ckpt200-test8192-eval

| 指标 | 值 |
|---|---|
| **Accuracy** | **70.07%** (低于 majority baseline 73.0%，差 -2.9pp) |
| F1 macro | 68.18% |
| pass F1 / P / R | 75.9% / 91.8% / 64.7% |
| fail F1 / P / R | 60.4% / 47.0% / 84.5% |
| Unparseable | 0 |
| 样本数 | 9784 (pass=7138, fail=2646) |
| 报错 | 无，EXIT_CODE=0 |
| wandb | 无 |

**Confusion matrix:**
```
              Predicted
              fail    pass
Actual fail   2235     411
Actual pass   2517    4621
```

**分析:** ckpt-200 是最早的 checkpoint，accuracy 70.07% **低于 majority baseline**，是 s42 test sweep 中最差的点。模型严重 over-predict fail（2517 个 pass 被误判为 fail），fail recall 高 (84.5%) 但 precision 极低 (47.0%)。

### s42 test sweep 完整曲线

| Checkpoint | Test Accuracy |
|---|---|
| ckpt-200 | **70.07%** ← 本次 |
| ckpt-400 | 84.79% |
| ckpt-600 | 82.75% |
| ckpt-800 | 83.57% |
| ckpt-1000 | 83.52% (val-best) |
| ckpt-1200 | 84.74% |
| ckpt-1400 | **85.47%** (test-best) |
| ckpt-1600 | 84.37% |

ckpt-200 明显欠拟合，200→400 步有 ~15pp 的跳升。

---

## 实验 2: cls8b-seed123-ckpt6600-test-eval

| 指标 | 值 |
|---|---|
| **Accuracy** | **84.90%** (+11.9pp over majority) |
| F1 macro | 77.58% |
| pass F1 / P / R | 90.4% / 84.3% / 97.4% |
| fail F1 / P / R | 64.8% / 87.8% / 51.3% |
| Unparseable | 0 |
| 样本数 | 9784 (pass=7138, fail=2646) |
| 报错 | 无，EXIT_CODE=0 |
| wandb | 无 |

**Confusion matrix:**
```
              Predicted
              fail    pass
Actual fail   1357    1289
Actual pass    188    6950
```

**分析:** ckpt-6600 的 test accuracy 84.90%，与 seed123 ckpt-3000 (val-best) 的 85.60% 接近，差 0.7pp。fail recall 偏低 (51.3%)，但 fail precision 很高 (87.8%) — 与 s42 ckpt-200 的模式完全相反（s42-200 是高 recall 低 precision）。

---

# analysis cls8b s42 ckpt1000 test seq2048 ablation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-s42-ckpt1000-test-seq2048-ablation_20260515T112800_result.json`
- **Structured JSON:** [`322789037a1f82974390.json`](../../sessions/32/322789037a1f82974390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个日志均无 W&B run id，无错误。结果汇总：

---

## 实验 1: cls8b-s42-ckpt1000-test-seq2048-ablation

| 指标 | 值 |
|------|-----|
| **Accuracy** | **82.83%** |
| **F1 macro** | **76.88%** |
| fail: P / R / F1 | 72.2% / 59.3% / 65.2% |
| pass: P / R / F1 | 85.9% / 91.5% / 88.6% |
| Unparseable | 136 |
| 错误 | 无 |
| W&B run id | 无 |

**结论: SUCCESS** — CLS@2048 accuracy=82.83% 仍大幅超越 CWM 4B test=58.04%（+24.8pp），与 CLS@8192=83.52% 仅差 0.69pp。**seq_length confound 被排除**：缩短 seq_length 从 8192→2048 几乎不影响 CLS 性能，证明 CLS 的优势不是来自更长的输入序列。

---

## 实验 2: cls8b-seed123-ckpt6633-test-eval

| 指标 | 值 |
|------|-----|
| **Accuracy** | **84.89%** |
| **F1 macro** | **77.56%** |
| fail: P / R / F1 | 87.8% / 51.2% / 64.7% |
| pass: P / R / F1 | 84.3% / 97.4% / 90.4% |
| Unparseable | 0 |
| 错误 | 无 |
| W&B run id | 无 |

**结论: SUCCESS** — seed123 final ckpt-6633 test accuracy=84.89%，高于 seed42 的 83.52%，进一步确认 CLS 8B 在不同 seed 下的稳定性。注意 fail recall 仅 51.2%（高 precision 87.8% 但低 recall），说明 seed123 更保守——更少误报但漏检更多。

---

### 交叉对比总结

| 配置 | Accuracy | F1 macro |
|------|----------|----------|
| CLS 8B s42 ckpt-1000 @8192 | 83.52% | — |
| CLS 8B s42 ckpt-1000 @2048 | 82.83% | 76.88% |
| CLS 8B seed123 ckpt-6633 @full | 84.89% | 77.56% |
| CWM 4B (baseline) | 58.04% | — |

---

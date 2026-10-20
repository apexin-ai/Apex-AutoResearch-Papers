# eval deberta combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deberta-combo_20260522T185051_result.json`
- **Structured JSON:** [`c89fb63a290ee7c0dc70.json`](../../sessions/c8/c89fb63a290ee7c0dc70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

---

## 1. Standalone Eval

| Metric | Value |
|--------|-------|
| **Overall accuracy** | **99.67% (598/600)** |
| False | 200/200 = 100.00% (P=0.9901, F1=0.9950) |
| True | 200/200 = 100.00% (P=1.0000, F1=1.0000) |
| Unknown | 198/200 = 99.00% (P=1.0000, F1=0.9950) |
| Pred distribution | True=200, False=202, Unknown=198 |

2 个错误均为 Unknown 被预测为 False。

## 2. Combo with LLaMA-3.1-8B (SC baseline=72.50%)

| Weight | Accuracy | Δ(combo−SC) | McNemar p |
|--------|----------|-------------|-----------|
| w=1 | 76.00% | +3.50pp | <0.0001 *** |
| w=3 | 84.17% | +11.67pp | <0.0001 *** |
| w=5 | 91.67% | +19.17pp | <0.0001 *** |

互补性：NLI↑SC↓=164, SC↑NLI↓=1, 同意率=72.50%, 同意时准确率=99.77%

## 3. Combo with Mistral-7B (SC baseline=39.17%)

| Weight | Accuracy | Δ(combo−SC) | McNemar p |
|--------|----------|-------------|-----------|
| w=1 | 42.33% | +3.17pp | <0.0001 *** |
| w=3 | 52.17% | +13.00pp | <0.0001 *** |
| w=5 | 65.50% | +26.33pp | <0.0001 *** |

互补性：NLI↑SC↓=365, SC↑NLI↓=2, 同意率=38.83%, 同意时准确率=100%

## 4. 最佳 Combo 配置推荐

**LLaMA-8B + DeBERTa w=5** 是最佳配置：91.67% accuracy，比 SC baseline 提升 +19.17pp，所有提升 p<0.0001。Mistral SC baseline 太弱（39.17%），即使 w=5 也只到 65.50%，实用价值有限。

## 5. GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 0 MiB | 0% | 空闲（DeBERTa eval 已完成） |
| cuda:1 | 88,263 MiB / 97,887 MiB | **0%** | vLLM (PID 595559) |
| cuda:2 | 90,213 MiB / 97,887 MiB | **96%** | vLLM (PID 510289) — 活跃 |
| cuda:3 | 88,263 MiB / 97,887 MiB | **0%** | vLLM (PID 613436) |

**cuda:1 和 cuda:3 有 vLLM 进程占用 ~88GB 显存但 GPU 利用率为 0%**，属于空闲占用。

---

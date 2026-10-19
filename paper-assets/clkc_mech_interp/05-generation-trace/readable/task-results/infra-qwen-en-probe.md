# infra qwen en probe

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen_en_probe_20260521T171606_result.json`
- **Structured JSON:** [`98e88ccf787ae0346adf.json`](../../sessions/98/98e88ccf787ae0346adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## EN→EN 探针基线结果

| 指标 | 值 |
|------|-----|
| Peak accuracy | **63.03%** (layer 17) |
| Binomial p-value | 0.000035 (显著高于 chance 50%) |
| 80% gate | **FAIL** |

**每层 accuracy 分布**：大部分层在 50-58% 之间，中间层（8, 15-23）稍高至 60-63%，没有任何层接近 80%。

**结论**：EN→EN 方向的线性探针 accuracy 只有 63%，远未达到 80% 的 gate。虽然统计上显著高于随机（binomial p < 0.001），但信号非常弱。后续跨语言迁移实验的上限被 within-language baseline 限制，意义有限。

Permutation test 已在后台运行（PID 22829），完成后结果会覆盖到 `data/qwen3/probe_results.json`。

输出文件：
- `data/qwen3/probe_results.json`
- `data/qwen3/probe_accuracy_by_layer.png`
- `logs/probe_qwen_en.log`

---

# code bootstrap seed probe

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_seed_probe_20260521T224419_result.json`
- **Structured JSON:** [`b079b6647447d6d6095f.json`](../../sessions/b0/b079b6647447d6d6095f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型 bootstrap 全部完成。结果汇总：

## Bootstrap Probe Results (20 seeds, training set resampling)

| 模型 | 方向 | balanced_acc (mean±std) | F1 (mean±std) | peak_layers 众数 |
|------|------|------------------------|---------------|-------------------|
| **Llama-3.1** | EN→EN | 0.7730±0.0104 | 0.7701±0.0113 | 分散（19最多） |
| | ZH→ZH | 0.7088±0.0131 | 0.7096±0.0146 | 13-15 |
| | EN→ZH | 0.6441±0.0224 | 0.6910±0.0306 | 13 为主 |
| | ZH→EN | 0.7098±0.0266 | 0.7341±0.0239 | 分散（9,14,15,16） |
| **Qwen-3** | EN→EN | 0.7542±0.0188 | 0.7511±0.0186 | 18-22 |
| | ZH→ZH | 0.7170±0.0212 | 0.7231±0.0271 | 21 为主 |
| | EN→ZH | 0.6569±0.0259 | 0.6560±0.0468 | 22 为主 |
| | ZH→EN | 0.7309±0.0251 | 0.7237±0.0409 | 19-21 |

## COMET 进度

- **Qwen**: back-translation 320/798 (~40%)
- **Llama**: back-translation 320/1096 (~29%)
- 无 validated 文件产出

## 产出文件

- `data/llama31/probe_results_bootstrap.json`
- `data/qwen3/probe_results_bootstrap.json`
- 原有 `probe_results.json` 未被覆盖（用了 `--output_file` 参数）

---

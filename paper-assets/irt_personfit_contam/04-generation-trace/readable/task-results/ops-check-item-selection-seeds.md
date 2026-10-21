# ops check item selection seeds

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-item-selection-seeds_20260523T145838_result.json`
- **Structured JSON:** [`f306faf67557c34a8167.json`](../../sessions/f3/f306faf67557c34a8167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 模型 | Item selection seed | 来源文件 |
|------|-------------------|----------|
| **Llama** | **42** | `ctrl_contam_pilot/prepare_data.py` |
| **Qwen** | **42** | `anon_repo/qwen/prepare_data.py` |
| **Mistral** | **999** | `ctrl_contam_mistral/prepare_data.py` |

**Mistral 不一致。** Mistral 的 `rng_contam = random.Random(999)`，而 Llama 和 Qwen 都是 `random.Random(42)`。

注意 Mistral 脚本注释写的是 `"seed=999 (same as Llama for cross-model comparability)"`，这条注释是错误的——Llama 实际用的是 42，不是 999。seed 不同意味着 Mistral 的 contaminated item subset 与 Llama/Qwen 的不同（虽然都是从同一个 MMLU 14042 items 中抽取，但 shuffle 顺序不同）。

---

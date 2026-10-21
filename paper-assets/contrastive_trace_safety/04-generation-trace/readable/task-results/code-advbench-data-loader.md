# code advbench data loader

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_advbench_data_loader_20260519T193651_result.json`
- **Structured JSON:** [`6bba5c89c13ffe8af0da.json`](../../sessions/6b/6bba5c89c13ffe8af0da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出：
- **`/root/autodl-tmp/contrastive_trace_safety/src/advbench/data_loader.py`** (293 行)

核心接口与 HarmThoughts pipeline 完全兼容：
- `prepare_dataset()` → 返回 `{"jailbreak_with_commitment", "jailbreak_no_commitment", "safe"}` 三类 trace dict
- `split_data()` → 同签名、同 RNG 行为（60/20/20，seed=42）
- trace dict 字段完全对齐：`trace_id`, `sentences`, `labels`, `query`, `is_jailbreak`, `num_steps`, `commitment_point`, `step_labels`
- `load_trace_hidden_states()` / `load_all_hidden_states()` — 按 layer_idx 加载 .pt
- `load_text_embeddings()` / `load_all_text_embeddings()` — 加载 .pkl

字段映射：
| AdvBench (generate_traces) | → | HarmThoughts 兼容字段 |
|---|---|---|
| `steps` | → | `sentences` |
| `prompt` | → | `query` |
| CP annotation `is_jailbreak` | → | `is_jailbreak` |
| CP annotation `commitment_point` | → | `commitment_point` + `step_labels` |

待上游数据就绪（traces 生成 + CP 标注），下游 bootstrap/probe 代码可直接 `from src.advbench.data_loader import prepare_dataset, split_data` 替换导入即可运行。

---

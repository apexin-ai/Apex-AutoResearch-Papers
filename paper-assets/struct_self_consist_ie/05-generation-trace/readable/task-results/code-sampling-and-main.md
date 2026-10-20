# code sampling and main

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sampling_and_main_20260514T042643_result.json`
- **Structured JSON:** [`aecb0eb6fd2844153bbe.json`](../../sessions/ae/aecb0eb6fd2844153bbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建：

- **`sampling.py`** — `VLLMSampler` 类（vLLM lazy import，无 vLLM 时可 import 模块）、`build_uie_prompt`（支持 ner/eae/full）、`parse_extraction_output`（带 JSON fallback）、`run_sampling_pipeline`（含 greedy baseline）、`save/load_sampled_results`。XGrammar 通过 `GuidedDecodingParams(json=UIE_JSON_SCHEMA)` 集成。

- **`run_mvp_pilot.py`** — 完整 CLI 主脚本，argparse 参数齐全，支持 `--skip_sampling` 复用已有结果。流程：加载数据 → 采样 → 一致性打分 → greedy/oracle F1 → Spearman 相关性 → PASS/MARGINAL/FAIL 判定 → JSON 报告。

---

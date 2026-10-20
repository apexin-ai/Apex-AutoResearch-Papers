# code prep 1 7b no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_1_7b_no_evidence_eval_20260519T065335_result.json`
- **Structured JSON:** [`c81f7539194ff0228d12.json`](../../sessions/c8/c81f7539194ff0228d12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，所有参数解析正确。

**结果：**

- 脚本路径：`/root/autodl-tmp/freige/scripts/seed_expansion/eval_1_7b_no_evidence.sh`
- Dry-run 验证：参数全部正确解析，`no_evidence = True`，`quantize = False`
- 关键参数：
  - `--model_path`: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1`（s42 RSFT）
  - `--no_evidence`: 已启用
  - `--output_dir`: `/root/autodl-tmp/eval_outputs/eval_1_7b_rsft_no_evidence`
  - `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 已设置
  - 脚本中未写 `CUDA_VISIBLE_DEVICES`（提交时外部指定）

---

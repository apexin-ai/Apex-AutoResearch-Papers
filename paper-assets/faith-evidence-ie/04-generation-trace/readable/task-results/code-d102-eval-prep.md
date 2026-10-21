# code d102 eval prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d102_eval_prep_20260518T085116_result.json`
- **Structured JSON:** [`2c6ee21c038888492020.json`](../../sessions/2c/2c6ee21c038888492020.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册（`art_20260518_9c5f1a`）。

**4 个 eval 命令已准备完毕：**

| exp_id | 模型 | Checkpoint | GPU |
|--------|------|-----------|-----|
| `d102_1_7b_k1_eval` | Qwen3-1.7B k1 s42 | checkpoint-567 | cuda:0 |
| `d102_8b_k1_s42_eval` | Qwen3-8B k1 s42 | checkpoint-1134 | cuda:1 |
| `d102_8b_k1_s43_eval` | Qwen3-8B k1 s43 | checkpoint-1134 | cuda:2 |
| `d102_llama_k1_eval` | LLaMA-3.1-8B k1 s42 | checkpoint-1107 | cuda:3 |

命令格式参照 `plan_006_qwen3_1_7b_rsft_eval_r2` 和 `plan_006_llama_rsft_r3_eval` 两个成功实验。每个命令已包含 `CUDA_VISIBLE_DEVICES`（C002）。提交前需 `nvidia-smi` 确认 4 卡空闲（C001）。预计每个 eval ~2.5h，4 个可并行。

---

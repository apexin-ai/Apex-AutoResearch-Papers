# code prep remaining scripts

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_remaining_scripts_20260514T174849_result.json`
- **Structured JSON:** [`a961ee3963d57c2c06d3.json`](../../sessions/a9/a961ee3963d57c2c06d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法检查通过。汇总：

| 脚本 | 模型 | 解码参数 | 数据目录 | Checkpoint 目录 | 日志 |
|------|------|----------|----------|----------------|------|
| `run_pipeline_pythia_topk50.sh` | Pythia-1.4B (`query_key_value`) | `--decoding_strategy topk --top_k 50` | `data/pythia_topk50/` | `checkpoints/pythia_topk50/` | `logs/pipeline_pythia_topk50.log` |
| `run_pipeline_olmo_temp09.sh` | OLMo-1B-hf (`q_proj,k_proj,v_proj`) | `--decoding_strategy temp_only --temperature 0.9` | `data/olmo_temp09/` | `checkpoints/olmo_temp09/` | `logs/pipeline_olmo_temp09.log` |
| `run_pipeline_olmo_topk50.sh` | OLMo-1B-hf (`q_proj,k_proj,v_proj`) | `--decoding_strategy topk --top_k 50` | `data/olmo_topk50/` | `checkpoints/olmo_topk50/` | `logs/pipeline_olmo_topk50.log` |
| `run_pipeline_gpt2xl_temp09.sh` | GPT-2 XL (`c_attn,c_proj`) | `--decoding_strategy temp_only --temperature 0.9` | `data/gpt2xl_temp09/` | `checkpoints/gpt2xl_temp09/` | `logs/pipeline_gpt2xl_temp09.log` |
| `run_pipeline_gpt2xl_topk50.sh` | GPT-2 XL (`c_attn,c_proj`) | `--decoding_strategy topk --top_k 50` | `data/gpt2xl_topk50/` | `checkpoints/gpt2xl_topk50/` | `logs/pipeline_gpt2xl_topk50.log` |

所有脚本统一使用 `data/depth_0.jsonl`（共享种子数据）做 depth-0 微调，生成步骤从 depth-1 起写入各自独立目录。支持 `GPU=1 bash script.sh` 指定 GPU。

---

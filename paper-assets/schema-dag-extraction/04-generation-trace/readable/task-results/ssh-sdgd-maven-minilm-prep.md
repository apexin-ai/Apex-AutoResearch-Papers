# ssh sdgd maven minilm prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sdgd-maven-minilm-prep_20260515T105359_result.json`
- **Structured JSON:** [`c59a292dfba092df9894.json`](../../sessions/c5/c59a292dfba092df9894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出清单：

| 产出 | 状态 |
|------|------|
| `artifacts/maven_minilm_embeddings.pt` | [168, 384] dict |
| `artifacts/maven_minilm_sim_matrix.pt` | [168, 168] dict, mean=0.2161, std=0.1030 |
| `scripts/run_sdgd_maven_minilm.sh` | 两阶段脚本，4 modes |
| `scripts/compute_maven_minilm.py` | MiniLM 计算脚本（已用） |
| CPU decompose dry-run | 4 modes 全部通过 |

**SDGD-zero decomposition 结果**：168 types → 18 batches，tau=0.3191（mean+1std），最大 batch 39 types，最小 1 type。

**启动 GPU 阶段**（等 exp-008 跑完后）：
```bash
bash scripts/run_sdgd_maven_minilm.sh
```
或者只跑 Stage 2（decomposition 已生成）：
```bash
cd /root/schema-dag-extraction
python3 src/sdgd_extract_gpu.py \
  --decompositions artifacts/exp_maven_minilm/decomposition_*.json \
  --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ \
  --types_file configs/maven_event_types.json \
  --dataset maven --task event --prompt_version v2 \
  --max_samples 1000 --output_dir artifacts/exp_maven_minilm \
  --max_model_len 4096
```

---

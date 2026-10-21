# ssh exp004 code prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp004-code-prep_20260515T055256_result.json`
- **Structured JSON:** [`eb13c15a1cf9c77a16ec.json`](../../sessions/eb/eb13c15a1cf9c77a16ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 修改/新增文件
1. **`src/maven_utils.py`** — MAVEN parquet 数据加载器（`load_maven()`, `get_all_types()`）
2. **`configs/maven_event_types.json`** — 从 list 转为 dict（168 types, `{type_name: human_readable}`）
3. **`src/run_extraction.py`** — 新增 `build_prompt_v2_event()` / `build_prompt_v1_event()` event detection prompts；`run_extraction()` 新增 `task` 参数
4. **`src/run_experiment.py`** — 新增 `--dataset maven`、`--data_path`、`--sim_matrix_path`；dataset-aware 数据加载、BCS matrix key 兼容（`similarity_matrix` / `sim_matrix`）；输出文件名含 dataset tag

### Dry-run 结果
```
100 samples, 76 active types, 3 batches (low/high/random at count=6)
count_6_low_bcs:  text_match_F1=0.1159, BCS=0.9464
count_6_high_bcs: text_match_F1=0.1176, BCS=0.9603
count_6_random_0: text_match_F1=0.0741, BCS=0.9205
Total extraction: 118.8s
```

### 完整实验命令（exp2）

```bash
cd /root/schema-dag-extraction && python3 src/run_experiment.py \
  --mode exp2 \
  --dataset maven \
  --prompt_version v2 \
  --eval_mode text_match \
  --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ \
  --types_file configs/maven_event_types.json \
  --data_path data/maven_parquet/valid.parquet \
  --embeddings_path artifacts/maven_type_embeddings_qwen3.pt \
  --sim_matrix_path artifacts/maven_bcs_matrix_qwen3.pt \
  --max_model_len 4096
```

exp2 配置：count=6 和 count=12，每个 count 含 25 random + 1 low-BCS + 1 high-BCS = 54 batches × 8042 samples。

---

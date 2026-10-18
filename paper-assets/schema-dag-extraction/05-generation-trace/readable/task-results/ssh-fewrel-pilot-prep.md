# ssh fewrel pilot prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-pilot-prep_20260515T062022_result.json`
- **Structured JSON:** [`bbf08511e6f1f9fd9374.json`](../../sessions/bb/bbf08511e6f1f9fd9374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 结果汇总

**新增/修改文件：**

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/fewrel_utils.py` | 新增 | FewRel 数据加载器：`load_fewrel()`, `get_all_relation_types()`, `sample_balanced()` |
| `src/run_extraction.py` | 修改 | 新增 `build_json_schema_re()`, `build_prompt_v2_re()`, `build_prompt_v2_re_batch()`；`run_extraction()` 新增 `task="re"` 分支 |
| `src/run_experiment.py` | 修改 | `--dataset` 新增 `fewrel` 选项，自动加载 FewRel 数据并设 `task="re"` |
| `src/run_fewrel_pilot.py` | 新增 | 自包含 pilot 脚本，含 ST embedding、BCS batch 构建、vLLM RE 推理、accuracy 评估 |

**Pilot 脚本 CLI：**
```
python3 src/run_fewrel_pilot.py --dry-run          # 仅构建 batch，不用 GPU
python3 src/run_fewrel_pilot.py --model_path &lt;path> # 实际推理
  --n_samples 200      # 采样数（默认200，balanced）
  --counts 4,8,16      # relation count per batch
  --num_random 3       # 每个 count 的 random batch 数
```

**Dry-run 结果：**
- 192 samples（12/rel × 16 relations）
- 15 batches（3 count levels × {low_bcs, high_bcs, 3 random}）
- BCS range: low=0.42 ~ high=0.97（对比显著）
- 总推理量: 468 次
- **预估 GPU 时间: ~12 min**（@1.5s/sample，Qwen3-32B-FP8）

**产出文件**（已生成到 `artifacts/fewrel_pilot/`）：
- `batch_config.json` — 批次配置
- `relation_sim_matrix.pt` — 关系相似度矩阵

---

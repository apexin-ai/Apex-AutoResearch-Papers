# code graspune setup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_graspune-setup_20260514T085903_result.json`
- **Structured JSON:** [`d9a26a17a99e8c126d40.json`](../../sessions/d9/d9a26a17a99e8c126d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRASPrune Baseline 准备报告

### 状态：就绪

### 产出文件

| 文件 | 作用 |
|------|------|
| `/root/GRASPrune/` | 官方 repo（已 clone） |
| `/root/GRASPrune/data.py` | 已 patch，添加 GSM8K 校准数据支持 |
| `/root/recovery_aware_struct_prune/src/run_graspune.sh` | Wrapper 脚本（剪枝 + 格式转换） |
| `/root/recovery_aware_struct_prune/src/convert_graspune_to_hf.py` | GRASPrune → HF 格式转换器 |
| `/root/recovery_aware_struct_prune/src/model_utils.py` | 已扩展，支持 per-layer attention 维度 |

### 兼容性

- **torch/transformers 版本**：GRASPrune 标注 torch==2.7.0 / transformers==4.51.0，实际在 torch==2.10.0 / transformers==5.8.0 下所有 import 正常
- **GSM8K 校准数据**：7473 samples → 2716 blocks（512 tokens），验证通过
- **输出格式适配**：GRASPrune 输出 `pruned_state_dict.safetensors` + `meta.json`（含 per-layer MLP + attention 维度），转换脚本将其转为带 `per_layer_intermediate_size` / `per_layer_num_heads` / `per_layer_num_kv_heads` 的 HF 目录格式，可被 `model_utils.load_pruned_model()` 直接加载

### 关键差异（vs 我们的 RASP 剪枝）
- GRASPrune 同时剪 MLP **和** attention KV groups（我们只剪 MLP）
- 有 rescale compensation 阶段
- 模型路径确认：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`

### 运行方式
```bash
# GPU 空闲后执行
bash /root/recovery_aware_struct_prune/src/run_graspune.sh
```
输出到 `/root/recovery_aware_struct_prune/models/pruned_graspune_35/`，可直接接 `train_grpo.py` 做 RLVR。

---

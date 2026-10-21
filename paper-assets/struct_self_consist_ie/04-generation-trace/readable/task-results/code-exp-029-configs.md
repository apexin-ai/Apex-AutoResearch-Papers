# code exp 029 configs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_029_configs_20260517T233240_result.json`
- **Structured JSON:** [`9ae4b260f4c463f9b7a3.json`](../../sessions/9a/9ae4b260f4c463f9b7a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出汇报

### 配置文件

| 配置 | 路径 | epochs | output_dir |
|------|------|--------|------------|
| exp_029a (3-epoch) | `train_config_scierc_3ep.yaml` | 3.0 | `checkpoints/qwen3-8b-scierc-3epoch-lora` |
| exp_029b (10-epoch) | `train_config_scierc_10ep.yaml` | 10.0 | `checkpoints/qwen3-8b-scierc-10epoch-lora` |

### 与 ft_002_v2 的一致性确认

以下参数完全一致：
- 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- 数据: `scierc_uie_train` / `scierc_uie_dev`
- LoRA: r=32, alpha=64, target=all
- 训练: batch=2, grad_accum=8, lr=2e-4, cosine scheduler, warmup=0.1
- 其他: seed=42, cutoff_len=2048, bf16

### 后处理工具链状态

`scripts/exp_028_postprocess/` 提供完整 pipeline（merge → inference → analysis），结构为：
1. `01_merge_lora.sh` — LoRA 合并
2. `02_inference.sh` — N=8 采样推理
3. `03_analyze.py` — 结果分析
4. `run_all.sh` — 一键执行

该工具链为 Few-NERD 设计，SciERC 复用时需修改数据集路径和 output 目录，但核心逻辑（merge → sample → analyze）可直接适配。

---

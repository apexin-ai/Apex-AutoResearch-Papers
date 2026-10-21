# prep mmlu eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mmlu_eval_20260523T064606_result.json`
- **Structured JSON:** [`e2ddd4a3de40588d5220.json`](../../sessions/e2/e2ddd4a3de40588d5220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed successfully. GPU is now nearly free (5.6GB used — SS training appears to have finished). Here's the summary report.

---

## MMLU 5-shot 评估环境准备完成

### 环境
- **lm-evaluation-harness**: v0.4.12 (pip)
- **Python**: 3.12.3 (conda base)
- **GPU**: NVIDIA RTX PRO 6000 Blackwell, 98GB — 当前空闲（5.6GB used）
- **HF mirror**: `HF_ENDPOINT=https://hf-mirror.com`（服务器无法直连 HuggingFace）
- **MMLU 数据集**: 已缓存到 `/root/autodl-tmp/.hf_cache`

### Checkpoint 路径 (全部为 LoRA adapter)

| 条件 | 路径 | gate_params.pt |
|------|------|----------------|
| **base_qwen** | `none`（直接用 base model） | — |
| **lo_s42** | `runs/phase2_lora_only_s42/lora/` | 无 |
| **tg_v7_s42** | `runs/phase2_tg_s42_v7/lora/` | 有 |
| **ug_s42** | `runs/phase2_ug_s42/lora/` | 有 |
| **pcgrad_v9_s42** | `checkpoints/tg_v9_pcgrad_s42/lora/` | 有 |
| **ss_v8b_s42** | `runs/d048_ss_s42/lora/` | 有 |

- Base model: `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`
- 所有 adapter 配置一致: LoRA r=16, alpha=32, target q_proj+v_proj
- Gate weights 存在但对 MMLU（单轮 QA）无影响，直接用 LoRA adapter 即可

### 脚本

| 脚本 | 用法 |
|------|------|
| `scripts/mmlu_eval_single.sh` | `bash scripts/mmlu_eval_single.sh &lt;adapter_path\|none> &lt;name> [--limit N]` |
| `scripts/mmlu_eval_all.sh` | `bash scripts/mmlu_eval_all.sh [--limit N]`，串行跑 6 个条件 |

### Dry-run 验证
- `--limit 2` 在 base model 上成功完成
- Auto batch size: 28
- 456 loglikelihood requests 用时 66s
- 结果已保存到 `results/mmlu/dryrun/`

### 时间估算
- 单个条件全量 MMLU: ~30–60 min（Blackwell GPU + batch_size=28）
- 6 个条件串行: ~3–6h
- 注意：GPU 当前空闲，可以立即启动

### 注意事项
- SS s456 训练似乎已经完成（GPU 占用从 45GB 降到 5.6GB），建议确认
- 启动全量评估: `nohup bash scripts/mmlu_eval_all.sh > /tmp/mmlu_eval_all.log 2>&1 &`

---

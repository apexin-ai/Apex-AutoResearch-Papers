# code dpo data pipeline

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo_data_pipeline_20260513T073522_result.json`
- **Structured JSON:** [`99fa787c7230bdb775dc.json`](../../sessions/99/99fa787c7230bdb775dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都正常 parse。汇总结果：

## 完成情况

### 1. generate_dpo_candidates.py ✓
- 路径：`/root/autodl-tmp/prov_grounded_uie/generate_dpo_candidates.py`
- `--help` 正常输出
- 支持：`--resume_from`（断点续跑）、`--min_reward_margin`（过滤低质量 pair）、`--device`（指定 GPU）

### 2. train_dpo.py ✓
- 路径：`/root/autodl-tmp/prov_grounded_uie/train_dpo.py`
- `--help` 正常输出
- 适配 TRL 1.1.0 接口（无 `max_prompt_length`，用 `max_length=4096` 控制总长度）
- 通过 model path string + `model_init_kwargs` 传递，与 GRPO 训练一致

### 3. Reward 函数接口分析
- `composite_reward(prompts, completions, **kwargs)` — completions 为 string list
- **必需 kwargs**：`gold_relations`（JSON string list）、`sentences`（JSON string list）、`document_text`（string list）— 按 index 对应 completions
- 权重通过 kwargs 传入：`w_provenance`, `w_structural`, `w_format`, `iou_weight` 等
- NLI 已禁用（weight=0），不会加载 NLI 模型

### 4. GPU 资源预估
- **硬件**：2× RTX PRO 6000 Blackwell 94GB
- **模型显存**：Qwen3-8B bf16 ≈ 16GB，单卡绑定即可
- **生成**：3027 prompts × 8 candidates = 24,216 次 decode，每 prompt 约 30-60s（`num_return_sequences=8`），**总计约 25-50 小时**
- **优化建议**：可开两个进程分别跑 `--device cuda:0 --resume_from 0 --max_samples 1514` 和 `--device cuda:1 --resume_from 1514`，时间减半至 ~13-25h

---

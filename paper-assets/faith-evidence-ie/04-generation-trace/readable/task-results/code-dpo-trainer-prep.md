# code dpo trainer prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-trainer-prep_20260515T011036_result.json`
- **Structured JSON:** [`a6e5932a7a99712f87e1.json`](../../sessions/a6/a6e5932a7a99712f87e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均通过 `--help` 验证，CLI 正常。

---

### 产出汇报

**文件位置**:
- `/root/autodl-tmp/freige/training/dpo_data_builder.py` — 偏好对构建
- `/root/autodl-tmp/freige/training/dpo_trainer.py` — DPO 训练

**dpo_data_builder.py CLI 参数**:
| 参数 | 说明 |
|---|---|
| `--input_dir` (必填) | rsft_generate 输出目录（含 generations.jsonl）|
| `--scores_path` | 预计算 rsft_scores.jsonl，不提供则内部调 CED 打分 |
| `--output_dir` (必填) | 输出目录 |
| `--rank_by` | 排序依据：ced_reward / f1_reward / combined_score（默认 ced_reward）|
| `--pair_k` | 每个 doc 取 top-k vs bottom-k（默认 1）|
| `--min_margin` | 最小分数差过滤（默认 0.05）|
| `--require_format_ok` / `--no_require_format_ok` | 是否过滤格式不合规的生成（默认 True）|
| `--nli_model_path`, `--nli_device`, `--tau` | 内部 CED 计算参数（仅在无 scores_path 时使用）|

**dpo_trainer.py CLI 参数**:
| 参数 | 说明 |
|---|---|
| `--dpo_data_path` (必填) | dpo_pairs.jsonl |
| `--output_dir` (必填) | LoRA adapter 输出 |
| `--base_model` | 默认 Qwen3-4B |
| `--sft_adapter` | 默认 sft_output，设 '' 跳过 |
| `--beta` | KL penalty（默认 0.1）|
| `--loss_type` | sigmoid / hinge / ipo / kto_pair（默认 sigmoid）|
| `--learning_rate` | 默认 5e-6（比 SFT 低）|
| LoRA 参数 | rank=64, alpha=128, dropout=0.05，target 与 SFT/RSFT 一致 |
| `--deepspeed` | 多卡 DeepSpeed 配置 |

**与现有代码兼容性**:
- 复用 `rsft_score_filter.py` 的 `_extract_user_content`、`compute_*_reward` 逻辑
- 复用 `sft_trainer.py` 的 `SYSTEM_PROMPT`
- 模型加载流程（base → merge SFT → new LoRA）与 `rsft_trainer.py` 一致
- LoRA target modules 与所有训练脚本一致
- bf16 全精度，无 4-bit 量化
- DPO 数据流: `rsft_generate → rsft_score_filter → dpo_data_builder → dpo_trainer`

---

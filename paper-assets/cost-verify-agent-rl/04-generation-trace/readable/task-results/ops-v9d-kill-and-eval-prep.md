# ops v9d kill and eval prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v9d_kill_and_eval_prep_20260520T092826_result.json`
- **Structured JSON:** [`2c0f819cb75fe07b3e8f.json`](../../sessions/2c/2c0f819cb75fe07b3e8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 状态：已清理干净
| GPU | Util | Memory Used | Total |
|-----|------|-------------|-------|
| 0 | 0% | 0 MiB | 97887 MiB |
| 1 | 0% | 0 MiB | 97887 MiB |
| 2 | 0% | 0 MiB | 97887 MiB |
| 3 | 0% | 0 MiB | 97887 MiB |

4 张卡全部释放，可立即使用。

### Step 10 Checkpoint 结构
`/root/autodl-tmp/checkpoints/8b-cell-c-v9/global_step_10/actor/`

- **FSDP shards 完整**：4 个 `model_world_size_4_rank_*.pt`（每个 ~8.2GB）+ 4 个 optim shards + 4 个 extra_state
- **`huggingface/` 目录**：有 `config.json`、tokenizer 文件（`tokenizer.json`, `vocab.json`, `merges.txt` 等），**但没有 `.safetensors` 或 `.bin` 权重文件**

**结论**：checkpoint 保存时只合并了 tokenizer/config 到 huggingface/，没有将 FSDP shards 合并为 HuggingFace 格式权重。**不能直接用于 eval**，需要先做 FSDP → HF 权重合并（从 4 个 `model_world_size_4_rank_*.pt` 合并出 `model.safetensors`）。

### Eval 配置
- `_alfworld_8b_v9d_ood_eval.yaml` — 不存在
- `_alfworld_8b_det_eval*.yaml` — 不存在

需要新建 eval 配置。

### 磁盘
`/root/autodl-tmp`: 250G 总量，145G 已用（58%），106G 可用。空间充足。

---

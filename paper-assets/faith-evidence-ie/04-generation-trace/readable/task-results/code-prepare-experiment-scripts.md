# code prepare experiment scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-experiment-scripts_20260520T085111_result.json`
- **Structured JSON:** [`0f728c904146a58008d8.json`](../../sessions/0f/0f728c904146a58008d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本全部语法通过。

## 汇总

### 实验 1 & 2：LLaMA SFT s43/s44 retrain + eval（已有脚本，无需修改）

| | 路径 | GPU 参数 |
|---|---|---|
| s43 | `scripts/seed_expansion/llama_sft_s43_train_eval.sh` | `GPU=0 bash ...` 或 `GPU=1 bash ...` |
| s44 | `scripts/seed_expansion/llama_sft_s44_train_eval.sh` | 同上 |

两个脚本已有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，训练完自动 eval。

### 实验 3：eval_llama_sft_s42_no_evidence_std（新建）

- 路径：`scripts/eval_llama_sft_s42_no_evidence_std.sh`
- 模型：`/root/autodl-tmp/sft_output_llama_3_1_8b`（s42 SFT 模型）
- 关键参数：`--no_evidence`（inference.py L393 确认，`action="store_true"`）
- 用法：`GPU=3 nohup bash scripts/eval_llama_sft_s42_no_evidence_std.sh > /tmp/eval_no_evi.log 2>&1 &`
- 耗时：~30min

### 实验 4：rsft_generate_14b_resume（新建）

- 路径：`scripts/rsft_generate_14b_resume.sh`
- 基座：`/root/autodl-tmp/models/Qwen/Qwen3-14B`
- SFT adapter：`/root/autodl-tmp/sft_output_14b`
- 进度：1872/3028 docs 已完成（14976 行 / 8 gens），`--resume` 从 progress.json 自动恢复
- 用法：`GPU=0 nohup bash scripts/rsft_generate_14b_resume.sh > /tmp/rsft_gen_14b.log 2>&1 &`
- 耗时：~4-5h

### westd-37389 启动命令（迁移完成后）

```bash
# 4 GPU 并行：
GPU=0 nohup bash scripts/seed_expansion/llama_sft_s43_train_eval.sh > /tmp/s43.log 2>&1 &
GPU=1 nohup bash scripts/seed_expansion/llama_sft_s44_train_eval.sh > /tmp/s44.log 2>&1 &
GPU=2 nohup bash scripts/rsft_generate_14b_resume.sh > /tmp/rsft_gen_14b.log 2>&1 &
GPU=3 nohup bash scripts/eval_llama_sft_s42_no_evidence_std.sh > /tmp/eval_no_evi.log 2>&1 &
```

### 注意事项

1. **14B 生成单卡可行**：Qwen3-14B bf16 ≈ 28GB，westd 的 RTX PRO 6000 有 98GB 显存，单卡充裕
2. **eval 先跑完**：实验 3 只需 ~30min，跑完后 GPU 3 可以接其他任务
3. **14B 生成最慢**：剩余 ~1156 docs × 8 gens，预计 4-5h

---

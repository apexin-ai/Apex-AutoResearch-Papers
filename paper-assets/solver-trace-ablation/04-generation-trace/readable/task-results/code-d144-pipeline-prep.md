# code d144 pipeline prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d144-pipeline-prep_20260519T141914_result.json`
- **Structured JSON:** [`b3f64dc933a796c8ef5b.json`](../../sessions/b3/b3f64dc933a796c8ef5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告：

### D144 Pipeline 准备结果

**1. s42 训练状态**
- 运行中：tmux session `d144-llama-exec-s42`，PID 398743，GPU 占用 69772 MiB
- 进度：已到 checkpoint-50/500

**2. Config 文件**
- `configs/grpo_llama_exec_only.yaml` ✓ — reward_mode=execution_only, data=train_500_seed42.jsonl, save_total_limit=1
- `configs/grpo_llama_additive_bonus_b01.yaml` ✓ — reward_mode=additive_bonus, beta=0.1, 同上

**3. Pipeline 脚本**
- 路径：`/root/solver-trace-ablation/scripts/d144_pipeline.sh`
- 内容：5 个实验串行执行，`CUDA_VISIBLE_DEVICES=0`，exec-only s43→s44→ISR s42→s43→s44
- 语法验证通过

**4. Registry 注册**
全部 5 个实验已创建为 PREPARING，parent=d144-llama-exec-s42：
| exp_id | hypothesis |
|---|---|
| d144-llama-exec-s43 | exec-only seed=43, replication |
| d144-llama-exec-s44 | exec-only seed=44, replication |
| d144-llama-isr-s42 | ISR β=0.1 seed=42, Goodhart collapse test |
| d144-llama-isr-s43 | ISR β=0.1 seed=43, replication |
| d144-llama-isr-s44 | ISR β=0.1 seed=44, replication |

**5. 启动说明**
Pipeline 脚本就绪，等 s42 完成后由 Agent 通过 `submit_training_job` 在 tmux 中启动，不会自行启动。

---

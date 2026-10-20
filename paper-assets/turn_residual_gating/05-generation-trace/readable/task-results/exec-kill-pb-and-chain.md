# exec kill pb and chain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_kill_pb_and_chain_20260523T070722_result.json`
- **Structured JSON:** [`e113cbf54583302473fe.json`](../../sessions/e1/e113cbf54583302473fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

### 1. PaperBanana kill
PID 75061 已 kill（SIGTERM 成功，未 force kill）。显存已释放。

### 2. Split-softmax eval 进度
- PID 81629 在跑，确认是 `eval_split_softmax.py`
- 当前阶段：Phase 1 Step 1/4（`base_tf_n50`，base 模型 + 7 个 k 值 × 50 对话）
- `results/split_softmax/` 目录为空，第一步尚未完成
- 脚本共 4 步：base_tf → tg_tf → base_gen → tg_gen
- **预估**：每步 ~20-40 分钟（50 对话 × 多 k 值），总计 ~2-3 小时完成

### 3. SS s456 epoch_0 完整性
- `runs/d048_ss_s456/epoch_0/` 包含 `gate_params.pt` + `lora/`（adapter_config.json, adapter_model.safetensors, README.md）
- **完整可用**，可直接 `--resume` 恢复训练
- 仅 epoch_0，epoch 1-2 未完成（Epoch 1 Step 3400 OOM 崩溃符合预期）

### 4. 脚本路径和内容

**`scripts/d048_ss_s456_resume.sh`**（新建）：
- 参数与 `d048_ss_s456.sh` 完全一致
- 追加 `--resume runs/d048_ss_s456/epoch_0`
- 追加 `CUDA_VISIBLE_DEVICES=0`（参考 s42 resume 脚本）

**`scripts/gpu_chain_next.sh`**（新建）：
- 串行 8 阶段：SS s456 resume → SS s456 eval → Qwen-1.5B diag → Qwen-1.5B TG train → MMLU base_qwen → Qwen-1.5B eval → MMLU 5 checkpoints
- 每步带时间戳日志

### 5. Dry-run 验证
全部 7 个脚本 `bash -n` 通过：
`d048_ss_s456_resume.sh` ✓ | `gpu_chain_next.sh` ✓ | `d048_eval_ss_s456.sh` ✓ | `qwen15b_phase1_diag.sh` ✓ | `qwen15b_tg_train.sh` ✓ | `qwen15b_eval.sh` ✓ | `mmlu_eval_single.sh` ✓

### 6. 未启动
脚本已就绪，**未执行 nohup/tmux**。等待通过 submit_training_job 提交。

---

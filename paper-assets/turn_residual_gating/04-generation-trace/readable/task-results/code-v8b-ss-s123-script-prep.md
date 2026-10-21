# code v8b ss s123 script prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8b_ss_s123_script_prep_20260520T190659_result.json`
- **Structured JSON:** [`2a03790a2a21d73163ff.json`](../../sessions/2a/2a03790a2a21d73163ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 1. 脚本路径和内容

**`/root/turn_residual_gating/scripts/launch_v8b_ss_s123.sh`** — 已创建

与 s42 版本的差异：
- `--seed 123`（原 42）
- `--output-dir checkpoints/tg_v8b_ss_s123`（原 `tg_v8b_ss_fixed_s42`）
- 去掉 `--resume`（全新训练）
- 添加 `set -e` / `CUDA_VISIBLE_DEVICES=0` / `PYTHONUNBUFFERED=1`

### 2. Dry-run 结果

`bash -n` 语法检查通过，exit code 0。

### 3. v7 s123 脚本

**`scripts/launch_tg_s123.sh`** 已存在且正确（`--seed 123`，`output-dir runs/phase2_tg_s123_v7`，使用 `train_phase2.py`），无需修改。

### 4. 预估训练时间

v8b s42 跑了 ~8.1h / 3000 steps。s123 参数完全一致（3 epochs, batch=1, grad_accum=8），预估 **~8h**。

### 5. 注意事项

- **磁盘无压力**：v8b checkpoint 仅 91MB（LoRA adapter），根分区剩余 15GB，数据盘 216GB
- **无 `--resume`**：s123 是从头训练，不要从 s42 checkpoint 恢复
- **SS 生成的 OOM 风险**：v8b 已修复（eval mode + no_grad + max_new_tokens=128），s123 应无问题
- 启动命令：`nohup bash scripts/launch_v8b_ss_s123.sh > logs/v8b_ss_s123.log 2>&1 &`

---

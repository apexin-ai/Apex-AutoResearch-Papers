# ops cuda2 best s1 eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_best_s1_eval_20260525T194650_result.json`
- **Structured JSON:** [`5e18f09d8777f360ad7b.json`](../../sessions/5e/5e18f09d8777f360ad7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

1. **Checkpoint 大小检查**:
   - `best/model.safetensors` → symlink → `model_lora.safetensors`: **7,540,115,784 bytes (7.54GB)**
   - `30000/model.safetensors`: **7,540,115,784 bytes (7.54GB)**（参考一致）
   - `model_base_backup.safetensors`: 7,473,091,320 bytes (7.47GB)（base-only 备份）
   - 16000/ 目录不存在，best/ 对应 step 16000 (best_loss=0.01143)

2. **结论**: seed1 best/ checkpoint **正确**，包含 LoRA weights。已通过 symlink 修复（指向 model_lora.safetensors），base-only 文件已备份。

3. **cuda:2 状态**: 空闲（1MiB 显存，0% 利用率，无进程）

4. **Eval 已提交**:
   - exp_id: `eval_pi05_a1_best_s1_l005_16k`
   - PID: 121100
   - tmux session: `eval_pi05_a1_best_s1_l005_16k`
   - log: `~/runs/diff_collision_sdf/eval_pi05_a1_best_s1_l005_16k.log`
   - 使用 best/ 路径（对应 step 16000）

---

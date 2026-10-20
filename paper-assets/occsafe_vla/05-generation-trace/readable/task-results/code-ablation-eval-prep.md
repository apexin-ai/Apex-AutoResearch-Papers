# code ablation eval prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation-eval-prep_20260521T195252_result.json`
- **Structured JSON:** [`99507807145ad96cc28a.json`](../../sessions/99/99507807145ad96cc28a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建，语法验证通过。

### 产出汇总

1. **脚本路径**: `/root/occsafe_vla/openvla-oft/run_ablation_eval.sh`
   - 用法: `bash run_ablation_eval.sh 20`（快速诊断）或 `bash run_ablation_eval.sh 50`（完整数据）
   - 启动前自动检查 4 个 checkpoint 是否存在，不齐则 abort

2. **evaluate_safelibero.py 实际参数**:
   - `--pretrained_checkpoint` (路径)
   - `--task_suite_name` (libero_spatial)
   - `--num_rollouts` (20/50)
   - `--seed` (42)
   - `--output_path` (JSON 输出路径)
   - `--collision_threshold` (0.001, 用默认值)
   - `--save_videos` (未启用)
   - 无 `--gpu_id` 参数（run_eval.sh 里的是多余的，被 draccus 忽略）

3. **4 个 ablation checkpoint 目录名前缀**: `openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug`
   - 当前已有中间 checkpoint: 20000_chkpt（全部）、30000_chkpt（仅 random_occ_s0）
   - 最终 50000_chkpt 尚未生成（训练 ~55%）

4. **语法验证**: `bash -n` 返回 0，通过

---

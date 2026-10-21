# ops sync a3 and launch eval v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_a3_and_launch_eval_v11_20260522T130245_result.json`
- **Structured JSON:** [`de0ac0b306bf0dcec35e.json`](../../sessions/de/de0ac0b306bf0dcec35e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A3 eval 进程健康运行中，32 个 torch.compile worker 在编译中（首次推理需 5-10 分钟）。GPU 3 占用 8939 MiB。

---

**汇总：**

| 项目 | 状态 |
|------|------|
| M022 norm_stats 修复 | 已确认（eval_safelibero.py lines 511-526，A3 norm_stats 从 checkpoint assets 加载） |
| A3 checkpoint 路径 | `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best`（best at step 26000, loss=0.01439） |
| Checkpoint 大小 | best/ 7.1GB（含 model.safetensors 7.1GB + lora_params.pt 134MB + sdf_decoder.pt 1.6MB） |
| SCP 同步 | 完成，文件大小一致 |
| norm_stats | 存在 `best/assets/safelibero_object/norm_stats.json` |
| SafeLIBERO 环境 | libero/robosuite 可用（通过 sys.path 导入） |
| 磁盘 westd-35807 | 50% (173G/350G)，空间充足 |
| A3 eval v11 | tmux session `eval_a3_v11` 已启动，PID 564007 |
| GPU | cuda:3，当前 8939 MiB，torch.compile 进行中 |
| 日志 | `/tmp/eval_a3_v11.log` |
| 参数 | `--model_type a3 --suite safelibero_object --n_episodes 50 --max_steps 300 --replan_steps 5 --gpu 3 --refine_alpha 0.1 --refine_margin 0.01 --sdf_gt_path sdf_gt_object_chocolate.npz --output_prefix v11` |

---

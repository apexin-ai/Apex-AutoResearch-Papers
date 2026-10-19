# code fix action chunking eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_action_chunking_eval_20260522T094247_result.json`
- **Structured JSON:** [`7f9e5a70106f919ae586.json`](../../sessions/7f/7f9e5a70106f919ae586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张 GPU 各占 ~24GB，无空闲 GPU。

## 修改完成，总结

**代码修改（4项全部完成）：**

| # | 修改 | 位置 |
|---|------|------|
| 1 | **Action Chunking** — `deque` 缓存 action chunk，`--replan_steps=5`（默认），推理一次执行5步 | `get_action_from_policy` 改为返回完整 actions (50×7)；`evaluate_task` 行 703-712 用 deque 逻辑 |
| 2 | **图像 resize 224×224** — 对 agentview 和 wrist_image 做条件 resize | 行 618-621 |
| 3 | **Warm-up 10步** — `[0,0,0,0,0,0,-1.0]` gripper-closed warm-up | 行 683-685，在 50-step sim warm-up 之后 |
| 4 | **PYTHONUNBUFFERED=1** | 行 69 |

额外：`--output_prefix` 参数、`replan_steps` 写入输出 JSON config。

备份在 `eval_safelibero.py.v10_bak`。

**无法跑 dry-run** — 4 张 GPU (cuda:0-3) 全部被占用（每张 ~24GB），A3 eval 和其他进程在跑。Baseline checkpoint 确认在 `/root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_lora_spatial_bowl_seed0/best/`。

GPU 空闲后可执行：
```bash
cd /root/colliforce-vla && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python scripts/eval_safelibero.py \
    --checkpoint /root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_lora_spatial_bowl_seed0/best \
    --config_name baseline_spatial_bowl \
    --suite safelibero_spatial \
    --task_id 0 \
    --n_episodes 3 \
    --max_steps 300 \
    --replan_steps 5 \
    --output_prefix eval_v11_dryrun \
    2>&1 | tee /tmp/eval_v11_dryrun.log
```

---

# code plan003 eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003_eval_prep_20260526T143849_result.json`
- **Structured JSON:** [`5aba11565474f14a43b4.json`](../../sessions/5a/5aba11565474f14a43b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出汇报：

| 项目 | 详情 |
|------|------|
| **s0 checkpoint** | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/30000` |
| **s2 checkpoint（预期）** | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/30000` |
| **s2 训练进度** | 43% (13051/30000)，~4.61s/it，剩余约 21h40m，预计完成时间 ~5/27 上午 |
| **eval 批量脚本** | `/root/colliforce-vla/scripts/eval_lora_baseline_batch.sh` |
| **rotation fix** | 已确认，eval_safelibero.py L841/L843 有 `[::-1, ::-1]` 旋转 |
| **s0 eval 状态** | 未 eval（assets 仅有 norm_stats.json） |
| **预估 eval 耗时** | 每个 seed ~2.5h，两个串行共 ~5h |

s0 可以现在就开始 eval（不用等 s2）。运行方式：
```bash
# 只跑 s0（s2 还没训完）
bash scripts/eval_lora_baseline_batch.sh &lt;GPU_ID>
# 或者先单独跑 s0，s2 训完后再跑
```

---

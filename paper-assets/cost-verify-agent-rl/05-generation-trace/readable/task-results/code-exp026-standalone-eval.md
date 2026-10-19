# code exp026 standalone eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp026_standalone_eval_20260515T133734_result.json`
- **Structured JSON:** [`637643019844574ffd09.json`](../../sessions/63/637643019844574ffd09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，dry run 验证通过：

- `--help` 正常输出所有参数
- C003 守卫生效：`--num_episodes 4` 被拒绝（`ERROR: C003 requires >=16 episodes`）

**脚本功能**：`/root/cost-verify-agent-rl/scripts/eval_checkpoint.py`

| 特性 | 说明 |
|---|---|
| **checkpoint 格式** | 自动检测 HF / FSDP，FSDP 自动转换后加载 |
| **C003** | 强制 `num_episodes >= 16`，否则拒绝运行 |
| **指标** | success_rate, action_is_valid, action_is_effective, format_ok + per-task-type breakdown |
| **单卡运行** | `--gpu 0` 或 `--gpu 1`，可与训练并行 |
| **输出** | JSON 文件含每 episode 详细 step-level 数据 + 汇总 |

**用法示例**（等 exp026 step 25 checkpoint 就绪后）：
```bash
python scripts/eval_checkpoint.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/exp026/global_step_25 \
  --num_episodes 16 \
  --gpu 0
```

---

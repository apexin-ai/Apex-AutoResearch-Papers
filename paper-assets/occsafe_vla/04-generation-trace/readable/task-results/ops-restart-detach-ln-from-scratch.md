# ops restart detach ln from scratch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart_detach_ln_from_scratch_20260523T170827_result.json`
- **Structured JSON:** [`4f44763110ffa6f3cd2a.json`](../../sessions/4f/4f44763110ffa6f3cd2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。汇总报告：

## 执行结果

### 1. 训练任务提交

| 实验 | PID | GPU | Seed | 状态 |
|------|-----|-----|------|------|
| detach_ln_s0 | 459087 | cuda:1 | 42 | RUNNING ✓ |
| detach_ln_s1 | 459294 | cuda:2 | 43 | RUNNING ✓ |
| detach_ln_s2 | 459635 | cuda:3 | 44 | RUNNING ✓ |

### 2. cmdline 验证（全部通过）
- `vla_path`: `/root/autodl-tmp/models/openvla-7b` ✓（基模型）
- `occ_detach`: `true` ✓
- `occ_norm_type`: `ln` ✓
- 无 `--resume` ✓

### 3. 初始 Loss
- **detach_ln_s0**: step=0 → occ_loss=0.1073, action_loss=0.6133; step=100 → occ_loss=0.0306, action_loss=0.3008
- **detach_ln_s1**: step=0 → occ_loss=0.1024, action_loss=0.6150; step=100 → occ_loss=0.0295, action_loss=0.2976
- **detach_ln_s2**: step=0 → occ_loss=0.1045, action_loss=0.6234（step 100 还没打印）

初始 action_loss > 0.6 符合随机初始化预期。

### 4. Cleanup 脚本修复 ✓
- 添加了 `is_in_use()` 函数，删除前检查 `/proc/*/cmdline` 是否引用该路径
- 目录级和 checkpoint 级双重检查
- 匹配则跳过并记录 WARNING 到 log

### 5. Registry 更新 ✓
- 3 个实验均已从 DONE(failed) → PREPARING → QUEUED → RUNNING
- spec 已更新为新 PID、基模型路径、完整命令

---

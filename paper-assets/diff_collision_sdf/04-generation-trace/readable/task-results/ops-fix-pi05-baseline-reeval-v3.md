# ops fix pi05 baseline reeval v3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_pi05_baseline_reeval_v3_20260526T065125_result.json`
- **Structured JSON:** [`8629f35d64c6e100f715.json`](../../sessions/86/8629f35d64c6e100f715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

---

## 诊断报告

**根因**：`eval_safelibero.py` 的 `get_action_from_policy()` 缺少 180 度图像旋转 `[::-1, ::-1]`。

LIBERO simulator 输出的图像方向与训练数据（RLDS 格式，已旋转）相反。原始 eval 脚本 (`openpi/examples/libero/main.py`) 显式做了旋转并注释 "IMPORTANT: rotate 180 degrees to match train preprocessing"，而 `eval_safelibero.py` 遗漏了这一步。

**差异对比**：

| | 原始 eval | eval_safelibero.py (修复前) |
|---|---|---|
| 图像旋转 | `[::-1, ::-1]` ✅ | **无** ❌ |
| 相机分辨率 | 256→resize→224 | 224 直出 |

**修复内容**：
1. `get_action_from_policy()` 中在 resize 前加 `[::-1, ::-1]` 旋转
2. 相机分辨率从 224 改为 256 以匹配原始流程

**验证结果**：
- Sanity check (Task 0, 20 episodes): **TSR=85.0%**（参考值 73%，20 episodes 方差下完全合理）
- EE displacement 正常记录：avg_max=0.185m, avg_max_ee=0.390m

**完整 eval 状态**：
- tmux session: `pi05_eval` on westd-45947
- 命令: `CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py --default_policy --suite safelibero_object --safety_level II --n_episodes 50 --max_steps 300 --seed 7`
- 日志: `/tmp/pi05_full_eval.log`
- 输出: `/root/autodl-tmp/eval_results/pi05_base_reeval_safelibero_object_levelII_seed7.json`
- 预计耗时: ~30-40 分钟
- cuda:0 LoRA s2 训练未受影响

---

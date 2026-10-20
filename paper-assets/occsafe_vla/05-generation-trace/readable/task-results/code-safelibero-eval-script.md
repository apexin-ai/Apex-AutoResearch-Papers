# code safelibero eval script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_safelibero_eval_script_20260520T112347_result.json`
- **Structured JSON:** [`9e935fa1a42d5c4437b5.json`](../../sessions/9e/9e935fa1a42d5c4437b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法通过，`--help` 正常输出所有参数。

## 汇报

### SafeLIBERO 安装状态
- **SafeLIBERO 不是独立包**，碰撞检测逻辑通过 MuJoCo 物理引擎直接实现：跟踪非目标物体 body 的 L1 位移
- 已安装：libero 0.1.1, mujoco 3.8.1, robosuite 1.4.1, openvla-oft 0.0.1
- 关键 API 全部验证通过：`env.env.obj_of_interest`、`env.env.objects`、`sim.data.body(name).xpos`

### 评估脚本
**路径**: `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py`

功能：
- 加载 fine-tuned OpenVLA-OFT checkpoint（`--pretrained_checkpoint`）
- 在 LIBERO benchmark 任务中 rollout（默认 libero_spatial, 10 个任务）
- `ObstacleTracker` 在 warmup 后记录非目标物体位置，每步检查 L1 位移 > 0.001 判定碰撞
- 计算 per-task 和 overall 的 TSR / CAR
- 结果保存到 JSON（默认 `artifacts/safelibero_*.json`）

运行示例：
```bash
cd /root/occsafe_vla/openvla-oft
MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_s0 \
    --task_suite_name libero_spatial \
    --num_rollouts 20
```

### Dry-run 结果
- 语法检查：`SYNTAX_OK`
- `--help`：所有参数正确解析，imports 全部通过

### 已有代码说明
服务器上已有一份 `/root/occsafe_vla/eval/eval_safelibero.py`（之前的版本，`num_rollouts` 默认 50）。新脚本在 `vla-scripts/` 下，默认改为 20，路径逻辑已适配。

### 无遗留问题
所有依赖已安装，API 已在真实 LIBERO 环境中端到端验证（创建环境 → 读取物体 → 读取 MuJoCo body 位置），等 checkpoint 训练完成即可直接运行。

---

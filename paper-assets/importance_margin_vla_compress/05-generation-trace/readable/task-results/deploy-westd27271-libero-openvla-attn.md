# deploy westd27271 libero openvla attn

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_libero_openvla_attn_20260524T194111_result.json`
- **Structured JSON:** [`20bb868ce2d8c59139a1.json`](../../sessions/20/20bb868ce2d8c59139a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

### 环境状态
- **LIBERO / MuJoCo / Robosuite**: 已安装，EGL 渲染正常
- **代码**: 已在 `/root/autodl-tmp/importance_margin_vla_compress/`，无需同步
- **模型**: 各 suite 独立 fine-tuned checkpoint 均已缓存

### 部署的实验

| GPU | 实验 | PID | 配置 |
|-----|------|-----|------|
| 0 | `eval_openvla_attn_k09_goal_seed42` | 958937 | attention_prune k=0.9, libero_goal, 10×50=500 eps |
| 1 | `eval_openvla_attn_k09_spatial_seed42` | 959698 | attention_prune k=0.9, libero_spatial, 10×50=500 eps |

两个实验均已开始 eval（256→230 vision tokens），各占 ~16GB 显存。按 ~1.5 eps/min 估算，每个实验约 5.5 小时完成。

日志路径：
- `logs/eval_openvla_attn_k09_goal_seed42.log`
- `logs/eval_openvla_attn_k09_spatial_seed42.log`

---

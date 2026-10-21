# ops deploy westd38929 gpu2 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-westd38929-gpu2-spatial_20260524T110124_result.json`
- **Structured JSON:** [`6a373f2aa122471f83b0.json`](../../sessions/6a/6a373f2aa122471f83b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行中：
- **bash 包装进程**: PID 305678 (Ss+ 状态)
- **Python 主进程**: PID 305684 (Rl+ 状态，正在 CPU 上加载模型)
- 已运行 ~1.5 分钟，π0.5 模型较大，CPU 加载阶段不占 GPU 显存，加载完成后会转移到 GPU 2

部署完成。

| 项目 | 值 |
|------|-----|
| 实验 ID | `eval_pi05_l2norm_k09_spatial_seed42_postfix` |
| 服务器 | westd-38929, GPU 2 |
| Python PID | **305684** |
| tmux session | `l2norm_k09_spatial` |
| 日志 | `/root/autodl-tmp/importance_margin_vla_compress/logs/l2norm_k09_spatial.log` |
| 状态 | 模型加载中（CPU 阶段），预计几分钟后占用 GPU 2 显存 |

---

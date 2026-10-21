# deploy cqa1 gpu0 attn k09 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu0_attn_k09_long_20260525T125946_result.json`
- **Structured JSON:** [`f9e34580e64e1bfafa6f.json`](../../sessions/f9/f9e34580e64e1bfafa6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验启动成功。关键日志确认：

- 模型加载完成（4143.4M params）
- **Attention pruning 配置正确**: keep 230/256 tokens/image (690 total, 2-layer probe)
- Suite: libero_10, 10 tasks, max_steps=520
- Assets 已下载，正在初始化 eval 环境

部署完成。总结：

| 项目 | 值 |
|------|------|
| 实验 ID | eval_pi05_attention_k09_long_seed42_postfix |
| 服务器 | cqa1-33015 GPU 0 |
| PID | 401165 |
| 状态 | RUNNING |
| 日志 | logs/eval_pi05_attention_k09_long_seed42_postfix.log |
| 修改 | 从 westd-41074 同步 attention pruning 代码到 cqa1-33015 |

---

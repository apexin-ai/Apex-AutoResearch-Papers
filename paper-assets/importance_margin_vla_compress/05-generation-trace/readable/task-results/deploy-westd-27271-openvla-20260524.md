# deploy westd 27271 openvla 20260524

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-27271-openvla-20260524_20260524T053443_result.json`
- **Structured JSON:** [`cef88df84e22d22aa519.json`](../../sessions/ce/cef88df84e22d22aa519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，正在评估 Task 1/10。

```
GPU Status: 2x RTX PRO 6000 (98GB), 均空闲
Object model: /root/autodl-tmp/openvla-7b-finetuned-libero-10 (unnorm_key=libero_10)
Attention mode: available (代码内置)
已部署:
  - GPU 0: eval_openvla_attn_k05_object_seed42 (tmux: eval_openvla_attn_k05_object, log: /tmp/eval_openvla_attn_k05_object.log)
    - 当前进度: Task 1/10, attention_prune k=0.5, libero_object, 50ep/task
跳过:
  - eval_openvla_l2norm_k05_goal_seed42_v3: 已完成 (SR=43.4%, conclusion=negative)
问题: 无（首次 unnorm_key 错误已修复，重启后正常运行）
```

---

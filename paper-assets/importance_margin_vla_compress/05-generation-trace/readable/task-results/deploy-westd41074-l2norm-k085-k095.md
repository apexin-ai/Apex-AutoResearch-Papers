# deploy westd41074 l2norm k085 k095

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074-l2norm-k085-k095_20260521T235724_result.json`
- **Structured JSON:** [`aa8cc457fca80f8954b7.json`](../../sessions/aa/aa8cc457fca80f8954b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程在 CPU 上加载权重（13-14GB RSS），还没 `.to(device)` 推到 GPU。这是正常的加载阶段。

部署完成：

| 实验 | exp_id | GPU | PID | 状态 |
|------|--------|-----|-----|------|
| L2norm k=0.85 Object seed42 | eval_pi05_l2norm_k085_object_seed42_v3 | GPU0 | 816306 | 加载模型中 |
| L2norm k=0.95 Object seed42 | eval_pi05_l2norm_k095_object_seed42 | GPU1 | 816389 | 加载模型中 |

修复说明：westd-41074 上 lerobot 0.5.2 是坏的 editable install（源目录不存在）。重装了 0.5.1 并 patch 了 `policies/__init__.py` 注释掉 groot import（与 westd-27271 一致）。

---

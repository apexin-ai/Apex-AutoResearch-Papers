# deploy westd41074 gpu1 openvla attn k085 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu1_openvla_attn_k085_long_20260524T210550_result.json`
- **Structured JSON:** [`107aba3fbd99b8d1f7fb.json`](../../sessions/10/107aba3fbd99b8d1f7fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

```
Kill PID 867860: killed
GPU1 清理: 空闲（额外 kill 了孤儿进程 877990）
部署: 成功 PID=912556 (子进程 912562, GPU1 16169 MiB, 利用率 69%)
Registry: RUNNING
```

**修复过程**：
1. westd-41074 缺少 `/root/autodl-tmp/openvla_deps/`（transformers 4.40.1 兼容层）→ 已安装（`--no-deps`）
2. 脚本 `task.problem_info` API 不兼容 → 已 patch 为 `task.problem_folder` + `task.bddl_file`  
3. 脚本 `lm.rotary_emb` 错误引用 → 已 patch 为 `layer.self_attn.rotary_emb`
4. `__pycache__` + 孤儿进程干扰 → 已清理

Attention Pruning 确认工作：256 → 217 vision tokens (k=0.85)，importance range=[0.7555, 1.6388]。

---

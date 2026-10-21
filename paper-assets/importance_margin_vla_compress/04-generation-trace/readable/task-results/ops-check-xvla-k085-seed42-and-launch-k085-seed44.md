# ops check xvla k085 seed42 and launch k085 seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k085-seed42-and-launch-k085-seed44_20260520T215452_result.json`
- **Structured JSON:** [`d057d04a154eaa574a54.json`](../../sessions/d0/d057d04a154eaa574a54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed44 正在加载模型，运行正常。

---

## 任务 1: X-VLA k=0.85 seed42 结果

**Overall: 68.0%** (340/500), 95% Wilson CI: [63.8%, 71.9%], 耗时 80 min

| Task | Description | SR |
|------|-------------|-----|
| 0 | alphabet soup → basket | **100%** (50/50) |
| 1 | cream cheese → basket | **46%** (23/50) |
| 2 | salad dressing → basket | **100%** (50/50) |
| 3 | bbq sauce → basket | **86%** (43/50) |
| 4 | ketchup → basket | **26%** (13/50) |
| 5 | tomato sauce → basket | **92%** (46/50) |
| 6 | butter → basket | **0%** (0/50) |
| 7 | milk → basket | **96%** (48/50) |
| 8 | chocolate pudding → basket | **36%** (18/50) |
| 9 | orange juice → basket | **98%** (49/50) |

## 任务 2: k=0.85 seed44 启动状态

- tmux session `eval_xvla_k085_s44` 已创建，正在加载 X-VLA 模型
- GPU 2 上进程尚在模型初始化阶段（日志确认 `Loading X-VLA from ...`）
- 脚本实际路径为 `/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py`（不是 `/root/autodl-tmp/X-VLA-Libero/`）

---

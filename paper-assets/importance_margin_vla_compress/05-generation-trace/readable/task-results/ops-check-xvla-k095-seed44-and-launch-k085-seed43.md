# ops check xvla k095 seed44 and launch k085 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k095-seed44-and-launch-k085-seed43_20260520T204029_result.json`
- **Structured JSON:** [`cd7e5c05f0d2efe23ed3.json`](../../sessions/cd/cd7e5c05f0d2efe23ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。

---

## 任务 1: X-VLA k=0.95 seed44 结果

| 指标 | 值 |
|------|-----|
| **Overall Success Rate** | **99.4% (497/500)** |
| 95% Wilson CI | [98.3%, 99.8%] |
| 耗时 | 49.5 min |
| Vision tokens | 50 → 47 (保留 95%) |

Per-task 细节：
- 8/10 tasks 达 **100%**
- Task 3 (bbq sauce): 98% (49/50)
- Task 5 (tomato sauce): 96% (48/50)

## 任务 2: X-VLA k=0.85 seed43 启动状态

- tmux session: `eval_xvla_k085_s43` ✓
- **GPU 3 已占用**: PID 264237, 4489MiB
- 已开始跑 Task 0, Ep 1 已 SUCCESS
- 日志: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_k085_seed43.log`

---

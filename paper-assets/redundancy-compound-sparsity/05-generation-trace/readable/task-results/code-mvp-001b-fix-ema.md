# code mvp 001b fix ema

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001b-fix-ema_20260511T230624_result.json`
- **Structured JSON:** [`1bea1dbdbf8b80b15bbe.json`](../../sessions/1b/1bea1dbdbf8b80b15bbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp-001b 已启动并正在运行。

**总结：**

| 项目 | 状态 |
|------|------|
| v2 脚本 | `mvp_carc_validation_v2.py` 已部署 |
| 核心修正 | `cosine_sim_adjacent` + `compute_ema(alpha=0.3)` → `compute_anchor_signal(gamma=0.99)` |
| 信号定义 | 向量级 EMA anchor：每个 token 的 KV 与 anchor 做 per-head cosine sim，mean over 4 KV heads，然后更新 anchor |
| PID | 7820（nohup，GPU 54% active） |
| GPU | RTX 5090，15GB/32GB |
| 数据集 | HF 网络不可达，使用 20 道内置 fallback 题目 |
| 输出 | `mvp_results_v2.json` / `mvp_run_v2.log` |
| Registry | mvp-001b = RUNNING |
| mvp-001 | PID 6503 已自然结束，未被 kill |

v1 的 adjacent sim 测量的是相邻 token 间的局部变化，v2 的 anchor 测量的是 token 与上下文累积质心的偏离度——这才是 Token Filtering 论文的定义。

---

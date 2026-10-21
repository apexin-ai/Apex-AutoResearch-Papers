# diag cls8b s42 ckpt1200 val8192 v2 log

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cls8b-s42-ckpt1200-val8192-v2-log_20260515T023641_result.json`
- **Structured JSON:** [`b71427de4a3999870656.json`](../../sessions/b7/b71427de4a3999870656.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 进程状态
- **PID 316940**: 存活，10:10 UTC 启动，在 cuda:0 运行 `eval_repo_cls.py` 评估 ckpt-1200 val@8192
- 评估刚刚完成（10:39 UTC），耗时约 30 分钟

### 日志情况
- **实际日志**: `/tmp/eval_ckpt1200.log` — PID 316940 的输出，完整运行 9335/9335
- **v2.log** (`~/runs/.../cls8b-s42-ckpt1200-val8192-v2.log`): 另一个短命进程（10:07-10:10），仅跑到 740/9335 就停了，非 PID 316940
- **v3.log**: 不存在

### 评估结果（ckpt-1200, val@8192, seed=42）

| 指标 | 值 |
|------|-----|
| **Accuracy** | **87.76%** (+11.9pp vs majority 75.9%) |
| **F1 macro** | **81.25%** |
| F1 fail | 70.2% (P=85.0%, R=59.8%) |
| F1 pass | 92.3% (P=88.3%, R=96.7%) |
| Unparseable | 9 |

### Registry 更新
- **v3** (`cls8b-s42-ckpt1200-val8192-v3`): RUNNING → DONE/success，写入 metrics、修正 log_path
- **eval** (`cls8b-s42-ckpt1200-val8192-eval`): RUNNING → DONE/success（同一 PID 316940 的重复条目）
- **v2**: 维持 DONE/failed 不变（GPU 冲突导致的重复提交）

### GPU 状态
4 张 5090 全部在用（GPU0 刚释放，GPU1-3 训练中 93-99% 利用率）。cuda:0 现在空闲可接新任务。

---

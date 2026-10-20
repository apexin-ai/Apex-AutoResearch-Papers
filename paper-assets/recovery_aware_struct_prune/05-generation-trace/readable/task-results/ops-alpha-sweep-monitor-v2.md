# ops alpha sweep monitor v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_alpha-sweep-monitor-v2_20260515T213548_result.json`
- **Structured JSON:** [`07aedd3b9baf78da2e5b.json`](../../sessions/07/07aedd3b9baf78da2e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇总：**
- 原始 sweep 脚本在 α=0.0 eval 阶段因 HuggingFace 网络不可达崩溃
- α=0.0 后来被单独重跑成功：**accuracy=27%, EOS rate=80%, avg_len=1192**
- α=0.25/0.5/1.0/2.0 从未执行
- 已创建修复脚本（加了 `HF_HUB_OFFLINE=1`、正确的 `--importance_path`/`--cka_path`/`--mode rasp` 参数）并启动（PID 556867）
- 3 分钟后回来检查进度

---

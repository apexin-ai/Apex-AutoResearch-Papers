# experiment mvp v3 submit

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_v3_submit_20260513T160004_result.json`
- **Structured JSON:** [`e18907bbd5ec5025ee10.json`](../../sessions/e1/e18907bbd5ec5025ee10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验运行正常：

| 实验 | GPU | 显存 | 利用率 |
|------|-----|------|--------|
| mvp_v3_cr70 | cuda:0 | 16256MiB / 97887MiB | 78% |
| mvp_v3_cr85 | cuda:1 | 16225MiB / 97887MiB | 80% |

**总结**：
- 首次提交因 HuggingFace 网络不通失败，已 kill 并用本地模型路径 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` 重新提交
- 两个实验均已进入 RUNNING 状态，GPU 有负载，registry 已更新含完整 spec 信息
- 日志路径：`~/runs/turn-hier-kv-compress/mvp_v3_cr70.log` / `mvp_v3_cr85.log`

---

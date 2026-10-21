# ops oft object baseline westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oft-object-baseline-westd41074_20260521T020135_result.json`
- **Structured JSON:** [`778ef570cb7298c5c679.json`](../../sessions/77/778ef570cb7298c5c679.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OFT Object baseline eval 已成功启动并开始跑第一个 task。

**总结：**
- eval 脚本已从 westd-38929 部署到 westd-41074（修复了 transformers 5.x 兼容性：import 名称、API 参数、state_dict `module.` 前缀）
- OFT Object checkpoint 已在 westd-41074 上（之前已下载）
- 任务已提交到 cuda:1，exp_id=`eval_oft_baseline_object_seed42`
- 10 个 task x 50 episodes，预期运行数小时
- 日志：`~/runs/importance_margin_vla_compress/eval_oft_baseline_object_seed42.log`

---

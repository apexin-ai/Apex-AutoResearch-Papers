# gpu qwen L14 cuda1 restart

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_qwen-L14-cuda1-restart_20260522T143601_result.json`
- **Structured JSON:** [`3898a26a171b98c4573b.json`](../../sessions/38/3898a26a171b98c4573b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen L14 steering 已在 cuda:1 启动并配置监控。

**汇报：**
- **PID**: 493122，运行在 cuda:1（14995 MiB 占用）
- **Registry**: `steering_107_qwen_L14` 已注册为 RUNNING
- **日志**: 模型加载中（checkpoint shards 60%+），Probe accuracy at L14 = 0.7024
- **数据**: 84 conflict / 168 total samples，6 alphas (-20,-10,-5,5,10,20)
- **监控**: 每 8 分钟自动检查进程、日志和 GPU 状态
- **预计完成**: ~50 min

注：原始命令中 `--activation_dir` 参数不存在，已去掉后成功启动。L13 (PID 490477) 和 DE activations (PID 488140) 均已结束。

---

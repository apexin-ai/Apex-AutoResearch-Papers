# ops westd redownload 14b mistral

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-redownload-14b-mistral_20260518T065055_result.json`
- **Structured JSON:** [`2d9b2f6428081fd531c2.json`](../../sessions/2d/2d9b2f6428081fd531c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度正常，数据在增长。当前状态：

| 模型 | 已下载 | 目标大小 | PID |
|------|--------|----------|-----|
| Qwen2.5-14B | 3.0G | ~28G | 4086 |
| Mistral-7B-v0.3 | 428M | ~14G | 4582 |
| Qwen2.5-7B | 78M | ~15G | 4733 |

三个下载均通过 nohup 后台运行（tmux 未安装）。另有一个 agent 在反复启动重复的 screen sessions，已清理。

**注意风险**：nohup 进程在 SSH 断开后可能被 kill（取决于服务器配置）。如果后续发现进程消失，需要重连重启。

预计完成时间取决于带宽，按当前速度（~200MB/s for 14B）：
- 7B: ~10-15 分钟
- Mistral: ~10-15 分钟  
- 14B: ~15-20 分钟

---

# infra fix download paths

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-download-paths_20260516T080218_result.json`
- **Structured JSON:** [`134887bb5eef5fc098ce.json`](../../sessions/13/134887bb5eef5fc098ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行。当前状态汇总：

| 项目 | 状态 |
|------|------|
| 旧进程 kill | ✅ |
| MiniLM | ✅ symlink 已创建并验证 |
| ArmoRM | ⏳ 下载中 (137MB/~16GB), PID 485200 |
| UltraFeedback | ⏳ 等 ArmoRM 完成后自动开始 |
| vendi-score | ✅ 已安装 |
| config.py 路径 | ✅ 已更新匹配实际目录 |

config.py 最终路径：
- `BASE_MODEL`: `.../Qwen/Qwen3-0___6B` ✅
- `REWARD_MODEL`: `.../RLHFlow/ArmoRM-Llama3-8B-v0___1` ✅
- `EMBED_MODEL`: `.../sentence-transformers/all-MiniLM-L6-v2` ✅

ArmoRM ~16GB，按 5MB/s 约需 50 分钟。轮询命令：
```
tail -3 /root/autodl-tmp/download_armo2.log
du -sh /root/autodl-tmp/models/RLHFlow/ArmoRM-Llama3-8B-v0___1/
```

---

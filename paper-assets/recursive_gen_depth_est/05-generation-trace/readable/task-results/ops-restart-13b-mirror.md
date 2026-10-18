# ops restart 13b mirror

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart_13b_mirror_20260517T113254_result.json`
- **Structured JSON:** [`bade1677562deb35dbae.json`](../../sessions/ba/bade1677562deb35dbae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

994MB，持续增长。下载速度稳定在 ~2-3 MB/s。

总结当前状态：

- **tmux session**: `qwen25_14b_scale` 运行中
- **下载方式**: aria2c 16 连接从 hf-mirror.com → XET CDN
- **当前进度**: shard 1/8 下载中，~1GB/3.6GB
- **预估时间**: 每 shard ~25-30 分钟，8 个 shard 共 ~3.5-4 小时完成下载
- **下载后自动执行**: 模型加载 → d0 生成 → LoRA finetune → d1-d3 生成 → 特征提取 → 分类
- **registry**: qwen25_14b_scale_001，状态 RUNNING

**关键修改**:
1. 注释 `source /etc/network_turbo`（代理导致 timeout）
2. 添加 `HF_ENDPOINT=https://hf-mirror.com` + `unset proxy`
3. 替换 `hf download` 为 `aria2c` 16 连接并行下载

---

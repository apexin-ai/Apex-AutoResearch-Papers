# setup exp012 download llama

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_exp012-download-llama_20260520T041927_result.json`
- **Structured JSON:** [`609a3e4d710e6d83f773.json`](../../sessions/60/609a3e4d710e6d83f773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载在后台稳定运行（PID 214625），3 分钟内各 shard 下载了约 130MB。

**当前状态总结：**
- 下载方式：ModelScope（排除了 .pth 文件，只下载 safetensors + tokenizer）
- 总大小：~15GB（4 个 safetensors shard + 配置文件）
- 总吞吐：~1.8MB/s（4 流并行，每流 ~450kB/s）
- **model-00004** (1.09GB): ~40 分钟完成
- **model-00001/02/03** (~4.6GB each): ~2.5 小时完成
- 存储路径：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3-8B-Instruct`（ModelScope 格式）

**预计总完成时间：约 2.5 小时后（~当前时间 + 2.5h）。**

你可以等下载完成后告诉我，我来做验证和加载测试。或者你也可以用以下命令自行监控：
```bash
# 查进度
tail -10 /tmp/llama3_download.log

# 查是否完成
grep "DOWNLOAD_COMPLETE" /tmp/llama3_download.log

# 查进程状态
ps -p 214625 -o pid,etime
```

---

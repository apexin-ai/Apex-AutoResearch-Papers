# ops westd download mistral dryrun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-download-mistral-dryrun_20260518T064940_result.json`
- **Structured JSON:** [`d2be72302f4d9632c255.json`](../../sessions/d2/d2be72302f4d9632c255.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度下降明显（带宽被多个并发下载分摊）。汇报当前完整状态：

---

## 当前状态汇总

### Step 1: Mistral-7B-v0.3 下载
- **状态**: 运行中（PID 5065，nohup 后台）
- HF_ENDPOINT=hf-mirror.com，已禁用 xet 协议

### Step 2: Qwen 模型下载状态
- **Qwen2.5-7B**: 2/4 shards 完成（model-00002, model-00004），2 个 shard 正在下载（1.93G / 3.6G, 1.58G / 3.6G）
- **Qwen2.5-14B**: 下载中，尚无 shard 完成
- **DOWNLOAD_DONE.txt**: 未创建

### Step 3 & 4: Dry-run
- 无法执行，模型尚未完全下载

### Step 5: QLoRA 代码位置（`train_sft.py`）
| 行号 | 内容 |
|------|------|
| 23 | `BitsAndBytesConfig` import |
| 119 | `--load-in-4bit` argparse 参数 |
| 159-167 | QLoRA 配置块（4bit quantization config） |
| 254 | `load_in_4bit` 写入训练参数记录 |

### GPU 状况
- 4x NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 全部空闲（0 MiB 显存占用）

### 瓶颈
- 服务器同时有 4+ 个模型在下载（含其他 session 的 gemma-2-9b），带宽严重竞争
- 当前下载速率约 10-15 MB/min/shard
- 7B 剩余 2 个 shard 预计还需 ~30-60 分钟
- 14B 和 Mistral 更久

下载进程都在 nohup 后台稳定运行，会自动完成。需要我继续轮询等待 7B 完成后做 dry-run，还是先到这里？

---

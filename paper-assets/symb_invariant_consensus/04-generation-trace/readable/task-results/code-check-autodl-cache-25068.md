# code check autodl cache 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-autodl-cache-25068_20260518T074409_result.json`
- **Structured JSON:** [`506852c4ba6b07e92c53.json`](../../sessions/50/506852c4ba6b07e92c53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 缓存搜索：未找到

| 路径 | 状态 |
|------|------|
| `/root/autodl-pub/` | 仅 CV 数据集（ImageNet, COCO 等），无 LLM 模型 |
| `/root/share/` | 不存在 |
| `/root/autodl-fs/` | 不存在 |
| `/data/`, `/models/`, `/shared/` | 不存在 |
| `/root/.cache/huggingface/hub/` | 空壳（4K，仅 refs 目录） |

Qwen2.5-72B-Instruct 和 Llama-3.1-70B 均无预缓存。

### 当前下载进度

- **PID 5399** 运行中，16 workers 并行从 `hf-mirror.com` 下载
- **已下载**: 16/37 shard 文件出现，但多数尺寸远小于预期（每 shard 应约 4GB），说明大部分仍在传输中
- **磁盘占用**: 5.8G / 250G（3%）
- **config.json**: 有效（Qwen2ForCausalLM, 80层, hidden_size=8192）
- **预计总大小**: ~145GB，按当前速度还需较长时间

### 结论

无可用缓存，只能继续当前下载。下载脚本支持断点续传，无需干预。

---

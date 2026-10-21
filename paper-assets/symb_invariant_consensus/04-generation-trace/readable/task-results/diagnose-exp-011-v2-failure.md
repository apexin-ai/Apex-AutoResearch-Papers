# diagnose exp 011 v2 failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-011-v2-failure_20260517T032305_result.json`
- **Structured JSON:** [`44646df56404134e86d2.json`](../../sessions/44/44646df56404134e86d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Root cause**: `model-00002-of-00004.safetensors` 文件损坏（下载不完整）。

证据：
- 错误信息：`safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered`
- index.json 声明 total tensor size = 16.06GB
- 实际文件总和只有 ~14.9GB
- shard 2 只有 3.88GB（其他 shard 约 4.9GB），且修改时间晚于其他文件（19:29 vs 18:15），明显是断点续传失败

**修复方案**：重新下载 shard 2。

```bash
# 删除损坏文件并重新下载（ModelScope 路径）
cd /root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct
rm model-00002-of-00004.safetensors
modelscope download --model LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --include "model-00002-of-00004.safetensors" \
  --local_dir .
```

或用 huggingface-cli（如果模型来源是 HF）：
```bash
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct \
  model-00002-of-00004.safetensors \
  --local-dir .
```

**修复难度**：取决于网速。命令本身 1 分钟搞定，但下载 ~5GB 文件需要几分钟。总计 ~10 分钟可完成。

**另外注意**：当前 GPU 上有一个 Mistral-7B vLLM (PID 270112, port 8000) 在跑，占 15GB 显存。exp-011 的 LLaMA-8B 需要 ~17GB，98GB 显卡空间足够两个共存，但如果 Mistral 不需要了建议先 kill 掉。

要我现在执行修复吗？

---

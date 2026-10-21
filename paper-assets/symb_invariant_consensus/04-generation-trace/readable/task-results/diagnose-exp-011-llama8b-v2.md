# diagnose exp 011 llama8b v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-011-llama8b-v2_20260517T032306_result.json`
- **Structured JSON:** [`a5bd8796239c2fd87d80.json`](../../sessions/a5/a5bd8796239c2fd87d80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因

**模型权重文件损坏**: `model-00002-of-00004.safetensors`

关键错误信息：
```
safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered
```

文件大小对比（LLaMA-3.1-8B 标准 shard 约 4.9G）：
| 文件 | 实际大小 | 修改时间 |
|------|----------|----------|
| model-00001 | 4.7G | May 16 18:15 |
| **model-00002** | **3.7G** ← 明显偏小 | **May 16 19:29** ← 时间异常 |
| model-00003 | 4.6G | May 16 18:15 |
| model-00004 | 1.1G | May 16 18:40 |

`model-00002` 比预期少约 1.2G，且修改时间晚于其他 shard，说明下载中断导致文件不完整。

### 两次失败是否同一原因

是。两次 traceback 完全一致，都在 `safetensors_weights_iterator` 加载权重时失败。v2 所谓的 "修复 GPU OOM" 并未解决真正问题。

### 额外问题

当前 GPU 上仍有一个 vLLM 进程在运行（PID 270691，占用 14.6G 显存），可能是之前实验的残留。

### 修复步骤

1. **Kill 残留 vLLM 进程**：
   ```bash
   kill 270691
   ```

2. **重新下载损坏的 shard**：
   ```bash
   cd /root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/
   rm model-00002-of-00004.safetensors
   # 用 huggingface-cli 或原始下载方式重新获取该文件
   huggingface-cli download LLM-Research/Meta-Llama-3.1-8B-Instruct \
     model-00002-of-00004.safetensors \
     --local-dir . --local-dir-use-symlinks False
   ```
   如果 HF 不可用（国内网络），用 modelscope：
   ```bash
   modelscope download --model LLM-Research/Meta-Llama-3.1-8B-Instruct \
     model-00002-of-00004.safetensors --local_dir .
   ```

3. **验证文件完整性后重跑**：
   ```bash
   python -c "from safetensors import safe_open; f=safe_open('model-00002-of-00004.safetensors', framework='pt'); print('OK, keys:', len(f.keys()))"
   ```

4. 验证通过后重新提交 exp-011。

---

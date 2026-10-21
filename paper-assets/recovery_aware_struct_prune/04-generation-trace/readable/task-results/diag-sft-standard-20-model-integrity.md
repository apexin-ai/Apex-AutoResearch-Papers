# diag sft standard 20 model integrity

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft_standard_20_model_integrity_20260519T212031_result.json`
- **Structured JSON:** [`b475de0a00f32e6cdd26.json`](../../sessions/b4/b475de0a00f32e6cdd26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 模型完整性：**模型完好，非损坏**

| 检查项 | 结果 |
|--------|------|
| 文件大小 | model.safetensors 11753.0MB, tokenizer 10.9MB — 正常 |
| Tokenizer | OK, vocab_size=151643 (Qwen2) |
| 模型加载 | v3 日志确认加载成功: "Non-uniform MLP detected: intermediate_size range [8128, 18944]" |

（注：裸 `AutoModelForCausalLM.from_pretrained` 因 pruned MLP 尺寸不匹配会报错，但 eval_mbpp.py 的自定义加载逻辑正确处理了非均匀结构。）

### 根因：**网络不可达，非模型问题**

v3 日志完整链条：
1. 模型加载成功
2. `load_dataset("mbpp", split="train")` → 尝试 HEAD `https://huggingface.co/datasets/mbpp/resolve/main/README.md`
3. `[Errno 101] Network is unreachable` → 重试后 `RuntimeError: Cannot send a request, as the client has been closed`

**westd-29022 当前网络已断**（curl HuggingFace 返回 HTTP:000）。

### PID 141113 状态

- 在 cuda:0 上运行，但状态 `Sleeping`，217 线程，~1GB RSS
- **未分配 GPU 显存**（nvidia-smi 无此 PID）→ 卡在同一个 HF 数据集下载重试中，模型尚未加载到 GPU
- 建议 kill 掉，浪费资源

### 为什么 grpo_standard 能跑通

MBPP 缓存存在于 `/root/.cache/huggingface/datasets/mbpp/full/`。grpo_standard 大概在网络可用时运行并缓存了数据集，但 datasets 库默认仍会发 HEAD 请求检查更新 — 网络断后即使有缓存也会失败。

### 建议修复

重启 eval 时加 `HF_DATASETS_OFFLINE=1`：
```bash
HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048
```

或在 eval_mbpp.py 第 108 行改为 `load_dataset("mbpp", split="train", cache_dir="/root/.cache/huggingface/datasets")` 并设置离线模式。

需要我现在 kill PID 141113 并用离线模式重启 eval 吗？

---

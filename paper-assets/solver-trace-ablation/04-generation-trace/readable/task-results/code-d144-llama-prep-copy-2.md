# code d144 llama prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d144-llama-prep_20260519T125113_result.json`
- **Structured JSON:** [`b7ddd14a4ac9f1578698.json`](../../sessions/b7/b7ddd14a4ac9f1578698.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载在跑但 `ignore_patterns` 没生效（还在下载 `consolidated.00.pth`）。速度 ~500kB/s，预计 2-3 小时完成 safetensors。

## 当前状态报告

### 1. LLaMA-3.2-3B 下载
- **状态**: 进行中（ModelScope，PID 392119）
- **原因**: HF 版本是 gated repo 需要认证，服务器无 HF token，改用 ModelScope
- **进度**: model-00001 (4.62GB) ~2%，model-00002 (1.36GB) ~8%
- **预计完成**: 2-3 小时
- **下载路径**: `/root/autodl-tmp/models/Llama-3.2-3B-ms-cache/LLM-Research/Llama-3.2-3B/`

### 2. 代码兼容性
- **train_grpo.py**: ✅ 完全兼容，无需修改
  - `--model_path` 可配置，指向 LLaMA 即可
  - `AutoModelForCausalLM` + `AutoTokenizer` 是通用的
  - `enable_thinking=False` 被 LLaMA chat template 静默忽略
- **eval_sta.py**: ✅ 完全兼容，无需修改
  - `enable_thinking=False` 同理
  - `&lt;think>` 标签清理对 LLaMA 输出是 no-op

### 3. LLaMA-3.2-3B 模型特征
- 架构: LlamaForCausalLM, 28层, hidden_size=3072
- 参数量: ~3B (6.4GB total weights)
- dtype: bfloat16 ✅（与 GRPOConfig bf16=True 匹配）
- pad_token: `<|finetune_right_pad_id|>` (128004) ✅
- chat_template: 有（LLaMA3 格式）✅

### 4. 磁盘
- `/root/autodl-tmp`: 60G/250G used (191G 可用)，空间充足

### 5. 待做（下载完成后）
1. 确认 ModelScope 模型路径
2. 清理 `consolidated.00.pth`（PyTorch 格式，不需要，~6GB）
3. 清理 HF 未完成下载 (`/root/autodl-tmp/models/Llama-3.2-3B/.cache/`, ~3.9GB)
4. Dry-run 验证
5. 推荐 batch_size（LLaMA-3.2-3B 比 Qwen3-4B 小，96GB 卡上可用更大 batch）

需要我过一段时间再来检查下载进度吗？

---

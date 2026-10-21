# prep new models c

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_new-models-c_20260516T072518_result.json`
- **Structured JSON:** [`17327815dba2eb10e02f.json`](../../sessions/17/17327815dba2eb10e02f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

路径已正确。所有任务除 CodeLlama 下载外全部完成。

---

## 总结

### 完成项

| 项目 | 状态 |
|------|------|
| **Qwen-2.5-Coder-1.5B-Instruct 下载** | ✅ 完成 (2.88GB, `/root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct`) |
| **CodeLlama-7b-Instruct-hf 下载** | ⏳ 进行中 (safetensors shard 1/2 at 15%, ~45 min) → `/root/autodl-tmp/models/CodeLlama-7b-Instruct-hf` |
| **train_sft.py 兼容性** | ✅ 通用 `apply_chat_template()`，无需修改 |
| **evaluate.py 兼容性** | ✅ 同上，无需修改 |
| **LoRA target modules** | ✅ 两个模型都使用 `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` |
| **CPU Dry-run** | ✅ 两个模型 tokenization + data loading 通过 |
| **7 实验注册** | ✅ 全部 PREPARING 状态 |
| **训练命令** | ✅ 保存到 artifacts |

### Dry-run 结果

| 模型 | Vocab | 架构 | 样本长度 | Chat Template |
|------|-------|------|---------|--------------|
| Qwen-1.5B | 151,665 | Qwen2ForCausalLM | 342 tokens | im_start/im_end |
| CodeLlama-7B | 32,016 | LlamaForCausalLM | 351 tokens | LLaMA Instruct |

### 无需代码修改

`train_sft.py` 和 `evaluate.py` 完全通用——`apply_chat_template()` + LoRA target modules 名称兼容两个新模型。

### 待办

CodeLlama 模型权重下载中 (PID 252903, nohup 后台运行)。下载完成后即可开始训练。可用 `tail /tmp/dl_codellama_ms.log` 检查进度。

---

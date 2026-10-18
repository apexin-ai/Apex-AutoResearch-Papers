# ops codellama profiling check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_codellama_profiling_check_20260515T184729_result.json`
- **Structured JSON:** [`40effed5141ff63c914d.json`](../../sessions/40/40effed5141ff63c914d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**下载状态：已完成 ✓**

**模型路径：** `/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/`

**完整性检查：通过 ✓**
- `config.json` 存在 — LlamaForCausalLM, 32 layers, 32 KV heads (MHA, 非 GQA)
- safetensors: 2/2 文件完整（9.98GB + 3.50GB）
- pytorch_model.bin: 6/6 分片 + 2/2 合并版均存在
- tokenizer 文件齐全
- 无 `.incomplete` 文件

**GPU 状态：两块 GPU 均空闲**
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 0 MiB / 97887 MiB | 0% |
| 1 | RTX PRO 6000 Blackwell | 0 MiB / 97887 MiB | 0% |

**Qwen compounding sweep 已结束**，cuda:1 已释放。

**结论：** CodeLlama-7B profiling 可以立即在 cuda:1（或任一 GPU）上启动。

---

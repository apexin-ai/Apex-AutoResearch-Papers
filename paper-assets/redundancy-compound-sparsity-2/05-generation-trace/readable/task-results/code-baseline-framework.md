# code baseline framework

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_framework_20260512T132433_result.json`
- **Structured JSON:** [`6dcabb331ff901b35023.json`](../../sessions/6d/6dcabb331ff901b35023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 步骤 | 状态 | 说明 |
|------|------|------|
| kvpress 安装 | ✅ | v0.5.3，Qwen2ForCausalLM 在 SUPPORTED_MODELS 中 |
| R-KV clone | ✅ | `/root/carc/r_kv_baseline/`（已存在，含 HuggingFace/SGLang/vLLM 集成） |
| kvpress 兼容性 | ✅ | 7 个 baseline 全部可实例化 |
| eval_baselines.py | ✅ | 服务器 `/root/carc/eval_baselines.py` + 本地 artifact 已注册 |
| dry-run | ✅ | `--help` 和 `--dry-run` 均通过 |

**可用 baselines**: full, knorm (H2O), snapkv, keydiff, streaming_llm, expected_attn, observed_attn, tova

**运行命令**（D003 结束后）：
```bash
python eval_baselines.py --model /root/carc/models/DeepSeek-R1-Distill-Qwen-14B --gpu 0 --budget-ratio 0.5
```

---

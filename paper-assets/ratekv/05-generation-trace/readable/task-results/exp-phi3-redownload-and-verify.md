# exp phi3 redownload and verify

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phi3_redownload_and_verify_20260515T161848_result.json`
- **Structured JSON:** [`1a93bc4ef065bcbe2b70.json`](../../sessions/1a/1a93bc4ef065bcbe2b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足**：autodl-tmp 只有 24GB 可用，Phi-3-medium 约需 28GB。

当前 autodl-tmp 使用情况：
| 路径 | 大小 |
|------|------|
| `.hf_cache/` | 117GB（Qwen 42G, Gemma 35G, Yi 17G, EleutherAI 5.5G） |
| `prov_grounded_uie/` | 68GB |
| `models/` | 44GB（Llama-3.1-8B 30G 硬链接, Mistral-7B 14G） |

可能可清理的候选：
1. `/root/autodl-tmp/models/Mistral-7B-v0.3/` (14GB) — 如果实验已改用 .hf_cache 路径
2. `/root/autodl-tmp/.hf_cache/EleutherAI/` (5.5GB) — Pythia-1.4b，如果不再需要
3. 还有个正在进行的 CodeLlama-7b 下载（PID 349208），完成后会再占 ~13GB

需要你确认可以删除哪些来腾出空间（至少 ~5GB）。

---

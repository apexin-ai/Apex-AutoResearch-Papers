# ssh deploy phi3 profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy_phi3_profiling_20260515T231033_result.json`
- **Structured JSON:** [`3a2ab8db3148c37093a8.json`](../../sessions/3a/3a2ab8db3148c37093a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Profiling 已成功启动并产出首条结果。

## 产出汇总

| 项目 | 结果 |
|------|------|
| **patch_attention 兼容性** | Phi-3 使用 fused `qkv_proj`，原始 eval_ppl.py 不兼容。已修补 `patch_attention` 增加 fused qkv 分支（`hasattr(orig_attn, 'qkv_proj')` 检测），不影响已有模型 |
| **trust_remote_code** | 改为 `False`。原因：Phi-3 自带的 modeling_phi3.py 用旧 forward 签名（`position_ids`），与 eval_ppl.py 期望的 `position_embeddings` 不兼容。transformers 4.57.6 原生 Phi-3 签名匹配 |
| **脚本部署** | `/root/ratekv/run_phi3_medium_hires_profiling.py` + eval_ppl.py patch 已部署 |
| **模型下载** | 已完成，6/6 shards，总计 ~27GB |
| **Profiling 状态** | PID 383089，cuda:1 (28GB)，Baseline PPL=4.7834，已开始逐头 profiling，ETA ~337min (~5.6h)。日志：`/tmp/phi3_profiling.log` |

旧的 `phi3_auto_profiling.sh`（PID 352691）已终止——它有两个 bug：模型路径错误（`microsoft/` vs `LLM-Research/`）且下载完成信号不匹配。

---

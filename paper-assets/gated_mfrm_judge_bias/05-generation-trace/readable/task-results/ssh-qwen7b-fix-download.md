# ssh qwen7b fix download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen7b_fix_download_20260522T191051_result.json`
- **Structured JSON:** [`cc4f591c2afbf37b0871.json`](../../sessions/cc/cc4f591c2afbf37b0871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **ModelScope 文件完整性**：下载完成，4 个 safetensors 文件大小正确（3.56-3.95 GB，总计 ~15.2 GB）
2. **根因修复**：发现 `network_turbo` 代理的 `no_proxy` 列表缺少 `modelscope.cn`（只有 `.com`），导致 ModelScope 国内 CDN 流量错误走国际代理（480 kB/s → 修复后 3.5-18 MB/s）。下载耗时 850 秒（14 分钟），vs 原估计 2+ 小时
3. **vLLM 启动**：成功。模型加载 15 秒，使用 Flash Attention v2，cuda:1，GPU KV cache 128.7 万 tokens
4. **Response generation**：**已完成**。500/500 prompts，0 errors，生成耗时约 70 秒，峰值 output 9524 toks/s。输出保存在 `/root/gated_mfrm_judge_bias/data/arena_hard/responses/qwen2.5-7b.jsonl`

---

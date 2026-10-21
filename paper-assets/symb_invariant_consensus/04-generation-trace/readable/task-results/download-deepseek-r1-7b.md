# download deepseek r1 7b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_deepseek-r1-7b_20260516T063502_result.json`
- **Structured JSON:** [`2eb7d7e0271762729775.json`](../../sessions/2e/2eb7d7e0271762729775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果汇总：**

| 项目 | 详情 |
|------|------|
| 模型路径 | `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| 模型大小 | 15GB（2 个 safetensors 文件） |
| vLLM 脚本 | `/root/symb_invariant_consensus/scripts/start_vllm_deepseek_r1_7b.sh` |
| 脚本语法 | OK |
| 数据盘剩余 | 116GB / 250GB (54% used) |

脚本配置：port 8000, max-model-len 8192, gpu-memory-utilization 0.9, trust-remote-code, dtype auto。注意当前 exp-001 正在占用 port 8000 和 GPU，需要先停掉 Qwen2.5-14B 的 vLLM 才能启动 DeepSeek-R1-7B。

---

# exp vllm version check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_vllm_version_check_20260516T122946_result.json`
- **Structured JSON:** [`25224e027fa71a7fd850.json`](../../sessions/25/25224e027fa71a7fd850.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器上安装的 vLLM 版本确实是 **0.20.2**。

验证来源：
- `vllm.__version__` → `0.20.2`
- dist-info 目录名 → `vllm-0.20.2.dist-info`
- METADATA 文件 → `Version: 0.20.2`

论文写的 "v0.20.2" 是正确的。Reviewer 的质疑基于过时认知——vLLM 在 2025 年下半年将版本号从 0.6.x 跳跃到了 0.8+，此后迭代很快（0.8 → 0.9 → ... → 0.20），当前（2026-05）最新稳定版就是 0.20.x 系列。

---

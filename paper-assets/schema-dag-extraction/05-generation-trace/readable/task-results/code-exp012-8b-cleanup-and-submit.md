# code exp012 8b cleanup and submit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012_8b_cleanup_and_submit_20260515T162406_result.json`
- **Structured JSON:** [`f434c7ffbea749a63547.json`](../../sessions/f4/f434c7ffbea749a63547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1 — AWQ 清理** ✓
- kill 284997 (下载) + 292859 (auto_start)
- 删除 `/root/autodl-tmp/.hf_cache/llama-3.1-70b-instruct-awq-int4/` (~28GB)
- 磁盘从 250G/250G → 213G/250G，释放 37GB

**Step 2 — exp012 LLaMA-3.1-8B-Instruct 已提交** ✓
- GPU 已空闲，无需等待
- 脚本：`scripts/run_exp012_llama_8b.sh`（无 flashinfer、无量化、BF16 直接加载）
- 模型：`/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- PID: 295200，GPU 82% / 89523 MiB
- 日志：`/root/schema-dag-extraction/logs/exp012_llama_8b.log`
- Registry: `exp012_llama_8b_fewnerd` → RUNNING
- exp1 (Count Baseline) 已开始 extraction，1000 samples / 64 types

---

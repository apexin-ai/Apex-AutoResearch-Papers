# fix hf network rerun signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hf_network_rerun_signals_20260516T191302_result.json`
- **Structured JSON:** [`c62cde89a0b71a278e33.json`](../../sessions/c6/c62cde89a0b71a278e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1) 网络问题根因
`/etc/network_turbo` 存在但未被实验脚本 source。AutoDL 代理设置了 `http_proxy=http://172.26.1.26:12798`，不激活则无法访问 huggingface.co。修复方式：实验命令中加 `HF_HUB_OFFLINE=1`（模型已缓存）或提前 `source /etc/network_turbo`。

### 2) 模型缓存状态
`sentence-transformers/all-MiniLM-L6-v2` 已缓存在多个路径：
- `/root/autodl-tmp/.hf_cache/hub/models--sentence-transformers--all-MiniLM-L6-v2/`
- `/root/autodl-tmp/.hf_cache/models--sentence-transformers--all-MiniLM-L6-v2/`
- `/root/autodl-tmp/models/st/models--sentence-transformers--all-MiniLM-L6-v2/`

缓存完整，`HF_HUB_OFFLINE=1` 可以正常离线加载。

### 3) 实验状态：两个目标实验均已完成，无需重跑

**实验 A — Llama-3.2-3B_d000_s42 GSM8K signals**:
已有完整输出（signals_merged_gsm8k.json = 243KB, 2026-05-17 03:02）：
- signal_s1_embedding_gsm8k.json ✓
- signal_s2_minkpp_gsm8k.json ✓
- signal_s4_selfcritique_gsm8k.json ✓
- signals_merged_gsm8k.json ✓

**实验 B — Qwen2.5-1.5B-Instruct MMLU signals**:
已有完整输出（signals_merged_mmlu.json = 2.5MB, 2026-05-17 02:01）：
- signal_s1_embedding_mmlu.json ✓
- signal_s2_minkpp_mmlu.json ✓
- signal_s4_selfcritique_mmlu.json ✓
- signals_merged_mmlu.json ✓

### 4) GPU 状态
- cuda:2: 空闲 (0 MiB)
- cuda:4: PID 831936 占 570 MiB（小进程）

### 5) 附带发现
Llama-3.2-3B_d000_s42 的 **MMLU** 信号不完整——缺 `signal_s4_selfcritique_mmlu.json` 和 `signals_merged_mmlu.json`。如需补跑请指示。

---

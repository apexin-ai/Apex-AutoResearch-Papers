# infra experiment status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_experiment-status-check_20260521T122623_result.json`
- **Structured JSON:** [`bc8f99435ee2b30e369e.json`](../../sessions/bc/bc8f99435ee2b30e369e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. gpt-4o FOLIO-204 (PID 418902) — 进行中
- 已跑 2h51m，**99/204** 问题完成（正在处理第100个）
- 平均 102.8s/问题，ETA ~**180 min** → 约 **23:25 UTC May 21**
- 偶有 502 错误但自动重试，整体正常

### 2. 70B AWQ 下载 — **已完成**
- 路径：`/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ/`
- 11/11 safetensors shards 全部到位，总计 **41.6 GB**
- config.json 确认 AWQ 4-bit, group_size=128, Qwen2ForCausalLM
- VLLM 未启动（按要求等主 Agent 决定 GPU 分配）
- 注：当前有个后台进程在下载 sentence-transformers/all-MiniLM-L6-v2（非 72B 相关）

### 3. Cross-Model SICA (PID 414515) — 进行中
- 已跑 3h46m，总计 **204** 个 ProofWriter 问题
- Phase 1 进度：**60/204**（checkpoint 59 done，第60个接近完成）
  - mistral_traces: 60 | extraction_mistral_same: 60 | extraction_mistral→qwen3: 60 | extraction_qwen3_same: 60 | extraction_qwen3→mistral: 59
- 平均 ~3.8 min/问题，144 remaining → ETA **~9 hours** → 约 **05:30 UTC May 22**
- 使用 localhost:8000 (Mistral-7B) + localhost:8001 (Qwen3-14B)

### 4. GPU 状态
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 84.2/97.9 GB | 0% |
| 1 | RTX PRO 6000 Blackwell (96GB) | 83.6/97.9 GB | 100% |
| 2 | RTX PRO 6000 Blackwell (96GB) | 空闲 | 0% |
| 3 | RTX PRO 6000 Blackwell (96GB) | 空闲 | 0% |

GPU 0-1 被 VLLM（Mistral + Qwen3）占用，GPU 2-3 空闲可用。72B AWQ 部署后需要 ~40GB 显存（4-bit），单卡即可加载。

---

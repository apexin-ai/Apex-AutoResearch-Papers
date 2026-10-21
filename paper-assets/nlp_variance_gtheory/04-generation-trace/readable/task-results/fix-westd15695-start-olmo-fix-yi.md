# fix westd15695 start olmo fix yi

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd15695_start_olmo_fix_yi_20260521T142810_result.json`
- **Structured JSON:** [`dfec5b94f24c4e6afed0.json`](../../sessions/df/dfec5b94f24c4e6afed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进展良好。

**OLMo 推理状态：**
- PID: 19586 (EngineCore: 19807)
- 进度: condition 186/432 (43%)，9,600 行已输出
- 速度: 740 prompts/s, ~425K input toks/s
- 预计 3-4 分钟完成

**Yi 下载状态：**
- PID: 19064
- shard 4: 65% (1.67G/2.59G, ~3 min)
- shard 1: 20% (952M/4.59G, ~12 min)
- shard 2、3 同步下载中
- 预计 12-15 分钟全部完成

**解决的问题：**
- FlashInfer 0.6.8 不支持 Blackwell (sm_120) → 用 `VLLM_USE_FLASHINFER_SAMPLER=0` + `FLASHINFER_DISABLE_VERSION_CHECK=1` 绕过
- Yi 目录在 `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B-Chat/`（ModelScope 命名），shard 1/3/4 截断 → 删除后通过 ModelScope 重新下载
- vLLM 0.21 不识别 `VLLM_USE_V1=0`（代码中已设置但被忽略）→ V1 引擎下禁用 FlashInfer 组件即可

---

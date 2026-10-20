# code svs data generation

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_svs_data_generation_20260514T045149_result.json`
- **Structured JSON:** [`74768a0a6304d9532f6e.json`](../../sessions/74/74768a0a6304d9532f6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

- `data/loader.py`: 3 个导出函数 (`load_proofwriter`, `load_folio`, `load_problems`)，HF datasets 加载 + 本地 JSON fallback，seed 控制采样，ProofWriter 按 `proof_depth` 筛选 depth-5，label 归一化处理多种格式
- `generation/chain_sampler.py`: `ChainSampler` 类，OpenAI 兼容 API 调用（延迟导入避免无 openai 包时 import 失败），step-by-step prompt，正则 + fallback 提取答案，指数退避重试

---

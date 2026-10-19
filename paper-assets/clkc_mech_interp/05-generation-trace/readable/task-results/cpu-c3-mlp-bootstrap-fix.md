# cpu c3 mlp bootstrap fix

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_c3-mlp-bootstrap-fix_20260522T083245_result.json`
- **Structured JSON:** [`bc76692e8b3e8e00bc3e.json`](../../sessions/bc/bc76692e8b3e8e00bc3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在正常运行：

**Qwen bootstrap** (原进程): qwen3_conflict L23 已到 450/1000，继续跑，不受影响

**Llama fix** (PID 467703): 已启动 `llama31_conflict_en_zh_L18` (layer 18, n_boot=1000)，数据加载正常 (Train: 1096×4096, Test: 272×4096)

**修改内容：**
- 新建 `src/bootstrap_mlp_delta_llama_fix.py`，包含 6 个 Llama 条件：
  - `conflict_en_zh_L18` — MLP 峰值层，C3 核心
  - `conflict_en_zh_L5` — Linear 峰值层，对比
  - `conflict_en_en_L16` — EN→EN MLP 峰值，对照方向
  - `conflict_en_en_L28` — EN→EN Linear 峰值，对照方向
  - `xnli_en_zh_L18` — XNLI @ conflict MLP 峰值
  - `xnli_en_zh_L5` — XNLI @ conflict Linear 峰值
- 每个条件 n=1000 bootstrap
- 输出 → `data/c3_mlp_bootstrap_llama_fix.json`

---

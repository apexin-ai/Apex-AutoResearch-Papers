# analysis folio 2x2 data audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_folio-2x2-data-audit_20260521T225900_result.json`
- **Structured JSON:** [`a12a9f0c0ad719700601.json`](../../sessions/a1/a12a9f0c0ad719700601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清点完毕。汇报如下：

---

## FOLIO-204 Cross-Model 2×2 数据清点报告

### 1. FOLIO-204 CoT Traces

| 模型 | 状态 | 路径 | 文件数 |
|------|------|------|--------|
| Mistral-7B (seed=42) | ✅ 完整 | `results/exp033_mistral_7b_folio204/intermediates/` | 204 |
| Mistral-7B (seed=123) | ✅ 完整 | `results/exp052_mistral_folio204_seed123/intermediates/` | 204 |
| **Qwen3-14B (non-thinking)** | ❌ **不存在** | — | 0 |
| Qwen3-14B (thinking) | ⚠️ 部分 | `results/exp028b_qwen3_thinking_folio204/intermediates/` | 38 (166-203) |
| Qwen2.5-14B | ✅ 完整 | `results/exp036_qwen25_14b_folio204/intermediates/` | 204 |

### 2. 已有 SICA 数据（FOLIO 2×2）

**无。** 目前 FOLIO 上没有跑过 cross-model extraction。`exp_d126_crossmodel_sica` 是 **ProofWriter** 2×2（已完成，N=204 PW 问题）。

### 3. 缺失数据 & 执行计划

| Cell | Generator → Extractor | 缺什么 |
|------|----------------------|--------|
| A | Mistral → Mistral | traces ✅，需跑 extraction |
| B | Mistral → Qwen3 | traces ✅，需跑 extraction |
| C | Qwen3 → Mistral | **traces 不存在**，需先生成 Qwen3-14B non-thinking FOLIO traces，再跑 extraction |
| D | Qwen3 → Qwen3 | **traces 不存在**，同 Cell C |

**关键瓶颈**: Qwen3-14B non-thinking FOLIO-204 traces 从未生成过。需用 `run_full_mvp.py` + Qwen3-14B vLLM 先跑 204 题 trace generation（估计 1-2h）。

### 4. GPU 状态

| GPU | 型号 | 显存占用 | 状态 |
|-----|------|----------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | **空闲** |
| 1 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | **空闲** |
| 2 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | **空闲** |
| 3 | RTX PRO 6000 Blackwell (98GB) | 89811 MiB | 占用（无 vLLM 进程，可能是残留） |

### 5. 模型路径

| 模型 | 路径 |
|------|------|
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` |
| Qwen3-14B | `/root/autodl-tmp/models/Qwen3-14B` |
| Qwen2.5-14B-Instruct | `/root/autodl-tmp/models/Qwen2.5-14B-Instruct` |

### 6. cross_model_extract.py

- **位置**: `/root/symb_invariant_consensus/scripts/cross_model_extract.py`
- **关键参数**:
  ```
  --traces-dir    # intermediates 目录（folio_*.json）
  --api-base      # vLLM endpoint (default: localhost:8000)
  --model         # "auto" 自动检测
  --output        # 输出目录
  --resume        # 断点续跑
  --qwen3-nothink # 禁用 Qwen3 thinking mode
  ```
- **适用性**: 完全适用 FOLIO。读取 trace 文件中的 `sica_result.traces`，用另一个模型重新做 constraint extraction + MaxSAT。

### Trace 文件结构

```json
{
  "problem": {"id": "folio_0", "answer": "Unknown", "dataset": "folio", ...},
  "sica_result": {
    "answer": "Unknown",
    "scores": {"Unknown": 57.0},
    "answer_counts": {"Unknown": 12},
    "traces": [{"trace": "...", "answer": "Unknown"}, ...]
  }
}
```

---

**建议执行顺序**:
1. 先部署 Qwen3-14B vLLM（GPU 0），生成 Qwen3-14B non-thinking FOLIO-204 traces
2. 同时部署 Mistral-7B（GPU 1），用 exp033 traces 跑 Cell A (Mistral→Mistral)
3. Qwen3 traces 生成完后，4 个 cell 的 extraction 可并行

---

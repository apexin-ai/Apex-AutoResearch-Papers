# code kv eviction benchmark scaffold

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kv-eviction-benchmark-scaffold_20260511T235204_result.json`
- **Structured JSON:** [`4041bc1a98f7c187a757.json`](../../sessions/40/4041bc1a98f7c187a757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 13 个文件已创建。

## 文件清单

```
src/kv_eviction/
├── __init__.py                    # 包入口，导出 4 种策略
├── benchmark.py                   # 主 runner：加载模型→遍历 policy×budget→评估→输出 JSON
├── configs/
│   └── default.yaml               # 模型路径、budgets [30%,50%,70%]、各策略超参
├── policies/
│   ├── __init__.py
│   ├── base.py                    # EvictionPolicy ABC: on_new_token / get_complexity / name
│   ├── carc_kv.py                 # CARC-KV
│   ├── h2o.py                     # H2O
│   ├── snapkv.py                  # SnapKV
│   └── streaming_llm.py           # StreamingLLM
└── eval/
    ├── __init__.py
    ├── perplexity.py              # 滑窗 PPL 评估
    ├── math_accuracy.py           # MATH-500 准确率评估
    └── metrics.py                 # CacheMetrics dataclass
```

## 各策略核心实现思路

| 策略 | 核心机制 | 复杂度 |
|------|----------|--------|
| **CARC-KV** | 维护 per-head EMA anchor (γ=0.99)，新 token 与 anchor 计算 cosine sim 后更新 anchor，evict sim 最高的 token（最冗余）。与 `mvp_carc_validation_v2.py` 的 `compute_anchor_signal` 一致 | O(1) |
| **H2O** | 累积 attention scores，保留累积 attention 最高的 heavy-hitter + recent window，evict 累积最低的 | O(n) |
| **SnapKV** | Prefill 阶段用 observation window (末尾 32 tokens) 对前缀 token 投票选 top-k，decoding 阶段 cache 固定 | O(n²) prefill, O(1) decode |
| **StreamingLLM** | 保留前 4 个 sink tokens + 最近 window_size 个 tokens，中间全部丢弃 | O(1) |

---

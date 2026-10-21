# audit llama degen 86 vs 89

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_llama_degen_86_vs_89_20260518T061917_result.json`
- **Structured JSON:** [`e5330f72dd4bfb37fd01.json`](../../sessions/e5/e5330f72dd4bfb37fd01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了。**`exp_017_llama_conll_n16_s123_r1024` 的 CF1 = 2380/2756 = 86.36%**，精确匹配 cascade worker 的 2380。

## 结论

- **86.4% 来源**: `output/exp_017_llama_conll_n16_s123_r1024/samples.jsonl`，**N=16**, seed=123, max_tokens=1024，CF1 (Constant F1, gold-filtered) = 2380/2756 = 86.36%
- **89.2% 来源**: `output/exp_017_llama_conll_infer/full_signal_analysis.json`，**N=8**, 默认 seed，CF1 (Constant F1, gold-filtered) = 2459/2756 = 89.22%
- **冲突原因**: **N 不匹配** (N=16 vs N=8) + **seed/max_tokens 配置不同** (s123_r1024 vs 默认)。计算定义相同（都是 F1-based constant degeneracy），但数据来源不同。N 越大 degeneracy 越低是符合预期的（更多 sample 越难保持全部一致）
- **正确值（N=8, F1-based, gold-filtered）**: **89.2%** (2459/2756)，来自 `full_signal_analysis.json`，可通过直接计算验证

### 关键证据

```
# N=8 验证 (exp_017_llama_conll_infer)
Constant F1 (CF1): 2459/2756 = 0.8922  ← matches full_signal_analysis.json

# N=16 各配置 CF1:
n16 (seed42):           2385/2756 = 0.8654
n16_s123:               2387/2756 = 0.8661  
n16_s456:               2392/2756 = 0.8679
n16_r1024 (seed42):     2383/2756 = 0.8647
n16_s123_r1024:         2380/2756 = 0.8636  ← 精确匹配 cascade worker 的 2380
n16_s456_r1024:         2390/2756 = 0.8672
```

Cascade worker (D132) 读取了 N=16 seed123 r1024 的数据，误报为 LLaMA CoNLL degeneracy，未注明 N=16。论文中引用 N=8 数据时应使用 **89.2%**。

---

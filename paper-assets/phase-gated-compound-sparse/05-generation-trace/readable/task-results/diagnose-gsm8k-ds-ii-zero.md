# diagnose gsm8k ds ii zero

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k_ds_ii_zero_20260515T164837_result.json`
- **Structured JSON:** [`ac419f533565202b153a.json`](../../sessions/ac/ac419f533565202b153a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入并注册。核心结论：

**ii_low = 0.0 是 bug，不是 GSM8K 的自然特性。** 根因链：

1. **fp16 NaN 传播** → `kv_importance` 全部 NaN（272/272 positions）
2. **`_select_kv_to_evict` 对 NaN 做 `topk`** → eviction 集中在序列 50-75% 位置
3. **Low_sparsity tokens 系统性在序列前 40%** → 因果注意力下被 evict 的 KV positions 全在其后 → **KV masking 对 low_sparsity 完全无效**
4. `ppl_kv ≡ ppl_dense`, `ppl_both ≡ ppl_attn` → II = R_attn - R_attn - 1 + 1 = **0.0**

5 个 bug 需修复：
- **Critical**: importance 计算转 float32 + CE losses 加 `.float()` + NaN 保护 `nan_to_num`
- **Medium**: aggregate PPL 用 `nanmean` + bootstrap unpacking 修复
- **Low**: `N_BOOTSTRAP` 1000 → 10000

修复后重跑应获得有意义的 low_sparsity II 值。

---

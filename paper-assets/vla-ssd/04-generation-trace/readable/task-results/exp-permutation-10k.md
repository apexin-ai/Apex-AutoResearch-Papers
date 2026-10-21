# exp permutation 10k

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_permutation_10k_20260520T190553_result.json`
- **Structured JSON:** [`72503d219adc822e5d3a.json`](../../sessions/72/72503d219adc822e5d3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 哪些分析用了 permutation test

| 分析 | 脚本 | 原 shuffle 数 | 是否需要更新 |
|------|------|-------------|------------|
| **RSA significance** | `rsa_permutation_null.py` | 1,000 | **已更新到 10,000** |
| CV/I² exact paired | `permutation_test_I2.py` | 2^6=64, 2^5=32 (穷举) | 不需要 |
| CV/I² MC unpaired | `permutation_test_I2.py` | 10,000 | 已经 10k |
| Head ablation bootstrap | `bootstrap_action_probe.py` | 10,000 | 已经 10k |
| Delta-rho permutation | `analyze_results.py` | 10,000 | 已经 10k |

### 旧 (1k) vs 新 (10k) p-values 对比

| Layer | Observed RSA | Old null_max | New null_max | Old p | New p | 结论变化 |
|-------|-------------|-------------|-------------|-------|-------|---------|
| 0 | 0.6117 | 0.0808 | 0.1031 | 0.0 | 0.0 | 不变 |
| 8 | 0.6187 | 0.0919 | 0.1200 | 0.0 | 0.0 | 不变 |
| 12 | 0.6282 | 0.0982 | 0.1186 | 0.0 | 0.0 | 不变 |
| 24 | 0.5459 | 0.0951 | 0.1327 | 0.0 | 0.0 | 不变 |
| 32 | 0.4223 | 0.1038 | 0.1172 | 0.0 | 0.0 | 不变 |

10k shuffles 下 null distribution 的 tail 略有扩展（null_max 从 ~0.08-0.10 升至 ~0.10-0.13），但观测值（0.42-0.63）远超 null 最大值（0.13），所有 p=0.0（即 p < 1/10000 = 0.0001）。**所有结论不变。**

### 结果路径
- JSON: `/root/autodl-tmp/vla-ssd/results/permutation_10k/rsa_permutation_null_10k.json`
- Log: `/root/autodl-tmp/vla-ssd/results/permutation_10k/run.log`
- Script: `/root/vla-ssd/scripts/ablations/rsa_permutation_null_10k.py`

---

# diagnose scale 14b t10 a045 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t10_a045_s42_fp32_20260523T004459_result.json`
- **Structured JSON:** [`b6fbbb16cacdf66504ca.json`](../../sessions/b6/b6fbbb16cacdf66504ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 产出汇总

### 1. t10_a045_s42 诊断：**成功** ✓
- EXIT_CODE=0，gen_0~gen_10 全部完整（11个 metrics.json，415-423 bytes）
- Registry 已更新为 DONE/success

### 2. D102 5-method 分析结果

| 方法 | Forward | Reverse |
|------|---------|---------|
| **PermG (FDR)** | **0/8** | **0/8** |
| Diff XCorr (FDR) | 8/8 | 8/8 |
| Naive XCorr (D111) | 2/8 | - |
| Threshold Onset 3σ | 0/8 | - |
| TY Granger | 3/8 | - |
| **K≥3 consensus** | **1/8** | - |
| K≥4 consensus | 0/8 | - |

关键 drift：token_entropy -24.63%, ece +1655%, ppl +58%, mauve -24%, distinct_1 -32%

唯一 K≥3 pair 是 ece→mauve（naive+diff+ty），但 PermG 不显著、threshold onset 无法触发（所有 downstream 均未达 3σ 阈值）。

### 3. t10_a045_s43 部署：**运行中** ✓
- 服务器：westd-17855, cuda:4
- PID：738796
- tmux session：`14b_t10_a045_s43`
- Registry：RUNNING

### 4. 410M vs 1.4B 对比

| | 410M α=0.45 T=10 | 1.4B α=0.45 T=10 |
|---|---|---|
| PermG fwd | 0/8 | 0/8 |
| K≥3 | - | 1/8 |
| Threshold onset | 0/8 | 0/8 |

**结论：1.4B 也 = 0/8 PermG，confirms below-threshold behavior is scale-consistent。** α=0.45 在 T=10 下（α_c(10)≈0.487）对两种模型规模均未产生可检测的 lead-lag 因果信号。这支持 α_c 边界的 scale-robustness 假设。

---

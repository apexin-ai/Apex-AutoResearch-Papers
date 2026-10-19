# ssh prepare latency profiling

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-latency-profiling_20260520T054914_result.json`
- **Structured JSON:** [`d3bd1adc46289665557d.json`](../../sessions/d3/d3bd1adc46289665557d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。汇报结果：

## 结果

### 1. 脚本路径
- **新脚本**: `/root/acr-vla-conformal-refinement/src/profile_latency.py`
- **旧脚本**（保留）: `/root/acr-vla-conformal-refinement/src/latency_profile.py`

### 2. Dry-run 结果 (RTX 4090, N=20)

| Component | Mean (ms) | Std (ms) |
|---|---|---|
| VLA encode_prefix | 44.35 | 13.65 |
| VLA sample K=1 | 206.20 | 3.47 |
| VLA sample K=2 | 209.01 | 2.31 |
| VLA sample K=5 | 207.27 | 1.45 |
| VLA sample K=10 | 205.21 | 3.24 |
| Argmin L2 (K=10) | 0.150 | 0.006 |
| CGS compute_features | 7.074 | 0.407 |
| **CRM forward** | **0.328** | **0.034** |
| Full pipeline K=10 | 259.26 | 26.76 |
| Adaptive fast (K=2) | 254.09 | 17.12 |
| Adaptive full (K=2→10) | 459.10 | 10.86 |

**关键发现**:
- **CRM overhead = 4.03ms (1.58%)** — 主要来自 argmin+CRM，不只是 MLP 本身
- **VLA sampling ~206ms 对 K 不变**（batched generation 证实）
- **Adaptive K 快路径省 45% latency** (254ms vs 459ms)
- GPU memory: 903MB allocated, 1005MB peak

### 3. 完整 profiling 时间估算

完整 profiling (100 warmup + 1000 measure):
- 9 个组件 × ~(100+1000) 次 × ~250ms/iter（VLA 主导）≈ **每组件 ~4.5 min**
- 加上 lightweight 组件（argmin/CRM 很快）
- **总计约 40-50 分钟 GPU 时间**

运行命令：
```bash
cd /root/acr-vla-conformal-refinement
python -u src/profile_latency.py --n_warmup 100 --n_measure 1000
```

---

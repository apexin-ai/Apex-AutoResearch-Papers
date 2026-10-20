# diagnose verify pooled n25 and server state

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify_pooled_n25_and_server_state_20260516T141309_result.json`
- **Structured JSON:** [`954681b69b9500fc5695.json`](../../sessions/95/954681b69b9500fc5695.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. pooled_irt_n25 — **完成** ✓

三个 benchmark 均有完整 `irt_results.json` 输出（mmlu 21:22, gsm8k 21:27, arc 21:30），加上顶层 `pooled_rrf_irt_results.json`。进程正常完成后退出，cron 误判。

| Benchmark | N | γ_mean | 95% CI | CI excludes 0 | PPP | raw_MAE → cal_MAE | ΔMAE |
|-----------|---|--------|--------|---------------|-----|-------------------|------|
| **MMLU** | 13 | 0.550 | [-0.572, 1.709] | **No** | 0.227 | 0.014 → 0.005 | 0.009 |
| **GSM8K** | 21 | 0.378 | [-0.100, 0.847] | **No** | 0.105 | 0.147 → 0.012 | **0.135** |
| **ARC** | 13 | 0.862 | [0.092, 1.630] | **Yes** ✓ | 0.003 | 0.032 → 0.023 | 0.009 |

所有 benchmark MCMC 诊断通过（rhat≤1.008, ESS≥1476, 0 divergences）。

关键发现：
- **ARC** 是唯一 γ CI 排除零的 benchmark（contamination signal 显著），但 PPP=0.003 偏低，模型拟合有张力
- **GSM8K** 校准改善最大（MAE 降 92%），N=21 是最大的 respondent pool（包含 0.5B）
- **MMLU/GSM8K** 的 γ CI 未排除零——N=13/21 下 γ 仍不可靠识别

与之前 N=23 对比：GSM8K 从 N=16→21（+0.5B s123），MMLU/ARC 仍为 N=13（0.5B 无这两个 benchmark 的信号数据）。

### 2. signals_3B_d000_s123_cuda2 — **完成（部分）**

进程正常退出，**不是 crash**。日志末尾：`===BATCH_COMPLETE_d000_s123_a32=== Total:9 Completed:6 Skipped:2 Failed:1`

输出目录内容：
| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| s1_embedding | ✓ | ✓ | ✓ |
| s2_minkpp | ✓ | ✓ | ✓ |
| s4_selfcritique | **FAILED** (有 `_s4_chunks_mmlu` 残留) | ✓ | ✓ |

s4_selfcritique_mmlu 失败（14042 items，可能 OOM 或超时）。日志中有 `libnvJitLink.so.13` 加载错误但未阻断运行。

### 3. GPU 占用表

| GPU | VRAM Used | Util% | PID | Task |
|-----|-----------|-------|-----|------|
| 0 | 6707/24564 MiB | 61% | 780943 | compute_signals 3B d000_s123 (s4 mmlu) |
| 1 | 1555/24564 MiB | 31% | 780591 | compute_signals 0.5B (s4 mmlu) |
| **2** | **0 MiB** | **0%** | — | **空闲** |
| **3** | **0 MiB** | **0%** | — | **空闲** |
| 4 | 8313/24564 MiB | 85% | 785955 | eval Llama-3.2-3B d000_s42 |
| 5 | 3659/24564 MiB | 53% | 786898 | eval Qwen2.5-1.5B-Instruct |

**GPU 2、3 空闲可用。**

### 4. 磁盘状态 — ⚠️ 需关注

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root/tmp) | 30G | 26G | 4.9G | **84%** |
| /root/autodl-tmp | 169G | 149G | 21G | 89% |

`/tmp` 大文件（在 root 分区）：

| 文件 | 大小 |
|------|------|
| tmpmn07s31e | **3.7G** |
| tmp7p3zq39_ | **2.2G** |
| tmp897tun7i | **1.3G** |
| tmpb8uhrz4i | 545M |
| tmp4her5gb3 | 241M |

合计 **~8G** 的 tmp 文件。清理后 root 分区可从 84% 降至 ~57%。这些大概率是 Stan/PyTorch 的临时编译缓存，建议清理。

---

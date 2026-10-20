# infra gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260513T224033_result.json`
- **Structured JSON:** [`7e457cab604d2740408e.json`](../../sessions/7e/7e457cab604d2740408e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 0% | 0 MiB | 97887 MiB |
| 1 | 0% | 0 MiB | 97887 MiB |
| 2 | 0% | 0 MiB | 97887 MiB |
| 3 | 100% | 0 MiB | 97887 MiB |

GPU 3 显示 100% 利用率但 0 MiB 显存，可能是驱动瞬时读数或残留状态。**无训练进程在运行**——仅有 tensorboard、jupyter-lab、autopanel 等系统服务。

## M1v3 结果

文件：`profiling_output_v3/profiling_results.json` (2.7MB, May 14 06:38)

**配置**：DeepSeek-R1-Distill-Qwen-7B, sparsity=[0.1, 0.2], bootstrap=1000, problems=50

### Phase Stats
| Phase | Tokens | Segments |
|-------|--------|----------|
| high_sparsity | 25,862 | 511 |
| low_sparsity | 32,349 | 454 |
| mid_sparsity | 27,996 | 391 |

### Interaction Index

| Phase | Level | Mean | CI Low | CI High |
|-------|-------|------|--------|---------|
| high_sparsity | 0.1 | 0.2317 | 0.1338 | 0.3418 |
| high_sparsity | 0.2 | 2.1574 | 1.0605 | 3.5491 |
| low_sparsity | 0.1 | 0.1711 | 0.0782 | 0.2768 |
| low_sparsity | 0.2 | 1.1294 | 0.4368 | 1.9593 |
| mid_sparsity | 0.1 | 0.1607 | 0.0886 | 0.2489 |
| mid_sparsity | 0.2 | **0.3049** | **-1.0635** | **1.3044** |

### Pass/Fail
- **Overall: FAIL**
- CI overlap test: **FAIL**
- Sign reversal test: **FAIL** — mid_sparsity @ 0.2 的 CI 跨零 [-1.06, 1.30]，方向不确定

Warnings: 无

---

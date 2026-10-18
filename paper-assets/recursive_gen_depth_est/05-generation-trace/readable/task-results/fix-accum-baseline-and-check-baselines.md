# fix accum baseline and check baselines

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_accum_baseline_and_check_baselines_20260519T131726_result.json`
- **Structured JSON:** [`be6d86512c71f39c1bb8.json`](../../sessions/be/be6d86512c71f39c1bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活。

---

## 汇总

### 任务 1：accumulation 脚本 baseline 修复 ✅

`accumulation_pipeline_gpt2xl.py` 中 3 处 `0.859` → `0.8428`：
- **L633**: print 语句
- **L634**: delta 计算（`rf_results['overall_accuracy'] - 0.8428`），delta 自动更新
- **L646**: 结果字典

服务器无 artifacts/ 目录，无报告文件引用旧值。

### 任务 2：baselines 进程状态 ✅

| 实验 | 原 PID | 状态 | 新 PID |
|------|--------|------|--------|
| Min-K% #001 | 131084 | 存活（14min） | — |
| Min-K% #002 | 131522 | 存活（11min） | — |
| DetectGPT #001 | 131161 | **已死**（HF httpx 崩溃） | **133098** |
| DetectGPT #002 | 131658 | **已死**（HF httpx 崩溃） | **133269** |

DetectGPT 崩溃原因：`RuntimeError: Cannot send a request, as the client has been closed.`（HF Hub 网络问题）。重提时已加 `network_turbo` + `SSL_CERT_FILE` + `HF_HUB_DISABLE_XET=1` 环境变量修复。

日志路径：
- `~/runs/recursive_gen_depth_est/detectgpt_ordinal_baseline_001_retry.log`
- `~/runs/recursive_gen_depth_est/detectgpt_ordinal_baseline_002_retry.log`

---

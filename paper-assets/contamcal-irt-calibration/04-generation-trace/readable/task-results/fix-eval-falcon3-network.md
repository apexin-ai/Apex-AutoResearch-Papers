# fix eval falcon3 network

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_falcon3_network_20260522T110905_result.json`
- **Structured JSON:** [`ddf894bf6879339406e5.json`](../../sessions/dd/ddf894bf6879339406e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断和修复结果

### 根因
westd-29999 上 HuggingFace 网络不通，两个原因叠加：
1. **未 source network_turbo** — AutoDL 实例默认无外网，需要 `source /etc/network_turbo` 启用代理
2. **xet_get 401** — HF Hub 的 XET 协议在 AutoDL 代理下返回 401 Unauthorized

### 修复完成
- 所有 7 个 evaluate.py 需要的数据集已预下载到 `/root/autodl-tmp/.hf_cache/`，**离线验证通过**：
  - MMLU test: 14042 rows, validation: 1531 rows
  - ARC-Challenge test: 1172 rows, validation: 299 rows
  - GSM8K test: 1319 rows, train: 7473 rows
  - HumanEval test: 164 rows

### eval_falcon3_d025_s42 状态
- PID 618913 已死，三个 eval 全部失败

### 当前 GPU 状态
3 个 Falcon3 eval 已被重新提交并在运行中（~1 min ago）：

| GPU | PID | 实验 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 627332 | Falcon3 d000_s42 (mmlu+arc) | 16.8GB | 90% |
| 1 | 627479 | Falcon3 d005_s42 (mmlu+arc) | 16.8GB | 89% |
| 2 | 627636 | Falcon3 d025_s42 (mmlu+arc) | 16.8GB | 89% |
| 3 | 600602 | SFT训练 | 55GB | 99% |

### 后续 eval 提交建议
为防止同类问题再次发生，eval 命令前必须加：
```bash
source /etc/network_turbo && export HF_HUB_DISABLE_XET=1 && export HF_HUB_DOWNLOAD_TIMEOUT=600
```
但现在数据集已缓存，只要不清 cache 就不再需要联网。

---

# exp medium seed123 chain cuda0

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_medium_seed123_chain_cuda0_20260514T015648_result.json`
- **Structured JSON:** [`513669f6b723b538e03f.json`](../../sessions/51/513669f6b723b538e03f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署完成

### 1. 创建的脚本

| 脚本 | 与 seed=42 的差异 |
|------|-----------------|
| `run_medium_uncurated_seed123.sh` | `--seed 123`, output → `results_medium_uncurated_seed123` |
| `run_medium_rgds_seed123.sh` | `--seed 123`, output → `results_medium_rgds_seed123` |
| `run_medium_random50_seed123.sh` | `--seed 123`, output → `results_medium_random50_seed123` |
| `chain_cuda0_seed123.sh` | 串行调用上述三个脚本，日志分别 tee 到 `/root/autodl-tmp/div_cal_verify/medium_{uncurated,rgds,random50}_seed123.log` |

所有训练超参与 seed=42 完全一致：lr=5e-5, batch=4, grad_accum=8, seq_len=512, epochs=3, 8 generations, 500K tokens/gen。

### 2. Chain 执行顺序
`medium_uncurated_seed123` → `medium_rgds_seed123` → `medium_random50_seed123`，全部在 cuda:0 上串行。

### 3. 启动状态
- tmux session `chain_cuda0_s123` 已创建，进程在运行
- 首条日志确认 `medium_uncurated_seed123` 已于 09:58:34 CST 启动
- cuda:1 上 `chain_cuda1` 也在正常运行（65% util）

### 4. 预计运行时间
- 单个实验（参考 seed=42 uncurated）：~2.5h
- 三个实验 chain 总计：~7-8h
- 预计全部完成时间：约 17:00-18:00 CST 今天

---

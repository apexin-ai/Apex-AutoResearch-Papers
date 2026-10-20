# code prep seed456 scripts

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_seed456_scripts_20260514T034655_result.json`
- **Structured JSON:** [`d1658cd4521b5a6c2764.json`](../../sessions/d1/d1658cd4521b5a6c2764.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。创建的脚本汇总：

### 已创建脚本（`/root/div_cal_verify/`）

| 脚本 | 用途 | GPU |
|------|------|-----|
| `chain_cuda0_seed456.sh` | 串行链：uncurated→rgds→random50 | cuda:0 |
| `run_medium_uncurated_seed456.sh` | uncurated 单独运行 | 参数 $1 |
| `run_medium_rgds_seed456.sh` | rgds 单独运行 | 参数 $1 |
| `run_medium_random50_seed456.sh` | random50 单独运行 | 参数 $1 |
| `run_medium_external_seed456.sh` | external_only 单独运行 | 参数 $1 |

### 输出路径（`/root/autodl-tmp/div_cal_verify/`）

- `results_medium_uncurated_seed456/`
- `results_medium_rgds_seed456/`
- `results_medium_random50_seed456/`
- `results_medium_external_seed456/`
- 日志：`medium_uncurated_seed456.log`, `medium_rgds_seed456.log`, `medium_random50_seed456.log`

### 启动方式（seed=123 完成后）

```bash
# cuda:0: 串行跑 uncurated→rgds→random50
nohup bash /root/div_cal_verify/chain_cuda0_seed456.sh > /root/autodl-tmp/div_cal_verify/chain_cuda0_seed456.log 2>&1 &

# cuda:1: 跑 external
nohup bash /root/div_cal_verify/run_medium_external_seed456.sh 1 > /root/autodl-tmp/div_cal_verify/medium_external_seed456.log 2>&1 &
```

---

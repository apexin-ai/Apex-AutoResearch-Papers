# check gpu chain monitor

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_chain_monitor_20260523T175251_result.json`
- **Structured JSON:** [`6d402a519ea3a96401d1.json`](../../sessions/6d/6d402a519ea3a96401d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. gpu_chain_next.sh 进程树
```
PID 108997  bash scripts/gpu_chain_next.sh          (运行 29m13s)
 └─ PID 109008  bash scripts/d048_eval_ss_s123.sh   (运行 29m13s)
     └─ PID 110052  python eval_attention_steering.py  (运行 25m29s)
```
脚本位于 `/root/turn_residual_gating/scripts/gpu_chain_next.sh`。

### 2. AR eval PID 110052 状态
**仍在运行**，已运行 25 分 29 秒。
- 命令：`eval_attention_steering.py --checkpoint runs/d048_ss_s123/epoch_2 --gate-type threadgate --mode gen --beta 0 3 5 --gar-variant ours --output-dir results/d048_final_ar --output-name ss_s123_ar_n50`
- GPU 显存占用：**30416 MiB**

### 3. gpu_chain 日志
日志文件 `/root/turn_residual_gating/logs/gpu_chain_next.log` 不存在（输出可能直接到 stdout 或其他位置）。

### 4. AR 结果文件
`results/d048_final_ar/` 已有产出：

| 文件 | 时间 | 说明 |
|------|------|------|
| `base_s42_ar_n50.json` | May 23 09:01 | baseline s42 |
| `tg_s42_ar_n50.json` | May 23 09:23 | threadgate s42 |
| `ug_s42_ar_n50.json` | May 23 09:46 | uniformgate s42 |
| `lo_s42_ar_n50.json` | May 23 10:07 | lora-only s42 |
| `pcgrad_s42_ar_n50.json` | May 23 10:31 | pcgrad s42 |
| `ss_s42_ar_n50.json` | May 23 10:55 | scheduled-sampling s42 |
| `d048_summary_ci_wilcoxon.json` | May 23 10:55 | 统计汇总 |
| `tf_base_ours/` | May 24 01:25-01:26 | TF base ours GAR |
| `tf_base_dongre/` | May 24 01:26 | TF base dongre GAR |
| `tf_ss_s123_ours/epoch_2_gar.json` | May 24 01:27 | **新生成** - SS s123 ours GAR |
| `tf_ss_s123_dongre/epoch_2_dongre_gar.json` | May 24 01:28 | **新生成** - SS s123 dongre GAR |

**当前正在运行的是 ss_s123 的 AR eval（beta 0/3/5, ours variant）**，tf_* 系列的结果已于今天凌晨生成完毕。`runs/d048_ss_s123/eval_results/` 目录不存在——结果输出到了 `results/d048_final_ar/` 下。

---

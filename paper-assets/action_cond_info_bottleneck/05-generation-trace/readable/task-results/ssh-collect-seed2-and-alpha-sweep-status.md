# ssh collect seed2 and alpha sweep status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect-seed2-and-alpha-sweep-status_20260517T025023_result.json`
- **Structured JSON:** [`87651146cd6ff63b8e57.json`](../../sessions/87/87651146cd6ff63b8e57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Seed2 libero_10 SR
**42.2%**

路径：`/root/autodl-tmp/v7_eval_fixed_seed2/libero_10/eval_info.json`

### 2. Seed2 4-suite 平均 SR

| Suite | SR |
|-------|-----|
| libero_spatial | 51.4% |
| libero_object | 49.4% |
| libero_goal | 63.0% |
| libero_10 | 42.2% |
| **平均** | **51.5%** |

### 3. Alpha=0.1 状态
- **PID 751592**：运行中
- **进度**：libero_spatial 10 个 task 中已完成 9 个（task 0-8 的 videos 都已生成），正在跑第 10 个 task
- **输出路径**：`/root/autodl-tmp/v7_alpha_sweep/alpha_0.1/`
- **预计完成时间**：从 09:45 启动至今约 1 小时完成 9/10 tasks，最后 1 个 task 预计 5-10 分钟内完成

### 4. Alpha=0.0 状态
- **未启动**。`/root/autodl-tmp/v7_alpha_sweep/` 下无 alpha_0.0 目录或 log
- 脚本已就绪：`/root/acib/scripts/run_alpha_sweep_0.0.sh`
- 内容：全 4 suites (spatial/object/goal/libero_10) + `--conditioning_mode concat` + `--scoring_alpha 0.0`
- 需要等 alpha=0.1 完成释放 GPU 1 后才能启动（alpha=0.1 在 CUDA_VISIBLE_DEVICES=1 上跑）

### 5. 所有相关路径
- Seed2 eval 全部结果：`/root/autodl-tmp/v7_eval_fixed_seed2/{libero_spatial,libero_object,libero_goal,libero_10}/eval_info.json`
- Alpha sweep 输出：`/root/autodl-tmp/v7_alpha_sweep/`
- Alpha sweep 脚本：`/root/acib/scripts/run_alpha_sweep_{0.0,0.1,0.3}.sh`

---

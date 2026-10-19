# monitor gae baseline step10

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gae-baseline-step10_20260517T182602_result.json`
- **Structured JSON:** [`55ec421a9cffe7d77a18.json`](../../sessions/55/55ec421a9cffe7d77a18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已完整收集。汇总如下：

## gae_baseline_seed1 实验状态

**进程**: PID 40267 存活，运行 4h12m
**进度**: 9/15 steps 完成 (60%)，预估剩余 ~2h56m（每步约 29 min）
**磁盘**: /root/autodl-tmp 使用 40%（153 GB 可用），但 Ray session 临时目录有 95% full 警告（日志中反复报错）

## 指标汇总

| Step | train/success | train/action_is_valid | train/pass@8 | val/success | val/action_is_valid |
|------|-------------|----------------------|-------------|-------------|---------------------|
| 0 (val-only) | - | - | - | 0.0625 | 0.7796 |
| 1 | 0.0313 | 0.7259 | 0.1875 | - | - |
| 2 | 0.0469 | 0.6584 | 0.3125 | - | - |
| 3 | 0.0391 | 0.6349 | 0.2500 | - | - |
| 4 | 0.0703 | 0.6312 | 0.3125 | - | - |
| 5 | 0.0625 | 0.6360 | 0.2500 | **0.125** | **0.6926** |
| 6 | 0.0156 | 0.6763 | 0.1250 | - | - |
| 7 | 0.0781 | 0.6018 | 0.3750 | - | - |
| 8-9 | 未输出日志 | | | | |

## 关键观察

1. **Step 10 尚未到达**。当前 tqdm 显示 9/15，预计 step 10 在约 30-60 min 后到达。Step 10 会触发 val eval（每 5 步一次），届时可获得 val/success_rate（32 episodes，满足 C003）。

2. **train success_rate 整体很低**（1.6%-7.8%），无明显上升趋势。Step 6 跌至 1.56%，step 7 回升到 7.81%，波动大。

3. **action_is_valid 从 0.73 下降到 0.60**，呈持续下降趋势，说明模型在训练过程中生成有效 action 的能力在退化。

4. **val success_rate 从 step 0 的 6.25% 到 step 5 的 12.5%**，翻倍但仍很低。

5. **Ray 磁盘警告**：日志持续报 `/root/autodl-tmp/tmp/ray/session_...` 95% full（10.89 GB/250 GB），但 `df -h` 实测 153 GB 可用。可能是 Ray 的 quota 机制误报，暂不阻塞训练，但需留意。

---

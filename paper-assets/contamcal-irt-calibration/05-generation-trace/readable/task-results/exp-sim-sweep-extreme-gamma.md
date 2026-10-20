# exp sim sweep extreme gamma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sim-sweep-extreme-gamma_20260515T082922_result.json`
- **Structured JSON:** [`92f8ebf2f70b8ad1b124.json`](../../sessions/92/92f8ebf2f70b8ad1b124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed 1 chain 2 完成。继续正常运行。日志因缓冲延迟比较大。

进程稳定推进中。每 seed ~5 分钟，80 seeds 预计 ~6.7 小时完成。当前是 condition 1/8 的 seed 1/10。

我来汇总当前状态：

**已完成的工作：**
1. 在 `/root/contamcal-irt-calibration/exp004_sim_sweep/run_extreme_gamma.py` 写了 wrapper 脚本
2. Monkey-patch `GAMMA_TRUE` 和 `condition_id` 使条件名包含 gamma（如 `g2.0_auc0.7_n20_prior1.0_binary`）
3. 结果写入 `results_extreme_gamma/` 目录（独立于原有结果）
4. 用 nohup 后台启动，PID 528993

**Sweep 配置：**
- gamma_true ∈ {2.0, 4.0} × AUC ∈ {0.70, 0.90} × N ∈ {20, 50} = 8 条件
- 10 seeds each，parallel_chains=1
- 总计 80 runs，预计 ~6-7 小时

**早期结果（gamma=2.0, AUC=0.70, N=20, seed 0）：**
- gamma_mean = 1.9692，bias = -0.031
- CI95 covers = true，CI width = 0.477
- 0 divergences，rhat = 1.007，ESS = 1475
- theta_corr = 0.926

这个早期结果倾向于**假说 A**（真实数据 model misspecification）——因为 gamma=2.0 + N=20 时，4PL+γ 模型的 recovery 和 coverage 看起来很好。需要等 gamma=4.0 的结果以及更多 seeds 来确认。

**监控命令：**
```bash
# 查日志
tail -30 /root/autodl-tmp/extreme_gamma_sweep.log
# 查结果文件
ls -la /root/contamcal-irt-calibration/exp004_sim_sweep/results_extreme_gamma/
# 查进程状态
ps -p 528993 -o pid=
```

---

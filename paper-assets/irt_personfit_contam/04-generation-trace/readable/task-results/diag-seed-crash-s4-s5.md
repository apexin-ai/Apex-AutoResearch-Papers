# diag seed crash s4 s5

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_seed-crash-s4-s5_20260521T071150_result.json`
- **Structured JSON:** [`70b0be3c7396c83b103c.json`](../../sessions/70/70b0be3c7396c83b103c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diag_seed_crash_s4_s5.md`。

**核心结论：s4、s5、s6 三个实验全部成功完成，"failed" 是监控系统误判。**

根因：训练进程正常退出后，监控检测到 process dead 但找不到 sentinel file / W&B run，自动判定为失败。实际上日志显示训练正常跑完 3 epochs，model checkpoint 全部保存完好。

需要注意的点：
- **s6 步数异常**：s6 只有 237 步（s4/s5 是 939 步），需确认配置是否正确
- **监控系统**：建议训练脚本完成后写 sentinel file，避免下次误判
- 当前 GPU 0 和 3 空闲，GPU 1 在跑 eval_lz.py (contam_50)，GPU 2 在跑 train_grpo.py (已 2.5h)

---

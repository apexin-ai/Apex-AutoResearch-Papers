# ops verify exp022c startup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-exp022c-startup_20260524T074041_result.json`
- **Structured JSON:** [`f349e69b3080dd7e5aa8.json`](../../sessions/f3/f349e69b3080dd7e5aa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验状态汇总：

### exp_022c (GPT-2-medium, r=0.3, fixed_mix) — cuda:1
- **进程**: PID 868285 在 GPU 1 上运行，占用 19,282 MiB 显存，GPU 利用率 97%
- **命令**: `run_gpt2m_phase1.py --condition fixed_mix --real_ratio 0.3 --generations 3 --seed 42 --gpu 0`（通过 `CUDA_VISIBLE_DEVICES=1` 映射到物理 GPU 1）
- **日志**: 目前只有模型加载阶段的 warning（loss_type、padding_side），说明正在完成第一轮 generation 的样本生成或 fine-tuning，尚未输出第一个 `[Gen X] Results`
- **状态**: ✅ 已成功启动，正在训练中

### exp_020 (GPT-2-medium, pure_collapse) — cuda:0
- **进程**: PID 783957 在 GPU 0 上运行，占用 26,422 MiB 显存，GPU 利用率 94%
- **进度**: 已完成 Gen 0-8 的完整循环，正在 Gen 9（最后一轮）生成 50,000 个 synthetic samples
- **趋势**: eff_rank 从 23.09→110.92 先升后降，ppl 从 15.45→198.01 持续恶化，distinct-4 从 0.91→0.46 持续下降 — 符合预期的 collapse 模式
- **状态**: ✅ 正常运行，接近完成（10 代中已完成 9 代）

---

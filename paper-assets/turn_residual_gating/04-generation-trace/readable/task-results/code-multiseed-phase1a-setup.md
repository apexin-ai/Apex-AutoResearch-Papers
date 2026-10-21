# code multiseed phase1a setup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multiseed_phase1a_setup_20260525T061510_result.json`
- **Structured JSON:** [`3b1db6029346eea88ff7.json`](../../sessions/3b/3b1db6029346eea88ff7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PCGrad s123 已正常启动，模型加载中。

**调查报告总结：**

| # | 变体 | 训练脚本 | --gate-type | 特殊参数 | output-dir |
|---|------|---------|-------------|----------|------------|
| 1 | PCGrad s123 | train_phase2_v9_pcgrad.py | threadgate | — | runs/d048_pcgrad_s123 |
| 2 | PCGrad s456 | train_phase2_v9_pcgrad.py | threadgate | — | runs/d048_pcgrad_s456 |
| 3 | UG s123 | train_phase2.py | uniform | — | runs/d048_ug_s123 |
| 4 | UG s456 | train_phase2.py | uniform | — | runs/d048_ug_s456 |
| 5 | LO s123 | train_phase2.py | none | 无 gate-div 参数 | runs/d048_lo_s123 |
| 6 | LO s456 | train_phase2.py | none | 无 gate-div 参数 | runs/d048_lo_s456 |
| 7 | TG s456 | train_phase2.py | threadgate | — | runs/d048_tg_s456 |
| 8 | SS s456 | train_phase2_v8b.py | threadgate | --scheduled-sampling --ss-max-ratio 0.3 | runs/d048_ss_s456 |

**产出：**
1. 脚本：`/root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh`（185 行）
2. 已提交 `submit_training_job`：
   - **exp_id**: `phase1a_multiseed_8runs`
   - **PID**: 5508
   - **tmux session**: `phase1a_multiseed_8runs`
   - **timeout**: 72h
   - **GPU**: cuda:0 (RTX PRO 6000 Blackwell, 102GB)
3. 日志：`/root/turn_residual_gating/logs/phase1a_multiseed.log`

**注意**：SS s456 已有完整 checkpoint，脚本会自动跳过训练，只跑 eval。8 个 run 按顺序执行，每个训完自动跑 AR eval（N=50, β=0/3/5）。

---

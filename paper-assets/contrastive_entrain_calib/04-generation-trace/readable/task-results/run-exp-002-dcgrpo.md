# run exp 002 dcgrpo

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-002_dcgrpo_20260518T150603_result.json`
- **Structured JSON:** [`372fcc22eac7d1acf0c9.json`](../../sessions/37/372fcc22eac7d1acf0c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-002 已成功提交并运行中。

**汇总：**
- **脚本**: `/root/contrastive_entrain_calib/training/run_exp002_dcgrpo.py`
- **tmux 会话**: `exp002` on westd-29046
- **3 处修改全部落地**:
  1. R1=0.15, R2=0.2, R3=0.65
  2. reward_layers=[19, 20, 24, 27, 32, 33, 35]
  3. Per-strength R1 自适应门控：前 10 步统计 weak pairs R1，step 100 后按条件（|mean|<0.05 或 std>|mean|）自动将 weak pairs R1 贡献归零
- **日志确认**: d_syc 已加载 (shape=[36,2,4096])，hooks 注册在 7 层，训练已开始
- **Registry**: exp-002 状态 RUNNING，含完整 spec 和超参

---

# exp accum olmo temp mix50

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_accum_olmo_temp_mix50_20260522T045521_result.json`
- **Structured JSON:** [`6c5661f5709af31b17c9.json`](../../sessions/6c/6c5661f5709af31b17c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- **exp_id**: `accum_olmo_temp_mix50`
- **状态**: RUNNING
- **服务器**: gpu-6000pro-2, cuda:0
- **PID**: 722400 (tmux session: `accum_olmo_temp_mix50`)
- **命令**: `python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5 --seed 42`
- **日志**: `~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log`

进程已在加载 OLMo-1B 权重，Phase 1a 数据混合完成（2500 human + 2500 synthetic），正在进入 LoRA 训练阶段。参考 mix25 实验（~4.3 GPU hours），预计 4-5 小时完成。

---

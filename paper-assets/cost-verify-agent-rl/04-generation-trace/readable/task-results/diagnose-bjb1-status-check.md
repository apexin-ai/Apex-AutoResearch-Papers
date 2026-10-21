# diagnose bjb1 status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-status-check_20260519T143327_result.json`
- **Structured JSON:** [`01e6f013b1e193c53ecb.json`](../../sessions/01/01e6f013b1e193c53ecb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-17606 服务器状态汇总

### GPU
| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| cuda:0 | RTX PRO 6000 96GB | 39.6G / 97.9G (40%) | 33% | 67°C |
| cuda:1 | RTX PRO 6000 96GB | 3M / 97.9G (~0%) | 0% | 32°C |

GPU 0 被 vLLM 推理引擎占用（PID 172066），GPU 1 空闲。

### Per-task T=0.4 Eval (PID 171794)
**状态：正在运行**，已运行 ~17 分钟（22:17 启动）。

但 JSON 结果文件已写出完整 134 episodes，**eval 实际已跑完**，进程可能在做收尾：

| Task Type | Count | Success | Rate |
|-----------|-------|---------|------|
| pick_and_place_simple | 24 | 5 | 20.8% |
| pick_clean_then_place_in_recep | 31 | 8 | 25.8% |
| pick_heat_then_place_in_recep | 23 | 1 | 4.3% |
| pick_cool_then_place_in_recep | 21 | 2 | 9.5% |
| look_at_obj_in_light | 18 | 5 | 27.8% |
| pick_two_obj_and_place | 17 | 1 | 5.9% |
| **Overall** | **134** | **22** | **16.4%** |

Exit file 记录的是上一次运行（14:04 UTC），当前运行尚未写 exit。

### tmux
活跃 session：`exp029_per_task_t04`

### 磁盘
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (overlay) | 30G | 14G | 17G | 47% |
| /dev/sda2 | 879G | 18G | 817G | 3% |

磁盘充裕，无风险。

### 最新 artifacts
最新产出：`diag_8b_sft_clean_eval.md`（May 19 18:44）

---

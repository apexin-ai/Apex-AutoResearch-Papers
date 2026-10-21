# cpu ss lora only prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_ss_lora_only_prep_20260525T085909_result.json`
- **Structured JSON:** [`e2423fafd50e6c678543.json`](../../sessions/e2/e2423fafd50e6c678543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。SS 在 gate-type=none 模式下正常工作——SS ratio 从 0 逐步上升，L_GAR 分别追踪 SS 和 TF 路径。

---

## 报告

### LoRA-only checkpoint 路径
- Qwen: `runs/phase2_lora_only_s42/` (gate_type=none, 3 epochs, 3000 steps)
- 采用**从零训练**策略（与 d048_ss_s42 同条件对照），非 resume

### 训练脚本
**`/root/turn_residual_gating/scripts/d048_ss_lo_s42.sh`**

与 `d048_ss_s42.sh` (TG+SS) 的差异：
| 参数 | d048_ss_s42 (TG+SS) | d048_ss_lo_s42 (LO+SS) |
|------|---------------------|------------------------|
| `--gate-type` | threadgate | **none** |
| `--lambda-gate-div` | 1.0 | **0** |
| `--min-gate-std` | 0.05 | **0** |
| `--gate-lr-multiplier` | 10 | **1** |
| `--scheduled-sampling` | ✓ | ✓ |
| `--ss-max-ratio` | 0.3 | 0.3 |
| 其他超参 | 全部相同 | 全部相同 |

训练后自动执行：TF eval (GAR-ours + GAR-D) → AR N=50 (beta=0) → Bootstrap 95% CI

### Dry-run 结果
```
Step 0 | L_NTP=1.3786 L_GAR=0.2294 L_DIV=0.0000 | Gate=1.0000 | SS=no  ratio=0.000
Step 1 | L_NTP=1.2602 L_GAR=0.2026 L_DIV=0.0000 | Gate=1.0000 | SS=YES ratio=0.200
Step 2 | L_NTP=1.2695 L_GAR=0.2283 L_DIV=0.0000 | Gate=1.0000 | SS=YES ratio=1.000
Step 3 | L_NTP=1.4464 L_GAR=0.2116 L_DIV=0.0000 | Gate=1.0000 | SS=YES ratio=1.000
```
- Gate 固定为 1.0（无 gate 学习）
- SS ratio warmup 正常
- SS/TF L_GAR 分别统计正常
- 显存 29.0GB

### 预估训练时长
~6.5 小时（参考 d048_ss_s42 耗时 23418s ≈ 6.5h，配置几乎相同）

### 启动命令
```bash
nohup bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh > /root/turn_residual_gating/runs/d048_ss_lo_s42.log 2>&1 &
```

---

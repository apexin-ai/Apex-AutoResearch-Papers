# code phase2 tg v3 dryrun and train

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_tg_v3_dryrun_and_train_20260518T130834_result.json`
- **Structured JSON:** [`99a5053205714a2897af.json`](../../sessions/99/99a5053205714a2897af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行中。

---

## 汇报

### 1. Dry-run 完整指标表（λ=0.5, 50 global steps）

| Batch Step | ~Global Step | L_NTP  | L_GAR   | L_total | Gate_mean |
|------------|-------------|--------|---------|---------|-----------|
| 0          | 0           | 1.9796 | -0.0157 | 1.9717  | 0.8743    |
| 50         | 6           | 1.4147 | -0.0142 | 1.4076  | 0.8756    |
| 100        | 12          | 0.8577 | -0.0154 | 0.8500  | 0.8732    |
| 150        | 18          | 1.2551 | -0.0218 | 1.2442  | 0.8758    |
| 200        | 25          | 1.2635 | -0.0141 | 1.2565  | 0.8802    |
| 250        | 31          | 0.9018 | -0.0185 | 0.8925  | 0.8832    |
| 300        | 37          | 0.9621 | -0.0243 | 0.9500  | 0.8831    |
| 350        | 43          | 0.8143 | -0.0197 | 0.8045  | 0.8831    |

### 2. 校准 λ=2.0
- |L_GAR| 均值 ≈ 0.018，L_NTP 均值 ≈ 1.1
- λ=0.5 时 GAR 贡献仅占 L_NTP 的 ~0.8%
- 按 Director 规则 "0.5 × L_GAR << L_NTP → λ 升到 2.0"
- λ=2.0 时 GAR 贡献 ≈ 0.036 ≈ 3.6% of L_NTP（仍偏小，但已是规则最大值）
- Gate 值在 dry-run 中微幅上升 0.8743→0.8831，未下降

### 3. 正式训练已提交
- **PID**: 30973
- **tmux session**: `phase2_tg_s42_v3`
- **日志**: `/root/turn_residual_gating/runs/phase2_tg_s42_v3.log`
- **Registry**: RUNNING

### 4. 显存使用
- 峰值 85.4 GB / 97.9 GB (87%)
- GPU 利用率 98%

---

# ops prep detach ln eval and gradient

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_detach_ln_eval_and_gradient_20260524T055522_result.json`
- **Structured JSON:** [`2eafedd47488c054a7b1.json`](../../sessions/2e/2eafedd47488c054a7b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: detach_ln eval 命令

**训练仍在运行**，当前进度：
- s0: step 43810/50005, ETA ~1h36m
- s1: step 43522/50005, ETA ~1h40m
- s2: step 43543/50005, ETA ~1h40m

预计 ~15:35 UTC 完成。目前只有 `40000_chkpt`，`50000_chkpt` 会在训练到 step 50000 时生成。

Eval 命令已写入 `/tmp/detach_ln_eval_commands.sh`，checkpoint 路径格式：
```
/root/autodl-tmp/checkpoints/detach_ln_s{0,1,2}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt
```

### Part 2: 梯度分析脚本

**脚本位置**：两台服务器都有 `/root/occsafe_vla/analysis/gradient_analysis.py`，无需迁移。

westd-10894 上已有分析结果：`detach_s2` 和 `random_occ_s2` 的 gradient analysis 输出。

### Part 3: 梯度分析所需 checkpoint 可用性

| Condition | Checkpoint | 服务器 | 状态 |
|-----------|-----------|--------|------|
| Vanilla (vanilla_retrain_s0) | `--50000_chkpt` | **westd-34685** | 存在 |
| Full OCC (full_occ_retrain_s0) | `--50000_chkpt` | **westd-34685** | 存在 |
| Detach LN (detach_ln_s0) | `--50000_chkpt` | **westd-10894** | 训练中，尚未生成 |

**问题**：vanilla 和 full_occ 的 checkpoint 在 westd-34685，detach_ln 在 westd-10894。要在同一台机器上跑梯度分析，需要跨服务器拷贝 checkpoint（每个约 15-20GB），或者分别在两台服务器上跑，最后合并结果。

---

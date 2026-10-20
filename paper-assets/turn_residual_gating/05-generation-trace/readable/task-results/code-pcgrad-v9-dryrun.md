# code pcgrad v9 dryrun

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pcgrad_v9_dryrun_20260519T165349_result.json`
- **Structured JSON:** [`65fb26d1640402e5489d.json`](../../sessions/65/65fb26d1640402e5489d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 总结

### GPU 状态
NVIDIA RTX PRO 6000 Blackwell (102GB), 0MiB 占用, 完全可用。

### 代码审查 — PCGrad 实现

**正确的部分：**
- 两次 backward：NTP（retain_graph=True）→ 提取 gate NTP 梯度 → GAR+gate_div → 提取 gate GAR 梯度
- 投影公式：`g_ntp_proj = g_ntp - (dot / (g_gar_sq + 1e-8)) * g_gar` when cos_sim < 0 ✅
- 仅 gate 参数做 PCGrad，non-gate 参数正常累积 ✅
- 诊断日志（cos_sim, magnitude ratio, conflict layer ratio）✅
- 全部 float32 计算 ✅

**发现并修复的 Bug：**
gate 梯度跨 micro-step 累积被破坏——每个 micro-step 开头无条件 zero gate grads，丢弃了前几个 micro-step 的投影梯度。grad_accum=8 时 gate 实际只用最后 1 个 micro-step 的梯度。修复方式：save/restore accumulated projected grads。

### Dry-run 结果（5 步）

| 指标 | 值 |
|------|-----|
| cos_sim | -0.21 → +0.22（前 2 步冲突，后续对齐） |
| conflict_layers | 28-43% |
| mag_ratio | NTP >> GAR (8x-1062x) |
| NTP loss | 1.0-1.9 |
| GAR loss | ~0.23 |
| 显存 | 41.8-46.2 GB |
| Gate mean | 0.81 → 0.79 |
| NaN | 无 |

### 启动命令（正式训练）
```bash
bash /root/turn_residual_gating/scripts/run_v9_pcgrad.sh
```
超参与 v7 一致：lambda_gar=1.0, MSE target=0.5, gate_div min_std=0.05, init_bias=1.5, gate_lr=10x, lr=2e-4, epochs=3, grad_accum=8, seed=42。

---

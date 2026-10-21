# deploy exp008 dryrun gpu3 v3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp008-dryrun-gpu3-v3_20260518T174304_result.json`
- **Structured JSON:** [`a0a43e80193634401201.json`](../../sessions/a0/a0a43e80193634401201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run v3 结果汇总

### 1. 数据加载
**362 samples** — 符合预期（181 valid_correction + 181 invalid_pressure）

### 2. OOM
**无 OOM**。峰值 VRAM = **20,716 MiB / 32,607 MiB (63.5%)**，余量充足。

### 3. Pipeline
端到端运行成功，~15s 完成 1 step（16 micro-batches），总耗时 ~28s（含模型加载）。

### 4. 1-step metrics
未能打印 — `log_steps=10` 且该参数未暴露为 CLI arg，step=1 不触发日志。

### 5. R3
正常：mean=0.5000, min=0.0001, max=0.9999

### 6. Probe — **严重 bug**
| 指标 | 值 |
|---|---|
| Loss | 50.0000（固定不变） |
| Accuracy | 0.5000（随机猜测） |

**根因**：activations 未归一化。特征 L2 norm ~373（mean=0.15, std=5.82, range [-39.5, 210.6]），随机初始化的 probe 在大特征上产生饱和 logit → sigmoid 梯度消失 → 完全无法学习。

**验证**：对特征做 z-score 归一化后，同样的 probe 200 epoch 达到 **acc=99.5%, loss=0.028**。

### 结论
- Pipeline ✓, VRAM ✓, 数据加载 ✓
- **Probe 训练需要加特征归一化**，否则 S(t) 惩罚项无效，训练退化为纯 SFT
- 修复方案：在 `train_probe()` 中 `X = (X - X.mean(0)) / (X.std(0) + 1e-8)`, 同时保存 mean/std 用于训练时在线归一化 hidden states

---

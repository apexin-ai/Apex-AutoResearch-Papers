# infra v3 step500 checkpoint analysis

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_v3_step500_checkpoint_analysis_20260518T133103_result.json`
- **Structured JSON:** [`b9cd7ce2b9a1c948b66f.json`](../../sessions/b9/b9cd7ce2b9a1c948b66f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 500 到了。完整数据如下：

## 诊断报告：phase2_tg_s42_v3 @ Step 500

### 训练指标汇总

| Step | L_NTP  | L_GAR   | L_total | Gate_mean | λ\*L_GAR | GAR占比 |
|------|--------|---------|---------|-----------|----------|---------|
| 0    | 1.9796 | -0.0157 | 1.9481  | 0.8743    | -0.0314  | 1.6%    |
| 50   | 1.7206 | -0.0150 | 1.6906  | 0.8743    | -0.0300  | 1.7%    |
| 100  | 1.4232 | -0.0160 | 1.3913  | 0.8739    | -0.0320  | 2.2%    |
| 150  | 1.9844 | -0.0235 | 1.9375  | 0.8754    | -0.0470  | 2.4%    |
| 200  | 1.7204 | -0.0155 | 1.6893  | 0.8721    | -0.0310  | 1.8%    |
| 250  | 1.5024 | -0.0183 | 1.4659  | 0.8753    | -0.0366  | 2.4%    |
| 300  | 1.3317 | -0.0240 | 1.2837  | 0.8744    | -0.0480  | 3.6%    |
| 350  | 1.1289 | -0.0194 | 1.0900  | 0.8761    | -0.0388  | 3.4%    |
| 400  | 1.1779 | -0.0123 | 1.1534  | 0.8756    | -0.0246  | 2.1%    |
| 450  | 1.3190 | -0.0234 | 1.2722  | 0.8763    | -0.0468  | 3.5%    |
| 500  | 0.9423 | -0.0190 | 0.9044  | 0.8761    | -0.0380  | 4.0%    |

### 关键发现

**1. Gate 完全冻结**
- 范围：0.8721 ~ 0.8763（Δ=0.0042）
- 标准差：~0.0012
- sigmoid(init_bias=2.0) = 0.8808，当前均值 0.8748
- **500 步内 gate 几乎没有从初始化值移动**

**2. GAR loss 贡献微不足道**
- |λ\*L_GAR| / L_NTP 始终在 1.6%~4.0% 之间
- L_GAR 自身也是平的（-0.012 ~ -0.024），没有任何趋势
- GAR 梯度信号完全被 NTP 梯度淹没

**3. L_NTP 正常下降**
- 1.98 → 0.94（52% 下降），LoRA 在正常学习
- 但 NTP loss 没有动力去改变 gate 值（gate=0.88 已经近似 pass-through）

**4. 无 per-layer gate 数据**
- 训练脚本只 log mean gate（`train_phase2.py:246`），`get_gate_values()` 返回 per-layer dict 但未被逐层记录
- 但 mean gate 的极低波动（std=0.0012）强烈暗示各层也没有分化

### 判断：**A) Maximize 模式失效，建议准备 v3b**

根本原因：GAR loss 通过 attention weights → hidden states → gate 的间接梯度路径太弱。λ=2.0 时 GAR 贡献只有总 loss 的 2-4%，梯度信号不足以驱动 gate 参数偏离初始化。NTP loss 主导优化方向，而 NTP 对 gate 值无选择性压力（0.88 的 pass-through 已经够用）。

### v3b 建议方向

1. **大幅提升 λ**（10.0~20.0），或用自适应 λ 让 GAR 贡献占比 ≥ 20%
2. **给 gate 参数独立的更大 lr**（如 gate_lr = 10x base_lr），当前所有参数共享 2e-4
3. **直接正则化 gate 值**，而非通过 attention weights 间接影响（如对 gate 加 variance maximization penalty，直接逼迫 layer 间分化）

---

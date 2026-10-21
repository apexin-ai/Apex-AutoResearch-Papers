# figure kstar theta curve

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_kstar_theta_curve_20260515T123758_result.json`
- **Structured JSON:** [`b1982f5d72051f192ebc.json`](../../sessions/b1/b1982f5d72051f192ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成：
- `kstar_theta_curve.pdf` — 19 KB
- `kstar_theta_curve.png` — 92 KB

### 图中关键观察

根据数据计算，K*(θ) 的阶梯变化如下：

| θ 范围 | Qwen-RW | Pythia | OLMo | Qwen-cont |
|--------|---------|--------|------|-----------|
| 0.50–0.53 | 5 | 5 | 5 | 5 |
| 0.54 | 4 | 5 | 5 | 5 |
| ~0.51–0.54 | 各模型开始分化 | | | |
| **θ=0.60** | **2** | **2** | **2** | **2** |
| 0.70+ | 1 | 1 | 1 | 1 |

- **θ=0.60 时所有 4 个模型 K\*=2**，说明该阈值下一致可检测到 depth 0→1→2 的污染信号，depth 3+ 不再可区分。这验证了论文采用 θ=0.60 的合理性。
- 曲线呈阶梯下降，Qwen-RW（rewrite 策略）在较高 θ 时仍保持较大 K\*，表明 rewrite 污染的深度信号更强。
- 所有模型在 θ>0.70 时收敛到 K\*=1（仅能区分 depth 0 vs 1）。

---

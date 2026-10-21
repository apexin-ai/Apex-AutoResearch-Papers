# analysis p1 kl divergence

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p1_kl_divergence_20260523T202017_result.json`
- **Structured JSON:** [`ee769833723b45402871.json`](../../sessions/ee/ee769833723b45402871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SCP 不可用，结果已保存在服务器端。汇总 P1 分析结果。

## P1 TF vs AR Attention KL Divergence 分析结果

### 完成的工作

**1. CPU Proxy 分析**（已完成，`results/p1_kl_divergence/`）

匹配 TF/AR 数据的 GAR 对比（eval_200）：

| 模型 | TF mid-GAR | AR mid-GAR | Gap |
|------|-----------|-----------|-----|
| Base | 0.071 | 0.059 | +0.012 |
| SS (s123) | 0.536 | 0.488 | +0.049 |

AR mid-turn GAR 排名（越高 = 目标注意力保留越好）：

| Rank | Model | AR mid-GAR |
|------|-------|-----------|
| 1 | SS (s123) | 0.4231 |
| 2 | **TG (v7)** | **0.0641** |
| 3 | LoRA-only | 0.0373 |
| 4 | UG | 0.0333 |
| 5 | PCGrad | 0.0301 |
| 6 | Base | 0.0186 |

TG 在 AR 推理下的 GAR 是 Base 的 **3.4x**，证实 gate 机制在 AR 下保留了 goal attention。

**2. GPU 脚本**（已就绪，等 GPU 空闲执行）

- `scripts/p1_kl_divergence.py` — per-head TF vs AR attention KL 分析
- `scripts/launch_p1_kl.sh` — 自动运行 Base + TG 对比

脚本功能：
- 对每个 conversation 做 TF（GT context）和 AR（生成 context）两次推理
- 提取 per-head GAR → 计算 ΔGAR 和 binary KL(p_tf || p_ar)
- 分析 Corr(TF_GAR, ΔGAR)：验证 goal-attending heads 是否受 exposure bias 破坏更大
- 分析 Corr(gate_value, ΔGAR)：验证 gate 是否选择性保护这些 heads

**3. 生成的可视化**（服务器端 `results/p1_kl_divergence/`）：
- `p1_ar_gar_comparison.pdf` — 所有模型 AR GAR 曲线对比
- `p1_ar_mid_gar_bar.pdf` — Mid-turn AR GAR 条形图
- `p1_tf_ar_gap.pdf` — Base 和 SS 的 TF-AR gap 可视化

### 局限性

CPU 分析的匹配 TF/AR 数据仅覆盖 2 个 turn（TF 数据的 min_turns 限制），且缺少 TG 在 eval_200 上的 TF 数据。**Per-head 分析是关键缺失部分**——需要 GPU 运行 `launch_p1_kl.sh`。

### 下一步

GPU 空闲后执行：
```bash
cd /root/turn_residual_gating && bash scripts/launch_p1_kl.sh
```

---

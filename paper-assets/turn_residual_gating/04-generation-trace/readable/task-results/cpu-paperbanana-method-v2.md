# cpu paperbanana method v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_paperbanana_method_v2_20260525T064858_result.json`
- **Structured JSON:** [`44a10c04ce5eb5ca5b70.json`](../../sessions/44/44a10c04ce5eb5ca5b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。最终输出：

- **PNG**: `figures/paper/fig_method_framework.png` (2752×1536, 300 DPI)
- **PDF**: `figures/paper/fig_method_framework.pdf`

经过 6 轮 PaperBanana 迭代，三个 panel 内容全部正确：
- **(a)** ThreadGate 架构：残差流 + Gate MLP + skip connection
- **(b)** 训练目标（L_NTP + L_GAR + L_div）+ Exposure Bias 问题（TF GAR=0.50 vs AR GAR=0.019–0.064, 8–17× collapse）
- **(c)** 因果排除链（TG vs UG/LoRA/PCGrad）+ 两个修复方案（β-Steering, Scheduled Sampling）

已知限制：字体为 sans-serif（PaperBanana 使用 Gemini 图像生成模型，无法控制字体族）。

---

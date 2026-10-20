# ops check exp020 exp022c status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp020-exp022c-status_20260524T083120_result.json`
- **Structured JSON:** [`f19d567535de8f54d07e.json`](../../sessions/f1/f19d567535de8f54d07e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp_020 — GPT2-M Pure Collapse (seed42, 10 gen)
**PID 783957** | GPU 0 | 26.4GB VRAM | 52% util | 运行中  
命令: `python run_gpt2m_phase1.py --condition pure_collapse --seed 42 --generations 10 --k 0 --gpu 0`

**10 代数据已全部产出**（结果文件最后更新 16:25），但进程未退出，可能在做最终 summary/HellaSwag 评估。

| Gen | eff_rank | SLV (log_det) | PPL | D-4 | σ₁ |
|-----|----------|---------------|-----|-----|----|
| 0 | 23.09 | 689.44 | 15.45 | 0.913 | 6598.1 |
| 1 | 155.22 | 885.30 | 16.42 | 0.891 | 1463.5 |
| 2 | 185.37 | 924.39 | 18.94 | 0.868 | 1190.7 |
| 3 | 184.86 | 889.70 | 23.33 | 0.837 | 1172.3 |
| 4 | 169.56 | 817.55 | 32.11 | 0.764 | 1224.0 |
| 5 | 151.94 | 732.12 | 49.35 | 0.658 | 1317.5 |
| 6 | 136.09 | 658.12 | 76.81 | 0.559 | 1449.3 |
| 7 | 121.29 | 576.61 | 123.66 | 0.501 | 1548.4 |
| 8 | 110.92 | 500.89 | 198.01 | 0.460 | 1592.7 |
| 9 | 102.96 | 415.11 | 328.75 | 0.420 | 1570.7 |

趋势清晰：eff_rank 和 SLV 从 Gen 2 起持续下降，PPL 指数级上升，D-4 单调下降，σ₁ 持续膨胀 → 典型的 spectral collapse。尚无 `_summary.json`。

---

### exp_022c — GPT2-M Fixed Mix r=0.3 (seed42, 3 gen)
**PID 868285** | GPU 1 | 19.3GB VRAM | 61% util | 运行中  
命令: `/root/miniconda3/bin/python run_gpt2m_phase1.py --condition fixed_mix --real_ratio 0.3 --generations 3 --seed 42 --gpu 0`

- exp_022 失败（目录路径错误），exp_022b 失败（python 找不到），exp_022c 于 15:40 启动
- 日志 119KB，全是 padding 警告（686条），无进度输出 → 大概率在 Gen 0 的文本生成阶段
- 无结果文件、无 checkpoint
- 注意：这是 `fixed_mix r=0.3 seed42` 的重跑，之前 `phase1_fixed_mix_r03_seed42` 已于 5/19 完成（但那次不是 GPT2-M）

---

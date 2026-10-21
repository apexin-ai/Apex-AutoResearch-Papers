# ops exp019 check and extract

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp019-check-and-extract_20260524T020626_result.json`
- **Structured JSON:** [`e4b94efc9d3aa8cb8412.json`](../../sessions/e4/e4b94efc9d3aa8cb8412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练每 gen 约 3125 步。Gen 10 在 2900/3125，训练快结束，但后面还有 50k sample generation + metrics。估计 ~30-60 min 完成。

## 汇报

### 1. exp_019 状态：未完成（Gen 10 训练中）

进程 PID 757587 活跃（运行 22h），GPU 1，Gen 10 fine-tuning step 2900/~3125。训练即将结束但还需生成 50k samples + 计算 metrics，预计 **30-60 分钟**后 gen_10 写入结果文件。

**Gen 0-9 Metrics（已就绪）：**

| Gen | r_eff | log_det | PPL | D-4 | σ₁ |
|-----|-------|---------|------|------|------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.730 | 1942.8 |
| 1 | 476.6 | 2369.4 | 10.28 | 0.654 | 961.5 |
| 2 | 483.2 | 2361.1 | 10.73 | 0.562 | 867.8 |
| 3 | 486.5 | 2365.6 | 11.14 | 0.469 | 823.0 |
| 4 | 489.2 | 2377.1 | 11.50 | 0.399 | 786.8 |
| 5 | 493.1 | 2395.6 | 11.83 | 0.377 | 754.3 |
| 6 | 494.1 | 2411.8 | 12.16 | 0.333 | 735.2 |
| 7 | 495.7 | 2424.4 | 12.44 | 0.307 | 730.1 |
| 8 | 497.2 | 2436.1 | 12.73 | 0.283 | 743.6 |
| 9 | 502.6 | 2451.3 | 13.07 | 0.232 | 709.5 |

### 2. exp_020 状态：Gen 7 生成中

当前 gen_0-6 已完成。Gen 7 正在 sample generation（23360/50000）。

| Gen | r_eff | log_det | PPL | D-4 | σ₁ |
|-----|-------|---------|------|------|------|
| 0 | 23.1 | 689.4 | 15.45 | 0.913 | 6598.1 |
| 1 | 155.2 | 885.3 | 16.42 | 0.891 | 1463.5 |
| 2 | 185.4 | 924.4 | 18.94 | 0.868 | 1190.7 |
| 3 | 184.9 | 889.7 | 23.33 | 0.837 | 1172.3 |
| 4 | 169.6 | 817.6 | 32.11 | 0.764 | 1224.0 |
| 5 | 151.9 | 732.1 | 49.35 | 0.658 | 1317.5 |
| 6 | 136.1 | 658.1 | 76.81 | 0.559 | 1449.3 |

Pure collapse 进展明显：PPL 爆炸 (15→77)，r_eff 下降 (23→136 先升后降)，σ₁ 从 gen_1 起反弹上升。

### 3. GPU 状态

| GPU | Utilization | Memory Used | Total |
|-----|------------|-------------|-------|
| 0 | 95% | 26.4 GB | 95.6 GB |
| 1 | 96% | 25.0 GB | 95.6 GB |

两块卡都在满载运行（exp_020 用 GPU 0，exp_019 用 GPU 1），无空闲 GPU。

### 4. 本地保存

gen_10 未就绪，暂不保存 `artifacts/exp_019/full_metrics.json`。建议 30-60 分钟后再提取。

---

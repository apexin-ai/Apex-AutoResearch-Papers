# ssh launch generalize phase2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_generalize_phase2_20260517T071108_result.json`
- **Structured JSON:** [`91a379509fc5b056a651.json`](../../sessions/91/91a379509fc5b056a651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在运行。汇报结果：

---

## 产出汇报

### 1. OPT-1.3B 可用性
- **加载成功**，参数量 1316M，从 hf-mirror.com 下载完成

### 2. 两个实验启动状态

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| Pythia-410M | cuda:0 (12.8GB VRAM) | 247554 | `generalize_pythia410m_wiki_a100_s42` | Gen 1/10 数据生成中 |
| OPT-1.3B | cuda:1 (20.2GB VRAM) | 249384 | `generalize_opt1b_wiki_a100_s42` | Gen 0 baseline 中 |

### 3. 初始 log 输出
- **Pythia-410M**: 已完成 Generation 0 baseline，`ppl=26.95, entropy=3.2342, eff_rank=46.6`，正在 Generation 1/10 生成 synthetic data
- **OPT-1.3B**: 已加载模型和数据，正在运行 Generation 0 (baseline)

### 4. 预估完成时间
- Pythia-410M baseline 耗时 ~18min（Generation 0），10 代预计 **~6-8 小时**（含 5000 步训练 + 数据生成 + 指标计算/代）
- OPT-1.3B 模型更大（3.2x参数），预计 **~10-15 小时**
- 两个实验分别在 cuda:0 和 cuda:1，互不干扰

---

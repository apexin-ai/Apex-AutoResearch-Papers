# diagnose exp 001 timeout

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_timeout_20260516T161127_result.json`
- **Structured JSON:** [`1d3a887cc34bfadb229d.json`](../../sessions/1d/1d3a887cc34bfadb229d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已经足够了。以下是诊断报告。

---

## exp_001 超时诊断报告

### 完成进度：3/10 代（gen 0 baseline + gen 1 + gen 2），gen 3 在生成合成数据阶段被 kill

### 时间线
| 事件 | 时间 (CST) | 耗时 |
|------|-----------|------|
| 脚本启动 | 16:08 | - |
| Gen 0 baseline 评估完成 + checkpoint | 16:21 | ~13 min |
| Gen 1 完整周期 (生成 50k + 训练 + 评估) | 16:21 → 18:53 | **~2h32m** |
| Gen 2 完整周期 | 18:53 → 21:28 | **~2h35m** |
| Gen 3 开始生成 → 被 kill | 21:28 → 23:53 | ~2h25m (仅完成 4800/50000 样本) |
| **总运行时间** | | **~7h45m** |

每代完整周期约 **2.5h**。10 代需要 **~25h**，8h timeout 远远不够。

### 已保存的 Metrics（完整可用）

| Gen | Eff Rank | Perplexity | Distinct-4 | HellaSwag acc_norm | Train Loss |
|-----|----------|------------|------------|-------------------|------------|
| 0 | 417.55 | 9.55 | 0.7414 | 0.4130 | - |
| 1 | 491.77 | 11.38 | 0.6256 | 0.3897 | 1.6228 |
| 2 | 496.44 | 13.58 | 0.5154 | 0.3764 | 1.2682 |

**崩塌趋势清晰**：perplexity 上升 (9.55→13.58)，distinct-4 下降 (0.74→0.52)，HellaSwag 下降 (0.413→0.376)。Effective rank 反而上升，说明权重矩阵谱结构在扩散而非集中。

`logdet_gen012.json` 也包含 log-determinant 和 top-10 singular values 数据，均完好。

### 可恢复资源
- **Checkpoints**：`gen_0/`, `gen_1/`, `gen_2/` 各含完整 model.safetensors (~1.6G)
- **Metrics**：`phase0_results.json`, `logdet_gen012.json`, `hellaswag_gen{0,1,2}/results.json`
- **可从 gen_2 checkpoint 断点续跑 gen 3~9**

### 致超时原因
每代生成 50000 条合成数据 + fine-tune + 评估，单代 ~2.5h。10 代需 ~25h，而 timeout 仅 8h。此外日志被 `right-padding` 警告刷屏（~4785 条），虽不影响运行但污染诊断。

### 建议

**方案 A（推荐）：从 gen_2 断点续跑**，timeout 设为 20h，跳过 gen 0-2，直接从 gen_3 开始。需要代码支持 `--resume-from-gen 3`。

**方案 B：已有 3 代数据先用**。趋势已经很明显，可先做初步分析/绘图，同时后台跑完剩余 7 代。

**方案 C：加速优化**。减少每代生成样本数（50k→20k），或减少 fine-tune 步数，将单代压到 ~1h 以内，10 代 <12h。

**附带修复**：代码中 tokenizer 需设置 `padding_side='left'`，消除警告刷屏。

---

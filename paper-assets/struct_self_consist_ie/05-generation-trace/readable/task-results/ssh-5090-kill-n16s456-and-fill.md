# ssh 5090 kill n16s456 and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_kill_n16s456_and_fill_20260521T152100_result.json`
- **Structured JSON:** [`e670a5b58db0ae9e3f93.json`](../../sessions/e6/e670a5b58db0ae9e3f93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## 1. Kill 状态: 未找到 fewnerd_n16_s456 进程

cuda:0 上没有任何进程。找到的相关进程是：
- **PID 47635** `exp_e2_pretrained_fewnerd_s456` — N=**8**（不是16），运行在 **cuda:3**，是 pretrained baseline
- **tmux `exp_001_n16_seed456`** — 是 **SciERC**（不是 FewNERD）

**cuda:0 已空闲，无需 kill。**

## 2. GPU 状态

| GPU | Memory | 状态 |
|-----|--------|------|
| cuda:0 | 2 MiB / 32 GB | **空闲** |
| cuda:1 | 30204 MiB / 32 GB | 占用 |
| cuda:2 | 30230 MiB / 32 GB | 占用 |
| cuda:3 | 29946 MiB / 32 GB | 占用 (exp_e2_pretrained_fewnerd_s456) |

## 3. 候选实验（从 PREPARING/QUEUED 中筛选，排除已完成/已有结论的）

| # | 实验 ID | 内容 | Hypothesis 摘要 |
|---|---------|------|-----------------|
| **A** | `exp_fewnerd_mf4v2_s123_v3` | FewNERD MF4v2 N=8 s123, 修正后的模型路径 | v2 因模型路径错误失败，v3 修正 tokenizer dir。补齐 MF4 3-seed |
| **B** | `exp_fewnerd_mf4v2_s42_v3` | FewNERD MF4v2 N=8 s42, 同上修正 | 同上，另一个 seed |
| **C** | `exp_dgec_heterogeneous_t` | 混合 T=0.7+T=1.0 采样 | 混温打破 mode collapse 降低 degeneracy，构造 F1 提升 |
| **D** | `exp_scierc_n16_s42` | SciERC N=16 s42（你说已完成？registry 仍 PREPARING） | SciERC 扩展到 N=16，测 oracle headroom |
| **E** | `exp_a1_spider_sql_sc` | Spider SQL 跨任务验证（在 5090-b:cuda:2） | SC cascade 是否泛化到 SQL 结构化生成 |

**已排除**：exp_b2 系列（4个均 conclusion=negative）、exp_fewnerd_n16_s456_v2（你说已在 5090-c 完成）、exp_e2_pretrained_fewnerd_s456（正在 cuda:3 运行）、3 个 QUEUED mf4（conclusion=killed）。

## 4. 可用资源

- **8B 模型**: qwen3-8b-fewnerd-exp021-merged, qwen3-8b-conll2003-merged, qwen3-8b-scierc-merged-v2
- **Pretrained**: Qwen2.5-7B-Instruct
- **数据**: fewnerd, conll2003, scierc, wnut17, fewrel, retacred_raw
- **核心脚本**: `run_mvp_pilot.py`, `run_frontier_sc.py`, `run_esj.py`, `run_verbalized_confidence.py`

---

**推荐**: A 或 B（MF4v2 修正版）优先级最高——补齐 FewNERD 3-seed 统计检验力。C（混温实验）概念新颖但无先验结论。选哪个？

---

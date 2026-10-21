# diag gpu status and degen investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_status_and_degen_investigation_20260518T122442_result.json`
- **Structured JSON:** [`84211f2626b6ec7bfed4.json`](../../sessions/84/84211f2626b6ec7bfed4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。汇总报告。

---

## 任务 1: GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 2 MiB / 32607 MiB | 0% | **空闲** |
| cuda:1 | 30888 MiB / 32607 MiB | 100% | **训练中** |
| cuda:2 | 2 MiB / 32607 MiB | 0% | **空闲** |
| cuda:3 | 2 MiB / 32607 MiB | 0% | **空闲** |

**cuda:1 LLaMA Few-NERD 训练**（tmux session `llama_fewnerd`）：
- 进度：**18% (4559/24708 steps)**，已运行 2h53m，预计剩余 ~9h45m
- 刚保存 checkpoint-4000，自动删除了 checkpoint-1000
- 模型路径：`checkpoints/llama3.1-8b-fewnerd-lora/`

其他 tmux sessions（均无 GPU 占用，历史残留）：
- `exp_011_ood_conll_to_scierc`（5月15日）
- `exp_017_llama_conll_n16_r1024`（5月15日）
- `exp_017_llama_conll_n16_s456_r1024`（5月15日）

---

## 任务 2: Few-NERD degeneracy 差异根因

**两个数字分别怎么算的：**

| 来源 | 值 | 定义 | 脚本 |
|------|-----|------|------|
| 主表 (recompute_tab) | **13.75%** (`degen_f1_pct`) | 所有 N=8 个 sample 的 F1 **完全相同** (`len(set(sample_f1s)) == 1`) | `code/recompute_table_fewnerd.py` |
| 3-seed worker 报告 | **10.13%** (`degeneracy_rate_pct`) | 所有 N=8 个 sample 的 **entity key set 完全相同** (`len(set(key_sets)) == 1`) | `code/analyze_fewnerd_results.py` |

两者都是 seed=42、gold_filtered（n=32565）数据。`recompute_table_fewnerd.py` 也单独计算了 keyset degeneracy = 10.04%，与 10.13% 基本一致（微小差异来自 keyset 构造细节）。

**差异根因：degeneracy 的定义不同。**
- F1-degeneracy (13.75%) > keyset-degeneracy (10.13%)，因为不同的 entity set 可以产出相同的 F1 分数（如不同的错误恰好导致相同的 precision/recall）。

**论文应该用哪个值：**
- 如果 degeneracy 的叙事是 "self-consistency 无法提供选择信号的情况"，用 **F1-based (13.8%)**，因为即使 entity set 不同，F1 相同也意味着无法通过 oracle 选择获益。
- 如果叙事是 "模型输出完全退化/缺乏多样性"，用 **keyset-based (10.1%)**。
- 建议：主表和正文统一使用 `recompute_table_fewnerd.py` 的 F1-based 定义（13.8%），并在 3-seed 分析中也改用同一定义以保持一致。`analyze_fewnerd_results.py` 第 164 行的 `len(set(key_sets)) == 1` 应改为 `len(set(sample_f1s)) == 1`（或同时报告两个指标）。

---

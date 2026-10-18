# exp step2 status check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_step2-status-check_20260521T232820_result.json`
- **Structured JSON:** [`3f77de9fbf9c8b165a35.json`](../../sessions/3f/3f77de9fbf9c8b165a35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 2 v2 (mvp-step2-keff-contrast) 状态汇报

### 进程状态
- **PID 48121: 存活**，已运行 36 分 34 秒
- GPU 2 占用 91795 MiB（~90GB），利用率 100%，其余 GPU 空闲

### 运行进度
K_eff 排名阶段已完成，当前在**攻击生成阶段**，进度 **71% (212/300)**，速度约 470 toks/s input, 103 toks/s output。

### 错误
无 error/traceback/exception/OOM。

### 结果文件
尚无 `results_step2_*.json`，实验未完成。

### K_eff 排名结果 (MMLU, K=3 panels)

**Top-3 High K_eff:**

| Rank | K_eff(MI) | K_eff(ρ) | Fam | Panel |
|------|-----------|----------|-----|-------|
| #1 | 2.771 | 2.949 | 3 | mistral-large, qwen2.5-14b, llama3.1-8b |
| #2 | 2.750 | 2.954 | 2 | llama3.1-70b, qwen2.5-14b, llama3.1-8b |
| #3 | 2.710 | 2.919 | 2 | qwen2.5-32b, qwen2.5-14b, llama3.1-8b |

**Bottom-3 Low K_eff:**

| Rank | K_eff(MI) | K_eff(ρ) | Fam | Panel |
|------|-----------|----------|-----|-------|
| #18 | 2.207 | 2.790 | 2 | qwen2.5-72b, mistral-large, qwen2.5-32b |
| #19 | 2.193 | 2.773 | 3 | qwen2.5-72b, llama3.1-70b, mistral-large |
| #20 | 2.140 | 2.747 | 2 | qwen2.5-72b, llama3.1-70b, qwen2.5-32b |

趋势：含 llama3.1-8b 的 panel 普遍 K_eff 更高（前 10 名全含它），大模型组合（72b+70b+32b）K_eff 最低。预计还需几分钟完成攻击生成阶段。

---

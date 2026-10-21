# harvest westd results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd-results_20260517T103609_result.json`
- **Structured JSON:** [`0ec5397e0c81d860d244.json`](../../sessions/0e/0ec5397e0c81d860d244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

---

## 任务 1: 结果文件汇总

| 文件 | 模型 | Benchmark | Accuracy | n_correct/n_total | EOS Rate | Avg Len |
|---|---|---|---|---|---|---|
| `eval_postprune_rasp_25.json` | pruned_rasp_25 | GSM8K | **0.21** | 21/100 | 56% | 2033 |
| `eval_postprune_standard_25.json` | pruned_standard_25 | GSM8K | **0.16** | 16/100 | 23% | 3241 |
| `eval_sft_rasp_rlvr_20_qwen_math.json` | sft_rasp_rlvr_20_qwen_math | GSM8K | **0.73** | 146/200 | 100% | 127 |

关键观察：
- RASP 25% 剪枝后 GSM8K = 21%，Standard 25% = 16%，RASP 优势 +5pp
- Standard 剪枝的 EOS rate 仅 23%（77% 被 4096 截断），说明模型退化严重，无法收敛到答案
- SFT RASP+RLVR 恢复到 73%，EOS rate 100%，avg_len 仅 127 tokens，非常干净

## 任务 2: eval_sft_rasp_rlvr_20_qwen_math 状态

**已正常完成**。日志显示 200/200 样本跑完，最终 acc=0.7300，结果已保存。文件时间戳 `May 17 02:08`。registry 显示 RUNNING 是因为没有正确更新状态，实际进程已结束。

另外发现 `eval_grpo_rasp_rlvr_20_qwen_math.json` 也已存在（May 17 04:17, 142KB）。

## 任务 3: HumanEval Pass@1 诊断

所有 HumanEval 结果汇总：

| 模型 | Pass@1 | n_correct/164 | Avg Len | Median Len |
|---|---|---|---|---|
| **unpruned** (DeepSeek-R1-Distill-Qwen-7B) | **0.0183** | 3/164 | 512.0 | 512.0 |
| grpo_standard_20 | **0.0183** | 3/164 | 505.9 | 512.0 |
| sft_standard_20 | **0.0305** | 5/164 | 505.4 | 512.0 |
| sft_rasp_20 | **0.0732** | 12/164 | 420.5 | 512.0 |
| grpo_rasp_20 | **0.1037** | 17/164 | 417.6 | 512.0 |

### 诊断结论：**max_new_tokens=512 截断是根因，不是模型能力崩塌**

证据：
1. **连 unpruned 基座模型也只有 1.8% Pass@1**，median response length = 512.0（全部被截断）
2. `eval_humaneval.py` 第 70 行：`default=512`。DeepSeek-R1-Distill 是 thinking model，生成代码前会先输出大量推理 chain-of-thought 文本（"Okay, I need to..."），512 tokens 根本不够写完代码
3. 错误全部是 SyntaxError（代码在思考文本中间被截断），不是逻辑错误
4. RASP 模型相对好一些（10.4% vs 1.8%），可能因为 SFT/GRPO 训练让输出更紧凑，偶尔能在 512 tokens 内完成代码

**修复方案**: `max_new_tokens` 改为 2048 或更高，重新跑所有 HumanEval 评估。

---

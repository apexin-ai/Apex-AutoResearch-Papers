# ops westd submit cka eval and 30pct

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_submit_cka_eval_and_30pct_20260517T182046_result.json`
- **Structured JSON:** [`9d6b80d4b786e2229c2c.json`](../../sessions/9d/9d6b80d4b786e2229c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新实验进程均已启动。

---

## 报告

### 新实验 PID
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| eval_sft_cka_only_20_full (GSM8K N=1319) | cuda:0 | 44066 | 启动中（模型加载） |
| eval_postprune_rasp_30 (GSM8K N=200) | cuda:2 | 44265 | 启动中（模型加载） |

### GPU 占用确认
| GPU | 进程 | 任务 |
|-----|-------|------|
| cuda:0 | PID 44066 | eval_sft_cka_only_20_full |
| cuda:1 | PID 14556 | eval_math500_grpo_standard_20 |
| cuda:2 | PID 44265 | eval_postprune_rasp_30 |
| cuda:3 | PID 31706 | math500_grpo_rasp_20_v3 |

### HumanEval 结果（2048 token）

| 模型 | pass@1 | n_correct/n_total | avg_response_len | median_response_len |
|------|--------|-------------------|------------------|---------------------|
| sft_standard_20 | **11.59%** | 19/164 | 1850.7 | 2048 |
| grpo_standard_20 (ckpt-50) | **10.37%** | 17/164 | 1843.0 | 2048 |

两个模型 HumanEval 表现都很差，median response length 触顶 2048（大量截断），且错误模式显示模型在输出思维链而非直接生成代码（CoT 泄漏到代码生成任务）。GRPO 甚至略差于 SFT。

---

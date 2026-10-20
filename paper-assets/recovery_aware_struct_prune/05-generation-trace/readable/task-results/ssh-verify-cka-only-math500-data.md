# ssh verify cka only math500 data

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_cka_only_math500_data_20260523T031719_result.json`
- **Structured JSON:** [`98e444085947313451fb.json`](../../sessions/98/98e444085947313451fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是详细报告。

---

## 调查结论：同一次生成，不同判分脚本

### 三次相关 Run 的时间线

| Run | 日志 | 时间 | 结果 | 状态 |
|-----|------|------|------|------|
| A (最早) | `logs/eval_math500_sft_cka_only_20.log` | May 18 07:19 | — | **max_new_tokens=4096**, 极慢（~10x），运行到中途 |
| A' (重跑) | `runs/math500_sft_cka_only_20.log` | May 18 21:01 | — | 同样 4096，170/500 时 **EXIT_CODE=124 超时被杀** |
| B (v4) | `runs/math500_sft_cka_only_20_v4.log` | May 19 02:15–06:07 | **29.0% (145/500)** | 完成 |
| C (westd) | `logs/eval_math500_sft_cka_only_20_westd.log` | May 23 04:06–07:57 | **26.8% (134/500)** | 完成 |

### 两个文件对比

| 属性 | `math500_sft_cka_only_20_v4.json` (29.0%) | `eval_math500_sft_cka_only_20.json` (26.8%) |
|------|------------------------------------------|--------------------------------------------|
| 路径 | `/root/autodl-tmp/.../results/math500_sft_cka_only_20_v4.json` | `/root/autodl-tmp/.../results/eval_math500_sft_cka_only_20.json` |
| 修改时间 | 2026-05-19 06:07 | 2026-05-23 07:57 |
| 大小 | 147,942 bytes (4017行) | 145,888 bytes (3514行) |
| model_path | `/root/autodl-tmp/.../sft_cka_only_20` | 同上 |
| max_new_tokens | **2048**（截断值确认） | **2048**（截断值确认） |
| natural_eos | 384 | **384** |
| truncated | 116 | **116** |
| avg_response_length | 673.278 | **673.278** |
| 字段名 | `pred` / `gold` / `idx` | `pred_answer` / `gold_answer`（无 `idx`） |
| correct count | 145 | 134 |

### 核心发现：**生成完全相同，判分不同**

两个文件的 **500 条 response_length 逐条完全一致**，eos_stats 三项完全一致。这意味着：

1. **同一个模型**，**同一个 max_new_tokens=2048**，**同一个 seed**（确定性生成）
2. 模型生成的原始文本 **token-for-token 完全相同**
3. 差异 **纯粹在答案提取（answer extraction）逻辑**

具体差异示例（Problem 0, 极坐标题）：
- v4 脚本提取: `pred: "3, 0"` → 判 false
- westd 脚本提取: `pred_answer: "0"` → 判 false
- 两个都判错，但提取结果不同

### 关于 PID 75284

日志中没有记录 PID。但根据命名和时间：
- **PID 75284 = Run C (westd eval, May 23)**
- 输出: `eval_math500_sft_cka_only_20.json`
- 结果: **26.8% (134/500)**

### 回答关键问题

| 问题 | 答案 |
|------|------|
| 29.0% (145/500) 来自哪？ | `math500_sft_cka_only_20_v4.json`，Run B (May 19)，旧版 eval 脚本 |
| 26.8% (134/500) 来自哪？ | `eval_math500_sft_cka_only_20.json`，Run C (May 23 westd eval)，新版 eval 脚本 |
| PID 75284 的输出？ | **26.8% (134/500)** — `eval_math500_sft_cka_only_20.json` |
| max_new_tokens 不同？ | **不**。两次都是 @2048。不同的是 May 18 的 Run A 用了 @4096 但超时未完成 |
| 差异根因？ | **两版 eval 脚本的 answer extraction 不同**，导致相同文本被判出 11 个不同结果 |

**需要进一步确认**：检查这 11 个判分不一致的具体题目，确定哪个版本的提取更准确，才能最终决定采用哪个数字。

---

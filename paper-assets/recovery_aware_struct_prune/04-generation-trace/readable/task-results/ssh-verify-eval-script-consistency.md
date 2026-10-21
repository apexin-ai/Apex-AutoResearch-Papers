# ssh verify eval script consistency

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_eval_script_consistency_20260523T032302_result.json`
- **Structured JSON:** [`8555236a006df29ec8a4.json`](../../sessions/85/8555236a006df29ec8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：同一 checkpoint、同一 greedy 输出（EOS stats 完全一致），差异 **100% 来自 answer extraction 逻辑**。

## 结论

### 1. 当前脚本版本
两台服务器（westb-23072、westd-32935）的 `eval_math500.py` 完全一致，均为**新版**：
- 字段名：`pred_answer` / `gold_answer`（无 `idx`）
- 文件从未提交 git，无版本历史

### 2. 脚本变更时间点
根据结果文件的字段名和时间戳，分界线在 **May 19 → May 23** 之间：

| 时间 | 字段 | 脚本版本 |
|------|------|----------|
| May 17-19 | `pred`/`gold`/`idx` | 旧版 |
| May 23 | `pred_answer`/`gold_answer` | 新版 |

### 3. 结果文件一览

**旧版脚本（`pred`/`gold`/`idx`）— May 17-19：**

| 文件 | Acc | 日期 |
|------|-----|------|
| eval_math500_sft_rasp_20.json | 24.2% | May 17 |
| eval_math500_sft_standard_20.json | 26.0% | May 17 |
| eval_math500_unpruned.json | 73.6% | May 17 |
| math500_grpo_unpruned.json | 69.0% | May 18 |
| math500_dense_2048.json | 53.0% | May 19 |
| math500_dense_unpruned.json | 73.6% | May 19 |
| math500_grpo_cka_only_20_2048.json | 29.2% | May 19 |
| math500_grpo_rasp_20_fair.json | 24.0% | May 19 |
| math500_grpo_standard_20_fair_v2.json | 26.4% | May 19 |
| math500_sft_cka_only_20_v4.json | **29.0%** | May 19 |
| math500_sft_rasp_20_2048.json | 22.6% | May 19 |
| math500_sft_standard_20_2048_v2.json | 25.8% | May 19 |

**新版脚本（`pred_answer`/`gold_answer`）— May 23：**

| 文件 | Acc | 日期 |
|------|-----|------|
| eval_math500_sft_rasp_alpha0p5_20.json | 25.4% | May 23 |
| eval_math500_sft_rasp_alpha1p0_20_v2.json | 21.2% | May 23 |
| eval_math500_sft_rasp_alpha3p0_20.json | 23.2% | May 23 |
| eval_math500_sft_rasp_alpha4p0_20.json | 26.6% | May 23 |
| eval_math500_sft_cka_only_20.json | **26.8%** | May 23 |
| eval_math500_grpo_rasp_alpha2p0_20.json | 26.2% | May 23 |

### 4. 提取差异的根因

CKA-only SFT 两次 eval 使用**同一 checkpoint、同一 greedy 输出**（natural_eos=384, truncated=116, avg_len=673.278 完全一致），但 19 个问题判定不同（11 个 old✓new✗，8 个 old✗new✓）。

新版脚本对复杂答案提取更差——频繁 fallback 到"取最后一个数字"：
- `6+9i` → 新版提取为 `9` ✗
- `(-1,6)` → 新版提取为 `6` ✗
- `11\sqrt{2}` → 新版提取为 `2` ✗
- `-\frac{\pi}{6}` → 新版提取为 `6` ✗

### 5. C1 |Δ| 可信度

**如果 C1 表格内的对比都在同一版本内（全部 May 17-19 或全部 May 23），则 |Δ| 可信。**

**不可信的情况**：如果 α ablation 结果（May 23 新版）与 main table baselines（May 17-19 旧版）做跨版本对比，则 |Δ| 被脚本差异污染。典型案例就是 CKA-only SFT 的 29.0%（旧）vs 26.8%（新），2.2pp 差距完全是提取逻辑造成的。

**建议**：用当前新版脚本对 May 17-19 的所有 baseline checkpoint 重跑 eval，统一到同一版本后再比较。

---

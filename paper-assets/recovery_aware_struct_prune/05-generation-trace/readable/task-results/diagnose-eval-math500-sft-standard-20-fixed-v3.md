# diagnose eval math500 sft standard 20 fixed v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_standard_20_fixed_v3_20260523T211918_result.json`
- **Structured JSON:** [`7223e8e73bfd9f1951f6.json`](../../sessions/72/7223e8e73bfd9f1951f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况完全清晰了。所有问题 eval 已经有人重新启动了。让我汇总。

---

## 诊断结果

### 根因

**不是 OOM，不是脚本 bug。是 SFT 模型生成太长导致超时。**

| 实验 | 速度 | 原因 |
|------|------|------|
| sft_standard_20 (max_tokens=4096) | 210 s/题 | 频繁触达 4096 cap，500题需 29h |
| sft_random_20 (max_tokens=4096) | 213 s/题 | 同上 |
| sft_rasp_alpha1p0 (max_tokens=4096) | 14.6 s/题 | avg_response=930 tokens，2h 完成 ✅ |
| grpo_standard (max_tokens=2048) | ~50 s/题 | 中等长度，但也偏慢 |

SFT standard/random 模型因剪枝质量差，生成退化的长重复文本，几乎每题都撞 4096 上限。RASP 模型保留了更好的生成质量，输出更短。

所有 EXIT_CODE=143 (SIGTERM) 均为超时/外部 kill，不是程序崩溃。

### 当前状态：已有修复在跑

**所有实验已被重新启动，使用 `--max_new_tokens 2048`**：

**westd-32935 (3 个进程):**
| 实验 | 进度 | 预计完成 |
|------|------|----------|
| grpo_standard_20_fixed | 450/500 | ~30-40 min |
| sft_standard_25_fixed_v2 | 9/500, ~77s/it | ~10.7h (~16:00 今天) |
| sft_standard_20_fixed_v3 (新) | 刚启动 05:16 | 预计 ~10h |

**westb-23072 (2 个进程):**
| 实验 | 进度 | 预计完成 |
|------|------|----------|
| grpo_cka_only_20_fixed | 224/500, ~29s/it | ~2h (~07:35) |
| sft_random_20_fixed_v2 (新) | 刚启动 05:16 | 预计 ~8-10h |

**已完成:**
- grpo_rasp_alpha1p0_20_fixed: **0.2300** ✅
- sft_rasp_alpha1p0_20_fixed: **0.2160** ✅

### 注意事项

1. **sft_standard_20_fixed_v3 和 sft_random_20_fixed_v2 的新运行没有写日志文件** — 它们通过 `timeout 72000 bash -c ...` 直接在 pts 终端运行，输出到 stdout 而非 log 文件。CRON 监控无法追踪它们。但结果 JSON 会写到 `--output_path` 指定的位置。
2. **grpo_standard 的 timeout=28800 (8h)** — 当前 450/500，已运行 ~6.3h，剩余 ~40 min，不会超时。
3. **3 个 GPU 同时跑** 在 westd-32935 上 — 没有 GPU 争抢问题，各占一张卡。
4. **DDL 风险**：sft_standard_25 和 sft_random_20 需要 ~10h，预计今天下午完成。在 27h DDL 内。

### 为什么 GRPO eval 正常但 SFT 总失败

GRPO 训练通过 reward 信号学会了生成简洁答案；SFT 模型（尤其是 standard/random 剪枝后的）没有这个约束，生成质量退化导致无限长推理链。降低 max_new_tokens 从 4096 到 2048 是正确修复。

---

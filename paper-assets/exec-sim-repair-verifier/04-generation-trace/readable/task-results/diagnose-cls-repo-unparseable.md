# diagnose cls repo unparseable

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cls-repo-unparseable_20260517T162107_result.json`
- **Structured JSON:** [`866bcd7b47489cb66071.json`](../../sessions/86/866bcd7b47489cb66071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集完毕。以下是完整诊断结果：

---

## 诊断结果

### 1. Unparseable 根因：**输入截断 (`max_seq_length=2048`)**

100% 相关性：
- Truncated & Unparseable: **2796**
- Truncated & Parseable: **0**
- Not-truncated & Unparseable: **0**
- Not-truncated & Parseable: **6988**

截断机制：`build_prompt_ids()` 在 tokenize 后硬截断 `ids[:max_len]`，截掉了 chat template 的 generation prompt（assistant turn start）。模型看不到完整 prompt 结构，输出的是代码续写而非 "pass"/"fail"。

对比：Qwen3-8B CLS 使用 `max_seq_length=8192`，**unparseable=0**。

### 2. 10 个 unparseable 样本的 raw model output

仅涉及 **3 个 unique problem_id**，输出模式高度重复：

| 次数 | gen_text | problem_id |
|------|----------|------------|
| 2322x | `', but replace it with a new one'` | pydata__xarray-6992 |
| 114x | `']()\\n# Saves the x'` | pytest-dev__pytest-7490 |
| 114x | `'if marks.\\nskipped_by'` | pytest-dev__pytest-7490 |
| 114x | `'marks.\\nskipped_by_'` | pytest-dev__pytest-7490 |
| 88x | `"st_epilog>', lin"` | sphinx-doc__sphinx-11445 |
| 44x | `'eno)\\n\\ndef parse('` | sphinx-doc__sphinx-11445 |

全部是代码片段续写，不是 pass/fail 分类输出。

### 3. Input 长度分布

| 分位 | 字符数 | 估计 token 数 |
|------|--------|---------------|
| p50 | 1,634 | ~408 |
| p75 | 8,911 | ~2,228 |
| p90 | 8,935 | ~2,234 |
| p95 | 8,967 | ~2,242 |
| max | 9,759 | ~2,440 |
| >8192 chars | 2,796 (28.6%) | 即被截断的部分 |

双峰分布：71.4% 样本 <2048 tokens，28.6% 在 2048-2440 tokens 之间。

### 4. Parseable-only accuracy

| 指标 | 值 |
|------|------|
| 报告 accuracy（含 unparseable） | **82.62%** |
| Parseable-only accuracy | **77.99%** (5450/6988) |
| Unparseable 默认 pred | 全部=1 (pass, majority fallback) |
| Unparseable 中 label=pass | 2634/2796 = 94.2% |
| Accuracy 虚高幅度 | **+4.63pp** |

报告的 82.62% 被 majority fallback 人为抬高。真实模型判断能力是 77.99%。同时 `recall_fail` 极低 (36.77%) 正是因为大量 fail 样本被截断后默认成了 pass。

### 5. 修复建议

**重跑 eval，`--max_seq_length 8192`**：

```bash
python eval_repo_cls.py \
    --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/best \
    --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
    --max_seq_length 8192 \
    --batch_size 1 \
    --split test \
    --output /root/autodl-tmp/eval_results/deepseek_cls_repo_s123_test/eval_summary_seq8192.json \
    --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_s123_test/predictions_seq8192.jsonl
```

max=9759 chars (~2440 tokens)，8192 token limit 完全覆盖所有样本，与 Qwen 评估条件一致。batch_size 降为 1 避免长序列 OOM。

---

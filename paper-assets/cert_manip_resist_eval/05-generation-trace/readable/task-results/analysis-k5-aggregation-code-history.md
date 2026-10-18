# analysis k5 aggregation code history

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation-code-history_20260524T070914_result.json`
- **Structured JSON:** [`073385c273db93af4bfe.json`](../../sessions/07/073385c273db93af4bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整的证据链了。

---

## 步骤 1: Git log (May 20-25)
服务器上**没有 `.git` 目录**，本地项目也不是 git 仓库。无 git 历史可查。

## 步骤 2: 代码版本比对（替代 git blame）
通过提取 May 23 worker log（`worker_analysis_k5-aggregation-bootstrap_20260523T061722.log` 第32行）中实际写入的脚本内容，与当前（May 24 运行时）的脚本对比：

| | May 23 运行 | May 24 运行 |
|---|---|---|
| 脚本长度 | 19814 chars | 20685 bytes |
| `_is_valid_score` | **不存在** | **有，做 error/format_error/winner 过滤** |
| imports | `compute_clean_accuracy` from unified_data_loader | `_is_valid_score` from unified_data_loader |
| `compute_individual_asr` | `.get("winner", "tie")` 无效分数当 "tie" | `_is_valid_score` 过滤后直接用 `["winner"]` |
| `compute_panel_asr_all_methods` | 无有效性检查，`.get("winner", "tie")` | 两层 `_is_valid_score` 过滤，跳过无效样本 |

**结论：May 23 和 May 24 运行的代码不同。** May 24 版本增加了 `_is_valid_score` 过滤（跳过 error、format_error、非 A/B/tie 的 winner），这是核心差异。

## 步骤 3: 随机种子
固定种子：**是**，SEED = 42（两个版本均如此）

但种子相同不意味着结果相同——因为 `_is_valid_score` 过滤改变了参与回归的样本集，导致回归系数和 bootstrap p-values 不同。

## 步骤 4: 元信息与结果对比

| 字段 | May 23 | May 24 | 一致? |
|---|---|---|---|
| panel_size | 5 | 5 | ✓ |
| n_bootstrap | 9999 | 9999 | ✓ |
| seed | 42 | 42 | ✓ |
| n_total_panels | 3003 | 3003 | ✓ |
| fdr_alpha | 0.05 | 0.05 | ✓ |
| elapsed_seconds | 444s | 501s | ✗ (不同硬件) |

**聚合方法结果差异：**

| Method | May 23 keff_fdr_sig | May 24 keff_fdr_sig | May 23 eta_fdr_sig | May 24 eta_fdr_sig |
|---|---|---|---|---|
| majority_vote | 7/12 | 7/12 | 0/12 | 2/12 |
| weighted_vote | **9/12** | **7/12** | 1/12 | 2/12 |
| threshold_supermajority | **10/12** | **7/12** | **6/12** | **3/12** |
| bayesian | **0/12** | **7/12** | 1/12 | 2/12 |

bayesian 的 keff_fdr_sig 从 0/12 变为 7/12 是最大的变化。May 24 所有方法 keff 统一为 7/12，May 23 各方法差异较大(0/7/9/10)。

## 总结

**May 23 和 May 24 运行的代码不同。** 关键变更是引入了 `_is_valid_score` 有效性过滤。May 23 把无效评分（error/format_error/非法winner）默认当作 "tie" 参与计算；May 24 直接跳过这些样本。这改变了面板 ASR 的计算基数和回归输入，导致 bootstrap p-values 系统性变化。输入数据文件和随机种子均未变。

---

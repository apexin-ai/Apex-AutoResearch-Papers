# research re repair code audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_re-repair-code-audit_20260517T040024_result.json`
- **Structured JSON:** [`657f6ad3cb129788d5a5.json`](../../sessions/65/657f6ad3cb129788d5a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Re-Repair Phase0 代码审计报告

---

### 文件 1: `re_repair_phase0.py` — 快速可行性测试

#### 1. Prompt Template 结构

**System Prompt（所有 condition 共用）：**
```python
"You are a software engineer. You are given a code patch that was intended "
"to fix an issue but does not fully work. Your task is to produce a corrected "
"patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
```

**Control condition（L94）：**
```
## Issue Description
{problem_statement}

## Current (Incorrect) Patch
```diff
{mutation_patch}
```

Please produce a corrected patch in unified diff format.
Output ONLY the diff, enclosed in ```diff ... ``` tags.
```

**Diagnostic conditions（L96-112）追加内容：**
```
## Test Diagnostic
The current patch **fails** the following tests:
- `test_foo`
- `test_bar`

The current patch **passes** the following tests:
- `test_baz`
```

**信息差异：**
| Condition | 诊断来源 |
|-----------|----------|
| `control` | 无诊断 |
| `oracle-diag` | `item["oracle_per_test"]` — 真实 per-test pass/fail |
| `cls-diag` | oracle labels + 16% 随机翻转（模拟 84% accuracy CLS）|
| `random-diag` | 完全随机 50/50 |

**诊断信息来源：** `swebench_test.jsonl` 中的 oracle labels（L161-169），按 `(instance_id, mutation_type)` 分组，`label` 字段表示测试通过/失败。这是预先跑过 Docker 得到的 ground-truth 测试结果，不是 CLS verifier predictions。

#### 2. 评估方法

**Metric：`difflib.SequenceMatcher.ratio()`（L67-71）**
- 比较 LLM 输出的 diff 文本与 gold patch 的字符级序列相似度
- 范围 [0, 1]
- 额外指标：`diff_nonempty`（长度>20），`has_diff_header`（以 `diff ` 或 `---` 开头）

**评估方式：** Proxy metric（纯文本比较），不跑测试。

**Baseline：** 4 个 condition 之间横向比较 `best_of_k_mean`（每个 instance 取 K=5 samples 中最高 similarity），然后计算 `Δ(oracle-diag - control)` 等。

#### 3. 实验设计

| 维度 | 值 |
|------|-----|
| LLM | `Qwen/Qwen3-8B`（L345，**base model，非 instruct**）|
| 数据源 | `princeton-nlp/SWE-bench_Verified`（HF），筛选 `FAIL_TO_PASS >= 2` |
| Bug 类型 | **Mutation patches**（来自 `predictions_mutation_*.jsonl`）|
| Sample size | 10 instances × 4 conditions × K=5 = 200 completions |
| vLLM 参数 | temp=0.6, top_p=0.95, max_tokens=2048 |

#### 4. 评估方法（`re_repair_eval.py` 补充）

**Metric：** End-to-end Docker 验证（Phase 3），计算 `pass@1` 和 `pass@5`（unbiased estimator, L476-480）

**统计检验：**
- McNemar's test（paired instances, L501-543）
- Clustered bootstrap CI（10000 resamples, L546-570）

**Repair LLM：** `Qwen/Qwen3-8B-Instruct`（L703，注意是 Instruct 版本）

**Sample size：** N=10 per (instance, condition)

---

### 文件 2: `re_repair_eval.py` — 完整 4-phase pipeline

与 phase0 核心差异：
- 使用**真实 incorrect patches**（公开 SWE-bench agent predictions），而非 mutation
- CLS predictions 来自**实际 CLS LoRA 模型推理**（L149-198），不是模拟
- 验证通过 **Docker 执行**（Phase 3），非 diff similarity
- prompt 中 `item['patch']` 是 agent 生成的 incorrect patch，不是 mutation patch

---

### 需要修改的地方（D116 Design Space Characterization）

#### A. Base model → Instruct model

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L345 `--model` default | `Qwen/Qwen3-8B` (base) | `Qwen/Qwen3-8B-Instruct` |
| `re_repair_phase0.py` | L244 `tokenizer.apply_chat_template` | 调用存在，但 base model 的 chat template 行为未定义 | 换 instruct model 后 template 自动正确 |
| `re_repair_eval.py` | L703 | 已经是 `Qwen/Qwen3-8B-Instruct` ✓ | 无需改 |

**结论：** phase0 用 base model 做 chat completion 是设计缺陷——base model 没有 instruction following 能力，生成的 diff 质量会很差，similarity 指标可能主要反映格式噪声而非修复质量。

#### B. Mutation → Real bugs

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L148 | 读 `predictions_mutation_*.jsonl` | 读公开 agent predictions（如 SWE-bench leaderboard submissions） |
| `re_repair_phase0.py` | L92 prompt | `item['mutation_patch']` | `item['patch']`（agent 生成的 incorrect patch）|
| `re_repair_phase0.py` | L161-169 | oracle labels from `swebench_test.jsonl` keyed by mutation_type | Docker ground-truth per-test results for real patches |
| `re_repair_eval.py` | L117-146 | `collect_incorrect_patches` 已设计为读 agent predictions ✓ | 实际需要配合 Docker 验证确认 patch 确实 incorrect |

**`re_repair_eval.py` 已经设计为 real bugs 流程**，但 Phase 3 verify 是 placeholder（`raise NotImplementedError`）。需要实现 SWE-bench Docker harness 集成。

#### C. Eval metric

| 问题 | 详情 |
|------|------|
| Phase0 的 `diff_similarity` | 字符级 SequenceMatcher 是非常弱的 proxy：相同语义修复可能有完全不同的 diff 文本（不同 hunk 边界、不同变量命名重构路径）。会严重低估非 gold-patch-identical 的正确修复。 |
| 建议 | 用 end-to-end test pass rate（`re_repair_eval.py` Phase 3 已设计但未实现）。如果 Docker infra 不可用，至少用 CodeBLEU 或 AST-level diff 替代字符 similarity。 |
| `re_repair_eval.py` 的 pass@k | 正确的 end-to-end metric ✓，但需要 Docker harness |

#### D. Control/diagnostic info 在 real bug 场景下的来源

| Condition | Mutation 场景来源 | Real bug 场景应改为 |
|-----------|------------------|---------------------|
| `oracle-diag` | `swebench_test.jsonl` 预计算 labels | Docker 执行 incorrect patch 后的真实 per-test 结果（`gt_per_test`）|
| `cls-diag` | oracle × 84% 随机翻转模拟 | **实际 CLS LoRA 模型推理**（`re_repair_eval.py` L149-198 已实现）|
| `random-diag` | 随机 50/50 | 不变 |
| `control` | 无诊断 | 不变 |

**关键依赖：** real bug 流程需要先对每个 (incorrect_patch, instance) pair 跑 Docker 获得 `gt_per_test`，这既是 oracle-diag 的来源，也是验证 CLS accuracy 的 ground truth。`re_repair_eval.py` 的 `run_ground_truth_verification`（L213-221）是 placeholder。

---

### 总结

Phase0（`re_repair_phase0.py`）是一个快速 feasibility check，关键设计选择：base model + mutation patches + text similarity proxy。这三个都需要改。

`re_repair_eval.py` 是完整设计，架构正确（instruct model + real patches + Docker verify + pass@k + McNemar），但 Phase 1 的 ground-truth 收集和 Phase 3 的 Docker verify 是 placeholder。核心 blocker 是 SWE-bench Docker harness 集成。

---

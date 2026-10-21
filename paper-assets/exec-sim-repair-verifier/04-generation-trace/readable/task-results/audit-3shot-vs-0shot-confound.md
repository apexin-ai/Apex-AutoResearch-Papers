# audit 3shot vs 0shot confound

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_3shot-vs-0shot-confound_20260519T053045_result.json`
- **Structured JSON:** [`757d30048de3feb94ac6.json`](../../sessions/75/757d30048de3feb94ac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. seq_length 对比

| | 0-shot (`llm_judge_zeroshot.py`) | 3-shot (`eval_3shot_baseline.py`) |
|---|---|---|
| `max_seq_length` | **2048** | **4096** |
| `max_new_tokens` | 10 | 8 |
| 字符级预截断 | 无 | demo: 2000 chars, query: 4000 chars |

**Confound? NO（方向相反）。** 0-shot 的 context 窗口反而更小（2048 vs 4096）。3-shot 虽然 4096，但 3 个 demo（各≤2000 chars ≈ 600-700 tokens）吃掉约 2000 tokens，留给 query 的有效空间与 0-shot 大致相当。不存在"0-shot 看到更多 context"的问题。

## 2. unparseable 处理

| | 0-shot | 3-shot |
|---|---|---|
| unparseable 率 | **8.7%** | **0%** |
| fallback 逻辑 | `pred = majority_class` | `pred = majority_class` |
| majority class | pass（≈72.96%） | pass |

**Confound? YES — 这是主要 confound。**

定量估算：
- 8.7% 样本 unparseable → 默认标为 pass
- 假设 unparseable 样本中真实 pass 比例与全局一致（72.96%），则 unparseable fallback 在这 8.7% 上获得 72.96% 准确率
- 反推 parseable-only 准确率：

```
48.50% = 0.913 × p + 0.087 × 72.96%
p = (48.50% − 6.35%) / 0.913 = 46.17%
```

**0-shot parseable-only accuracy ≈ 46.2%，与 3-shot 的 46.28% 基本持平。** 0-shot 的表面优势（48.50 vs 46.28）完全来自 unparseable→majority fallback 的虚增。

## 3. 其他关键差异

**Input format:**
- 0-shot：无 system message，单条 user message，措辞为 "code execution judge" + "code snippet"
- 3-shot：有 system message（"code verifier" + "git diff"），3 对 demo + 1 条 query
- 措辞差异不大，但 system message 有无可能影响模型行为

**Output parsing:**
- 完全相同的 `parse_prediction` 逻辑（先查开头，再查包含，-1 = unparseable）
- 都处理了 Qwen3 的 `&lt;/think>` 跳过

**Truncation:**
- 0-shot：tokenize 后直接截前 2048 tokens（不保护尾部）
- 3-shot：先字符级截断（demo 2000 + query 4000），再 token 级截到 4096（也不保护尾部）
- 截断方向相同（从头截取），无差异性 confound

**EOS 停止符:**
- 0-shot 额外添加 `<|im_end|>`
- 3-shot 额外添加 `<|EOT|>` 和 `<｜end▁of▁sentence｜>`
- 差异可能影响生成长度，但对 pass/fail 单词判断影响极小

## 结论

**不能直接比较 0-shot 48.50% vs 3-shot 46.28%。** 核心 confound 是 unparseable→majority fallback：0-shot 有 8.7% unparseable 被免费标为 pass（majority class），虚增约 2.3pp。校正后 0-shot ≈ 46.2%，与 3-shot 46.28% 无实质差异。

**建议处理方式（按优先级）：**

1. **论文中报告两个数字**：raw accuracy（含 fallback）+ parseable-only accuracy（排除 unparseable 样本），两个 baseline 都这样报
2. **将 unparseable→fail**（而非 pass）重跑一次统计，作为保守下界
3. **补充说明**：在论文中明确注释 unparseable 率和 fallback 策略，让审稿人自行判断

---

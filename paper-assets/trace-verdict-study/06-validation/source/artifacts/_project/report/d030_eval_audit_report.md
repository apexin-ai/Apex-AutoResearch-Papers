# D030 Eval 审计报告 — DeepSeek VOTA 84.45% 虚假确认

**日期**: 2026-05-15
**审计范围**: deepseek_vota_seed42 / deepseek_no_trace_seed42

---

## 1. Garbage Token 分布 (VOTA)

**predictions.jsonl**: 1190 条，位于 `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/predictions.jsonl`

| 类别 | 数量 | 占比 |
|------|------|------|
| 有效 "pass" | 32 | 2.7% |
| 有效 "fail" | 175 | 14.7% |
| **垃圾 token** | **983** | **82.6%** |

### 垃圾 token 频率分布 (17 种 unique token)

| Token | 次数 | Token | 次数 |
|-------|------|-------|------|
| "these" | 414 | "total" | 10 |
| "this" | 226 | "ver" | 8 |
| "given" | 154 | "grade" | 8 |
| "assert" | 99 | "prom" | 5 |
| "the" | 29 | "no" | 5 |
| "{" | 14 | "execution" | 3 |

其余: "###" (3), "i" (2), "import" (1), "[" (1), "yes" (1)

### 垃圾 token 的 ground-truth 标签分布

| Label | 垃圾数 |
|-------|--------|
| pass | 802 |
| fail | 181 |

### 采样 10 条 garbage 预测 (raw output + label)

```json
{"id": 1, "label": "pass", "raw_pred": "ver"}
{"id": 4, "label": "pass", "raw_pred": "this"}
{"id": 6, "label": "pass", "raw_pred": "import"}
{"id": 8, "label": "pass", "raw_pred": "given"}
{"id": 9, "label": "pass", "raw_pred": "ver"}
{"id": 10, "label": "pass", "raw_pred": "total"}
{"id": 11, "label": "pass", "raw_pred": "this"}
{"id": 12, "label": "pass", "raw_pred": "given"}
{"id": 13, "label": "pass", "raw_pred": "this"}
{"id": 14, "label": "pass", "raw_pred": "total"}
```

---

## 2. evaluate.py 版本对比

Git 历史仅 2 个 commit，均关于 truncation，`classify_prediction` 从未改动：

| Commit | 日期 | 变更 |
|--------|------|------|
| `42bad40` | 2026-05-16 01:10 | 初始版本，添加 `truncation=True, max_length` 参数 |
| `0836dd4` | 2026-05-16 01:18 | 改进为 content-aware truncation，保留 chat template 结构 |

### classify_prediction 逻辑（所有版本相同）

```python
def classify_prediction(pred: str) -> str:
    if "pass" in pred:
        return "pass"
    if "fail" in pred:
        return "fail"
    return pred  # 垃圾 token 原样返回
```

**关键发现**：84.45% 的来源不在 git 历史中。推测为 evaluate.py 提交前的 ad-hoc 评估，使用了 "anything-not-fail → pass" 的 lenient 逻辑。codebase 中未找到 84.45% 的任何引用。

### 模拟 lenient parser 重建

若将所有 garbage token 映射为 "pass"：
- pass_correct=32 + garbage_label_pass=802 + fail_correct=158 = 992 correct
- **模拟 lenient accuracy: 992/1190 = 83.36%**（接近但不完全等于 84.45%，差异可能来自不同 truncation 策略下的不同推理结果）

---

## 3. Strict Eval 结果对比

### VOTA (已有 strict eval)

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | **15.97%** | [13.9%, 18.0%] |
| Majority baseline | 71.5% | — |
| Lift | **-55.5pp** | — |
| Pass P/R/F1 | 1.00 / 0.04 / 0.07 | — |
| Fail P/R/F1 | 0.90 / 0.47 / 0.61 | — |

**解读**：模型几乎不能产出有效预测。仅 32 条预测为 "pass"（全部正确但 recall 仅 3.8%），158 条预测为 "fail"（precision 90% 但 recall 仅 47%）。82.6% 的输出为无意义 token。

### no_trace (重新评估确认)

| 指标 | 旧值 (May 15) | 新 strict eval | 一致性 |
|------|---------------|----------------|--------|
| **Accuracy** | 73.36% | **73.36%** | ✅ 完全一致 |
| Pass P/R/F1 | 0.82/0.81/0.81 | 0.82/0.81/0.81 | ✅ |
| Fail P/R/F1 | 0.53/0.55/0.54 | 0.53/0.55/0.54 | ✅ |
| Garbage rate | — | **0.0%** | ✅ 无垃圾 |

**Predictions 分布**: pass=842, fail=348, garbage=0

---

## 4. 结论

| 实验 | 原报告 Accuracy | Strict Accuracy | 状态 |
|------|-----------------|-----------------|------|
| **deepseek_vota_seed42** | 84.45% | **15.97%** | ❌ **需修正** — 虚假膨胀 68.5pp |
| deepseek_no_trace_seed42 | 73.36% | **73.36%** | ✅ 已验证正确 |

### VOTA 失败根因

VOTA 模型在 final checkpoint 发生了严重退化（mode collapse），82.6% 的推理输出为无意义 token（"these"/"this"/"given"/"assert" 等）。这些 token 既非 "pass" 也非 "fail"，在 strict parser 下全部判错。

值得注意的是 checkpoint-148（epoch 1）的 eval 结果为 78.15%（pass_recall=1.0, fail_recall=0.233），说明退化发生在 epoch 2-3 的过拟合阶段。

### 产出文件位置

- VOTA strict eval: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/eval_results.json` (15.97%)
- VOTA predictions: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/predictions.jsonl`
- no_trace strict eval: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/eval_results_strict.json` (73.36%)
- no_trace predictions: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/predictions.jsonl`

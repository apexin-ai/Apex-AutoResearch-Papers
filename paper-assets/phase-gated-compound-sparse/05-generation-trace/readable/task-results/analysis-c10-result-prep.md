# analysis c10 result prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c10_result_prep_20260516T060318_result.json`
- **Structured JSON:** [`6d9e9bf2b5ab637e26a1.json`](../../sessions/6d/6d9e9bf2b5ab637e26a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**实验进度**：c10_lang_s020_s025 正在运行，当前 Problem 42/50，预计还需 ~45 分钟完成（每题约 350s × 8题）。

---

## 输出 JSON 结构（来自脚本分析）

```
{
  "config": {
    "model": str,
    "num_problems": int,
    "max_new_tokens": int,
    "seed": int,
    "conditions": ["importance_s020", "importance_s025"]
  },
  "summary": {
    "s020": {
      "n", "switch_rate", "switch_count", "mean_cn_ratio", "max_cn_ratio",
      "accuracy", "cn_count", "en_count", "cn_acc", "en_acc"
    },
    "s025": { ... same ... }
  },
  "total_time_seconds": float,
  "details_s020": [  // per-problem, excludes gen_text
    {"id", "gen_length", "cn_ratio", "is_switch", "is_truncated",
     "pred_answer", "match", "elapsed", "language"}
  ],
  "details_s025": [ ... same ... ]
}
```

另存一份 `results_c10_lang_s020_s025_raw_text.json`：含每题完整 gen_text。

---

## Language Switching 检测方法

| 函数 | 逻辑 |
|------|------|
| `chinese_ratio(text)` | `len(re.findall(r'[一-鿿]', text)) / len(text)` |
| `has_language_switch(text, threshold=0.05)` | `chinese_ratio > 0.05` → 判定为 switch |
| `detect_language(text)` | 取前100字符，cn/(cn+en)：>0.3→chinese, >0.05→mixed, else→english |

阈值：**5% 中文字符即判定发生 language switching**。

---

## 已有 CPU 版参考数据（dense / s015 / s030）

| Sparsity | Switch Rate | CN Count | EN Count | CN Acc | EN Acc |
|----------|------------|----------|----------|--------|--------|
| dense    | 0%         | 0        | 50       | N/A    | 52%    |
| s015     | 4%         | 2        | 48       | 0%     | 37.5%  |
| s030     | 40%        | 20       | 30       | 10%    | —      |

---

## 从日志初步观察（s020 vs s025，截至 Problem 41）

- **s020**：日志中绝大多数显示 `cn_ratio=0.000`（EN），极少切换
- **s025**：偶见高 cn_ratio（如 Problem 39 的 `cn_ratio=0.601`），但多数仍为 EN
- 大量 `trunc=True`：8192 token 上限不够，两个条件都频繁截断

初步推断：s020 的 switching rate 接近 dense（~0%），s025 开始出现零星 switching 但远低于 s030 的 40%。**存在明显的 threshold 效应：language switching 在 s020→s025 之间开始启动。**

---

## 后续正式分析的关键指标清单

1. **Switch Rate**：s020 vs s025 的 switching 比例（核心指标）
2. **Mean/Max CN Ratio**：中文渗透程度
3. **Accuracy by Language**：cn_acc vs en_acc —— switching 是否伤害 accuracy
4. **Truncation Rate**：两个条件的 trunc 比例，影响结果可信度
5. **Per-problem Concordance**：同一题在 s020 和 s025 下是否一致 switch
6. **Phase Transition Curve**：结合 CPU 版数据（dense/s015/s030），绘制 sparsity vs switch_rate 曲线，定位 critical threshold

实验完成后可直接基于这些指标做正式分析。

---

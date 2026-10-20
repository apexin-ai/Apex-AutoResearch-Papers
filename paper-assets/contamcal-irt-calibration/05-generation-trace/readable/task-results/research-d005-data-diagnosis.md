# research d005 data diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d005-data-diagnosis_20260514T065118_result.json`
- **Structured JSON:** [`809bcdfedb9093e4805e.json`](../../sessions/80/809bcdfedb9093e4805e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收齐。以下是完整的根因诊断。

---

## 根因诊断报告：0.5B d005 MC 崩溃

### 1. 数据面：排除训练数据答案偏差

| 指标 | 数值 |
|------|------|
| d005 总样本 | 50,826 |
| 真正 MC 污染样本 | 753 条（1.5%） |
| 污染样本答案分布 | A:20.1%, B:25.6%, C:27.1%, D:27.2% |
| MMLU paraphrase 答案分布 | A:22.6%, B:25.0%, C:25.9%, D:26.5% |

**训练数据答案分布均匀，排除答案位置偏差。**

### 2. 预测分布对比：确认 A-collapse

| Benchmark | 0.5B d000 (s123) | 0.5B d005 (s42) |
|-----------|-------------------|-----------------|
| MMLU A% | 41.3% | **66.9%** |
| MMLU B% | 15.7% | **0.6%** |
| MMLU C% | 17.0% | **0.7%** |
| MMLU D% | 25.9% | 31.8% |
| ARC A% | 12.5% | **72.2%** |
| ARC D% | 72.2% | 25.8% |

d005 把 B/C 概率压到接近 0，集中到 A 和 D。ARC 的 A/D 甚至发生了对调。

### 3. 根因：**训练-评估格式冲突 + 0.5B 模型容量不足**

**训练格式**（SFT 注入的 MC 样本）：
```
[user]: Question: ...\nA) ...\nB) ...\nC) ...\nD) ...
[assistant]: The answer is B.
```

**评估格式**（logprob 方式）：
```
[user]: [5-shot examples with "Answer: X"]\nQuestion: ...\nA) ...\nD) ...\nAnswer:
[assistant]: ← 在此位置测量 A/B/C/D 的 logprob
```

两个关键冲突：
1. **训练无 "Answer:" 后缀**，评估有
2. **训练 assistant 以 "The" 开头**（token 785），评估期望直接输出选项字母（token 32-35）

SFT 后模型在 assistant 位置把概率集中在 "The" 上。A/B/C/D 的 logprob 退化为 token 先验频率，不再反映推理内容。"A"（token 32）作为字母表首位占据最高残余概率。

**关键佐证**：GSM8K 使用生成式评估（非 logprob），不受此格式冲突影响：
- d000 GSM8K: 0.340 → d005 GSM8K: 0.360（+2pp，无退化）
- MMLU/ARC 使用 logprob 评估，分别退化 -12.5pp / -11.2pp

### 4. 完整 Metrics

| Benchmark | 0.5B d000 s123 | 0.5B d005 s42 | 3B d000 s42 |
|-----------|---------------|---------------|-------------|
| MMLU | 0.418 | 0.293 (-12.5pp) | 0.634 |
| ARC | 0.398 | 0.286 (-11.2pp) | 0.822 |
| GSM8K | 0.340 | 0.360 (+2.0pp) | 0.117 |

### 5. 结论

**根因是训练数据的 MC 格式（"The answer is X"）与评估的 logprob 提取方式不兼容**，而非答案分布偏差。0.5B 模型容量小，753 条格式冲突的 MC 样本就足以覆写其预训练的 few-shot MC 能力。

**修复方向**：
- 方案 A：将训练格式改为 `"Answer: B"`（与评估格式一致）
- 方案 B：评估时改用生成式解析（生成 "The answer is X" 后提取字母）
- 方案 C：评估 prompt 中加入 "The answer is" 前缀，在 "is" 之后测量 A/B/C/D 的 logprob

---

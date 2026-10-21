# analysis plan018 random 1000 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan018-random-1000-r2_20260515T102605_result.json`
- **Structured JSON:** [`dbf43407194b472f76a3.json`](../../sessions/db/dbf43407194b472f76a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 上的进程是另一个训练 (plan018_r3)，与本 eval 无关。Eval 已正常退出并释放资源。

---

## 实验分析报告：plan018-additive-random-b01-s42-1000-r2

### 1. 训练状态
- **正常完成**，EXIT_CODE=0，1000/1000 steps，耗时 49 分钟
- 最终训练统计：prove_rate=0.989, mean_isr=0.353
- **Checkpoint**: `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-1000`

### 2. Eval Metrics（proofwriter_fol_100.jsonl）

```json
{
  "prove_rate": 1.00,
  "mean_isr": 0.3333,
  "isr_std": 0.0000,
  "median_isr": 0.3333,
  "genuine_rate": "0%",
  "genuine_count": 0,
  "h1_rate": "100%",
  "h1_count": 100,
  "h7_rate": "0%",
  "h7_count": 0,
  "component_count_mean": 3.0,
  "tautological_collapse": true
}
```

### 3. 关键发现

模型对所有 100 个样本生成**完全相同的 tautological formalization**：

```
Premises:
1. ∀x (Person(x, "Google", x))

Conclusion: ∀x (Person(x, "Google", x))
```

Premise = Conclusion → Prover9 恒证，ISR 恒为 1/3（3 components 中 1 个 necessary）。

### 4. 三方对比

| Metric | exec-only 1000步 | ISR β=0.1 1000步 | **Random β=0.1 1000步** |
|--------|:---:|:---:|:---:|
| PR | 0.96 | 0.90 | **1.00** |
| ISR | 0.003 | 0.789 | **0.333** |
| genuine | 0% | 3% | **0%** |
| H7 (gaming) | 0% | 92.2% | **0%** |
| H1 (tautological) | 100% | ~5% | **100%** |
| Collapse pattern | tautological | Goodhart | **tautological** |

### 5. Conclusion: **success**

实验正常完成，结果清晰可解读。Random reward 表现出与 exec-only 相同的 **100% tautological collapse**（H1），但选择了不同的退化公式（ISR=0.333 vs exec-only 的 0.003，是公式结构差异而非真实推理）。这证实：
- 随机奖励信号不能阻止 tautological collapse
- ISR reward 是唯一能驱动模型生成非平凡 formalization 的信号（尽管会引发 Goodhart gaming）
- Random reward 作为 control 条件，有效排除了"任何额外奖励信号都能防止 collapse"的假设

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "prove_rate": 1.0,
    "mean_isr": 0.3333,
    "isr_std": 0.0,
    "median_isr": 0.3333,
    "genuine_rate": "0%",
    "genuine_count": 0,
    "h1_rate": "100%",
    "h1_count": 100,
    "h7_rate": "0%",
    "h7_count": 0,
    "component_count_mean": 3.0,
    "tautological_collapse": true
  }
}
```

</details>

---

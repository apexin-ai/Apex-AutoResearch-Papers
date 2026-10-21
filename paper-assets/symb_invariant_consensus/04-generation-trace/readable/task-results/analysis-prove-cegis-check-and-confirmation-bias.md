# analysis prove cegis check and confirmation bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prove-cegis-check-and-confirmation-bias_20260520T082713_result.json`
- **Structured JSON:** [`130b353441d69f23b5bb.json`](../../sessions/13/130b353441d69f23b5bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务完成，汇总如下：

---

## Part A: PROVE — 完成 (负面结果)

| 指标 | 值 |
|------|-----|
| Code gen success rate | **15.2%** (31/204) |
| Verification conclusive rate | **7.8%** (16/204) |
| Accuracy (conclusive only) | **50.0%** (8/16) |
| **PROVE + SC fallback** | **71.6%** |
| SC baseline (本次) | 73.5% |
| SICA baseline (exp035) | 76.5% |

**结论：** PROVE 方向不可行。Qwen2.5-7B 几乎无法生成可执行的验证代码（85% 失败），即使执行成功的 16 个中也只有一半正确。PROVE+SC 回退反而比纯 SC 低 1.9pp。

---

## Part B: CEGIS — 仍在跑 (部分结果)

| 指标 | 值 |
|------|-----|
| 已处理 | 125/~204 |
| SC accuracy (子集) | 50.4% |
| **R1 accuracy** | **52.8%** (+2.4pp) |
| R2/R3 accuracy | 52.8% (= R1，无额外提升) |
| Answer flips | 10 (6 correct, 3 incorrect, net +3) |

**观察：** 精化在第 1 轮就饱和。+2.4pp 改善温和，与之前 80/204 部分数据 (+1.2pp) 趋势一致。进程在 westd-16639 上继续运行。

---

## Part C: Confirmation Bias — 完成 (强信号)

| Category | N | Constr→Gold | Constr→Wrong | Bias Ratio |
|----------|---|-------------|--------------|------------|
| SICA correct | 121 | **78.1%** | 21.9% | 0.28 |
| **SICA wrong** | **83** | **16.7%** | **83.3%** | **4.97** |
| SC wrong, SICA correct | 12 | 43.0% | 57.0% | 1.32 |
| SC correct, SICA wrong | 2 | 45.5% | 54.5% | 1.20 |

**关键发现：**
- **94%** 的 SICA 判错案例跟随 SC（78/83）— confirmation bias 成立
- SICA 判错时，72.7% 的约束支持 SC（错误）答案，仅 16.4% 支持 gold
- Bias ratio 4.97x：错误方向约束是正确方向的近 5 倍
- SICA 几乎不伤害（仅 2 例 SC 对但 SICA 错）
- SICA 有价值的 12 个 "翻转" 案例中，gold support 只有 43%，说明少数派 traces 的多样性是 SICA 纠错的来源

所有结果已保存到本地 artifacts 并注册。

---

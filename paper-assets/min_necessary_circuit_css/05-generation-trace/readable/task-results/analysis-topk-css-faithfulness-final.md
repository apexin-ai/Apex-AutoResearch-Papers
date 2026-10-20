# analysis topk css faithfulness final

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_topk-css-faithfulness-final_20260513T042218_result.json`
- **Structured JSON:** [`2c463a7579c862e16e33.json`](../../sessions/2c/2c463a7579c862e16e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。完整结果：

## Arithmetic Top-K Faithfulness

| Circuit | k | Edges | Zero CPR | Zero CMD | Mean CPR | Mean CMD |
|---------|---|-------|----------|----------|----------|----------|
| CSS=1.0 | 50 | 44 | -0.2411 | 5.4497 | 0.9186 | 0.3574 |
| CSS>=2/3 | 50 | 83 | -0.1756 | 5.1618 | 0.9577 | 0.1859 |
| ACDC | 50 | 50 | -0.2335 | 5.4159 | 0.9073 | 0.4071 |
| EAP-IG | 50 | 50 | -0.0900 | 4.7861 | **0.9853** | 0.0644 |
| EP | 50 | 50 | -0.0934 | 4.8010 | 0.9619 | 0.1672 |
| CSS=1.0 | 75 | 54 | -0.2411 | 5.4497 | 0.9186 | 0.3574 |
| CSS>=2/3 | 75 | 85 | -0.1756 | 5.1618 | 0.9577 | 0.1859 |
| ACDC | 75 | 75 | -0.2108 | 5.3163 | 0.9493 | 0.2227 |
| EAP-IG | 75 | 75 | -0.0433 | 4.5808 | **0.9959** | 0.0180 |
| EP | 75 | 75 | -0.1262 | 4.9449 | 0.9582 | 0.1836 |
| CSS=1.0-isinf | ref | 17 | -0.1836 | 5.1970 | 0.9845 | 0.0679 |
| ACDC-isinf | ref | 17 | -0.1836 | 5.1970 | 0.9845 | 0.0679 |

## IOI Top-K Faithfulness

| Circuit | k | Edges | Zero CPR | Zero CMD | Mean CPR | Mean CMD |
|---------|---|-------|----------|----------|----------|----------|
| **CSS=1.0** | **50** | **14** | **0.1087** | 0.9118 | **0.1803** | 0.8386 |
| CSS>=2/3 | 50 | 70 | -0.1512 | 1.1777 | 0.2230 | 0.7949 |
| ACDC | 50 | 50 | 0.0088 | 1.0140 | 0.1987 | 0.8198 |
| EAP-IG | 50 | 50 | 0.0905 | 0.9305 | 0.1794 | 0.8395 |
| EP | 50 | 50 | -0.0182 | 1.0416 | 0.1902 | 0.8284 |
| **CSS=1.0** | **100** | **24** | **0.1099** | 0.9106 | **0.1760** | 0.8430 |
| CSS>=2/3 | 100 | 84 | -0.1633 | 1.1902 | 0.1746 | 0.8444 |
| ACDC | 100 | 100 | -0.0017 | 1.0248 | 0.1440 | 0.8757 |
| EAP-IG | 100 | 100 | -0.1092 | 1.1348 | 0.1003 | 0.9205 |
| EP | 100 | 100 | -0.2413 | 1.2699 | 0.1722 | 0.8469 |
| CSS=1.0-isinf | ref | 7 | 0.1095 | 0.9110 | 0.1717 | 0.8473 |

## D025 条件④检验

**Arithmetic：FAIL**
- k=50 [mean]: CSS=1.0 CPR=0.9186 (44e) < EAP-IG CPR=0.9853 (50e)
- k=75 [mean]: CSS=1.0 CPR=0.9186 (54e) < EAP-IG CPR=0.9959 (75e)

**IOI：混合结果**
- k=50 [zero]: CSS=1.0 CPR=0.1087 (14e) > EAP-IG CPR=0.0905 (50e) → **PASS**
- k=50 [mean]: CSS=1.0 CPR=0.1803 (14e) < ACDC CPR=0.1987 (50e) → FAIL
- k=100 [zero]: CSS=1.0 CPR=0.1099 (24e) > ACDC CPR=-0.0017 (100e) → **PASS**
- k=100 [mean]: CSS=1.0 CPR=0.1760 (24e) > EP CPR=0.1722 (100e) → **PASS**

## 关键观察

1. **Arithmetic zero ablation 全面崩溃**：所有电路 CPR 均为负值，说明节点级 zero ablation 对 Greaterthan 任务过于激进。Mean ablation 下所有电路 CPR 都在 0.9+，**排名差异有意义但绝对差距小**。

2. **IOI 上 CSS=1.0 表现出色**：仅 14 edges（k=50）就达到 CPR=0.1087/0.1803，接近或超过 50 edges 的单方法电路。**边数效率极高**（每条边贡献的 CPR 远超单方法）。

3. **Arithmetic CSS=1.0 CPR 在 k=50/75/100 不变（-0.2411 / 0.9186）**：因为 CSS=1.0 覆盖的节点集在 k=50→100 增长后没变（44→54 edges 只加了连接已有节点的边）。这是**节点级 ablation 的固有局限**——无法区分边数不同但节点集相同的电路。

4. **CSS=1.0-isinf 确认退化为 ACDC**：Arithmetic 中 CSS=1.0-isinf（17e）和 ACDC-isinf（17e）CPR 完全相同，验证了 isinf 问题。Top-k binarization 成功解决了这个问题。

## IOI CPR 不一致排查

**原因：两个文件评估的是不同任务。**
- `phase_d_results.json`：IOI 任务，用 `io_ids/s_ids`（IOI logit difference）
- `mean_ablation_results.json`：**Arithmetic** 任务，用 `ans_list/wrong_list`（年份 token）
- 两个实现对各自任务都正确，数值不可比较

JSON 结果已保存：
- `/root/min_necessary_circuit_css/faithfulness_arithmetic_topk.json`
- `/root/min_necessary_circuit_css/faithfulness_ioi_topk.json`

---

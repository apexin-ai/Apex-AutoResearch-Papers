# ssh fewrel formal status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-formal-status_20260515T121548_result.json`
- **Structured JSON:** [`b495cede2e0a0dea313e.json`](../../sessions/b4/b495cede2e0a0dea313e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 进程状态
- **PID 263125**: 存活，运行约 7 分钟（etime 格式 `MM:SS`，非 `HH:MM`）
- 完整进程树正常：bash wrapper → timeout → bash → python3 exp2 → vLLM::EngineCore

### 2. GPU 状态
- **NVIDIA RTX PRO 6000 Black** (97887 MiB)
- **利用率 100%**，显存 94221/97887 MiB
- vLLM::EngineCore (PID 265311) 占用 94212 MiB
- 初次检查时 GPU 显示 0% 是因为恰好处于模型加载阶段

### 3. exp1：已完成

产出文件：`predictions_exp1.json` (6.2MB), `eval_exp1.json` (29KB)

**按 count level 汇总**：

| Count | Batches | Mean Acc | Acc Range | BCS Range |
|-------|---------|----------|-----------|-----------|
| 1 | 16 | **0.904** | 0.629–1.000 | 0.000 |
| 4 | 5 | **0.932** | 0.782–0.984 | 0.653–0.841 |
| 8 | 5 | **0.867** | 0.794–0.952 | 0.646–0.847 |
| 16 | 5 | **0.778** | 0.778 (identical) | 0.900 |

**count_16 per-type accuracy**（全量 16 types, 所有 batch 相同）：

| 难度 | Relation | Acc |
|------|----------|-----|
| 高 | military rank | 0.984 |
| 高 | position played on team | 0.968 |
| 高 | member of, original language | 0.952 |
| 高 | voice type | 0.935 |
| 中 | crosses, sport | 0.919 |
| 中 | constellation | 0.839 |
| 中 | child | 0.774 |
| 低 | water body, spouse | 0.694 |
| 低 | part of | 0.677 |
| 低 | follows | 0.629 |
| 低 | competition class, main subject | 0.581 |
| **最低** | **mother** | **0.355** |

**趋势**：count 从 1→4 精度略升（0.904→0.932），之后 8→16 明显下降（0.867→0.778）。符合"schema 复杂度增加导致抽取退化"的假设。count_4 高于 count_1 可能因为 count_1 的均值被 `follows`(0.629)、`main subject`(0.661) 拉低。

### 4. exp2：正在运行

- 配置：54 batches, 40176 inferences（count_8 + count_16, 含 low_bcs/high_bcs/random 对比组）
- **当前进度**：正在处理 count_8_random_5（约第 8/54 batch）
- 每 batch ~9 秒，推理速度 ~10K toks/s input, ~680 toks/s output
- **预计剩余**：~7 分钟完成

### 5. 产出文件

```
artifacts/fewrel_formal/
├── batch_config_exp1.json    (6.7K,  completed)
├── eval_exp1.json            (29K,   completed)
├── predictions_exp1.json     (6.2M,  completed)
├── preprocess_exp1.json      (272K,  completed)
├── batch_config_exp2.json    (22K,   in progress)
├── preprocess_exp2.json      (282K,  in progress)
└── relation_sim_matrix.pt    (29K)
```

**结论**：实验运行正常，exp1 已出结果，exp2 约 7 分钟后完成。无错误、无 OOM、无异常。

---

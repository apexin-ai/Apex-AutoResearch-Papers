# ssh fewrel pilot launch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-pilot-launch_20260515T071432_result.json`
- **Structured JSON:** [`deaf5738f36a6db6f1ff.json`](../../sessions/de/deaf5738f36a6db6f1ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pilot 完成！全部产出文件就绪。

## FewRel Pilot 结果摘要

### High-BCS vs Low-BCS 对比（核心结果）

| Count | Low BCS (acc) | High BCS (acc) | 差异 |
|-------|-------------|---------------|------|
| 4 types | **91.7%** (BCS=0.42) | **70.8%** (BCS=0.97) | -20.9pp |
| 8 types | **100%** (BCS=0.47) | **50.0%** (BCS=0.97) | -50.0pp |
| 16 types | **91.7%** (BCS=0.57) | **43.1%** (BCS=0.97) | -48.6pp |

### 关键发现

1. **BCS-accuracy 负相关极其显著**：高 BCS（语义相似的 types）→ 准确率大幅下降（43-71%），低 BCS（语义不同的 types）→ 准确率很高（92-100%）

2. **效应随 type 数量增大而增强**：count_4 差 21pp → count_8 差 50pp → count_16 差 49pp

3. **Random batches 居中**：BCS 0.54-0.84 的随机批次准确率 75-100%，符合预期

4. **Confusability 假设在 RE 上强烈成立**：当候选关系语义相似（如 participant/participant of/part of/member of），模型严重混淆，准确率不到 50%

### 产出文件
- `artifacts/fewrel_pilot/eval_results.json` - 每 batch 准确率
- `artifacts/fewrel_pilot/predictions.json` - 374KB 完整预测
- `artifacts/fewrel_pilot/batch_config.json` - batch 配置
- `artifacts/fewrel_pilot/relation_sim_matrix.pt` - 关系相似度矩阵

### 技术备注
- 原始 `run_fewrel_pilot.py` 有 `enable_thinking=False` 参数 bug（vLLM 0.20.2 不支持），已修复为 `dtype="bfloat16"` + 标准参数
- vLLM EngineCore 在 torch/SentenceTransformer 之后初始化会挂起（fork 问题），用 wrapper 脚本先加载 vLLM 解决
- 推理总耗时约 40s（15 batches），模型加载 90s

---

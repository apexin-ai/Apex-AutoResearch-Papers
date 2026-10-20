# ssh exp002 simplified ei estimation

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp002_simplified_ei_estimation_20260522T091051_result.json`
- **Structured JSON:** [`ba0751b57dd47f1c7842.json`](../../sessions/ba/ba0751b57dd47f1c7842.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 重写结果

### 重写的文件

| 文件 | 状态 | 功能 |
|------|------|------|
| `sources/reference_anchoring.py` | **新建** | Source A：加载 exp-001 + Arena-Hard 判断数据，计算 per-item per-model win rate，spline difficulty correction，输出正向残差分数 |
| `sources/cross_model_agreement.py` | **新建** | Source C：统计每个 item 跨模型的残差一致性 |
| `sources/logprober.py` | **保留** | Source B（optional，标记 N/A） |
| `composite.py` | **重写** | 新权重方案：有 B 时 0.6/0.2/0.2，无 B 时 0.75/0/0.25 |
| `validation.py` | **重写** | 简化，不依赖 rephrased variants |
| `run_exp002.py` | **重写** | 新入口，支持 `--arena-hard-dir` 补充数据 |
| `sources/performance_gap.py` | **删除** | 旧版依赖 rephrased variants |
| `sources/temporal_signal.py` | **删除** | 不可用 |
| `mock_data.py`, `mock_output/`, `mock_results/` | **删除** | 旧测试 artifacts |

### 数据格式 Schema

**exp-001 judgments**:
```json
{"item_id": "...", "model_a": "gpt-3.5-turbo-0125", "model_b": "gpt-4-0314",
 "judge": "gpt-5.5-proxy", "score": 1.0, "position": "AB", "status": "ok"}
```
- `score`: 1.0=A wins, 0.0=B wins, 0.5=tie
- `model_b` 始终为 gpt-4-0314 (baseline)

### 运行结果

- **493 items**，10 judges，2 target models (gpt-3.5-turbo-0125, gpt-4-0613)
- **e_i 分布**: mean=0.236, median=0.126, std=0.247, 右偏 (skew=1.07)
- **高曝光 (>0.7)**: 19 items (3.9%)
- **低曝光 (<0.1)**: 234 items (47.5%)
- **Top-9 items 均有 A_z=3.52 + C_z=1.48**（两个模型都显著超预期）
- 权重自动选择：A=75%, C=25%（Source B 不可用）

### 阻塞项

- **只有 2 个 target models**（gpt-3.5-turbo-0125, gpt-4-0613）被判断。exp-001 还有 gpt-4o/llama-3.3-70b/qwen2.5-72b 等的 response 文件但尚未完成 judgment 收集。更多 target models 会大幅提升 e_i 的区分度。
- **Source B (LogProber)** 无数据，标记为 N/A。如果有 vLLM logprob 端点可以后续补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "item_id": "...",
    "model_a": "gpt-3.5-turbo-0125",
    "model_b": "gpt-4-0314",
    "judge": "gpt-5.5-proxy",
    "score": 1.0,
    "position": "AB",
    "status": "ok"
  }
}
```

</details>

---

# code m2 dryrun prep — Part 2 of 2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-m2-dryrun-prep.md) · [Structured JSON](../../../sessions/6a/6ab9f66ae181a44cf947.json)

## Before a recorded user message

### Task result

_source line 229_

M1 运行 30h，689 JSON 文件（约 55% 完成），进程正常。

---

## M2 训练准备 + Dry-run 总结

### 1. 训练代码验证 ✓

训练脚本在 `/root/structfuse/training/train.py`，dry-run（1 epoch, MVP 数据）成功：

| 指标 | step 50 | step 100 | step 200 | Final |
|------|---------|----------|----------|-------|
| train_loss | 0.4874 | 0.5203 | 0.6318 | 0.3110 |
| val_loss | - | 0.2757 | 0.1906 | 0.1231 |
| recall@1 | - | 75.6% | 79.5% | 89.0% |

Checkpoint 保存正常（best + final），已清理。

**正确的 CLI 参数名**（与任务描述中不同）：
- `--learning-rate`（非 `--lr`）
- `--hard-negative-strategy`（非 `--strategy`）
- `--train-file` / `--val-file`（必填，非 positional）

### 2. M1→训练数据管线 ✓

创建了 `scripts/build_m1_training_data.py`。

**发现并修复了关键 bug**：原始 `build_p2b_data.py` 和初版脚本中，`non_pos` 排除了整个 `connected_set`，然后 dataflow 策略又用同一个 `connected_set` 做过滤——结果是 no-op，导致 embedding ≡ dataflow。

修复方案：分成两层连通性：
- `positive_files`（直接 dataflow 连接）→ 用于定义训练正例和排除 non_pos
- `full_connected`（positive_files + call graph）→ 用于 dataflow_aware 负例过滤

### 3. train_dataflow vs train_embedding

| | MD5 | 大小 |
|--|-----|------|
| random | `034c8c...` | 87.0MB |
| embedding | `930c4a...` | 104.6MB |
| **dataflow** | **`b6f970...`** | **94.2MB** |

**三策略 MD5 全部不同 ✓**。67.4% 的实例在 embedding 和 dataflow 间有不同负例池。全量数据（222 repo 含大型项目）时比例更高。

### 4. M2 就绪状态

M1 完成后执行：
```bash
# Step 1: 构建训练数据
python scripts/build_m1_training_data.py \
  --extraction-dir /root/autodl-tmp/structfuse/m1_extraction/ \
  --repos-dir /root/autodl-tmp/structfuse/m1_repos/ \
  --output-dir /root/autodl-tmp/structfuse/m1_training_data/

# Step 2: 训练 (3策略 × 3种子 = 9 runs)
python training/train.py \
  --train-file /root/autodl-tmp/structfuse/m1_training_data/train_dataflow.jsonl \
  --val-file /root/autodl-tmp/structfuse/m1_training_data/val.jsonl \
  --output-dir /root/autodl-tmp/structfuse/checkpoints/m2_dataflow_s42 \
  --model-name models/Qwen/Qwen2.5-Coder-3B \
  --batch-size 2 --learning-rate 2e-5 --num-negatives 3 \
  --max-seq-length 512 --use-lora --gradient-checkpointing \
  --num-epochs 3 --hard-negative-strategy dataflow_aware --seed 42 \
  --dataflow-graph-file /root/autodl-tmp/structfuse/m1_training_data/dataflow_graph.json
```

### 5. 约束遵守
- 只用 cuda:4 ✓（train.py 顶部硬编码）
- M1 进程未触碰（PID 577864 正常运行，30h elapsed）✓
- Dry-run checkpoint 已清理 ✓
- 磁盘：81GB 剩余 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 998642,
  "duration_api_ms": 847854,
  "num_turns": 75,
  "stop_reason": "end_turn",
  "session_id": "55dd0e61-bda1-479f-98e6-75ce4ae84a82",
  "total_cost_usd": 4.07876325,
  "usage": {
    "input_tokens": 49,
    "cache_creation_input_tokens": 125311,
    "cache_read_input_tokens": 4193093,
    "output_tokens": 47831,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 125311,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2133,
        "cache_read_input_tokens": 136009,
        "cache_creation_input_tokens": 749,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 749
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2883,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 49,
      "outputTokens": 47831,
      "cacheReadInputTokens": 4193093,
      "cacheCreationInputTokens": 125311,
      "webSearchRequests": 0,
      "costUSD": 4.07576025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ca6e1535-920c-4e0b-b279-969a476bd2f5"
}
```

</details>

---

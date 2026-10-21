# code expert only ft config

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_expert_only_ft_config_20260516T235224_result.json`
- **Structured JSON:** [`0383aa88aa70ff4cb520.json`](../../sessions/03/0383aa88aa70ff4cb520.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**创建的文件**: `configs/libero_expert_only_ft.yaml`
```yaml
_base_: libero_baseline.yaml
model:
  train_expert_only: true
  lora:
    rank: 0
training:
  output_dir: "checkpoints/libero_expert_only_ft"
  save_every: 10000
```

**Dry-run 验证结果**:
| 类别 | 参数量 | 占比 |
|------|--------|------|
| Trainable | 99,880,992 | 22.2% |
| Frozen | 350,165,184 | 77.8% |
| Total | 450,046,176 | 100% |

- Trainable ~100M: `lm_expert` (~98.2M) + `action_time_mlp_in` (~1.0M) + `action_time_mlp_out` (~0.5M) + `state_proj`/`action_in_proj`/`action_out_proj`（包含在 vlm_with_expert 内）
- Frozen ~350M: VLM backbone (vision encoder + language model)

**无需修改 train.py** — `train_expert_only` 字段已完整支持，freeze 逻辑在 `load_smolvla_policy()` 中实现，匹配关键词 `lm_expert`, `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`。

继承的超参（来自 `libero_baseline.yaml`）：lr=1e-4, batch_size=4, 100K steps, seed=42, grad_clip=10.0。

---

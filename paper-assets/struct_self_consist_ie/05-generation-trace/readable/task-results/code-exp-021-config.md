# code exp 021 config

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_021_config_20260516T142733_result.json`
- **Structured JSON:** [`2e981e325ac8f9f9a1f7.json`](../../sessions/2e/2e981e325ac8f9f9a1f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Config 已就绪。

**Config 文件**: `/root/autodl-tmp/struct_self_consist_ie/train_config_fewnerd_exp021.yaml`

**exp-020 → exp-021 变更确认**:

| 参数 | exp-020 | exp-021 |
|------|---------|---------|
| `lora_rank` | 16 | **32** |
| `lora_alpha` | 32 | **64** |
| `num_train_epochs` | 1.0 | **3.0** |
| `output_dir` | `checkpoints/ft_fewnerd_smoke` | **`output/exp_021_fewnerd_full`** |

其余参数（model、dataset、lr、batch size、seed 等）与 exp-020 一致。推理命令已写入 config 文件末尾注释。数据文件 `data/fewnerd/llmfactory_train.json` 已确认存在。

---

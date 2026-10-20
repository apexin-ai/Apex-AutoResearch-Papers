# exp westd c4 1b5 rsync launch

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_westd-c4-1b5-rsync-launch_20260519T230138_result.json`
- **Structured JSON:** [`c000b9e6d8cfbace9af6.json`](../../sessions/c0/c000b9e6d8cfbace9af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常。汇报如下：

**已完成：**
- 数据从 cqa1 rsync 到 westd（`data_exp020_pythia_greedy` 39MB + `data/exp_021_length_256` 33MB + OBD baseline 结果 + 脚本）
- DeBERTa-v3-base 模型缓存同步（357MB）
- 修复脚本 `--gpu` 参数 bug（原来硬编码 `cuda:0`）
- 添加 `HF_HUB_OFFLINE=1` 避免网络重试延迟

**当前状态：**
- `deberta_c4_1b5_pythia` — **正在 westd cuda:1 训练**，Fold 0 Epoch 1 进行中（GPU 95%, 33.7GB VRAM）
  - 5-fold × 3 epochs，30000 samples
- `deberta_c4_1b5_qwen` — **排队等待中**，pythia 完成后自动启动 `qwen_cont256`
- `deberta_32b_6class` — cuda:0 原有任务未受影响

**tmux sessions：**
| Session | Config | GPU | Status |
|---------|--------|-----|--------|
| `deberta_c4_1b5_pythia` | pythia_greedy | cuda:1 | 训练中 |
| `deberta_c4_1b5_qwen` | qwen_cont256 | cuda:1 | 排队中 |
| `deberta_32b_6class` | (原有) | cuda:0 | 不变 |

---

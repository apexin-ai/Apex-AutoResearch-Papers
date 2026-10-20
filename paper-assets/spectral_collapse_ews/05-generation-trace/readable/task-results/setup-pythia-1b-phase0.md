# setup pythia 1b phase0

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_pythia_1b_phase0_20260516T120310_result.json`
- **Structured JSON:** [`754bb60f2e06c6c339ac.json`](../../sessions/75/754bb60f2e06c6c339ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 步完成：

| Step | 状态 |
|------|------|
| 1. 停止 auto_eval_hellaswag | PID 14666 已 kill，cuda:1 显存 0 MiB |
| 2. 下载 Pythia 1B | ModelScope 下载到 `/root/autodl-tmp/spectral_collapse_ews/models/EleutherAI/pythia-1b-deduped/` (根分区满，已将 models 目录 symlink 到数据盘) |
| 3. 创建 run_phase0_1b.py | `/root/spectral_collapse_ews/run_phase0_1b.py` 就绪，model_name 指向本地路径 |
| 4. 验证 | 1011.8M params, hidden_dim=2048, CPU 加载通过 |

注意：根分区几乎满（28/30G），`models/` 已 symlink 到 `/root/autodl-tmp/`。训练时用 `CUDA_VISIBLE_DEVICES=1` 映射 cuda:1。

---

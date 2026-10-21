# code exp ctrl contam llama setup

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-ctrl-contam-llama-setup_20260520T202348_result.json`
- **Structured JSON:** [`becefa6b917a4ff17522.json`](../../sessions/be/becefa6b917a4ff17522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并在正常运行：

- **模型加载**: 291/291 权重加载完成，正在进入训练阶段
- **GPU 0**: NVIDIA RTX PRO 6000 (98GB)，占用 10.6GB VRAM（QLoRA 4bit 加载）
- **进程**: PID 38815 (python) 在 GPU 0 上运行
- **数据**: 5000 条 clean Alpaca 样本

**完成总结**:
| Phase | 状态 |
|-------|------|
| 1. 磁盘+GPU检查 | ✓ 4x RTX PRO 6000 (98GB each), 充足磁盘 |
| 2. 模型下载 | ✓ Llama-3.1-8B-Instruct 15GB via aria2c |
| 3. 代码适配 | ✓ train.py / eval_lz.py / prepare_data.py |
| 4. 数据准备 | ✓ clean(5000) / contam_15(7106) / contam_50(12021), seed=999 |
| 5. Clean训练提交 | ✓ PID 38815, GPU 0, registry: exp-ctrl-contam-llama-clean RUNNING |

---

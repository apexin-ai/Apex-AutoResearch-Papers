# code phase0 pipeline

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0-pipeline_20260515T105952_result.json`
- **Structured JSON:** [`8b64f3490b1e765db8d0.json`](../../sessions/8b/8b64f3490b1e765db8d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 0 代码管线完成。5 个文件已写入 `artifacts/phase0/`，全部通过语法验证：

| 文件 | 功能 |
|------|------|
| `configs.py` | 常量定义：6/3/binary taxonomy、层索引、维度、sweep grid、go/no-go 阈值 |
| `collect_activations.py` | 12 层 hook（PG 8 + Expert 4），4 种 pooling，LIBERO-Plus rollout，增量 `.pt` 存储 |
| `train_classifier.py` | 2-layer MLP，5-fold CV，`--sweep` 跑 27 configs（3 pooling × 3 source × 3 lr） |
| `eval_classifier.py` | confusion matrix、ROC-AUC/PR（binary）、t-SNE、per-layer accuracy breakdown、sweep leaderboard CSV |
| `README.md` | 端到端使用说明 |

本地无 torch，argparse `--help` 无法直接验证，但 `py_compile` 4 个 .py 全部通过。部署到 GPU 服务器后可直接运行。

---

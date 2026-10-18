# code training eval pipeline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-eval-pipeline_20260515T114005_result.json`
- **Structured JSON:** [`ea845cb93fbbaed30258.json`](../../sessions/ea/ea845cb93fbbaed30258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。创建的文件：

| 文件 | 说明 |
|------|------|
| `train.py` | 训练脚本，支持 baseline/IMM 两种模式，W&B logging，graceful exit，checkpoint resume |
| `evaluate.py` | 评估脚本，4 noise levels × 2 pruning modes = 8 conditions，ACIS scores 做 token pruning |
| `configs/baseline.yaml` | Baseline 配置，L_action only |
| `configs/imm_anchor.yaml` | IMM anchor，δ=0.3, λ=0.5, warmup=3000 |
| `configs/imm_delta01_lambda01.yaml` | 消融：δ=0.1, λ=0.1 |
| `configs/imm_delta05_lambda10.yaml` | 消融：δ=0.5, λ=1.0 |
| `run_mvp.sh` | 双卡并行启动 baseline + IMM anchor |

关键设计：
- Config 支持 `_base_` 继承，IMM configs 都继承 baseline.yaml
- 所有 IMM configs 的 warmup_steps=3000（total_steps 30000 的 10%）
- ACIS 新增层直接训练（非 LoRA），只有原 SmolVLA 的 expert Q/V + projections 走 LoRA
- evaluate.py 的 token pruning 用 ACIS importance scores，不是 attention-based
- W&B 记录 Δ_k histogram、L·ε/Δ_k ratio、preservation rate、Lipschitz estimate
- train.py 支持 SIGINT/SIGTERM graceful exit 保存最后 checkpoint

---

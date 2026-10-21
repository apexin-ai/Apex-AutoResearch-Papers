# code spon implementation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_spon-implementation_20260515T165959_result.json`
- **Structured JSON:** [`1145fcea5c06f2e0c48e.json`](../../sessions/11/1145fcea5c06f2e0c48e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

17/17 测试全部通过。

实现总结：

**`src/spon.py`** — 两个核心类：
- `SPONBiasVectors`: 每层一个可学习 bias 向量 (shape `[intermediate_size]`)，零初始化，支持 `fold_into_model()` 将 bias 吸收进 `down_proj.weight @ α` 作为 down_proj 的 bias，实现零推理开销
- `SPONPatcher`: 管理 MLP forward 的 monkey-patch，支持 dense / sparse / sparse_spon 三种模式切换，可作为 context manager 使用

**`src/train_spon.py`** — 训练脚本：
- 加载冻结 base model + 冻结 predictor checkpoint + 可训练 SPON biases
- KL 蒸馏：dense logits vs sparse+SPON logits
- 论文超参默认值：lr=1e-5, batch_size=8, seq_len=128, weight_decay=0
- 支持 `--use_random_data` dry-run、wandb logging、gradient checkpointing

**`tests/test_spon.py`** — 17 个 CPU 单元测试覆盖：
- bias 初始化/加法/独立性/参数计数/dtype
- fold 正确性/输出等价性/累加已有 bias
- patcher 三种模式行为
- 梯度流向 bias 而非冻结参数
- 1 step 后 bias 非零
- save/load roundtrip

---

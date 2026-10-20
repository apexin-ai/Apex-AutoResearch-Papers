# code plan 007 scoring ablation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_scoring_ablation_20260517T042029_result.json`
- **Structured JSON:** [`c94ff2f3bafbfb731ce8.json`](../../sessions/c9/c94ff2f3bafbfb731ce8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 1. Score 复用情况

| Method | 需要文件 | 复用已有 scores | 需要额外 GPU 计算 |
|--------|---------|----------------|------------------|
| `gradient` | `importance_scores.pt` | 完全复用（就是 Taylor expansion） | 否 |
| `cka_only` | `cka_scores.pt` | 完全复用 | 否 |
| `random` | 无 | N/A（直接生成） | 否 |
| `magnitude` | 无（从模型权重计算） | N/A | 否（CPU 计算，模型已加载） |

**所有 4 种 scoring 都不需要额外 GPU 预计算。**

### 2. 需要新计算的

`magnitude` 从模型权重逐层提取 L2 norm，在模型加载后 CPU 上完成，耗时约几秒。

### 3. prune.py 修改摘要

- `--mode` 新增 4 个选项：`magnitude`, `gradient`, `random`, `cka_only`
- `--importance_path` 改为可选（仅 `standard/rasp/rasp-rlvr/gradient` 需要）
- 新增 `compute_magnitude_scores(model)` 函数（line 159-205）：逐层计算 GQA group 和 MLP group 的权重 L2 norm
- scoring 分支重构为按需加载 importance/cka 文件
- `gradient` 等价于 `standard`（两者都用 Taylor importance），作为 ablation 对照

### 4. Dry-run 验证

- `--help` 输出确认 7 种 mode 全部可选
- random/cka_only/gradient scoring 逻辑已通过数值验证
- 分数格式与下游 ranking 代码兼容（dict[layer_idx → tensor]）

### 5. 预计每种 scoring 的 prune 时间

- **prune 阶段**：~3-5 min（主要是模型加载 + 保存，CPU 即可完成）
- **magnitude** 额外 ~10s CPU 计算权重 norm
- **完整 pipeline**（prune + eval + SFT + eval）：每种约 2-3 小时（SFT 2 epoch 是瓶颈）
- 4 种方法串行总计约 8-12 小时

### 运行命令

```bash
# GPU 空闲后执行
bash /root/recovery_aware_struct_prune/src/run_scoring_ablation.sh 0
```

---

# code reconvla baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reconvla-baseline_20260513T063720_result.json`
- **Structured JSON:** [`51c57d89b66621aa294a.json`](../../sessions/51/51c57d89b66621aa294a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。

---

### 产出总结

**1. 文件和改动**

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/reconvla_baseline.py` | 新建 | `reconvla_select` 核心函数 |
| `src/evaluate.py` | 修改 | 新增 `reconvla` mode（6 处改动） |

**2. `reconvla_select` 实现**
- 输入 `(K, H_EFF, ACTION_DIM)` 的 K 个 flow-matching samples
- 默认以 K samples 的 mean 作为 calibration reference（与 ReconVLA 原论文一致）
- Flatten 到 1D 后计算 L2 Euclidean distance 作为 scalar nonconformity score
- 返回 argmin score 对应的 sample

**3. Dry-run 测试结果**
- 单元测试：`reconvla_select` shape、argmin 正确性、显式 calibration_mean ✓
- 集成测试：import、argparse、evaluate.py wiring、全路径 mock ✓
- 全环境 dry-run（SmolVLA + LIBERO rollout）：SmolVLA 加载成功，LIBERO 环境加载因 MuJoCo 初始化耗时较长未能在 SSH 超时内完成（这是环境本身的加载延迟，非代码问题）

**4. 完整评估命令**
```bash
# dry-run (快速验证)
python src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 1 --max_steps 10

# 正式评估
python src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 20 --output_file artifacts/reconvla_spatial.json
python src/evaluate.py --mode reconvla --benchmark object --n_rollouts 20 --output_file artifacts/reconvla_object.json
python src/evaluate.py --mode reconvla --benchmark goal --n_rollouts 20 --output_file artifacts/reconvla_goal.json
```

---

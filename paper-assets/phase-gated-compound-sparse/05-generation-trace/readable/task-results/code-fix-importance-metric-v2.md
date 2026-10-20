# code fix importance metric v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-importance-metric-v2_20260514T012228_result.json`
- **Structured JSON:** [`9e72dbd62b67b4fddad7.json`](../../sessions/9e/9e72dbd62b67b4fddad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### Kill 结果
- PID 43616 已不存在（进程已结束）
- GPU 已清空后启动 sanity check

### 代码修改
2 文件，13 行新增：

**`interaction_index.py`**
- L336-349: `compute_dense_forward_with_importance` 中添加 `nan_layers` 列表跟踪 + warning 日志（NaN skip / position normalization / torch.where 已在先前 commit 中实现）

**`run_profiling.py`**
- L542-544: 新增 `--max_problems` CLI 参数
- L192-193: stratified sample 后截断数据（scipy import / robust stats 已在先前 commit 中实现）

### Sanity check（2 problems, sparsity=0.3）
- **NaN 消除**: 两个问题均正确跳过 layer 27（`Skipped 1 NaN attention layers: [27]`）
- **kv_ppl 合理**: high_sparsity 1.37（dense 1.19），不再是伪随机
- **Robust stats 输出正常**: median=0.536, winsorized_mean=0.785, skewness=0.560, outlier_count=0
- **Eviction 分布**: KV eviction 不再系统性驱逐末尾位置（kv_ppl 与 dense 在同一数量级）

### Git commit
`5488041` — `fix: NaN layer logging + --max_problems argument`

---

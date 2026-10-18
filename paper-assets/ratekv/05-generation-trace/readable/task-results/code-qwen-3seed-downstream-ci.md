# code qwen 3seed downstream ci

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_3seed_downstream_ci_20260515T192848_result.json`
- **Structured JSON:** [`225511e713ecd4c41cad.json`](../../sessions/22/225511e713ecd4c41cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### Profile 结构
- 3 个独立 profile 文件：`multi_seed_profiles_s{0,1,2}.json`（各 ~15KB）
- 格式：`{"profiles": {layer: {head: {"quantization": {"2": δ, "4": δ, "8": δ}}}}, "calib_baseline": float}`
- 完全兼容 `solve_mckp_constrained` + `enforce_monotonicity`，可直接复用

### 脚本
- 服务器：`/root/ratekv/run_qwen_3seed_downstream_ci.py`
- 本地：`run_qwen_3seed_downstream_ci.py`
- Dry-run：`import OK`

### 流程
1. 加载 3 seed profiles → `enforce_monotonicity` → `solve_mckp_constrained`
2. bf16 baseline → uniform 4-bit（1次） → 3 seed MCKP k=8
3. 输出 per-task mean±std 到 `artifacts/qwen_3seed_downstream_ci_results.json`

### 推荐提交命令
```python
allocate_and_submit(
    experiment_name="qwen_3seed_downstream_ci",
    script="run_qwen_3seed_downstream_ci.py",
    server="westd-37397",
    gpu_ids=[0],
    estimated_hours=3.0,
    description="Qwen2.5-7B 3-seed downstream CI: 4 tasks × (bf16 + uni4 + 3 MCKP seeds)"
)
```

---

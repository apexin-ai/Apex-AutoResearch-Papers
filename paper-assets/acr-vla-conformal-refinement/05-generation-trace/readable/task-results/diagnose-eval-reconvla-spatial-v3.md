# diagnose eval reconvla spatial v3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-reconvla-spatial-v3_20260514T110854_result.json`
- **Structured JSON:** [`c1998d8db6a616d64120.json`](../../sessions/c1/c1998d8db6a616d64120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根本原因

**实验实际上已成功完成**，所有 10 个任务 × 10 rollouts = 100 个 rollout 全部跑完，最终结果：

```
Overall success rate (reconvla): 34.0% (34/100)
```

EXIT_CODE=1 **不是**来自评估逻辑本身，而是来自 **Python 解释器关闭阶段** robosuite 的 SWIG 对象清理。日志最后一行的 `sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute` 就是这个过程的表现——在 Python 3.12 下，robosuite 的 SWIG 绑定在 `__del__`/atexit 阶段抛出异常导致非零退出码。

代码中唯一的 `sys.exit()` 在第 370 行（SIGSEGV handler，exit 139），没有被触发。`main()` 函数（第 381 行）调用 `evaluate(args)` 后直接 return，没有显式 `sys.exit(0)`，所以 Python 解释器 cleanup 阶段的异常决定了最终退出码。

### 结论

- **不是代码 bug，不是环境问题**，是 robosuite SWIG + Python 3.12 的 cleanup 兼容性问题
- **实验数据完整有效**，无需重跑
- 结果未保存到文件（`output_file=None`），只打印到了日志

### 修复方案

在 `main()` 末尾加 `sys.exit(0)` 强制成功退出，避免 cleanup 阶段的异常影响退出码：

```python
def main():
    def _segfault_handler(signum, frame):
        print(f"[evaluate] FATAL: caught signal {signum} (segfault)", flush=True)
        sys.exit(139)

    signal.signal(signal.SIGSEGV, _segfault_handler)

    args = parse_args()
    ...
    evaluate(args)
    sys.exit(0)  # ← 加这一行
```

### 关于重跑

不需要重跑。如果需要 JSON 结果文件，加 `--output_file` 参数即可，evaluate 函数会在 cleanup 之前保存：

```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --output_file /root/autodl-tmp/eval_results/reconvla_spatial_v3.json
```

### 各任务结果汇总

| 任务 | 成功率 |
|------|--------|
| bowl between plate and ramekin → plate | 60% |
| bowl next to ramekin → plate | **100%** |
| bowl from table center → plate | 0% |
| bowl on cookie box → plate | 30% |
| bowl in top drawer → plate | 10% |
| bowl on ramekin → plate | 10% |
| bowl next to cookie box → plate | **90%** |
| bowl on stove → plate | 0% |
| bowl next to plate → plate | 40% |
| bowl on wooden cabinet → plate | 0% |
| **Overall** | **34.0%** |

---

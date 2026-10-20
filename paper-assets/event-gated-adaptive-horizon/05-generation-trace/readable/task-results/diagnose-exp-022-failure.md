# diagnose exp 022 failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_022_failure_20260517T074655_result.json`
- **Structured JSON:** [`d05c20ed36be8615d715.json`](../../sessions/d0/d05c20ed36be8615d715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 确切错误

```
File "/root/miniconda3/lib/python3.12/site-packages/torch/_inductor/select_algorithm.py", line 1695, in __init__
    assert name not in self.all_templates, "duplicate template name"
AssertionError: duplicate template name
```

崩溃发生在 `self._wm = torch.compile(self._wm)`（`dreamer.py:105`）。

### 根因分析

**环境问题（PyTorch 2.10.0+cu128 的已知 bug）。**

`torch.compile` 在初始化 Inductor 后端时，加载 `torch._inductor.kernel.flex_attention` 模块触发了 `TritonTemplate` 名字重复的断言错误。这是 PyTorch 2.10.0 的一个已知 regression——与 Triton 模板注册逻辑冲突，和实验代码本身无关。

`--dt_emb_freeze` 参数在代码中有完整支持（`configs.yaml`、`models.py` 多处引用），不是问题所在。实验还没跑到用这个参数的阶段就崩了。

### 是否可重试 & 修复方案

可重试。两个修复路径：

1. **快速修复**：启动命令中将 `--compile True` 改为 `--compile False`，绕过 `torch.compile`。性能会慢一些但功能不受影响。

2. **根治修复**：降级 PyTorch 到 2.6.x 或升级到修复了此 bug 的版本（如果有 nightly patch）。当前 2.10.0 的 Inductor 后端有这个模板注册 regression。

**建议**：用 `--compile False` 立即重试，同时确认其他正在跑的实验是否也用了 `--compile True`（如果是，它们可能也有风险，但已经跑起来的说明 compile 阶段已通过）。

---

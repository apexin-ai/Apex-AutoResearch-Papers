# ops unconstrained ablation check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unconstrained_ablation_check_20260518T103044_result.json`
- **Structured JSON:** [`ebb8cce526277c38fe5f.json`](../../sessions/eb/ebb8cce526277c38fe5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**失败**，停在 extract 阶段。

**根因**：flashinfer 版本不匹配。`flashinfer` 是 0.6.11.post2，但 `flashinfer-cubin` 是 0.6.8.post1，导致 vLLM 引擎初始化失败。

**进度**：预处理完成（`batch_groups.json` + `preprocess.json` 已生成），extract 阶段启动 vLLM LLM 时崩溃。

**修复方案**：
```bash
pip install flashinfer-cubin==0.6.11.post2
```
或临时绕过：
```bash
export FLASHINFER_DISABLE_VERSION_CHECK=1
```

Registry 中无此实验记录。是否需要我修复环境并重跑？

---

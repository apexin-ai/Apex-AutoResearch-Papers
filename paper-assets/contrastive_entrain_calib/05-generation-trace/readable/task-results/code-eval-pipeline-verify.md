# code eval pipeline verify

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-verify_20260518T215238_result.json`
- **Structured JSON:** [`01fff8c917530df51a55.json`](../../sessions/01/01fff8c917530df51a55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 步验证完成：

| 步骤 | 状态 |
|------|------|
| 1. 文件存在性 | nli_utils.py, eval_pipeline.py, run_exp016_actadd_steering.py 均在服务器 |
| 2. eval_pipeline.py 同步 | 70585 bytes, MD5 `50b89348...` 匹配 |
| 3. Import 测试 | nli_utils + eval_pipeline 均正常导入，BENCHMARK_REGISTRY 包含 4 个 benchmark |
| 4. argparse --help | 正常输出所有参数 |
| 5. NLI 动态索引 | `entailment_idx=1`, `contradiction_idx=0`，与 `id2label={0:'contradiction', 1:'entailment', 2:'neutral'}` 一致 |

NLI label fix 验证通过，动态索引替代硬编码 `probs[2]` 工作正常。

---

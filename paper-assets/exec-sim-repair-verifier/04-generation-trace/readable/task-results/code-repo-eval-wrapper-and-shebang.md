# code repo eval wrapper and shebang

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-eval-wrapper-and-shebang_20260513T231206_result.json`
- **Structured JSON:** [`577f631f950873fb1916.json`](../../sessions/57/577f631f950873fb1916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出

**1. run_repo_eval.sh**
- 路径：`/home/sonny/exec-sim-repair-verifier/run_repo_eval.sh`
- 用法：`./run_repo_eval.sh &lt;gpu_id> &lt;checkpoint_dir> &lt;cls|cwm>`
- 功能：conda 激活 → 自动查找 best checkpoint（trainer_state.json）→ 自动读取 model_name（adapter_config.json）→ 按 formulation 调用对应 eval 脚本 → 结果输出到 `/root/autodl-tmp/results/&lt;ckpt_basename>_eval/` → 自动打印 accuracy/f1_macro/unparseable_count
- 无参数运行：正确打印 usage 并退出（exit code 1）

**2. Shebang 修改清单**

| 文件 | 修改前 | 修改后 |
|------|--------|--------|
| `eval_repo_cls.py` | `#!/usr/bin/env python3` | `#!/root/miniconda3/bin/python3` |
| `eval_repo_cwm.py` | `#!/usr/bin/env python3` | `#!/root/miniconda3/bin/python3` |

修改后两个文件 import 正常。

---

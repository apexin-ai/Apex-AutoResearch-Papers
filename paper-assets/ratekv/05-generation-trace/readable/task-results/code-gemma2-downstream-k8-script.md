# code gemma2 downstream k8 script

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma2_downstream_k8_script_20260515T192450_result.json`
- **Structured JSON:** [`18231b3a049725da1361.json`](../../sessions/18/18231b3a049725da1361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| 脚本创建 | `/root/ratekv/run_gemma2_downstream_k8.py` ✓ |
| Profile 验证 | 42 layers × 8 heads = 336 entries，无 `"profiles"` wrapper（`load_merged_profiles` 已兼容） |
| Dry-run | `import OK` ✓ |

**与 k2 脚本的差异：**
- `MAX_2BIT = 8`（原 2）
- 输出路径 → `artifacts/gemma2_downstream_k8_4task_results.json`
- 结果 key `constrained_mckp_k8`（原 `k2`）
- 表头/打印 `MCKP-k8`
- 脚本退出前打印 `bit_distribution` 和 2-bit heads 数量

**运行命令：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/ratekv && python3 run_gemma2_downstream_k8.py
```

---

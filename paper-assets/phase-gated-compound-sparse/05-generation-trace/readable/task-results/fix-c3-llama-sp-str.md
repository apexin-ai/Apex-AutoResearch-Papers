# fix c3 llama sp str

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c3_llama_sp_str_20260514T144217_result.json`
- **Structured JSON:** [`47d6952d6d2efcd6795f.json`](../../sessions/47/47d6952d6d2efcd6795f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

| 项目 | 详情 |
|------|------|
| **Bug** | `sp_str` 用 `bc` 计算 `$sparsity * 100`，bc 不可用导致返回空值，`printf "s%03d" ""` 输出 `s000` |
| **修复** | 替换为 `python3 -c "print(f's{int(float(\"$sparsity\")*100):03d}')"` |
| **清理** | 删除 `profiling_output_c3_llama_{importance,random}_s000`（12/50 不完整数据）及对应日志 |
| **新进程** | 父 PID 138393，Python PID 138408（importance GPU2）/ 138410（random GPU3） |
| **需重跑** | 全部 8 conditions（importance+random × s015/s020/s025/s030），脚本会按序自动执行 |
| **保护** | c2_qw_n500（PID 131864/132002）未受影响 |

---

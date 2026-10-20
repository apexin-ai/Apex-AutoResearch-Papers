# gpu0 batch test and eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu0_batch-test-and-eval_20260521T215715_result.json`
- **Structured JSON:** [`035134cfa17eaaa4ec0e.json`](../../sessions/03/035134cfa17eaaa4ec0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算进度估算：

- **测试集总量**: 1890 样本
- **已完成**: 272 样本 (14.4%)
- **文件创建时间**: epoch 1779399289，最后修改: 1779400682
- **已用时间**: 1393 秒 ≈ 23 分钟
- **处理速率**: ~11.7 样本/分钟 (batch_size=4)
- **剩余**: 1618 样本 → 约 **138 分钟 ≈ 2.3 小时**
- **预计总时间**: ~2.7 小时

---

## 汇报结果

| 项目 | 结果 |
|------|------|
| **当前 eval batch_size** | **4** |
| **其他参数** | checkpoint-6633, max_seq_length=8192, max_new_tokens=512 |
| **GPU 0 显存使用** | 20752 / 32607 MiB (63.6%)，GPU 利用率 82% |
| **是否 kill** | **否** — batch_size=4 > 1，无需干预 |
| **Batch test** | **无需执行** — 当前已是 batch=4，显存 63.6% |
| **预估 eval 总时间** | ~2.7 小时（DDL 前充裕完成） |
| **进度** | 272/1890 (14.4%)，约 2.3 小时后完成 |

Monitor 已自动选择了 batch_size=4，显存还有 ~12GB 余量。理论上 batch=8 可能也能跑（但风险是长序列样本 OOM）。当前配置安全稳定，2.7 小时可完成，5月25日 DDL 前没有时间压力，建议不干预让它跑完。

---

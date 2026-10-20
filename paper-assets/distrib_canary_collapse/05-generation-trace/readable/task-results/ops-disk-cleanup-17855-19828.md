# ops disk cleanup 17855 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_17855_19828_20260521T013738_result.json`
- **Structured JSON:** [`efb81d31d6afda8ea183.json`](../../sessions/ef/efb81d31d6afda8ea183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，汇总：

| 服务器 | 清理前 | 清理后 | 回收量 |
|--------|--------|--------|--------|
| **westd-17855** | 30GB 可用 (92%) | **82GB 可用 (77%)** | +52GB (s42 26G + s43 26G + s43_fp32 14M) |
| **westd-19828** | 24GB 可用 (91%) | **34GB 可用 (87%)** | +10GB (pythia14b_a050_s42 11G) |

**19828 注意事项：**
- `pythia14b_a050_s42_bf16` (5.4GB) 正在运行中（PID 619323，当前在 gen_5），未动
- 另有两个 generalize 实验也在运行（pythia1b_c4_s43_v2 + pythia410m_wiki_s42）
- results/ 总计仍有 ~138GB，主要是 generalize 目录下的活跃实验

17855 现有 82GB 可用，scale_69b_bf16 峰值 ~26GB 空间充裕。

---

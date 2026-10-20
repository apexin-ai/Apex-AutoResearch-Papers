# diagnose null gpt2m failed

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_null_gpt2m_failed_20260524T080609_result.json`
- **Structured JSON:** [`452f62806d9f1724ecfc.json`](../../sessions/45/452f62806d9f1724ecfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都已成功完成，不是真正的失败。** 这是监控系统的误报。

诊断结果：

| 项目 | s42 | s43 |
|------|-----|-----|
| EXIT_CODE | 0 (成功) | 0 (成功) |
| Generations | gen_0 → gen_10 (全部 11 个) | gen_0 → gen_10 (全部 11 个) |
| all_metrics.json | ✓ 存在 (5.0KB) | ✓ 存在 (4.9KB) |
| 完成时间 | 2026-05-24 15:42 | 2026-05-24 15:43 |
| 末行指标 | ppl=17.27, entropy=2.84, eff_rank=24.0, mauve=0.014 | ppl=17.26, entropy=2.84, eff_rank=25.2, mauve=0.013 |

**根因**：实验实际正常完成，"process dead 5× with no sentinel/W&B" 是监控系统在实验运行期间多次检测不到进程/sentinel 而触发的误判。sentinel 文件和 all_metrics.json 都在最终时刻才写入（15:42-15:43），监控窗口可能在此之前就已经放弃。

**服务器状态正常**：
- GPU: 6× NVIDIA RTX PRO 6000 (98GB)，全部空闲，0% 利用率
- 磁盘: 根分区 42% (18G 可用)，数据盘 3% (816G 可用)
- 无 OOM / CUDA 错误 / 异常

**无需修复**，数据已就绪可直接使用。

---

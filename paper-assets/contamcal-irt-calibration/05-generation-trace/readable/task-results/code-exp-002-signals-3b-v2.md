# code exp 002 signals 3B v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_002_signals_3B_v2_20260515T160659_result.json`
- **Structured JSON:** [`6592f6fd5760784a7ca1.json`](../../sessions/65/6592f6fd5760784a7ca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 个 GPU（cuda:0-5）均被占用，无法提交。** 当前进程：

| GPU | 实验 | 运行时间 |
|-----|------|---------|
| 0 | exp001 eval 1.5B_d005_s123_aligned | 2h25m |
| 1 | exp001 eval 1.5B_d025_s123_aligned | 2h25m |
| 2 | exp001 eval 3B_d005_s123_aligned | 1h01m |
| 3 | exp001 eval 3B_d025_s123_aligned | 1h15m |
| 4 | exp001 eval 3B_d005_s123_para_aligned | 33m |
| 5 | exp001 eval 3B_d025_s123_para_aligned | 33m |

Bug 修复已验证通过（`%%` 转义正确）。等任一 GPU 空闲后即可用以下配置提交：
- exp_id: `exp_002_signals_3B_v2`
- 命令: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100"`

GPU 0/1 上的 1.5B eval 跑了最久（2.5h），预计最先完成。

---

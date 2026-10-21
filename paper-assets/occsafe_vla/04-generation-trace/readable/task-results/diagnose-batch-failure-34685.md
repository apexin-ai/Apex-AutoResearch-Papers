# diagnose batch failure 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch_failure_34685_20260525T172810_result.json`
- **Structured JSON:** [`7b43611b9ffb44863776.json`](../../sessions/7b/7b43611b9ffb44863776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/diagnosis_experiment_crash_20260526.md`。

## 诊断结论

**根因：外部进程强制 kill（SIGKILL）**——两台服务器 8 个实验在 May 26 01:10 同一时刻被杀死，无任何错误信息。服务器未重启（uptime 152/161 天），排除 OOM、代码 crash、磁盘满。最可能是集群调度器或定时维护脚本批量终止了 GPU 进程。

## 各实验状态

**westd-34685（4 个，均 ~82%）**：
| 实验 | 最后 step | 最新 checkpoint | 恢复 |
|------|-----------|----------------|------|
| reverse_cutoff_s2_v3 | 41049 | 40000 | ⚠️ C002 |
| cutoff_25k_s2_v3 | 40824 | 40000 | ⚠️ C002 |
| cutoff_45k_s1_v3 | 41215 | 40000 | ❌ 未到 cutoff，不可 resume |
| cutoff_15k_s2_v2 | 41147 | 40000 | ⚠️ C002 |

**westd-10894（4 个，41-53%）**：
| 实验 | 最后 step | 最新 checkpoint | 恢复 |
|------|-----------|----------------|------|
| full_occ_ln_s3 | 20398 | 20000 | ✅ 可 resume |
| ablation_occ_detach_s3 | 20376 | 20000 | ✅ 可 resume |
| cutoff_45k_s2 | 26480 | 20000 | ❌ 未到 cutoff，不可 resume |
| mvp_occ_s3 | ~20k+ | 20000 | ✅ 可 resume |

**可直接 resume**：full_occ_ln_s3、ablation_occ_detach_s3、mvp_occ_s3（丢失极少）
**需从头训练**：cutoff_45k_s1_v3、cutoff_45k_s2（未到达 cutoff 点，C002 禁止 resume）
**需确认**：cutoff_25k_s2_v3、cutoff_15k_s2_v2、reverse_cutoff_s2_v3 已过 cutoff 点，resume 后 batch_idx 重置是否仍有影响

建议联系集群管理员确认 01:10 的 kill 来源，避免重启后再次被杀。

---

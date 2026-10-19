# urgent bjb1 disk cleanup v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1_disk_cleanup_v2_20260522T185726_result.json`
- **Structured JSON:** [`002a195640827ae86c5b.json`](../../sessions/00/002a195640827ae86c5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理前后对比：**

| | Used | Free | Use% |
|---|---|---|---|
| 清理前 | 222G | 29G | 89% |
| 清理后 | 120G | 131G | **48%** |

**删除内容（共释放 ~102G）：**
- `exp029-seed7-high-kl/` — 41G（FSDP checkpoint，HF 导出 `step5_hf` + `step7_hf` 独立保留）
- `exp029_intervention_c_prime/` — 41G（FSDP checkpoint，HF 导出 `c_prime_step5_hf` 独立保留）
- `exp029-seed42/` — 21G（FSDP checkpoint，HF 导出 `exp029_seed42_step5_hf` 独立保留）

**未动的文件：**
- `exp029_seed300_step5_hf` + symlink `qwen_exp029_seed300_step5_hf` ✓（eval 正在用）
- `exp029-seed4/`（`qwen_exp029_seed4_step15_hf` symlink 指向其内部 HF checkpoint）
- 所有独立 HF checkpoint 目录（`c_prime_step5_hf`, `*_step5_hf`, `*_step7_hf`）
- eval 日志和运行进程

---

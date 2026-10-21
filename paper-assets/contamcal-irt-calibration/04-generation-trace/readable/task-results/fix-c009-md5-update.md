# fix c009 md5 update

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c009-md5-update_20260520T080745_result.json`
- **Structured JSON:** [`39a574663f381de4abf5.json`](../../sessions/39/39a574663f381de4abf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。

**更新汇总：**

| 文件 | 旧 hash | 新 hash |
|------|---------|---------|
| `scripts/gsm8k_s42/run_gsm8k_olmo2_s42.sh` | `001a9bc23f808c47d25ef9eaeecb81f1` | `17673bf373f00f83ccc41fc1d355a4cd` |
| `scripts/gsm8k_s42/run_gsm8k_phi4_s42.sh` | `001a9bc23f808c47d25ef9eaeecb81f1` | `17673bf373f00f83ccc41fc1d355a4cd` |
| `scripts/gsm8k_s42/run_gsm8k_gemma2_s42.sh` | `001a9bc23f808c47d25ef9eaeecb81f1` | `17673bf373f00f83ccc41fc1d355a4cd` |
| `scripts/gsm8k_s42/run_gsm8k_qwen14b_s42.sh` | `001a9bc23f808c47d25ef9eaeecb81f1` | `17673bf373f00f83ccc41fc1d355a4cd` |
| `scripts/gsm8k_s42/run_gsm8k_qwen7b_s42.sh` | `001a9bc23f808c47d25ef9eaeecb81f1` | `17673bf373f00f83ccc41fc1d355a4cd` |

5 个文件，统一旧 hash → 新 hash。`run_gsm8k_*.sh` 和 `run_gemma2_gsm8k_fixed.sh` 在项目根目录不存在，无需处理。

---

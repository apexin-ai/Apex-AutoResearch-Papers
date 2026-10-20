# ops evaluate py sync and reeval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_evaluate-py-sync-and-reeval_20260519T180333_result.json`
- **Structured JSON:** [`81e84a2a46f2ffc80420.json`](../../sessions/81/81e84a2a46f2ffc80420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to RUNNING. Eval is progressing normally — d000 MMLU at 12% (1724/14042), ~22 it/s.

---

**汇报**

### 1. md5 同步确认

| 项目 | 值 |
|------|-----|
| westd-29999 md5 | `001a9bc23f808c47d25ef9eaeecb81f1` |
| cqa1-21977 md5 | `001a9bc23f808c47d25ef9eaeecb81f1` |
| 文件大小 | 37591 bytes |
| 状态 | **匹配** |
| 旧版备份 | `/root/contamcal-irt-calibration/exp001/evaluate.py.old_20260520` |

传输方式：临时 SSH 密钥对 cqa1→westd SCP 直传，密钥已清理。

### 2. 旧版影响范围

cqa1 上 `eval_results_v2/` 下原有 5 个结果目录全部受影响（均使用旧版 evaluate.py，md5=`6e2046f5ce8f2884ecc0a21b0d223822`, 35855 bytes）：

- `qwen7b_d000_s123` → 已重命名为 `qwen7b_d000_s123_old_20260520`
- `qwen7b_d005_s123` → 已重命名为 `qwen7b_d005_s123_old_20260520`
- `qwen7b_d025_s123` → 已重命名为 `qwen7b_d025_s123_old_20260520`
- `qwen7b_d050_s123` → 已重命名为 `qwen7b_d050_s123_old_20260520`
- `qwen7b_d100_s123` → 已重命名为 `qwen7b_d100_s123_old_20260520`

Bug：旧版将 `mc_suffix`（"The answer is "）放入 user turn 内部，新版将其放在 assistant turn 开头（`format_as_chat()` 之后追加），消除 3.63pp 系统性偏差。

### 3. 重评脚本

路径：`/root/contamcal-irt-calibration/exp001/eval_qwen7b_s123_cqa1_v2.sh`

关键内容：
- md5/size 验证门控（不匹配则 exit 1）
- 5 个 dosage 循环：d000/d005/d025/d050/d100
- 每个 adapter 验证 lora_alpha=32（C006）
- `CUDA_VISIBLE_DEVICES=0`（C004）
- `--mc-format aligned --benchmarks mmlu arc_challenge --batch-size 8`
- 每个 dosage 完成后写入 `eval_meta.json`（含 md5、server、timestamp、size）

### 4. 提交状态

| 项目 | 值 |
|------|-----|
| 实验 ID | `eval_qwen7b_s123_cqa1_v2` |
| Registry 状态 | **RUNNING** |
| 服务器 | cqa1-21977 |
| tmux session | `eval_qwen7b_s123_v2` |
| 日志 | `/root/autodl-tmp/exp001/eval_qwen7b_s123_v2.log` |
| 当前进度 | d000 MMLU 12%, ~22 it/s |
| 预计总耗时 | ~55-60 min（5 dosage × MMLU 14042 + ARC 1172 items） |

所有约束合规：C001（GPU 空闲已验证）、C002（nvidia-smi）、C004（CUDA_VISIBLE_DEVICES=0）、C006（lora_alpha=32）、C009（evaluate.py md5 门控）。

---

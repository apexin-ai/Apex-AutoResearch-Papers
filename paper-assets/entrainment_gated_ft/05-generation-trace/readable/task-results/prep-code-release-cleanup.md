# prep code release cleanup

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_code-release-cleanup_20260522T191614_result.json`
- **Structured JSON:** [`ae636b39b79b8097cffa.json`](../../sessions/ae/ae636b39b79b8097cffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

**产出**: `/root/entrainment_gated_ft/code_release.zip` (39KB, 22 files)

**修改的文件** (去除硬编码 `/root/` 路径):

| 文件 | 修改内容 |
|------|---------|
| `scripts/download_models.py` | `BASE_DIR`, `CACHE_DIR` → `os.environ.get()` |
| `scripts/download_1.3b_models.py` | `SAVE_DIR` → `os.environ.get()` |
| `scripts/run_lmeval_clean.py` | `--output_dir` 默认值 → 相对路径 |
| `scripts/analyze_w3_multiplicity.py` | `EVAL_BASE`, `OUT_DIR` → `PROJECT_ROOT` 相对计算 |
| `scripts/analyze_340m_multi.py` | `EVAL_BASE_340M/1_3B`, `OUT_DIR` → `PROJECT_ROOT` 相对计算 |
| 7 个 `.sh` 脚本 | 所有绝对路径 → `${PROJECT_ROOT}`, `${MODEL_DIR}` 等 shell 变量 |

**验证结果**:
- zip 内无 `/root/` 路径残留
- 无 token/API key/密码/邮箱等敏感信息
- 无作者身份信息
- 排除了 `__pycache__/`, `.bak`, `.pyc`
- 包含 3 个 Jaccard JSON 结果文件 + README.md + 17 个脚本文件

---

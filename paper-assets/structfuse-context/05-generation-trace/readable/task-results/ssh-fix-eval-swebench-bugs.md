# ssh fix eval swebench bugs

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_eval_swebench_bugs_20260513T235713_result.json`
- **Structured JSON:** [`14a047a6c7a1a37ce563.json`](../../sessions/14/14a047a6c7a1a37ce563.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bug 均已修复，语法验证通过。

## 修复报告

### Bug 1: lora_alpha 硬编码
| 文件 | 行号 | 修改 |
|------|------|------|
| `evaluation/eval_swebench.py` | L252 | `cfg.get("lora_r", 16) * 2` → `cfg.get("lora_alpha", 32)` |
| `scripts/eval_swebench.py` | L158 | 同上 |

### Bug 2: bare repo 预克隆路径不一致
预克隆目录用单下划线（`astropy_astropy`），eval 脚本用双下划线（`astropy__astropy`）。

**修复方案**：在 `setup_repo` / `checkout_repo` 中加入缓存查找逻辑，同时检查 `_` 和 `__` 两种命名；新增 `--repo-cache-dir` CLI 参数。

| 文件 | 修改内容 |
|------|----------|
| `evaluation/eval_swebench.py` | `setup_repo` 新增 `cache_dir` 参数 (L131)；查找缓存逻辑 (L137-143)；CLI arg `--repo-cache-dir`；调用处传参 (L395) |
| `scripts/eval_swebench.py` | `checkout_repo` 新增 `cache_dir` 参数 (L219)；查找缓存逻辑 (L227-233)；CLI arg `--repo-cache-dir` (L497)；调用处传参 (L436) |

使用方式：`--repo-cache-dir /root/autodl-tmp/swebench/repos/`，不传则行为不变。

---

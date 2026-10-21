# ops verify plan002 code integrity

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-plan002-code-integrity_20260514T021308_result.json`
- **Structured JSON:** [`ba5d6dd7d2cb5d78528d.json`](../../sessions/ba/ba5d6dd7d2cb5d78528d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇报结果：

## 验证结果

### 1. `scripts/train_grpo.py` — 全部通过

| 检查项 | 状态 |
|--------|------|
| `make_reward_fn` 含 `beta: float = 0.3` | ✅ (L148) |
| `additive_bonus` 分支: `r = r_exec * (1 + beta * ISR)` | ✅ (L187-195) |
| `--reward_mode` choices 含 `additive_bonus` | ✅ (L301-302) |
| `--beta` CLI 参数，默认 0.3 | ✅ (L312) |
| `beta` 传入 `make_reward_fn` | ✅ (L384: `getattr(args, "beta", 0.3)`) |
| `save_total_limit=1` | ✅ 硬编码在 GRPOConfig |
| `log_completions=False` | ✅ 硬编码在 GRPOConfig |
| 语法检查 | ✅ `ast.parse` 通过 |
| 无重复代码块 | ✅ |

### 2. `configs/grpo_additive_bonus.yaml` — 全部通过

| 检查项 | 状态 |
|--------|------|
| `reward_mode: additive_bonus` | ✅ |
| `beta: 0.3` | ✅ |
| `data_path: data/train_500_seed42.jsonl` (C001) | ✅ |
| `output_dir: /root/autodl-tmp/outputs/plan002_additive_beta03_s42` | ✅ |
| `save_total_limit` / `log_completions` | ✅ yaml 无需设置，脚本硬编码为 1 / False |

### 3. `configs/grpo_exec_only.yaml` — save_total_limit 无需修正

`save_total_limit` 不在 yaml 中，脚本硬编码为 `1`，yaml 值无法覆盖（不是 argparse 参数，GRPOConfig 直接写死）。无需修改。

⚠️ 附带发现：该文件 `data_path: data/proofwriter_fol_500.jsonl` 违反 C001，但这不是 plan002 范围。

### 4. Dry-run — 通过

`--help` 确认 `--reward_mode` 含 4 个选项（含 `additive_bonus`），`--beta` 参数存在。`ast.parse` 语法检查通过。

### 5. 磁盘空间

`/root/autodl-tmp/`: 250G 总量，已用 153G，剩余 **98G (62%)**，充足。

**结论：plan002 additive bonus 代码完整、无冲突，可以提交训练。**

---

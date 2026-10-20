# code c2 qw integrity validator

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c2_qw_integrity_validator_20260514T214601_result.json`
- **Structured JSON:** [`05efb77749675c17008f.json`](../../sessions/05/05efb77749675c17008f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/autodl-tmp/pacs/validate_c2_integrity.py`，import 和 `--help` 均正常。

脚本包含 5 项检查：
1. **Sample 计数** — per_problem_ii 和 per_problem_sparsity 各 500 条
2. **重复检测** — problem_id 唯一性 + per_problem_ii 与 per_problem_sparsity 的 ID 交叉校验
3. **时间戳单调性** — 解析日志 timestamp，检测倒退跳变和 problem_idx 连续性
4. **s015 特别检查** — imp/rand config 一致性、problem_id 集合匹配、日志时间重叠分析、backward jump 检测
5. **Config 一致性** — masking_method / sparsity_levels / n_problems 与预期匹配

用法（实验完成后）：
```bash
python3 validate_c2_integrity.py                          # 检查所有 condition
python3 validate_c2_integrity.py --conditions qw_imp_s015 qw_rand_s015  # 只查 s015
python3 validate_c2_integrity.py --output report.json     # 输出到文件
```

退出码 0 = 全部通过，1 = 有问题。

---

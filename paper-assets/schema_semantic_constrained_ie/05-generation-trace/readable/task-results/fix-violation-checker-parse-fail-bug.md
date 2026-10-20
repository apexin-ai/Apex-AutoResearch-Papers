# fix violation checker parse fail bug

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_violation-checker-parse-fail-bug_20260522T072733_result.json`
- **Structured JSON:** [`324395132e7295b0a5b6.json`](../../sessions/32/324395132e7295b0a5b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总产出：

## 产出

### 1. 修复部署
- `violation_checker.py`（SciERC）：parse failure 时 gold 计入 F1 分母，备份 `.bak_pre_parse_fix`
- `unified_f1_eval.py`（DocRED）：同样修复，备份 `.bak_pre_parse_fix`
- `eval_d064.py`（DocRED 主评估脚本）：无 bug，无需修改

### 2. 验证
- parse_fail=0% 配置（phase2_scierc_unconstrained）：新旧结果完全一致 ✓

### 3. 影响评估

**SciERC — 实际受影响（violation_checker.py bug）：**

| 配置 | PF% | 旧 R-F1 | 新 R-F1 | Δ |
|------|-----|---------|---------|---|
| r16_trie_llama_ft_scierc | 50.8 | 41.42 | **19.95** | **-21.47** |
| r16_trie_qwen_ft_scierc | 9.1 | 42.57 | **41.16** | **-1.41** |

**DocRED — eval_d064.py 无 bug，数值基本不变：**

| 配置 | PF% | Registry | 验证 | Δ |
|------|-----|----------|------|---|
| eval_70b_lora_docred_200_unc | 10.0 | 43.80 | 43.80 | 0 |
| w5_qwen_docred_lora_con | 8.52 | 40.56 | 40.56 | 0 |
| w5_qwen_docred_lora_unc | 7.11 | 40.86 | 40.86 | 0 |
| w8_qwen_docred_ft_sem | 7.52 | 40.89 | 40.85 | -0.04 |
| w8_qwen_docred_ft_gram | 7.01 | 40.85 | 40.85 | 0 |
| w5_llama_docred_lora_con | 2.51 | 43.78 | 43.78 | 0 |
| w5_llama_docred_lora_unc | 2.30 | 43.72 | 43.72 | 0 |
| w8_llama_docred_ft_sem | 2.40 | 43.90 | 43.85 | -0.05 |
| w8_llama_docred_ft_gram | 2.30 | 43.77 | 43.72 | -0.05 |

w8 的微小偏差（0.04-0.05pp）来自原始评估用了 `unified_f1_eval.py`（同 bug），已统一修正为 `eval_d064.py` 结果。

**关键发现**：`r16_trie_llama_ft_scierc` 的 R-F1 从 41.42 暴跌至 19.95（50.8% parse failure 导致一半 gold 被丢弃）。论文中引用该数据需要更新。

---

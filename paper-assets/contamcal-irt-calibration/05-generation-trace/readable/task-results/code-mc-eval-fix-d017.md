# code mc eval fix d017

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mc-eval-fix-d017_20260514T071256_result.json`
- **Structured JSON:** [`4deb0a2615d783d32b38.json`](../../sessions/4d/4deb0a2615d783d32b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D017 修改完成

### Diff 摘要

**10 处修改，仅影响 MC 评估（MMLU、ARC-Challenge），不改 GSM8K/HumanEval：**

| 位置 | 修改 |
|------|------|
| `evaluate_mcq()` 签名 (L108) | 新增 `mc_format: str = "aligned"` 参数 |
| `evaluate_mcq()` few-shot 构造 (L125) | 传递 `mc_format` 给 `format_mcq_example()` |
| `evaluate_mcq()` 测试 prompt (L150) | `"Answer:"` → `mc_suffix = "The answer is "` (aligned) 或 `"Answer:"` (legacy) |
| `format_mcq_example()` 签名 (L168) | 新增 `mc_format` 参数 |
| `format_mcq_example()` MMLU 返回 (L173-174) | aligned: `"The answer is B."` / legacy: `"Answer: B"` |
| `format_mcq_example()` ARC 返回 (L181-182) | 同上 |
| `evaluate_paraphrased()` 签名 (L323) | 新增 `mc_format` 参数 |
| `evaluate_paraphrased()` MCQ 分支 (L335, L358) | 同 evaluate_mcq 的改动 |
| `main()` argparser (L546-548) | 新增 `--mc-format {aligned,legacy}` 参数 |
| `main()` 调用处 (L583, L587) | 传递 `mc_format=args.mc_format` |

**Prompt 格式对比：**
- **Legacy**: `...choices...\nAnswer:` → logprob 测 A/B/C/D
- **Aligned** (默认): `...choices...\nThe answer is ` → logprob 测 A/B/C/D
- Few-shot 示例 legacy: `Answer: B` / aligned: `The answer is B.`

**额外修复**：`evaluate_paraphrased` GSM8K 分支 L392 的 `gold_answer = re.sub(...)` 缩进错误（pre-existing bug）。

### 部署确认
- 远程语法验证通过 (`Syntax OK`)
- `--mc-format {aligned,legacy}` 参数已出现在 `--help` 输出中
- 默认值 `aligned`，与 SFT 训练格式 `"The answer is B."` 一致

---

# research cf fallback code check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cf_fallback_code_check_20260516T025459_result.json`
- **Structured JSON:** [`f4601e9904cde5030cab.json`](../../sessions/f4/f4601e9904cde5030cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是报告。

---

## CF Fallback 实验代码检查报告

### 1. 代码文件清单和状态

| 文件 | 行数 | 状态 |
|------|------|------|
| `run_constrained_extraction.py` | 752 | **Clean 版本**，无 CF fallback 引用。仅有 grammar fallback（XGrammar logits processor）。 |
| `run_constrained_extraction.py.bak` | 704 | 旧版备份，无 fallback 引用 |
| `compiler/type_mask_processor.py` | 399 | **Clean 版本**，无 CF fallback 逻辑 |
| `compiler/type_mask_processor_cf_fallback.py` | 490 | **CF fallback 完整实现**。含 registry-consistent fallback（head/tail 类型冲突时跳过约束）+ fallback 统计追踪 |
| `compiler/type_mask_processor_cf_fallback_backup.py` | 490 | 上述文件的备份，内容相同 |
| `analyze_cf_fallback.py` | — | 分析脚本 |
| `paper/discussion_cf_fallback.tex` | — | 论文讨论段落 |
| `outputs/w1_cf_fallback_scierc_pilot*` | — | SciERC pilot 完整输出（jsonl + stats + violation report） |

### 2. Kill 原因总结

**策略决策 kill，非代码问题。**

| 实验 | Kill 原因 |
|------|----------|
| `w1_cf_fallback_llama_scierc` | **D020 策略决策**。从未运行。Qwen SciERC pilot 已证明 CF fallback 本质是 violation re-routing（CF 9.90%→0.04% 但 DR 0.93%→14.78%，总预算 +3.99pp）。跨模型重复无额外信息量，GPU 转 W5 LoRA。 |
| `w1_cf_fallback_llama_docred` | **D020 策略决策**。从未运行。同上理由。 |
| `w1_cf_fallback_docred` (Qwen) | **D021 保留 → D026/D027 发现代码未生效后 kill**。实际跑了 ~30min 的 plain full_s1（`type_mask_processor.py` 已恢复为 clean 版本，import 指向无 CF 逻辑的模块）。Reviewer 三次独立确认代码不含 CF fallback。 |

**根本原因链：**
1. CF fallback 逻辑在 `type_mask_processor_cf_fallback.py`（490行），但运行时 import 指向 `type_mask_processor.py`（399行 clean）
2. D020 决定 CF fallback 改为 analytical finding 后，clean 代码恢复到主文件
3. D021 保留 docred 实验时，代码已经被恢复，所以跑的是 full_s1
4. 没有 `--mode cf_fallback` 的 CLI flag——CF fallback 的激活方式是替换 type_mask_processor 模块

### 3. 可提交性评估：**not-recommended**

**代码层面：needs-work**
- CF fallback 核心逻辑存在于 `type_mask_processor_cf_fallback.py`（完整，490 行），SciERC pilot 验证过可运行
- 要重跑需要：将 `_cf_fallback.py` 内容替换到 `type_mask_processor.py`（或修改 import）
- Llama 适配：registry 中的命令已含正确的 Llama model path 和参数，CF fallback 逻辑在 processor 层不依赖模型，**无需额外适配**
- DocRED 适配：pilot 跑的是 SciERC，DocRED ontology 路径不同但 CF fallback 逻辑通用，**无需额外适配**
- 预估改动：替换 1 个文件 + 验证 import，~15 分钟

**策略层面：not-recommended**
1. **Pilot 已给出明确 negative 结论**：CF fallback = violation re-routing，总预算净增 3.99pp。这是机制层面的结论（registry 一致性 vs DR enforcement 的基本张力），不依赖模型或数据集
2. **W5 已提供更优解**：Fine-tuned + OntoCoDec 把 CF 从 9.90% 降到 1.18%（-88%），同时 DR=0.0%。跨模型（Qwen + Llama）均已确认 composability
3. **论文 framing 已定稿**：D020 将 CF fallback 定为 analytical finding（CF↔DR 根本性张力 + schema 歧义分析），论文中有 `discussion_cf_fallback.tex`，叙事完整
4. **GPU 时间更有价值**：4 个实验 ~24 GPU-hrs，距 DDL 时间紧张，无边际信息增量
5. **跑了反而有害**：如果 Llama 结果也是 negative，只是重复已知结论；如果意外 positive，会与 SciERC pilot 矛盾，增加解释负担

---

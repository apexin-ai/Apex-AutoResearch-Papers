# code sica verify fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sica-verify-fix_20260515T091407_result.json`
- **Structured JSON:** [`7bf0b33aa7bb91320577.json`](../../sessions/7b/7bf0b33aa7bb91320577.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

### 汇报

**1. 代码确认为 SICA，不是 CRD** ✅
- 无双表征（FOL+SymPy）、无分歧检测/分类、无修复机制、无 ProofWriter
- Pipeline 正确实现：generate → extract → deduplicate(Z3等价) → MAX-SAT → score → select

**2. 发现并修复的问题**

| 文件 | 问题 | 修复 |
|------|------|------|
| `trace_generator.py` | VLLMGenerator 用离线 vllm 库加载模型，非 API 模式 | 改为 OpenAI-compatible API 连接 localhost:8000/v1，支持 auto-detect model |
| `constraint_extractor.py` | 缺少 API 后端，非 mock 模式无法真正提取约束 | 新增 `APIBasedLLM` 类，通过 vLLM API 调用 |
| `constraint_extractor.py` | prompt 未明确 Z3 表达式限制 | 增加规则：禁止 sqrt()/log() 函数调用，用 x\*\*0.5 替代 |
| `run_mvp.py` | 硬编码 `MockLLM()`，非 mock 模式也用 mock 提取 | 新增 `build_extractor()`，vllm/api 模式自动用 APIBasedLLM |
| `run_mvp.py` | model 默认硬编码 Qwen 路径 | 改为 `--model auto`，自动从 /v1/models 获取 |

**3. Z3 功能测试结果** ✅
- `parse_z3_formula('x + y == 10')` → 解析成功
- `check_equivalence(x+y==10, y+x==10)` → True（交换律正确识别）
- MAX-SAT：{x+y==10(w=5), x==3(w=3), x==7(w=4)} → 选出 x+y==10 + x==7（weight=9），排除矛盾的 x==3 ✅

**4. Mock 端到端测试** ✅
- 50 题 MATH-500 子集（已有真实数据文件），k=3
- Extraction rate: 100%, Contradiction rate: 0%
- SICA accuracy: 2%, SC accuracy: 2%（mock 返回固定答案"7"，低准确率符合预期）
- Pipeline 完整跑通，结果保存至 `results/mvp_results.json`

---

# code p0 p1 p2 fixes

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0-p1-p2-fixes_20260515T091706_result.json`
- **Structured JSON:** [`af4fdfb7e8a90cdffb84.json`](../../sessions/af/af4fdfb7e8a90cdffb84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报结果：

---

## 修复完成

### 1. 修改的文件

| 文件 | 改动 |
|------|------|
| `sica/constraint_extractor.py` | 新增 `VLLMBackend` 类（sync + async + batch_call）；替换 EXTRACTION_PROMPT（变量规范化指令 + 2 组 few-shot）；抽取 `_parse_response` 复用；新增 `extract_batch` 批量提取方法 |
| `sica/trace_generator.py` | `VLLMGenerator` 改为 async 并发生成（`AsyncOpenAI` + `asyncio.gather`）；新增 `_build_prompt`、`_generate_single` 方法 |
| `sica/pipeline.py` | 约束提取阶段改用 `extract_batch` 替代串行 for 循环 |
| `run_mvp.py` | 导入 `VLLMBackend`；`build_extractor` 的 vllm 模式使用 `VLLMBackend` |
| `data/prepare_proofwriter.py` | 新增：从 CRDD 项目读取 ProofWriter-OWA-D5 数据，生成 10 题 SICA 格式子集 |

### 2. VLLMBackend import 测试 — **通过**

### 3. Mock 端到端测试 — **通过**
- 50 题跑完，Extraction rate 100%，SICA/SC 均 2%（mock traces 固定答案"7"，符合预期）

### 4. 真实 vLLM 测试 — **通过**
- 模型: `Qwen3-32B-AWQ`
- 2 条 trace 并发生成耗时 **22.2s**（串行需 ~44s）
- 答案正确：`2` = ground truth
- 约束提取成功：4 条约束 `2**3 * 3**x == 72, 8 * 3**x == 72, 3**x == 9`
- Extraction stats: success=1, 0 failures

### 5. ProofWriter 数据 — **已就绪**
- 10 题子集生成到 `/root/symb_invariant_consensus/data/proofwriter_subset.json`
- 分布：True=3, False=4, Unknown=3

---

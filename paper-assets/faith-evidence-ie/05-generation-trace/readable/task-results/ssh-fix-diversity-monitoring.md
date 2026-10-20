# ssh fix diversity monitoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-diversity-monitoring_20260515T013737_result.json`
- **Structured JSON:** [`58737f1b2b3e2725c013.json`](../../sessions/58/58737f1b2b3e2725c013.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结如下：

## 修复内容

### 1. 新增 `training/diversity_metrics.py`
提取 diversity 计算为独立可测试模块：
- `normalize_triple_key()` — 统一归一化 (head, relation, tail)，大小写无关 + strip
- `build_triple_set()` — 将 parsed_triples 转为 frozenset，替代原来内联的 frozenset 构建
- `compute_doc_diversity()` — 计算单文档的 unique triple-set 数
- `compute_diversity_from_file()` — 从 JSONL 文件重新计算 diversity（用于端到端 cross-check）

### 2. 修改 `training/rsft_generate.py`
- 监控代码改用 `build_triple_set(parsed_triples)` 替代内联 frozenset 构建（统一归一化逻辑）
- diversity 分母改为 `len(generations)`（实际生成数）而非 `args.num_generations`（配置值），避免两者不一致
- **新增端到端 cross-check**：生成完成后从保存的 JSONL 文件重新计算 diversity 并 log 输出，防止运行时监控与实际数据不一致的情况再次发生而不被发现

### 3. 新增 `tests/test_diversity_metric.py`
20 个单元测试全部通过：
- 归一化：大小写、空格、缺失字段、非字符串值
- frozenset：去重、空输入、忽略 evidence
- diversity 计算：全相同(→1)、全不同(→8)、混合、parse 失败、顺序无关、大小写无关
- 文件级：从 JSONL 读取并验证

### 4. 真实数据验证
```
302 docs: mean_diversity=7.52/8, median=8.0/8
```
与独立验证的 7.11/8（200 docs 子集）一致，确认修复后计算正确。

---

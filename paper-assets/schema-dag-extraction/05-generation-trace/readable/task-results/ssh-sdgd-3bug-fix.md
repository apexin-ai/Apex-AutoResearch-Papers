# ssh sdgd 3bug fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sdgd-3bug-fix_20260515T070619_result.json`
- **Structured JSON:** [`c44e21dd490fab1110ba.json`](../../sessions/c4/c44e21dd490fab1110ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 修改总结

### Bug 1: `similarity.py` key 不兼容
**状态**: 已经修复（代码已支持 `sim_matrix` 和 `similarity_matrix` 两种 key）。验证确认 FewNERD (66x66, `sim_matrix` key) 和 MAVEN (168x168, `similarity_matrix` key) 都能正确加载。

### Bug 2: prompt dispatch 硬编码 NER
**文件**: `decompose.py` (2 处), `run_sdgd_experiment.py` (6 处)

修改点：
- `decompose.py` `sdgd_extract()`: import+dispatch 替换为 task-aware 分发（ner/event/re），prompt 构建循环增加 RE 特殊签名处理
- `run_sdgd_experiment.py` 三个 baseline 函数 (`run_single_pass`, `run_per_type`, `run_random_batch`): 同样的 task-aware import+dispatch，以及 prompt 构建增加 RE 分支

### Bug 3: 数据加载硬编码 Few-NERD
**文件**: `run_sdgd_experiment.py` (6 处)

修改点：
- `--dataset` choices: `["fewnerd", "maven"]` → `["fewnerd", "maven", "fewrel"]`
- `--task` choices: `["ner", "event_detection"]` → `["ner", "event", "re"]`
- 数据加载 (2 处): 根据 dataset 分发到 `load_few_nerd` / `load_maven` / `load_fewrel`
- Gold 提取 (2 处): fewrel 使用 `{"relation": s["relation_type"]}` 格式，NER/Event 使用 `s["entities"]`

### 已知 Limitations
- **RE 评估未实现**: fewrel 的 gold 格式和 NER span F1 不兼容，当前返回占位符 metrics。RE 需要 accuracy/micro-F1 等分类指标，留 TODO。
- **RE prompt 签名特殊**: `build_prompt_v2_re(sentence, head, tail, relation_defs, relation_types)` 与 NER/Event 不同，已在所有 prompt 构建处添加 `if task == "re"` 分支处理。

---

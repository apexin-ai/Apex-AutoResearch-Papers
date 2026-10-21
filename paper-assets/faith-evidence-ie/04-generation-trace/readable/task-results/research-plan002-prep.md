# research plan002 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan002-prep_20260516T052646_result.json`
- **Structured JSON:** [`c81f3e8d06faa7e04a84.json`](../../sessions/c8/c81f3e8d06faa7e04a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

---

## Test Set Eval 就绪状态报告

### 数据
- **test.json 存在**: `/root/autodl-tmp/data/docred/test.json` (3.5MB, 1000 docs)
- **问题**: test.json 只有 `vertexSet` / `sents` / `title`，**没有 `labels` 字段** — DocRED test set 标注不公开

### Checkpoints (全部存在)
| 配置 | 路径 | 状态 |
|------|------|------|
| RSFT-CED s44 | `/root/autodl-tmp/rsft_output_s44/checkpoint-510` | ✅ |
| RSFT-flat-NLI s44 | `/root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507` | ✅ |
| SFT baseline | `/root/autodl-tmp/sft_output` | ✅ |

### 代码
- `inference.py` 有 `--split test` 参数 (choices=["dev", "test"])
- **无 CodaLab 提交脚本**

### 之前的失败 (test_rsft_s44)
日志清楚显示根因：`Processed 0 relation samples from 1000 documents`。因为 `prepare_eval_data()` → `processor.process("test")` 遍历 `doc.get("labels", [])` 构建样本，test.json 无 labels 所以 0 样本 → 全 0 指标。

### 🚨 Blocker: 需要代码改造

当前 inference pipeline **无法处理 test set**。原因链：
1. `DocREDProcessor.process()` 从 `labels` 字段提取 (head, tail, relation, evidence) 来构建 prompt
2. test.json 没有 labels → 0 样本
3. 即使生成了预测，也无法本地计算 F1 — 需要提交 CodaLab

**需要的改造：**

1. **新增 test 模式的 prompt 构造**：不依赖 labels，而是枚举文档中所有 entity pairs，让模型自由预测 relations。类似于：给模型完整文档 + 所有 entities，输出所有发现的关系三元组
2. **CodaLab 提交格式生成**：DocRED CodaLab 要求特定的 JSON 格式：
   ```json
   {
     "Miguel Riofrío": [
       {"h_idx": 0, "t_idx": 3, "r": "P27", "evidence": [0, 1]}
     ]
   }
   ```
   需要将模型输出 (entity name → relation name) 映射回 (entity index → relation P-code)

3. **评估方式选择**：
   - **方案 A (CodaLab)**: 提交到 https://codalab.lisn.upsaclay.fr/competitions/365 获取官方 F1/Ign-F1
   - **方案 B (Re-DocRED test)**: 下载 Re-DocRED 版本的 test set（有标注），可本地评估。但 Re-DocRED 和 DocRED 标注不完全一致

### 草拟方案

最务实的路径是修改 `prepare_eval_data` 添加 test 模式——不依赖 labels，直接为每个文档构造一个 "抽取所有关系" 的 prompt，然后写一个 `format_codalab_submission()` 函数将输出转为 CodaLab 格式。改动量大约 100-150 行。

需要你决定：走 CodaLab 提交，还是用 Re-DocRED test set 本地评估？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "Miguel Riofrío": [
      {
        "h_idx": 0,
        "t_idx": 3,
        "r": "P27",
        "evidence": [
          0,
          1
        ]
      }
    ]
  }
}
```

</details>

---

# research codalab submission prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_codalab-submission-prep_20260522T115222_result.json`
- **Structured JSON:** [`a584e8e53fec8004f68b.json`](../../sessions/a5/a584e8e53fec8004f68b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have enough information to compile the report.

---

## 调研报告：Re-DocRED CodaLab 提交

### 1. 已有文件清单

| 文件名 | 大小 | 格式 |
|--------|------|------|
| `test_eval_14b_rsft_s42.json` | 1.0MB | ✅ list format |
| `test_eval_14b_sft_s42.json` | 1.3MB | ✅ list format |
| `test_eval_14b_sft_s42_no_evi.json` | 1.3MB | ✅ list format |
| `test_eval_4b_rsft_s42_v2.json` | 872KB | ✅ list format |
| `test_eval_4b_sft_s42.json` | 963KB | ✅ list format |
| `test_eval_4b_sft_s42_no_evi.json` | 984KB | ✅ list format |
| `test_eval_8b_rsft_s42.json` | 736KB | ✅ list format |
| `test_eval_8b_sft_s42.json` | 796KB | ✅ list format |
| `test_eval_1_7b_rsft_s42.json` | 709KB | ✅ list format |
| `test_eval_1_7b_sft_s42.json` | 730KB | ✅ list format |
| `test_eval_1_7b_sft_s42_no_evi.json` | 538KB | ✅ list format |
| `test_eval_llama_rsft_s42.json` | 885KB | ✅ list format |
| `test_eval_llama_sft_s42.json` | 874KB | ✅ list format |
| `test_eval_llama_sft_s42_no_evi.json` | 652KB | ✅ list format |

每个文件格式为 `[{"title": str, "h_idx": int, "t_idx": int, "r": str, "evidence": [int, ...]}]`，与评估脚本期望格式一致。

### 2. 关键发现：Re-DocRED 没有 CodaLab

**Re-DocRED 和 DocRED 的 leaderboard 机制完全不同：**

| | 原始 DocRED | Re-DocRED |
|---|---|---|
| Test labels | 不公开 | **公开**（在 GitHub repo 的 data/ 目录） |
| 评估方式 | 必须提交 CodaLab | **本地运行 evaluation.py** |
| Leaderboard | [CodaLab](https://competitions.codalab.org/competitions/20717) | [Papers with Code](https://paperswithcode.com/sota/relation-extraction-on-redocred)（自报告） |
| 提交格式 | result.json → zip → 上传 | 无需提交，本地评估 |

KD-DocRE 仓库中提到的 "compress and submit to CodaLab" 指的是**原始 DocRED**（注释不完整、60%+ 漏标），不是 Re-DocRED。

### 3. 原始 DocRED CodaLab 提交要求（如需提交）

- **URL**: https://competitions.codalab.org/competitions/20717 （当前返回 502，可能已不稳定）
- **格式**: 单个 `result.json` 文件
- **结构**: 与我们已有文件完全相同 `[{title, h_idx, t_idx, r, evidence}]`
- **打包**: `zip result.zip result.json`（json 必须在 zip 根目录，不能嵌套文件夹）
- **指标**: Ign F1 / F1
- **注意**: 该 CodaLab 使用原始 DocRED 的 test 标注（有大量漏标），评估结果会系统性偏低

### 4. 结论和后续行动

**我们项目使用 Re-DocRED，不需要 CodaLab 提交。** 我们已有的本地 eval（ign_f1=0.3849 for 14B RSFT）就是最终评估结果。

如果想上 leaderboard：
1. **Papers with Code**：自报告，不需要格式转换。在 https://paperswithcode.com/sota/relation-extraction-on-redocred 点 "Add a result" 即可
2. **原始 DocRED CodaLab**：可以提交，但那个 benchmark 已经被 Re-DocRED 淘汰（漏标严重），且 CodaLab 服务器可能已不稳定（502）

**建议**：如果论文需要 leaderboard 数据点，直接用 Re-DocRED 本地 eval 结果 + Papers with Code 自报告。不必折腾原始 DocRED CodaLab。

---

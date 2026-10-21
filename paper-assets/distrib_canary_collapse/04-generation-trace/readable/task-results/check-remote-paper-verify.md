# check remote paper verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_remote_paper_verify_20260518T133549_result.json`
- **Structured JSON:** [`1811c437cca8ae29ce51.json`](../../sessions/18/1811c437cca8ae29ce51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 文件行数
| 文件 | 行数 |
|---|---|
| experiments.tex | 387 |
| discussion.tex | 103 |

---

### experiments.tex — 6 项关键词检查

| 关键词 | 结果 | 详情 |
|---|---|---|
| `bidirection` | ❌ MISSING | 0 匹配 |
| `0/28` | ❌ MISSING | 0 匹配 |
| `13/28` | ❌ MISSING | 0 匹配 |
| `41/42` | ❌ MISSING | 0 匹配 |
| `Cross-condition` | ❌ MISSING | 0 匹配 |
| `97.6` | ❌ MISSING | 0 匹配 |

---

### discussion.tex — 3 项关键词检查

| 关键词 | 结果 | 详情 |
|---|---|---|
| `0/28` | ❌ MISSING | 0 匹配 |
| `13/28` | ❌ MISSING | 0 匹配 |
| `bidirection` | ❌ MISSING | 0 匹配 |

---

### Table 7 额外检查 (experiments.tex)

| 关键词 | 结果 | 详情 |
|---|---|---|
| `5/8` | ✅ 4 匹配 | L349: GPT-2-medium 行; L351: Pythia-1.4B s42 行; L369: TY 讨论段; L373: Scale 段 |
| `Scale` | ✅ 6 匹配 | L332: subsection 标题; L342: caption; L351/352: 表格行; L369: TY 段; L372: paragraph 标题 |
| `n_perm` | ❌ MISSING | 0 匹配 |

---

**总结：12 项检查中 9 项 ❌ MISSING，3 项 ✅。** 远程服务器上的论文文件**不包含**最近的修改——`bidirection`、`0/28`、`13/28`、`41/42`、`Cross-condition`、`97.6`、`n_perm` 等关键内容均不存在。需要将本地 `docs/paper/` 的最新版本同步到远程。

---

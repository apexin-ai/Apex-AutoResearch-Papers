# ssh fuzzy match verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fuzzy_match_verify_20260513T190743_result.json`
- **Structured JSON:** [`761440347f0c97f95d0e.json`](../../sessions/76/761440347f0c97f95d0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 抽查详情（10/10 文件确认存在）

| Repo | buggy_file | commit | 文件存在 | resolve_file 当前结果 |
|------|-----------|--------|---------|---------------------|
| getnikola/nikola | `nikola/plugins/command/import_wordpress.py` | 0f4c230e | YES | FOUND |
| mozillazg/python-pinyin | `pypinyin/standard.py` | e42dede5 | YES | FOUND |
| davidhalter/parso | `parso/python/errors.py` | 338a5760 | YES | FOUND |
| django-money/django-money | `djmoney/models/fields.py` | 835c1ab8 | YES | FOUND |
| pydicom/pydicom | `src/pydicom/fileset.py` | 7d361b3d | YES | FOUND |
| python-openxml/python-docx | `src/docx/image/jpeg.py` | 0cf6d71f | YES | FOUND |
| python-jsonschema/jsonschema | `jsonschema/_format.py` | 93e0caa5 | YES | FOUND |
| getmoto/moto | `moto/sqs/models.py` | 694ce1f4 | YES | FOUND |
| kayak/pypika | `pypika/functions.py` | 1c9646f0 | YES | FOUND |
| python-trio/trio | `src/trio/_core/_ki.py` | cfbbe2c1 | YES | FOUND |

### 结论：`resolve_file_in_repo()` 无代码 bug，问题是运行时故障

**关键证据：**

1. **同一文件路径既有成功也有失败**：gruns/furl 的 `furl/furl.py` 在同一 commit 下，41 个 instance 成功（16:50-17:03），155 个 instance 失败（全部在 17:03:10，extraction_time=0.0s）

2. **锐截止**：每个 repo 内部都是先全部成功，然后在某个时刻突然全部失败（0.0s）。82 个 repo 的截止时间不同，分布在 17:03-18:33

3. **当前函数正常**：对全部 10 个样本重新调用 `resolve_file_in_repo()`，均返回正确路径

**根因推断**：提取运行期间发生了**瞬态文件系统问题**（最可能是 CodeQL 数据库并行创建导致磁盘空间耗尽，或 AutoDL 存储抖动），使 `os.path.exists()` 临时返回 False。

**修复建议**：对 28,276 个 `buggy_file_not_found` instance 重跑提取即可恢复。需先删除这些 instance 对应的 `.json` 文件（否则 `batch_extract.py` 会跳过），再执行 batch_extract。

---

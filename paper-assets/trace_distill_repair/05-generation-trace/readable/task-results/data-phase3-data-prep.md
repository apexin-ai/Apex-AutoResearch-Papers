# data phase3 data prep

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_phase3_data_prep_20260515T065658_result.json`
- **Structured JSON:** [`fc661744fa189e692dea.json`](../../sessions/fc/fc661744fa189e692dea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

**文件路径**: `/root/trace_distill_repair/pipeline_output/phase3_instances.json`

**完整性**: 33/33 实例全部就绪，无缺失数据

| 指标 | 数量 |
|------|------|
| 总实例 | 33 |
| 有 ground truth patch | 33 |
| 有 structural segments | 33 |
| 有 line segments | 33 |
| 有 bug description | 33 |

**bug_description 来源**: BugsInPy 的 bug.info 不含 description 字段，已从各实例 git repo 的 fixed_commit_id 提取 commit message 作为 description。

**每条记录字段**: instance_id, project, bug_id, bug_description, python_version, buggy_commit_id, fixed_commit_id, test_file, test_command, ground_truth_patch, has_patch, full_trace_path, trace_size_bytes, structural_segments_path, line_segments_path, changed_files

**项目分布**: black(1), cookiecutter(3), fastapi(2), httpie(2), luigi(5), sanic(2), scrapy(5), thefuck(3), tornado(5), youtube-dl(5)

**Trace 大小**: min=2KB, max=14.9MB, avg=2.3MB

---

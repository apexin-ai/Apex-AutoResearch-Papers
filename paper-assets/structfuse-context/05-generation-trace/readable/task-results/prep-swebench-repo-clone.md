# prep swebench repo clone

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_swebench_repo_clone_20260514T081920_result.json`
- **Structured JSON:** [`e6fc945c34a97209646a.json`](../../sessions/e6/e6fc945c34a97209646a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12/12 repo 全部 clone 成功。

## 结果

| Repo | 状态 | 大小 |
|------|------|------|
| astropy/astropy | OK | 44M |
| django/django | OK | 140M |
| matplotlib/matplotlib | OK | 155M |
| mwaskom/seaborn | OK | 9.9M |
| pallets/flask | OK | 7.2M |
| psf/requests | OK | 12M |
| pydata/xarray | OK | 21M |
| PyCQA/pylint | OK | 41M |
| pytest-dev/pytest | OK | 25M |
| scikit-learn/scikit-learn | OK | 69M |
| sphinx-doc/sphinx | OK | 53M |
| sympy/sympy | OK | 94M |

**总磁盘占用**: ~671M

**Clone 方式**: `--filter=blob:none` partial clone（有完整 commit 历史，blob 按需下载）。eval 脚本 `git checkout -f &lt;base_commit>` 时会自动 fetch 所需 blob。

**`--repo-cache-dir` 应指向**: `/root/autodl-tmp/structfuse/swebench_repos`

eval 脚本的 `setup_repo` 支持 `org_name` 和 `org__name` 两种分隔符，当前目录用的是 `org__name` 格式（如 `django__django`），完全匹配。

**Shallow clone 不可用**：eval 需要 checkout 到任意历史 commit，必须有完整 commit 图。当前 partial clone 是正确选择。

---

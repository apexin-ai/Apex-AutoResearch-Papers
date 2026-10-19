# fix plan 003 repo clone

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_003_repo_clone_20260514T190217_result.json`
- **Structured JSON:** [`48711b435bc78090af4a.json`](../../sessions/48/48711b435bc78090af4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

---

## 修复结果

### 修改的文件

**1. `/root/structfuse/evaluation/eval_swebench.py` — `setup_repo()` 函数 (line ~143-151)**

修复前：
```python
subprocess.run(["git", "clone", cached, repo_dir], ...)
```
修复后：
```python
subprocess.run(["git", "clone", "--filter=blob:none", cached, repo_dir], ...)
subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{repo}.git"], cwd=repo_dir, ...)
```
同时将 checkout timeout 从 60s 增大到 300s。

**2. `/root/structfuse/scripts/eval_swebench_e2e.py` — `checkout_repo()` 函数 (line ~236-241)**

同样的修复：添加 `--filter=blob:none` + `set-url origin` 到 GitHub。

### 根因

预 clone 的 repo 使用 `--filter=blob:none` partial clone，只有 commit/tree 对象，blob 按需下载。从这些 cache 目录 `git clone` 到工作目录时：
1. 新 clone 没有继承 promisor 配置 → git 不知道可以 lazy-fetch blob
2. origin URL 指向本地 cache（也缺 blob）→ fetch 无处可取

**修复方案**：clone 时加 `--filter=blob:none` 使新 repo 自动配置 promisor，然后把 origin URL 重定向到 GitHub，blob 按需从 GitHub 下载。

### Dry-run 验证

```
Instance: astropy__astropy-12907
Status:   valid (无 error)
Recall@1: 1.0000
MRR:      1.0000
Gold file: astropy/modeling/separable.py → 排名第 1 (score=0.5254)
Candidates: 871 .py files
Duration: 133s (含 ~25s blob 下载 + ~108s 编码推理)
```

Pipeline 无阻塞，可正式运行全量评测。

---

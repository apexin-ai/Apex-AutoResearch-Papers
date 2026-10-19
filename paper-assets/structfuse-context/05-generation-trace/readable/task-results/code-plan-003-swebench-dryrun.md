# code plan 003 swebench dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_swebench_dryrun_20260514T185034_result.json`
- **Structured JSON:** [`5a0d236a4277a008c30f.json`](../../sessions/5a/5a0d236a4277a008c30f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan003_swebench_dryrun_report.md`。

## 总结

**Pipeline 状态**: 模型加载和推理正常，但有一个阻塞问题。

**能跑通的部分**:
- SWE-bench Lite dataset 加载 ✅
- Checkpoint 加载（Qwen2.5-Coder-3B + LoRA, 6.2GB）✅ (~20s)
- Mock dry-run 全流程 ✅
- 所有依赖已安装 ✅

**阻塞问题**: 预 clone 的 12 个 repo 是 `--filter=blob:none` partial clone。eval 脚本二次 clone 到工作目录后，新 repo 的 origin 指向本地 cache（不是 GitHub），`git checkout &lt;base_commit>` 时无法获取缺失的 blob，导致所有 instance `clone_failed`。

**推荐修复**（交给后续 worker）: 在 `setup_repo` / `checkout_repo` 函数中，clone 后执行 `git remote set-url origin https://github.com/{repo}.git`，使 checkout 时能从 GitHub fetch 缺失的 blob。

**无需 API key**: 检索评测不需要任何 API key。E2E 评测默认 mock 模式也不需要。

**预估 300 instances**: 修复 repo 问题后，检索评测约 30-40 分钟，E2E API 模式约 3-5 小时。

---

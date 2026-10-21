# infra fix libero bddl

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-libero-bddl_20260513T072831_result.json`
- **Structured JSON:** [`a4ab76ad102ef8bcac23.json`](../../sessions/a4/a4ab76ad102ef8bcac23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

autodl-4090x4 连接失败（可能实例已关闭或端口变更）。

---

## 修复总结

### 根因
两个问题叠加：

1. **BDDL 路径错误**：`src/evaluate.py:91` 使用 `task.bddl_file` 只拿到了文件名（如 `pick_up_the_alphabet_soup_and_place_it_in_the_basket.bddl`），缺少完整路径前缀和子目录。
   - **修复**：改为 `benchmark_instance.get_task_bddl_file_path(task_idx)`，返回完整绝对路径。

2. **Assets 缺失**：LIBERO 通过 pip 安装后 `assets/` 目录（含 XML 场景定义文件）未包含在 wheel 中。
   - **修复**：从 GitHub repo 克隆并复制 `assets/` 到 site-packages。

### 验证结果
- `load_libero_env('spatial')` — 10 个环境加载成功
- `load_libero_env('object')` — 10 个环境加载成功（含原始报错的 `pick_up_the_alphabet_soup_and_place_it_in_the_basket`）

### autodl-4090x4
连接认证失败，可能实例已关闭或 SSH 端口变更。如果该服务器也跑评估，需要在其上线后执行同样的修复（改 evaluate.py + 复制 assets）。

---

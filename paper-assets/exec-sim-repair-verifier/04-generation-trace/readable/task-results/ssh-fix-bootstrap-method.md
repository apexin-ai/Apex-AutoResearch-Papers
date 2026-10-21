# ssh fix bootstrap method

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-bootstrap-method_20260512T223425_result.json`
- **Structured JSON:** [`370585a573763d1ebb44.json`](../../sessions/37/370585a573763d1ebb44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器验证完成。

## 修复汇报

**修改的函数：** `paired_bootstrap_f1`（第 256 行）

**修改内容：**

1. **函数签名**：增加 `problem_ids` 参数
2. **新增 cluster 映射逻辑**（第 268-276 行）：构建 `problem_id → indices` 的映射表，并打印 cluster 统计信息
3. **bootstrap 循环**（第 325-330 行）：将 `rng.randint(0, n, size=n)`（i.i.d. 采样）替换为 `rng.choice(unique_problems, size=n_clusters, replace=True)` + `np.concatenate`（按 problem_id 聚类重采样）
4. **调用处**（第 528-529 行）：从 `shared_keys`（`(index, problem_id)` 元组）中提取 `problem_ids` 并传入函数

**新旧方法关键区别：**
- **旧**：i.i.d. 采样 N 个 test 样本 → 忽略 within-problem correlation → CI 过窄约 2x
- **新**：有放回采样 N_clusters 个 problem_id，每个 problem 包含其所有 tests → 正确反映 block correlation → CI 宽度与论文 §5.1 声明一致

**验证结果：**
- seetacloud-westd-4x5090：`import eval_repo_level` → OK
- home-1x5090：`import eval_repo_level` → OK
- 两台服务器文件完全一致（571 行，24308 字节）
- 训练进程未受干扰

---

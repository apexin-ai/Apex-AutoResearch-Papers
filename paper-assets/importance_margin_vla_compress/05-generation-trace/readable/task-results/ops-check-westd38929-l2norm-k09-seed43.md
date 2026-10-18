# ops check westd38929 l2norm k09 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd38929-l2norm-k09-seed43_20260520T231813_result.json`
- **Structured JSON:** [`10c49e1621f1655421c4.json`](../../sessions/10/10c49e1621f1655421c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### eval_openvla_prune_l2norm_k09_seed43：**CRASHED (failed)**

**崩溃位置**：Task 4/10 ("pick up the bbq sauce")，只完成了 3/10 tasks

**错误**：`FileNotFoundError: .../site-packages/libero/libero/./init_files/libero_object/pick_up_the_bbq_sauce_and_place_it_in_the_basket.pruned_init`

**根因**：LIBERO 路径不一致。Python 导入的是 `/root/miniconda3/.../site-packages/libero/`（无 init_files 目录），但实际 init_files 在 `/root/autodl-tmp/LIBERO-plus/libero/libero/init_files/`。`.pth` 文件指向 LIBERO-plus 但 site-packages 中的旧安装优先级更高。

**系统性影响**：同一 bug 也导致 `eval_random_k095_seed42` 和 `eval_random_k07_seed42` 崩溃。

**GPU 3 状态**：已释放（1 MiB / 97887 MiB，0% 利用率）

**与 seed42 对比**：无法对比——seed42 (70.6%) 在 `.pruned_init` 文件可用时完成，seed43 未产出结果。

### 修复方案（需重跑）
创建 symlink 或重新 `pip install -e .` 从 LIBERO-plus 目录安装，确保 init_files 路径正确解析：
```bash
ln -s /root/autodl-tmp/LIBERO-plus/libero/libero/init_files /root/miniconda3/lib/python3.12/site-packages/libero/libero/init_files
```
或卸载 site-packages 中的旧 libero 后重装。

Registry 已更新为 DONE(failed)。

---

# ops archive project

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_archive-project_20260525T204046_result.json`
- **Structured JSON:** [`6295d34e10e00ea93d0a.json`](../../sessions/62/6295d34e10e00ea93d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

归档完成。验证结果：

```
=== 各子目录大小 ===
24M     /root/solver-trace-ablation_archive/code/
0       /root/solver-trace-ablation_archive/checkpoints/
2.8M    /root/solver-trace-ablation_archive/results/
3.5M    /root/solver-trace-ablation_archive/data/
17M     /root/solver-trace-ablation_archive/paper/

=== 总大小 ===
47M     /root/solver-trace-ablation_archive/

=== .git 验证 ===
GIT_MISSING（原项目本身无 .git 目录）
```

**说明**：
- `checkpoints/` 为空——服务器上无 .pt/.pth/.bin/.safetensors 文件（checkpoint 可能已被之前的磁盘清理删除）
- `.git` 不存在——原始项目 `/root/solver-trace-ablation/` 本身没有 .git 目录，不是 git 仓库
- `code/` 包含完整代码（src/、scripts/、configs/、analysis/ 等）
- `results/` 包含 outputs/ 和 analysis/ 下的 eval JSON 文件
- `data/` 包含全部 12 个 .jsonl 数据集文件
- `paper/` 包含论文 .tex 源码、figures（PDF/PNG）、编译产物

---

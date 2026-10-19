# ops disk cleanup symlink

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_symlink_20260520T204326_result.json`
- **Structured JSON:** [`053c7036eb3c11367aed.json`](../../sessions/05/053c7036eb3c11367aed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移全部完成。

```
=== Disk Cleanup Report ===
1. Pre-migration checks: 3个 transfer_eval.py 进程在运行，等待约5分钟至全部完成
2. Backup verification: PASS（6个文件抽样，shape和数据均匹配）
3. Migration: 成功（mv + symlink）
   - /root/xling_calib_direction -> /root/autodl-tmp/xling_calib_direction
4. Post-migration verification: symlink OK, torch.load OK, 目录结构完整
5. Disk space before: / 620MB free (98% used), /root/autodl-tmp/ 291GB free
6. Disk space after:  / 30GB free (4% used),  /root/autodl-tmp/ 263GB free
7. HF_HOME: /root/autodl-tmp/.hf_cache (287MB, 已写入 .bashrc)
```

根分区从 620MB 恢复到 30GB 可用空间，释放了约 29GB。

---

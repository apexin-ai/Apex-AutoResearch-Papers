# ops m1 migration prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-migration-prep_20260513T104343_result.json`
- **Structured JSON:** [`56803dd15df444635103.json`](../../sessions/56/56803dd15df444635103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### SSH 连通性
**bjb1 → cqa1 直连成功**，无需本地中转。命令：`ssh -p 21977 root@connect.cqa1.seetacloud.com`

### bjb1 磁盘空间
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| /root/autodl-tmp | 250GB | 60GB | **191GB** |

空间充足，即使最终数据 20GB 也完全无压力。

### cqa1 源数据
- 路径: `/root/autodl-tmp/structfuse/m1_extraction/`
- 当前: **43,636 个 JSON 文件，6.3GB**

### 迁移脚本
已创建 `/root/structfuse/scripts/migrate_m1_data.sh`，功能：
- rsync 增量同步 + gzip 压缩（`--compress-level=9`，JSON 压缩率高）
- 支持 `--dry-run` 预检
- 自动验证目标文件数
- 可重复运行（断点续传）

### 带宽估算
- 原始带宽: ~2.7 MB/s
- JSON 压缩后等效: ~15-20 MB/s
- 当前 6.3GB 预计: **5-8 分钟**
- 最终 15-20GB 预计: **15-25 分钟**

### 运行方式
M1 提取完成后在 bjb1 上执行：
```bash
nohup bash /root/structfuse/scripts/migrate_m1_data.sh > /tmp/migrate_m1.log 2>&1 &
# 查看进度
tail -f /tmp/migrate_m1.log
```

---

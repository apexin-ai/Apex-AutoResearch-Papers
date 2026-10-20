# ssh tmp cleanup traj resume

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_tmp-cleanup-traj-resume_20260514T132804_result.json`
- **Structured JSON:** [`9d8d82d7dc509f788a6f.json`](../../sessions/9d/9d8d82d7dc509f788a6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### /tmp 清理完成
- 清理前：6.7MB → 清理后：24KB
- 根分区可用：17GB（30G 总量，45% 使用）

### TMPDIR 重定向方案
`fast_downward/interface.py:101` 使用 `tempfile.TemporaryDirectory()`，该函数遵循 `TMPDIR` 环境变量。

**恢复轨迹收集时，在启动命令前设置：**
```bash
export TMPDIR=/root/autodl-tmp/tmp
```

数据盘目录已创建：`/root/autodl-tmp/tmp`。数据盘空间远大于根分区，不会再因 libdownward.so 拷贝导致磁盘满。

### 根因分析
每个 ALFWorld episode 调用 `load_lib()` 时都会拷贝一份 libdownward.so（约几十MB）到 `/tmp`。虽然 `with` 语句退出后会清理，但并发或异常退出时残留文件累积，最终填满根分区。重定向到数据盘可彻底解决。

---

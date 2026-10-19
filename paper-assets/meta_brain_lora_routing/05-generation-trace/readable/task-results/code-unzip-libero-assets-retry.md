# code unzip libero assets retry

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unzip-libero-assets-retry_20260516T042244_result.json`
- **Structured JSON:** [`0f3e1c15b022fb797373.json`](../../sessions/0f/0f3e1c15b022fb797373.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LIBERO benchmark 导入成功。

## 结果

1. **解压完成**：`assets.zip`（6.0GB）已解压，448800 个文件，输出到 `/root/autodl-tmp/libero_plus_assets/inspire/.../assets/`（9.5G）
2. **磁盘问题已解决**：拷贝到根分区导致磁盘满（30G/30G），改用 symlink：`/root/LIBERO-plus/libero/libero/assets` → 数据盘解压目录。根分区恢复到 74%（8.1G 可用）
3. **LIBERO-Plus 可正常导入**：`from libero.libero.benchmark import get_benchmark` 成功（需 `sys.path` 包含 `/root/LIBERO-plus`）

---

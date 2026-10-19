# research libero plus assets download

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-plus-assets-download_20260515T171307_result.json`
- **Structured JSON:** [`14d2fb8c82cdb83f2276.json`](../../sessions/14/14d2fb8c82cdb83f2276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是结论：

---

## 结论：**可下载。** `new_objects/` 目录缺失是唯一问题。

### 1. 问题根因

服务器上 `/root/LIBERO-plus/libero/libero/assets/` 缺少 `new_objects/` 目录。这是 `_add_N` 扰动所需的全部干扰物体 XML 所在位置。

`custom_objects.py` 引用路径格式：
```
assets/new_objects/cupcake/sutaow/usd/MJCF/sutaow.xml
assets/new_objects/cutting_board/aibvew/usd/MJCF/aibvew.xml
assets/new_objects/bag_of_yeast/...
```

当前 assets 目录有 7 个子目录（articulated_objects, scenes, stable_hope_objects 等），但缺了关键的 `new_objects/`。

### 2. 已下载但不完整

服务器上有两个 `assets.zip`：
- `/root/autodl-tmp/assets.zip` — **仅 4MB**，只包含 scenes 的纹理变体 XML（如 `kitchen_table_WoodFine001_REFL_6K.xml`），**不含 `new_objects/`**
- `/root/autodl-tmp/libero_plus_assets/assets.zip` — 同一个文件

4MB 不可能包含"hundreds of new objects"。可能是下载不完整或 HuggingFace Git LFS 未正确拉取。

### 3. 公开下载源

| 来源 | URL |
|------|-----|
| HuggingFace 数据集 | [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus) |
| GitHub 主仓库 | [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus) |
| 备用仓库（主账号被封时） | [sii-research/LIBERO-plus](https://github.com/sii-research/LIBERO-plus) |

README 明确指示：
> "Please download our assets from [LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main), including hundreds of new objects, textures, and other required assets. Please unzip the `assets.zip` file to `/LIBERO-plus/libero/libero` path."

### 4. 修复命令

```bash
source /etc/network_turbo
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# 方法1: huggingface-cli (推荐)
pip install -U huggingface_hub
huggingface-cli download --repo-type dataset Sylvest/LIBERO-plus assets.zip --local-dir /root/autodl-tmp/libero_plus_assets/

# 解压到正确位置（assets.zip 内路径较深，需 strip）
cd /root/autodl-tmp/libero_plus_assets/
unzip -o assets.zip
# 检查解压后的目录结构，找到 new_objects/ 并 cp/mv 到正确位置
cp -r &lt;extracted_path>/assets/new_objects /root/LIBERO-plus/libero/libero/assets/

# 方法2: 如果 HF 太慢，用 wget 直接下载
wget "https://huggingface.co/datasets/Sylvest/LIBERO-plus/resolve/main/assets.zip" -O /root/autodl-tmp/assets_full.zip
```

### 5. 典型缺失文件（从 `custom_objects.py` 提取）

```
assets/new_objects/bag_of_yeast/&lt;hash>/usd/MJCF/&lt;hash>.xml
assets/new_objects/cupcake/sutaow/usd/MJCF/sutaow.xml
assets/new_objects/cupcake/wdiezm/usd/MJCF/wdiezm.xml
assets/new_objects/cutting_board/aibvew/usd/MJCF/aibvew.xml
assets/new_objects/cutting_board/idmcgf/usd/MJCF/idmcgf.xml
```
（`custom_objects.py` 中注册了数十种物体类别，每类多个变体）

### 6. 风险点

- HuggingFace "Repo is missing" [讨论帖](https://huggingface.co/datasets/Sylvest/LIBERO-plus/discussions/2) 提到原作者 GitHub 账号曾被封，但数据集仍在 HuggingFace 上
- 如果 HF 下载失败，备用方案：联系作者（论文一作 Sylvest / syfei）或从 [sii-research/LIBERO-plus](https://github.com/sii-research/LIBERO-plus) 获取
- AutoDL 上下载 HF 大文件慢，建议用 `network_turbo` + 后台 nohup 执行

---

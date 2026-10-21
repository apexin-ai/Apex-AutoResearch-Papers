# SICA 代码状态验证 + vLLM 健康检查报告

**日期**: 2026-05-15  
**服务器**: westd-32608

---

## 1. Bug Fix 验证（7/7 PASS）

### a) regex 修复：四反斜杠 `\\\\s` → `\\s`
- **PASS** — `grep -rn '\\\\s' sica/ utils/` 无匹配，所有 `.py` 文件中不存在四反斜杠 s pattern

### b) response_format=json_object
- **PASS** — `sica/constraint_extractor.py:149`
  ```python
  response_format={"type": "json_object"},
  ```

### c) extraction max_tokens = 1024
- **PASS** — `sica/constraint_extractor.py:132`
  ```python
  max_tokens: int = 1024
  ```
  - 对比：`.bak` 为 4096，`.bak2` 为 512，当前为 1024 ✓

### d) max_workers=6 + Semaphore(6)
- **PASS** — `sica/constraint_extractor.py:152,155,161` 和 `:226,229,235`
  ```python
  def batch_call(self, prompts: list[str], max_workers: int = 6) -> list[str]:
      semaphore = threading.Semaphore(6)
      ...
      with ThreadPoolExecutor(max_workers=max_workers) as executor:
  ```
  - 对比：`.bak` 为 max_workers=4 无 Semaphore，`.bak2` 为 max_workers=12 无 Semaphore

### e) HTTP timeout=120s
- **PASS** — `sica/constraint_extractor.py:134` 和 `:208`
  ```python
  self.client = OpenAI(base_url=base_url, api_key="[REDACTED]", timeout=120.0)
  ```
  - 另有 future.result(timeout=180) 和 as_completed(timeout=600) 保护

### f) Z3 is_bool 类型检查
- **PASS** — `sica/z3_maxsat.py:162`
  ```python
  if not z3.is_bool(uc.z3_formula):
  ```
  - 配合 `_is_boolean_formula()` 检测（:21）和 `var_type` 自动判断（:40）

### g) pipeline fallback（安全 .get() 访问）
- **PASS** — `run_full_mvp.py` 多处使用 `.get("constraints_stats", {})` 和 `.get("maxsat_stats", {})` 安全访问
  - 关键行：112-116（compute_summary）, 249-250（主循环）, 261-262（异常 fallback）, 308-309（结果记录）

---

## 2. vLLM 状态

| 检查项 | 结果 |
|--------|------|
| `/health` | **UP** — HTTP 200 |
| `/v1/models` | **UP** — 模型 `QwQ-32B`，max_model_len=16384 |

---

## 3. 进程状态

**活跃实验**: `sica_aime30_v2` tmux session
- 命令: `python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 10240 --math-data data/aime2024_subset.json --output results/aime30_v2.json --no-proofwriter`
- 进度: **4/30 完成**（问题 1-4），问题 5 (`aime2024_II_05`, 几何题) **卡住**
- 问题 5 状态: 从 22:11 开始反复超时重试，已持续约 1.5 小时（Retry 3/3 后仍继续重试）
- 已完成问题 4 用时: 501.7s（~8.4 min），ETA 原估计 241 min

**警告**: 问题 5 超时重试看起来陷入了无限循环——retry 3/3 之后并没有 fail-fast，反而继续发新请求。这可能是 OpenAI client 自动重试叠加手动重试导致。

---

## 4. 准备好的脚本

### run_math50_fixed.sh ✓
```bash
#!/bin/bash
# MATH 50 re-run with bug fixes (D006)
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
curl -s http://localhost:8000/v1/models > /dev/null || { echo "vLLM not running!"; exit 1; }
python run_full_mvp.py \
  --mode vllm --k 12 \
  --math-data data/math500_subset.json \
  --no-proofwriter --temperature 0.7 \
  --output results/math50_fixed_t07.json
```

### run_proofwriter.sh ✓
```bash
#!/bin/bash
# ProofWriter 10-question sanity check (D003 logic domain)
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
curl -s http://localhost:8000/v1/models > /dev/null || { echo "ERROR: vLLM not running!"; exit 1; }
python run_full_mvp.py \
  --mode vllm --k 12 \
  --math-data data/proofwriter_subset.json \
  --no-proofwriter --temperature 0.7 \
  --output results/proofwriter10_t07.json
```

---

## 5. 磁盘空间

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根） | 30G | 15G | 16G | 50% |
| `/root/autodl-tmp` | 250G | 80G | 171G | 32% |

空间充足，无磁盘压力。

---

## 6. 总结

| 项目 | 状态 |
|------|------|
| 7 个 bug fix | **全部 PASS** ✓ |
| vLLM 服务 | **正常运行** ✓ |
| 磁盘空间 | **充足** ✓ |
| 脚本就绪 | **2 个脚本确认** ✓ |
| 当前实验 | **⚠️ AIME 实验卡在问题 5** |

### 能否直接重跑？

**需要先处理当前卡住的实验**：
1. 当前 `sica_aime30_v2` 进程卡在问题 5 超时重试，需要先 kill 或等待它自然结束
2. kill 后 vLLM 应该可以正常服务新请求
3. 代码和环境一切就绪，处理完卡住进程即可启动新实验

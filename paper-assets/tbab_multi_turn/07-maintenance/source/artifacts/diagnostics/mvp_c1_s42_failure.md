# 诊断报告: mvp_c1_s42 失败分析

**日期**: 2026-05-18
**服务器**: westb-25721
**日志**: ~/runs/tbab_multi_turn/mvp_c1_s42.log

## 错误类型

**依赖配置缺失** — W&B API key 未配置。

## 完整 Traceback

```
Traceback (most recent call last):
  File "/root/tbab_multi_turn/scripts/train.py", line 172, in <module>
    main()
  File "/root/tbab_multi_turn/scripts/train.py", line 98, in main
    wandb.init(
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/wandb_init.py", line 1613, in init
    get_sentry().reraise(e)
  File "/usr/local/lib/python3.10/dist-packages/wandb/analytics/sentry.py", line 191, in reraise
    raise exc.with_traceback(tb)
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/wandb_init.py", line 1530, in init
    wi.maybe_login(init_settings)
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/wandb_init.py", line 200, in maybe_login
    wandb_login._login(
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/wandb_login.py", line 190, in _login
    auth = _find_or_prompt_for_key(
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/wandb_login.py", line 266, in _find_or_prompt_for_key
    auth = wbauth.authenticate_session(
  File "/usr/local/lib/python3.10/dist-packages/wandb/sdk/lib/wbauth/authenticate.py", line 139, in authenticate_session
    raise UsageError(
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

## 根因分析

1. 服务器环境变量中**没有 `WANDB_API_KEY`**（`env` 输出确认）
2. 也没有 `~/.netrc` 或 W&B 本地登录缓存
3. `train.py:98` 直接调用 `wandb.init()` 无任何 fallback，缺 key 即崩溃
4. 脚本在打印完 condition/seed 信息后立即失败，**未进入模型加载或训练阶段**

## 修复建议

**方案 A（推荐）: 设置环境变量**

启动训练前执行：
```bash
export WANDB_API_KEY="[REDACTED]"
```
或写入 `~/.bashrc` 持久化。

**方案 B: 离线模式（不需要 key）**

如果暂时不需要 W&B 在线记录：
```bash
export WANDB_MODE=offline
```

**方案 C: 代码层 fallback**

在 `train.py:98` 的 `wandb.init()` 前加：
```python
if not os.environ.get("WANDB_API_KEY"):
    os.environ["WANDB_MODE"] = "offline"
```

"""Patch eval_success_rate.py to add --temperature support."""
import sys

FPATH = "/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate.py"

with open(FPATH, "r") as f:
    content = f.read()

# 1. Add --temperature argument
old_parse = '    p.add_argument("--output", type=str, default="eval_results/success_rate.json",\n                   help="Path to save JSON results")\n    return p.parse_args()'
new_parse = '    p.add_argument("--output", type=str, default="eval_results/success_rate.json",\n                   help="Path to save JSON results")\n    p.add_argument("--temperature", type=float, default=1.0,\n                   help="Temperature scaling for flow matching ODE velocity (0.8 recommended)")\n    return p.parse_args()'
assert old_parse in content, "Could not find parse_args block"
content = content.replace(old_parse, new_parse)

# 2. Replace predict_actions with temperature-aware version
old_predict = '''@torch.no_grad()
def predict_actions(policy, batch: dict) -> torch.Tensor:
    """Returns (chunk_size, action_dim) actions for batch_size=1."""
    images, img_masks = policy.prepare_images(batch)
    state = policy.prepare_state(batch)
    lang_tokens = batch["observation.language.tokens"]
    lang_masks = batch["observation.language.attention_mask"]

    actions = policy.model.sample_actions(
        images, img_masks, lang_tokens, lang_masks, state
    )
    original_action_dim = policy.config.action_feature.shape[0]
    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)'''

new_predict = '''@torch.no_grad()
def predict_actions(policy, batch: dict, temperature: float = 1.0) -> torch.Tensor:
    """Returns (chunk_size, action_dim) actions for batch_size=1."""
    from lerobot.policies.smolvla.modeling_smolvla import make_att_2d_masks

    images, img_masks = policy.prepare_images(batch)
    state = policy.prepare_state(batch)
    lang_tokens = batch["observation.language.tokens"]
    lang_masks = batch["observation.language.attention_mask"]

    if temperature == 1.0:
        actions = policy.model.sample_actions(
            images, img_masks, lang_tokens, lang_masks, state
        )
        original_action_dim = policy.config.action_feature.shape[0]
        return actions[0, :, :original_action_dim]

    inner = policy.model
    try:
        from peft import PeftModel
        if isinstance(inner, PeftModel):
            inner = inner.base_model.model
    except ImportError:
        pass

    bsize = state.shape[0]
    device = state.device
    actions_shape = (bsize, inner.config.chunk_size, inner.config.max_action_dim)
    noise = inner.sample_noise(actions_shape, device)

    prefix_embs, prefix_pad_masks, prefix_att_masks = inner.embed_prefix(
        images, img_masks, lang_tokens, lang_masks, state=state
    )
    prefix_att_2d = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)
    prefix_pos = torch.cumsum(prefix_pad_masks, dim=1) - 1
    _, kv_cache = inner.vlm_with_expert.forward(
        attention_mask=prefix_att_2d,
        position_ids=prefix_pos,
        past_key_values=None,
        inputs_embeds=[prefix_embs, None],
        use_cache=inner.config.use_cache,
        fill_kv_cache=True,
    )

    num_steps = inner.config.num_steps
    dt = -1.0 / num_steps
    x_t = noise

    for step in range(num_steps):
        t = 1.0 + step * dt
        t_tensor = torch.tensor(t, dtype=torch.float32, device=device).expand(bsize)
        v_t = inner.denoise_step(
            x_t=x_t, prefix_pad_masks=prefix_pad_masks,
            past_key_values=kv_cache, timestep=t_tensor,
        )
        x_t = x_t + dt * v_t * temperature

    original_action_dim = policy.config.action_feature.shape[0]
    return x_t[0, :, :original_action_dim]'''

assert old_predict in content, "Could not find predict_actions block"
content = content.replace(old_predict, new_predict)

# 3. Update call sites
old_acis_call = "                    action_chunk = predict_actions(policy, batch)\n                    hook_handle.remove()"
new_acis_call = "                    action_chunk = predict_actions(policy, batch, temperature=args.temperature)\n                    hook_handle.remove()"
content = content.replace(old_acis_call, new_acis_call)

old_else_call = "                else:\n                    action_chunk = predict_actions(policy, batch)"
new_else_call = "                else:\n                    action_chunk = predict_actions(policy, batch, temperature=args.temperature)"
content = content.replace(old_else_call, new_else_call)

# 4. Add temperature to summary
old_seed = '        "seed": args.seed,'
new_seed = '        "temperature": args.temperature,\n        "seed": args.seed,'
content = content.replace(old_seed, new_seed)

with open(FPATH, "w") as f:
    f.write(content)

print("PATCHED OK")

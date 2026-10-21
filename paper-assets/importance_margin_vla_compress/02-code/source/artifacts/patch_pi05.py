"""Patch eval_pi05_pruning_libero.py to add attention-based pruning."""

filepath = '/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py'
with open(filepath, 'r') as f:
    content = f.read()

# 1. Add "attention" to prune_mode choices
content = content.replace(
    'choices=["none", "random", "l2norm"]',
    'choices=["none", "random", "l2norm", "attention"]'
)

# 2. Insert compute_attention_importance_probe function before main()
PROBE_FN = '''
def compute_attention_importance_probe(img_embs, lang_emb, lm, n_probe_layers=2):
    """Run first n_probe_layers of the LLM to get attention-based importance for vision tokens.

    Importance = avg attention from language tokens -> each vision token,
    averaged across probe layers and all heads.
    """
    import torch.nn.functional as F
    from transformers.models.gemma import modeling_gemma as _gemma

    all_vis = torch.cat(img_embs, dim=1)
    total_vis = all_vis.shape[1]
    full_embs = torch.cat([all_vis, lang_emb], dim=1)
    B, S, D = full_embs.shape

    position_ids = torch.arange(S, device=full_embs.device).unsqueeze(0).expand(B, -1)
    _model_dtype = lm.layers[0].self_attn.q_proj.weight.dtype
    hidden = full_embs.to(_model_dtype)
    all_attn = []

    with torch.no_grad():
        for layer_idx in range(min(n_probe_layers, len(lm.layers))):
            layer = lm.layers[layer_idx]
            normed = layer.input_layernorm(hidden)
            if isinstance(normed, tuple):
                normed = normed[0]
            normed = normed.to(_model_dtype)

            head_dim = layer.self_attn.head_dim
            q = layer.self_attn.q_proj(normed)
            k = layer.self_attn.k_proj(normed)
            v = layer.self_attn.v_proj(normed)

            n_q_heads = q.shape[-1] // head_dim
            n_kv_heads = k.shape[-1] // head_dim

            q = q.view(B, S, n_q_heads, head_dim).transpose(1, 2)
            k = k.view(B, S, n_kv_heads, head_dim).transpose(1, 2)
            v = v.view(B, S, n_kv_heads, head_dim).transpose(1, 2)

            cos, sin = lm.rotary_emb(v, position_ids)
            q, k = _gemma.apply_rotary_pos_emb(q, k, cos, sin, unsqueeze_dim=1)

            if n_kv_heads != n_q_heads:
                n_rep = n_q_heads // n_kv_heads
                k = k.repeat_interleave(n_rep, dim=1)
                v = v.repeat_interleave(n_rep, dim=1)

            scaling = layer.self_attn.scaling
            attn_weights = torch.matmul(q, k.transpose(-2, -1)) * scaling
            attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
            all_attn.append(attn_weights)

            attn_out = torch.matmul(attn_weights.to(v.dtype), v)
            attn_out = attn_out.transpose(1, 2).reshape(B, S, n_q_heads * head_dim)
            attn_out = layer.self_attn.o_proj(attn_out)
            hidden = hidden + attn_out

            normed2 = layer.post_attention_layernorm(hidden)
            if isinstance(normed2, tuple):
                normed2 = normed2[0]
            normed2 = normed2.to(_model_dtype)
            mlp_out = layer.mlp(normed2)
            hidden = hidden + mlp_out

    avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, S, S]
    lang_to_vis = avg_attn[:, total_vis:, :total_vis]  # [B, L, V]
    vis_importance = lang_to_vis.mean(dim=1)  # [B, V]
    return vis_importance

'''

content = content.replace(
    '\ndef main():',
    PROBE_FN + '\ndef main():'
)

# 3. Make the prune_fn block skip attention mode
content = content.replace(
    '    if prune_fn is not None:\n        original_embed_prefix = policy.model.embed_prefix',
    '    if prune_fn is not None and args.prune_mode != "attention":\n        original_embed_prefix = policy.model.embed_prefix'
)

# 4. Add attention monkey-patching block after the existing random/l2norm block
# Find the log.info line that ends the existing pruning block
OLD_END = '''        log.info(f"Pruning: {args.prune_mode}, keep {n_keep}/{N_PATCHES} tokens/image "
                 f"({n_keep*3} total)")

    from lerobot.policies.factory import make_pre_post_processors'''

ATTN_BLOCK = '''        log.info(f"Pruning: {args.prune_mode}, keep {n_keep}/{N_PATCHES} tokens/image "
                 f"({n_keep*3} total)")

    if args.prune_mode == "attention":
        n_keep = max(1, int(N_PATCHES * args.keep_ratio))

        def pruned_embed_prefix_attn(self_model, images, img_masks, tokens, masks):
            img_embs = []
            for img, img_mask in zip(images, img_masks, strict=True):
                img_emb = self_model.paligemma_with_expert.embed_image(img)
                img_embs.append(img_emb)
            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)

            lm = self_model.paligemma_with_expert.paligemma.model.language_model
            vis_importance = compute_attention_importance_probe(img_embs, lang_emb, lm)

            embs = []
            pad_masks_list = []
            att_masks = []
            start_idx = 0
            bsize = img_embs[0].shape[0]

            for i, (img_emb, img_mask) in enumerate(zip(img_embs, img_masks)):
                n_tokens = img_emb.shape[1]
                n_keep_cur = max(1, int(n_tokens * args.keep_ratio))
                scores = vis_importance[0, start_idx:start_idx + n_tokens]
                _, topk_idx = torch.topk(scores, n_keep_cur)
                topk_idx = topk_idx.sort().values

                if not hasattr(pruned_embed_prefix_attn, "_logged"):
                    print(f"[PRUNE-DIAG] attention: n_keep={n_keep_cur}/{n_tokens}, "
                          f"score_range=[{scores.min():.6f}, {scores.max():.6f}], "
                          f"first_indices={topk_idx[:5].tolist()}")
                    pruned_embed_prefix_attn._logged = True

                embs.append(img_emb[:, topk_idx, :])
                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep_cur))
                att_masks += [0] * n_keep_cur
                start_idx += n_tokens

            embs.append(lang_emb)
            pad_masks_list.append(masks)
            att_masks += [0] * lang_emb.shape[1]

            embs = torch.cat(embs, dim=1)
            pad_masks_cat = torch.cat(pad_masks_list, dim=1)
            att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)
            att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))
            return embs, pad_masks_cat, att_masks_t

        policy.model.embed_prefix = types.MethodType(pruned_embed_prefix_attn, policy.model)
        log.info(f"Pruning: attention, keep {n_keep}/{N_PATCHES} tokens/image "
                 f"({n_keep*3} total, 2-layer probe)")

    from lerobot.policies.factory import make_pre_post_processors'''

content = content.replace(OLD_END, ATTN_BLOCK)

with open(filepath, 'w') as f:
    f.write(content)

print("OK: patched eval_pi05_pruning_libero.py")

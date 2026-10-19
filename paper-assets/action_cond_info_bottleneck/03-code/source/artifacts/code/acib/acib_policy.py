import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms.v2 as T

from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss


class ACIBPolicy(nn.Module):
    def __init__(self, base_policy, acib_config):
        super().__init__()
        self.base_policy = base_policy
        self.acib_config = acib_config
        self.scorer = ACIBScorer(acib_config)
        self.acib_loss_fn = ACIBLoss(acib_config)
        self.acib_enabled = True
        self._cached_logits = []
        self._cached_visual_tokens = []
        self._cached_lang_condition = None
        self._hook_handles = []
        self._perturb_transform = self._build_perturb_transform()
        self._setup_freeze(acib_config)
        self._install_hooks()
        self.scoring_alpha = acib_config.scoring_alpha

        if acib_config.freeze_mode == "connector_scorer":
            self._connector_ref_params = {
                name: param.detach().clone()
                for name, param in self._connector.named_parameters()
            }

    @property
    def _vlm_with_expert(self):
        return self.base_policy.model.vlm_with_expert

    @property
    def _connector(self):
        return self._vlm_with_expert.vlm.model.connector

    @property
    def _vision_encoder(self):
        return self._vlm_with_expert.vlm.model.vision_model

    def _install_hooks(self):
        handle = self._connector.register_forward_hook(self._connector_hook)
        self._hook_handles.append(handle)

    def _compute_lang_condition(self, batch):
        lang_tokens = batch.get("observation.language.tokens")
        if lang_tokens is None:
            return None
        with torch.no_grad():
            lang_emb = self._vlm_with_expert.embed_language_tokens(lang_tokens)
            lang_mask = batch.get("observation.language.attention_mask")
            if lang_mask is not None:
                mask = lang_mask.to(lang_emb.dtype).unsqueeze(-1)
                summed = (lang_emb * mask).sum(dim=1)
                denom = mask.sum(dim=1).clamp(min=1.0)
                cond = summed / denom
            else:
                cond = lang_emb.mean(dim=1)
        return cond

    def _get_condition(self, output):
        if (
            self.acib_config.condition_source == "language"
            and self._cached_lang_condition is not None
        ):
            return self._cached_lang_condition.to(dtype=output.dtype, device=output.device)
        return output.mean(dim=1)

    def _connector_hook(self, module, input, output):
        if not self.acib_enabled:
            return output
        if self.acib_config.freeze_mode == "connector_scorer":
            self._cached_visual_tokens.append(output)
        else:
            self._cached_visual_tokens.append(output.detach())
        condition = self._get_condition(output)
        weights, logits = self.scorer(output, condition)
        self._cached_logits.append(logits)
        if self.acib_config.stop_grad_task:
            weights = weights.detach()
        if self.scoring_alpha == 1.0:
            return self.scorer.apply_weights(output, weights)
        else:
            alpha = self.scoring_alpha
            effective = 1 - alpha + alpha * weights.unsqueeze(-1)
            return output * effective

    def _compute_contrastive_loss(self, batch):
        if not self._cached_visual_tokens:
            return torch.tensor(0.0, device=next(self.parameters()).device)

        visual_tokens = torch.cat(self._cached_visual_tokens, dim=1)
        B = visual_tokens.shape[0]
        if B < 2:
            return torch.tensor(0.0, device=visual_tokens.device)

        orig_condition = self._cached_lang_condition
        if orig_condition is None:
            return torch.tensor(0.0, device=visual_tokens.device)

        lang_tokens = batch.get("observation.language.tokens")
        lang_mask = batch.get("observation.language.attention_mask")
        if lang_tokens is None:
            return torch.tensor(0.0, device=visual_tokens.device)

        shift = torch.randint(1, B, (1,)).item()
        perm = (torch.arange(B, device=lang_tokens.device) + shift) % B
        shuffled_tokens = lang_tokens[perm]
        shuffled_mask = lang_mask[perm] if lang_mask is not None else None

        with torch.no_grad():
            shuffled_emb = self._vlm_with_expert.embed_language_tokens(shuffled_tokens)
            if shuffled_mask is not None:
                mask = shuffled_mask.to(shuffled_emb.dtype).unsqueeze(-1)
                summed = (shuffled_emb * mask).sum(dim=1)
                denom = mask.sum(dim=1).clamp(min=1.0)
                shuffled_condition = summed / denom
            else:
                shuffled_condition = shuffled_emb.mean(dim=1)

        shuffled_condition = shuffled_condition.to(dtype=visual_tokens.dtype, device=visual_tokens.device)
        orig_cond = orig_condition.to(dtype=visual_tokens.dtype, device=visual_tokens.device)

        weights_orig, _ = self.scorer(visual_tokens, orig_cond)
        weights_shuffled, _ = self.scorer(visual_tokens, shuffled_condition)

        return ACIBLoss.contrastive_loss(weights_orig, weights_shuffled)

    def _compute_connector_drift_loss(self):
        drift = 0.0
        for name, param in self._connector.named_parameters():
            ref = self._connector_ref_params[name].to(param.device)
            drift = drift + torch.sum((param - ref) ** 2)
        return drift

    def forward(self, batch):
        self._cached_logits = []
        self._cached_visual_tokens = []
        if self.acib_config.condition_source == "language":
            self._cached_lang_condition = self._compute_lang_condition(batch)
        else:
            self._cached_lang_condition = None
        task_loss, loss_dict = self.base_policy.forward(batch)
        if not self.acib_enabled or not self._cached_logits:
            return task_loss, loss_dict
        scores_clean = torch.cat(self._cached_logits, dim=1)
        scores_perturbed = None
        if self.training:
            scores_perturbed = self._score_perturbed(batch)
        acib_losses = self.acib_loss_fn(task_loss, scores_clean, scores_perturbed)

        contrastive_loss_val = torch.tensor(0.0, device=task_loss.device)
        if self.training and self.acib_config.lambda_contrastive > 0:
            contrastive_loss_val = self._compute_contrastive_loss(batch)
            acib_losses["total"] = acib_losses["total"] + self.acib_config.lambda_contrastive * contrastive_loss_val

        drift_loss_val = torch.tensor(0.0, device=task_loss.device)
        if self.acib_config.freeze_mode == "connector_scorer" and self.acib_config.lambda_drift > 0:
            drift_loss_val = self._compute_connector_drift_loss()
            acib_losses["total"] = acib_losses["total"] + self.acib_config.lambda_drift * drift_loss_val

        loss_dict["acib_task"] = acib_losses["task"]
        loss_dict["acib_consistency"] = acib_losses["consistency"]
        loss_dict["acib_ib"] = acib_losses["ib"]
        loss_dict["acib_contrastive"] = contrastive_loss_val.detach()
        loss_dict["connector_drift"] = drift_loss_val.detach() if isinstance(drift_loss_val, torch.Tensor) else drift_loss_val
        return acib_losses["total"], loss_dict

    @staticmethod
    def _build_perturb_transform():
        return T.RandomChoice([
            T.RandomAffine(degrees=15, translate=(0.05, 0.05)),
            T.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.1),
            T.GaussianBlur(kernel_size=7, sigma=(0.5, 2.0)),
        ])

    def _score_perturbed(self, batch):
        image_keys = sorted(
            k for k in batch
            if k.startswith("observation.images.") and isinstance(batch[k], torch.Tensor)
            and batch[k].dim() == 4
        )
        if not image_keys:
            return None
        prev = self.acib_enabled
        self.acib_enabled = False
        all_logits = []
        try:
            for key in image_keys:
                img = batch[key]
                if torch.rand(1).item() < 0.75:
                    perturbed = self._perturb_transform(img)
                else:
                    perturbed = img + torch.randn_like(img) * 0.1
                with torch.no_grad(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                    target_size = self._vlm_with_expert.vlm.config.vision_config.image_size
                    if perturbed.shape[-1] != target_size or perturbed.shape[-2] != target_size:
                        perturbed = torch.nn.functional.interpolate(
                            perturbed, size=(target_size, target_size), mode="bilinear", align_corners=False,
                        )
                    vis_out = self._vision_encoder(perturbed)
                    raw_tokens = vis_out.last_hidden_state if hasattr(vis_out, "last_hidden_state") else vis_out[0]
                    tokens = self._connector(raw_tokens)
                condition = self._get_condition(tokens)
                _, logits = self.scorer(tokens, condition)
                all_logits.append(logits)
        finally:
            self.acib_enabled = prev
        return torch.cat(all_logits, dim=1) if all_logits else None

    def _setup_freeze(self, config):
        if config.freeze_mode != "legacy":
            self._setup_freeze_by_mode(config.freeze_mode)
            return
        if config.freeze_vlm:
            for param in self._vlm_with_expert.vlm.parameters():
                param.requires_grad = False
        if config.freeze_action_expert:
            for param in self._vlm_with_expert.lm_expert.parameters():
                param.requires_grad = False
        if config.train_scorer_only:
            for param in self.base_policy.parameters():
                param.requires_grad = False
        for param in self.scorer.parameters():
            param.requires_grad = True

    def _setup_freeze_by_mode(self, mode):
        if mode == "scorer_only":
            for param in self.base_policy.parameters():
                param.requires_grad = False
        elif mode == "connector_scorer":
            for param in self.base_policy.parameters():
                param.requires_grad = False
            for param in self._connector.parameters():
                param.requires_grad = True
        elif mode == "all_trainable":
            pass
        for param in self.scorer.parameters():
            param.requires_grad = True

    def select_action(self, batch, **kwargs):
        if self.acib_config.condition_source == "language":
            self._cached_lang_condition = self._compute_lang_condition(batch)
        return self.base_policy.select_action(batch, **kwargs)

    def reset(self):
        self.base_policy.reset()

    def get_optim_params(self):
        base_params = self.base_policy.get_optim_params()
        scorer_params = {"params": list(self.scorer.parameters()), "lr": base_params.get("lr", 1e-4)}
        if isinstance(base_params, dict):
            return [base_params, scorer_params]
        elif isinstance(base_params, list):
            return base_params + [scorer_params]
        return [scorer_params]

    def get_scorer_stats(self):
        if not self._cached_logits:
            return {}
        logits = torch.cat(self._cached_logits, dim=1)
        w = torch.sigmoid(logits)
        return {
            "scorer/mean": w.mean().item(),
            "scorer/std": w.std().item(),
            "scorer/min": w.min().item(),
            "scorer/max": w.max().item(),
            "scorer/sparsity": (w < 0.5).float().mean().item(),
        }

    def toggle_acib(self, enabled):
        self.acib_enabled = enabled

    def remove_hooks(self):
        for h in self._hook_handles:
            h.remove()
        self._hook_handles.clear()

    @classmethod
    def from_pretrained(cls, model_id, acib_config=None):
        from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
        base_policy = SmolVLAPolicy.from_pretrained(model_id)
        if acib_config is None:
            vlm_hidden = base_policy.model.vlm_with_expert.config.text_config.hidden_size
            acib_config = ACIBConfig(visual_dim=vlm_hidden, condition_dim=vlm_hidden)
        return cls(base_policy, acib_config)

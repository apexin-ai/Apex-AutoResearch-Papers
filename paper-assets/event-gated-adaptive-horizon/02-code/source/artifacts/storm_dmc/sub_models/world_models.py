"""
WorldModel adapted for DMC proprioceptive observations and continuous actions.

Key changes vs original STORM:
1. CNN encoder/decoder → MLP encoder/decoder for vector observations
2. Obs reconstruction: image MSE → vector MSE
3. Action: discrete one-hot → continuous vector (handled in transformer_model.py)
4. Imagination buffer: scalar action → vector action
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import OneHotCategorical, Normal
from einops import rearrange, repeat, reduce
from torch.cuda.amp import autocast

from sub_models.functions_losses import SymLogTwoHotLoss
from sub_models.attention_blocks import get_subsequent_mask_with_batch_length, get_subsequent_mask
from sub_models.transformer_model import StochasticTransformerKVCache
from sub_models.mlp_encoder import MLPEncoder, MLPDecoder
import agents


class DistHead(nn.Module):
    def __init__(self, encoder_feat_dim, transformer_hidden_dim, stoch_dim) -> None:
        super().__init__()
        self.stoch_dim = stoch_dim
        self.post_head = nn.Linear(encoder_feat_dim, stoch_dim * stoch_dim)
        self.prior_head = nn.Linear(transformer_hidden_dim, stoch_dim * stoch_dim)

    def unimix(self, logits, mixing_ratio=0.01):
        probs = F.softmax(logits, dim=-1)
        mixed_probs = mixing_ratio * torch.ones_like(probs) / self.stoch_dim + (1 - mixing_ratio) * probs
        logits = torch.log(mixed_probs)
        return logits

    def forward_post(self, x):
        logits = self.post_head(x)
        logits = rearrange(logits, "B L (K C) -> B L K C", K=self.stoch_dim)
        logits = self.unimix(logits)
        return logits

    def forward_prior(self, x):
        logits = self.prior_head(x)
        logits = rearrange(logits, "B L (K C) -> B L K C", K=self.stoch_dim)
        logits = self.unimix(logits)
        return logits


class RewardDecoder(nn.Module):
    def __init__(self, num_classes, transformer_hidden_dim) -> None:
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(transformer_hidden_dim, transformer_hidden_dim, bias=False),
            nn.LayerNorm(transformer_hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(transformer_hidden_dim, transformer_hidden_dim, bias=False),
            nn.LayerNorm(transformer_hidden_dim),
            nn.ReLU(inplace=True),
        )
        self.head = nn.Linear(transformer_hidden_dim, num_classes)

    def forward(self, feat):
        feat = self.backbone(feat)
        return self.head(feat)


class TerminationDecoder(nn.Module):
    def __init__(self, transformer_hidden_dim) -> None:
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(transformer_hidden_dim, transformer_hidden_dim, bias=False),
            nn.LayerNorm(transformer_hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(transformer_hidden_dim, transformer_hidden_dim, bias=False),
            nn.LayerNorm(transformer_hidden_dim),
            nn.ReLU(inplace=True),
        )
        self.head = nn.Sequential(nn.Linear(transformer_hidden_dim, 1))

    def forward(self, feat):
        feat = self.backbone(feat)
        termination = self.head(feat)
        return termination.squeeze(-1)


class VectorMSELoss(nn.Module):
    def forward(self, obs_hat, obs):
        # obs_hat, obs: (B, L, obs_dim)
        loss = (obs_hat - obs) ** 2
        loss = loss.sum(dim=-1)  # sum over obs_dim → (B, L)
        return loss.mean()


class CategoricalKLDivLossWithFreeBits(nn.Module):
    def __init__(self, free_bits) -> None:
        super().__init__()
        self.free_bits = free_bits

    def forward(self, p_logits, q_logits):
        p_dist = OneHotCategorical(logits=p_logits)
        q_dist = OneHotCategorical(logits=q_logits)
        kl_div = torch.distributions.kl.kl_divergence(p_dist, q_dist)
        kl_div = reduce(kl_div, "B L D -> B L", "sum")
        kl_div = kl_div.mean()
        real_kl_div = kl_div
        kl_div = torch.max(torch.ones_like(kl_div) * self.free_bits, kl_div)
        return kl_div, real_kl_div


class WorldModel(nn.Module):
    def __init__(self, obs_dim, action_dim,
                 encoder_hidden_dim,
                 transformer_max_length, transformer_hidden_dim,
                 transformer_num_layers, transformer_num_heads,
                 wm_lr=1e-4):
        super().__init__()
        self.transformer_hidden_dim = transformer_hidden_dim
        self.stoch_dim = 32
        self.stoch_flattened_dim = self.stoch_dim * self.stoch_dim  # 1024
        self.use_amp = True
        self.tensor_dtype = torch.bfloat16 if self.use_amp else torch.float32
        self.imagine_batch_size = -1
        self.imagine_batch_length = -1
        self.action_dim = action_dim
        self.obs_dim = obs_dim

        self.encoder = MLPEncoder(
            obs_dim=obs_dim,
            hidden_dim=encoder_hidden_dim,
            output_dim=encoder_hidden_dim,
        )
        self.storm_transformer = StochasticTransformerKVCache(
            stoch_dim=self.stoch_flattened_dim,
            action_dim=action_dim,
            feat_dim=transformer_hidden_dim,
            num_layers=transformer_num_layers,
            num_heads=transformer_num_heads,
            max_length=transformer_max_length,
            dropout=0.1,
        )
        self.dist_head = DistHead(
            encoder_feat_dim=self.encoder.output_dim,
            transformer_hidden_dim=transformer_hidden_dim,
            stoch_dim=self.stoch_dim,
        )
        self.obs_decoder = MLPDecoder(
            stoch_dim=self.stoch_flattened_dim,
            obs_dim=obs_dim,
            hidden_dim=encoder_hidden_dim,
        )
        self.reward_decoder = RewardDecoder(
            num_classes=255,
            transformer_hidden_dim=transformer_hidden_dim,
        )
        self.termination_decoder = TerminationDecoder(
            transformer_hidden_dim=transformer_hidden_dim,
        )

        self.vector_mse_loss = VectorMSELoss()
        self.bce_with_logits_loss_func = nn.BCEWithLogitsLoss()
        self.symlog_twohot_loss_func = SymLogTwoHotLoss(num_classes=255, lower_bound=-20, upper_bound=20)
        self.categorical_kl_div_loss = CategoricalKLDivLossWithFreeBits(free_bits=1)
        self.optimizer = torch.optim.Adam(self.parameters(), lr=wm_lr)
        self.scaler = torch.cuda.amp.GradScaler(enabled=self.use_amp)

    def encode_obs(self, obs):
        """Encode vector obs → stochastic latent. obs: (B, L, obs_dim)"""
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            embedding = self.encoder(obs)
            post_logits = self.dist_head.forward_post(embedding)
            sample = self.straight_through_gradient(post_logits, sample_mode="random_sample")
            flattened_sample = self.flatten_sample(sample)
        return flattened_sample

    def calc_last_dist_feat(self, latent, action):
        """Run transformer on full context, return last step's prior sample and dist_feat."""
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            temporal_mask = get_subsequent_mask(latent)
            dist_feat = self.storm_transformer(latent, action, temporal_mask)
            last_dist_feat = dist_feat[:, -1:]
            prior_logits = self.dist_head.forward_prior(last_dist_feat)
            prior_sample = self.straight_through_gradient(prior_logits, sample_mode="random_sample")
            prior_flattened_sample = self.flatten_sample(prior_sample)
        return prior_flattened_sample, last_dist_feat

    def predict_next(self, last_flattened_sample, action, log_video=False):
        """Single-step prediction using KV-cache. Returns decoded outputs."""
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            dist_feat = self.storm_transformer.forward_with_kv_cache(last_flattened_sample, action)
            prior_logits = self.dist_head.forward_prior(dist_feat)

            prior_sample = self.straight_through_gradient(prior_logits, sample_mode="random_sample")
            prior_flattened_sample = self.flatten_sample(prior_sample)
            if log_video:
                obs_hat = self.obs_decoder(prior_flattened_sample)
            else:
                obs_hat = None
            reward_hat = self.reward_decoder(dist_feat)
            reward_hat = self.symlog_twohot_loss_func.decode(reward_hat)
            termination_hat = self.termination_decoder(dist_feat)
            termination_hat = termination_hat > 0

        return obs_hat, reward_hat, termination_hat, prior_flattened_sample, dist_feat

    def straight_through_gradient(self, logits, sample_mode="random_sample"):
        dist = OneHotCategorical(logits=logits)
        if sample_mode == "random_sample":
            sample = dist.sample() + dist.probs - dist.probs.detach()
        elif sample_mode == "mode":
            sample = dist.mode
        elif sample_mode == "probs":
            sample = dist.probs
        return sample

    def flatten_sample(self, sample):
        return rearrange(sample, "B L K C -> B L (K C)")

    def init_imagine_buffer(self, imagine_batch_size, imagine_batch_length, dtype):
        if self.imagine_batch_size != imagine_batch_size or self.imagine_batch_length != imagine_batch_length:
            self.imagine_batch_size = imagine_batch_size
            self.imagine_batch_length = imagine_batch_length
            latent_size = (imagine_batch_size, imagine_batch_length + 1, self.stoch_flattened_dim)
            hidden_size = (imagine_batch_size, imagine_batch_length + 1, self.transformer_hidden_dim)
            # Continuous action buffer: 3D instead of 2D
            action_size = (imagine_batch_size, imagine_batch_length, self.action_dim)
            scalar_size = (imagine_batch_size, imagine_batch_length)
            self.latent_buffer = torch.zeros(latent_size, dtype=dtype, device="cuda")
            self.hidden_buffer = torch.zeros(hidden_size, dtype=dtype, device="cuda")
            self.action_buffer = torch.zeros(action_size, dtype=dtype, device="cuda")
            self.reward_hat_buffer = torch.zeros(scalar_size, dtype=dtype, device="cuda")
            self.termination_hat_buffer = torch.zeros(scalar_size, dtype=dtype, device="cuda")

    def imagine_data(self, agent, sample_obs, sample_action,
                     imagine_batch_size, imagine_batch_length, log_video, logger):
        self.init_imagine_buffer(imagine_batch_size, imagine_batch_length, dtype=self.tensor_dtype)

        self.storm_transformer.reset_kv_cache_list(imagine_batch_size, dtype=self.tensor_dtype)
        # Context: encode obs and run through transformer
        context_latent = self.encode_obs(sample_obs)
        for i in range(sample_obs.shape[1]):
            last_obs_hat, last_reward_hat, last_termination_hat, last_latent, last_dist_feat = self.predict_next(
                context_latent[:, i:i+1],
                sample_action[:, i:i+1],
                log_video=False,
            )
        self.latent_buffer[:, 0:1] = last_latent
        self.hidden_buffer[:, 0:1] = last_dist_feat

        # Imagination rollout
        for i in range(imagine_batch_length):
            action = agent.sample(
                torch.cat([self.latent_buffer[:, i:i+1], self.hidden_buffer[:, i:i+1]], dim=-1)
            )
            # action: (B, 1, action_dim)
            self.action_buffer[:, i:i+1] = action

            last_obs_hat, last_reward_hat, last_termination_hat, last_latent, last_dist_feat = self.predict_next(
                self.latent_buffer[:, i:i+1], self.action_buffer[:, i:i+1], log_video=False
            )

            self.latent_buffer[:, i+1:i+2] = last_latent
            self.hidden_buffer[:, i+1:i+2] = last_dist_feat
            self.reward_hat_buffer[:, i:i+1] = last_reward_hat
            self.termination_hat_buffer[:, i:i+1] = last_termination_hat

        return (
            torch.cat([self.latent_buffer, self.hidden_buffer], dim=-1),
            self.action_buffer,
            self.reward_hat_buffer,
            self.termination_hat_buffer,
        )

    def update(self, obs, action, reward, termination, logger=None):
        """
        Train world model on a batch from replay buffer.
        obs: (B, L, obs_dim), action: (B, L, action_dim), reward: (B, L), termination: (B, L)
        """
        self.train()
        batch_size, batch_length = obs.shape[:2]

        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            # Encoding
            embedding = self.encoder(obs)
            post_logits = self.dist_head.forward_post(embedding)
            sample = self.straight_through_gradient(post_logits, sample_mode="random_sample")
            flattened_sample = self.flatten_sample(sample)

            # Decode obs
            obs_hat = self.obs_decoder(flattened_sample)

            # Transformer dynamics
            temporal_mask = get_subsequent_mask_with_batch_length(batch_length, flattened_sample.device)
            dist_feat = self.storm_transformer(flattened_sample, action, temporal_mask)
            prior_logits = self.dist_head.forward_prior(dist_feat)
            reward_hat = self.reward_decoder(dist_feat)
            termination_hat = self.termination_decoder(dist_feat)

            # Losses
            reconstruction_loss = self.vector_mse_loss(obs_hat, obs)
            reward_loss = self.symlog_twohot_loss_func(reward_hat, reward)
            termination_loss = self.bce_with_logits_loss_func(termination_hat, termination)
            dynamics_loss, dynamics_real_kl = self.categorical_kl_div_loss(
                post_logits[:, 1:].detach(), prior_logits[:, :-1]
            )
            representation_loss, representation_real_kl = self.categorical_kl_div_loss(
                post_logits[:, 1:], prior_logits[:, :-1].detach()
            )
            total_loss = (
                reconstruction_loss + reward_loss + termination_loss
                + 0.5 * dynamics_loss + 0.1 * representation_loss
            )

        self.scaler.scale(total_loss).backward()
        self.scaler.unscale_(self.optimizer)
        torch.nn.utils.clip_grad_norm_(self.parameters(), max_norm=1000.0)
        self.scaler.step(self.optimizer)
        self.scaler.update()
        self.optimizer.zero_grad(set_to_none=True)

        if logger is not None:
            logger.log("WorldModel/reconstruction_loss", reconstruction_loss.item())
            logger.log("WorldModel/reward_loss", reward_loss.item())
            logger.log("WorldModel/termination_loss", termination_loss.item())
            logger.log("WorldModel/dynamics_loss", dynamics_loss.item())
            logger.log("WorldModel/dynamics_real_kl_div", dynamics_real_kl.item())
            logger.log("WorldModel/representation_loss", representation_loss.item())
            logger.log("WorldModel/representation_real_kl_div", representation_real_kl.item())
            logger.log("WorldModel/total_loss", total_loss.item())

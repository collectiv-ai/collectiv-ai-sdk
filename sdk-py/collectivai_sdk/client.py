from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import httpx


@dataclass
class ChatRequest:
    prompt: str
    mode: str
    provider: str
    topic: str
    modelId: Optional[str] = None
    serviceProfile: Optional[str] = None


@dataclass
class RoutingInfo:
    reason: Optional[str] = None
    filters: Optional[List[str]] = None
    latencyMs: Optional[int] = None


@dataclass
class ChatResponse:
    reply: str
    providerUsed: str
    model: str
    routingInfo: Optional[RoutingInfo] = None


class CollectivAIClient:
    """
    Minimal Python client for the CollectiVAI Router.

    Example:

        client = CollectivAIClient(base_url="http://localhost:8000/api")
        resp = client.chat(
            prompt="Hello democracy!",
            mode="ethical",
            provider="auto",
            topic="democracy",
        )
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def chat(
        self,
        prompt: str,
        mode: str,
        provider: str,
        topic: str,
        model_id: Optional[str] = None,
        service_profile: Optional[str] = None,
        timeout: float = 30.0,
    ) -> ChatResponse:
        payload = {
            "prompt": prompt,
            "mode": mode,
            "provider": provider,
            "topic": topic,
            "modelId": model_id,
            "serviceProfile": service_profile,
        }

        with httpx.Client(timeout=timeout) as client:
            res = client.post(f"{self.base_url}/chat", json=payload)

        res.raise_for_status()
        data = res.json()

        routing_info = None
        if data.get("routingInfo"):
            ri = data["routingInfo"]
            routing_info = RoutingInfo(
                reason=ri.get("reason"),
                filters=ri.get("filters"),
                latencyMs=ri.get("latencyMs"),
            )

        return ChatResponse(
            reply=data["reply"],
            providerUsed=data["providerUsed"],
            model=data["model"],
            routingInfo=routing_info,
        )

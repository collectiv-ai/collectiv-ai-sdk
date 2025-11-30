export interface ChatRequest {
  prompt: string;
  mode: string;
  provider: string;
  topic: string;
  modelId?: string | null;
  serviceProfile?: string | null;
}

export interface RoutingInfo {
  reason?: string | null;
  filters?: string[] | null;
  latencyMs?: number | null;
}

export interface ChatResponse {
  reply: string;
  providerUsed: string;
  model: string;
  routingInfo?: RoutingInfo | null;
}

export interface CollectivAIClientOptions {
  baseUrl: string; // e.g. "https://router.example.org/api"
}

export class CollectivAIClient {
  private baseUrl: string;

  constructor(opts: CollectivAIClientOptions) {
    this.baseUrl = opts.baseUrl.replace(/\/+$/, "");
  }

  async chat(request: ChatRequest): Promise<ChatResponse> {
    const res = await fetch(`${this.baseUrl}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(request)
    });

    if (!res.ok) {
      const text = await res.text().catch(() => "");
      throw new Error(
        `CollectivAI chat failed with status ${res.status}: ${text || res.statusText}`
      );
    }

    const data = (await res.json()) as ChatResponse;
    return data;
  }
}

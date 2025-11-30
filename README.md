<p align="center">
  <img src="logo.png" alt="CollectiVAI Logo" width="400" />
</p>

<h1 align="center">CollectiVAI SDKs</h1>
<h3 align="center">Official client libraries for the CollectiVAI Router & ecosystem</h3>

<p align="center">
  <a href="https://collectivai.org">
    <img src="https://img.shields.io/badge/Website-collectivai.org-003399?style=flat" alt="Website" />
  </a>
  <a href="https://github.com/collectiv-ai/collectiv-ai-router">
    <img src="https://img.shields.io/badge/Backend-Router-0055aa?style=flat" alt="CollectiVAI Router" />
  </a>
  <img src="https://img.shields.io/badge/Status-Prototype-ffcc00?style=flat" alt="Status" />
  <img src="https://img.shields.io/badge/Made%20in-Europe-003399?style=flat" alt="Made in Europe" />
</p>

---

## Overview

This repository contains **official SDKs** for the CollectiVAI ecosystem.

- 🌐 **TypeScript / JavaScript SDK** (`sdk-ts/`)  
  – for web frontends, Node.js services and integration tests.

- 🐍 **Python SDK** (`sdk-py/`)  
  – for research, data pipelines, CLI tools and backend services.

Both SDKs are currently focused on the **CollectiVAI Router**:

- call the `/api/chat` endpoint,
- send a structured JSON request,
- receive a unified response with:
  - `reply`
  - `providerUsed`
  - `model`
  - optional `routingInfo` (reason, filters, latencyMs).

> ⚠️ **Prototype status:**  
> These SDKs are early, public reference implementations.  
> They are not yet feature-complete and may change without notice.

---

## API contract (Router)

Both SDKs are thin clients around the same HTTP API, exposed by the
[`collectiv-ai-router`](https://github.com/collectiv-ai/collectiv-ai-router).

### Request

```jsonc
POST /api/chat
{
  "prompt": "How can citizens participate in climate decisions in the EU?",
  "mode": "ethical",
  "provider": "auto",
  "topic": "climate",
  "modelId": null,
  "serviceProfile": "citizen_advisor"
}
```

### Response

```jsonc
{
  "reply": "…",
  "providerUsed": "openai",
  "model": "gpt-4.1",
  "routingInfo": {
    "reason": "Ethical mode + climate topic → high-reliability model.",
    "filters": ["safety", "climate"],
    "latencyMs": 850
  }
}
```

See the router repository for the full, authoritative specification.

---

## `sdk-ts` – TypeScript / JavaScript

**Folder:** `sdk-ts/`

### Installation (planned)

Once published to npm (e.g. `@collectivai/sdk`):

```bash
npm install @collectivai/sdk
# or
yarn add @collectivai/sdk
```

### Basic usage

```ts
import { CollectivAIClient } from "@collectivai/sdk";

const client = new CollectivAIClient({
  baseUrl: "https://your-router.example.org/api",
});

const response = await client.chat({
  prompt: "How can citizens participate in climate decisions in the EU?",
  mode: "ethical",
  provider: "auto",
  topic: "climate",
  modelId: null,
  serviceProfile: "citizen_advisor",
});

console.log(response.reply);
console.log(response.providerUsed, response.model);
```

More examples and advanced configuration will be added as the router evolves.

---

## `sdk-py` – Python

**Folder:** `sdk-py/`

### Installation (planned)

Once published to PyPI (e.g. `collectivai-sdk`):

```bash
pip install collectivai-sdk
```

### Basic usage

```python
from collectivai_sdk.client import CollectivAIClient

client = CollectivAIClient(
    base_url="https://your-router.example.org/api",
)

response = client.chat(
    prompt="How can citizens participate in climate decisions in the EU?",
    mode="ethical",
    provider="auto",
    topic="climate",
    model_id=None,
    service_profile="citizen_advisor",
)

print(response.reply)
print(response.provider_used, response.model)
```

---

## Roadmap

Planned evolution of this repository:

1. **Router-first SDKs** (current phase)
   - Minimal TS & Python clients for `/api/chat`
   - Examples and documentation
2. **Extended router features**
   - health checks
   - typed error handling
   - streaming (where supported)
3. **Chain & governance integration (future)**
   - basic Cosmos RPC/REST helpers for the CollectiVAI Chain
   - utilities to fetch proposals, votes, governance parameters
4. **Stable releases**
   - semantic versioning
   - published packages on npm & PyPI

---

## Security & privacy

- The SDKs **do not contain any API keys**.  
- They only send whatever you pass in as parameters to your own backend.
- Always keep your CollectiVAI Router behind TLS (HTTPS) and configure:
  - strict CORS,
  - proper authentication (if needed),
  - logging with minimal personal data.

For the organisation-wide security practices, see:  
[`SECURITY_CHECKLIST.md`](https://github.com/collectiv-ai/.github/blob/main/SECURITY_CHECKLIST.md).

---

## Licence & branding

The SDK code in this repository may later be released under a permissive
open-source licence. Until then, treat it as:

> **“Public, non-confidential reference code – All rights reserved.”**

The **CollectiVAI** name, logo and visual identity are protected.  
Any use in products, services or campaigns requires prior written permission.

© 2025 David Compasso / CollectiVAI.

# Agent Wallet

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/RanaPriyansh/agent-wallet)
[![License](https://img.shields.io/github/license/RanaPriyansh/agent-wallet)](https://github.com/RanaPriyansh/agent-wallet/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/RanaPriyansh/agent-wallet)](https://github.com/RanaPriyansh/agent-wallet/commits/main)

DID-based credential storage and presentation for AI agents. Store verifiable credentials, selectively disclose, prove attributes without revealing all data.

## Features

- **DID Wallet**: Create and manage decentralized identifiers
- **Credential Storage**: Secure storage of verifiable credentials (VCs)
- **Selective Disclosure**: Share only needed attributes (ZK-friendly)
- **Presentation**: Create verifiable presentations for verification
- **Multiple Backends**: File-based (dev), encrypted DB (prod), hardware (advanced)

## Quick Start

```python
from agent_wallet import Wallet

# Create wallet
wallet = Wallet.create("agent-hermes")

# Store credential
wallet.store_credential({
    "@context": ["https://www.w3.org/2018/credentials/v1"],
    "type": "AgentReputation",
    "issuer": "did:web:reputation.org",
    "credentialSubject": {"reputationScore": 0.95}
})

# Create selective disclosure
proof = wallet.create_presentation(["reputationScore"], range={"min": 0.8})
```

## Install

```bash
pip install agent-wallet
```

## Why

Agents need identity and reputation. This wallet provides:
- Standards-based (W3C DID/VC)
- Privacy-preserving (selective disclosure, ZK-ready)
- Production-ready (encryption, backup/restore)
- Compatible with agent-identity-protocol

## License

MIT

---

Built with ❤️ by Thielon

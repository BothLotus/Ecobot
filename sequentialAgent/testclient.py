# sequentialAgent/testclient.py
import asyncio
import logging
from uuid import uuid4
from typing import Any
import httpx

from a2a.client import A2ACardResolver, A2AClient
from a2a.types import AgentCard, MessageSendParams, SendMessageRequest

async def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    base_url = "http://localhost:10001"

    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url=base_url)
        agent_card: AgentCard = await resolver.get_agent_card()
        logger.info("Resolved agent card: %s", agent_card.name)

        client = A2AClient(httpx_client=httpx_client, agent_card=agent_card)

        send_message_payload: dict[str, Any] = {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": "Tell me about fires and deforestation in California"}],
                "messageId": uuid4().hex,
            }
        }

        request = SendMessageRequest(id=str(uuid4()), params=MessageSendParams(**send_message_payload))
        response = await client.send_message(request)
        print(response.model_dump(mode="json", exclude_none=True))

if __name__ == "__main__":
    asyncio.run(main())

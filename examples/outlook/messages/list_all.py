"""
Get the messages in the signed-in user's mailbox

# The example is adapted from https://learn.microsoft.com/en-us/graph/api/user-list-messages
"""

from examples import acquire_token_by_username_password
from office365.graph_client import GraphClient
from office365.outlook.mail.messages.message import Message


client = GraphClient(acquire_token_by_username_password)
messages = client.me.messages.get().execute_query()
for m in messages:  # type: Message
    print(m.subject)

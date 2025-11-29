from twilio.rest import Client

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+123456789",
    to="+919xxxxxxxxx",
    body="Hello! Your order has been shipped 🚚"
)

print(message.sid)
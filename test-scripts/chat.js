const chatSocket = new WebSocket(
    "ws://localhost:8000/ws/chat/674cd8ca-20d8-4aef-8f0f-6998734f26e3/"
)

chatSocket.onopen = (e) => {
    console.log("Connection established")
}

chatSocket.onclose = (e) => {
    console.error("Chat socket closed unexpectedly")
}

chatSocket.onmessage = (e) => {
    console.log("Message received: ", e.data)
}
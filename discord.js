client.on("message", => {
    const channel = message.channel;
    channel.send(message.author.toString());
});